# functions.py

import os
import tkinter as tk
from tkinter import messagebox
from rdflib import Graph, Literal, Namespace, RDF, URIRef
import sqlite3

# Step 1: Set up RDF graph
g = Graph()
brick = Namespace("https://brickschema.org/schema/Brick#")
unit = Namespace("http://qudt.org/vocab/unit/")
ref = Namespace("https://brickschema.org/schema/Reference#")
g.bind("brick", brick)
g.bind("unit", unit)
g.bind("ref", ref)

conn = None
timeseries_refs = []
current_point_index = 0

import os
import sqlite3
from tkinter import messagebox


def connect_to_db(db_entry, log_text, point_label, load_point):
    global conn, cursor, timeseries_refs, current_point_index
    db_path = db_entry.get()

    # Check if the database file exists before attempting to connect
    if not os.path.exists(db_path):
        messagebox.showerror("Error", f"Database file '{db_path}' does not exist.")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        messagebox.showinfo("Success", f"Connected to {db_path}")
        cursor.execute("SELECT timeseries_id, stored_at FROM TimeseriesReference")
        timeseries_refs = cursor.fetchall()
        current_point_index = 0
        if timeseries_refs:
            load_point(current_point_index, point_label)
        else:
            log_text.insert(tk.END, "No points found in the database.\n")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to {db_path}\n{e}")


def load_point(index, point_label):
    if timeseries_refs:
        timeseries_id, stored_at = timeseries_refs[index]
        point_label.config(
            text=f"Point {index + 1} of {len(timeseries_refs)}: {timeseries_id} stored at {stored_at}"
        )
    else:
        point_label.config(text="No points to display.")


def update_sensor_options(sensor_options, system_type, sensor_type):
    selected_system = system_type.get()
    if selected_system in sensor_options:
        sensor_type["values"] = sensor_options[selected_system]
    else:
        sensor_type["values"] = []


def add_to_rdf(
    db_entry, sensor_type, system_type, unit_type, log_text, load_point, point_label
):
    global current_point_index
    if conn is None:
        messagebox.showerror("Error", "Please connect to the database first.")
        return

    selected_sensor = sensor_type.get()
    selected_system = system_type.get()
    selected_unit = unit_type.get()

    if not selected_sensor or not selected_system or not selected_unit:
        messagebox.showwarning(
            "Incomplete Data", "Please select a sensor, system, and unit."
        )
        return

    # Example URIs
    sensor_uri = URIRef(f"http://example.org/{selected_sensor}")
    system_uri = URIRef(f"http://example.org/{selected_system}")

    # Add sensor/system/unit triples to RDF graph
    g.add((sensor_uri, RDF.type, brick[selected_sensor]))
    g.add((sensor_uri, brick.hasUnit, unit[selected_unit]))
    g.add((sensor_uri, brick.isPartOf, system_uri))

    # Retrieve and link timeseries metadata
    timeseries_id, stored_at = timeseries_refs[current_point_index]
    database_uri = URIRef("http://example.org/database")
    g.add((database_uri, RDF.type, ref.Database))
    g.add(
        (
            database_uri,
            RDFS.label,
            Literal("SQLite Timeseries Storage", datatype=XSD.string),
        )
    )
    g.add(
        (
            database_uri,
            URIRef("http://example.org/connstring"),
            Literal(f"sqlite:///{db_entry.get()}", datatype=XSD.string),
        )
    )

    timeseries_ref_uri = URIRef(
        f"http://example.org/timeseries_{timeseries_id.replace(' ', '_')}"
    )
    g.add((timeseries_ref_uri, RDF.type, ref.TimeseriesReference))
    g.add(
        (
            timeseries_ref_uri,
            ref.hasTimeseriesId,
            Literal(timeseries_id, datatype=XSD.string),
        )
    )
    g.add((timeseries_ref_uri, ref.storedAt, database_uri))
    g.add((sensor_uri, ref.hasExternalReference, timeseries_ref_uri))

    log_text.insert(
        tk.END,
        f"Added {selected_sensor} to RDF with system {selected_system} and unit {selected_unit}\n",
    )

    # Move to the next point if available
    if current_point_index < len(timeseries_refs) - 1:
        current_point_index += 1
        load_point(current_point_index, point_label)
    else:
        messagebox.showinfo("Completion", "All points have been processed.")
        log_text.insert(tk.END, "All points have been processed.\n")


def skip_point(load_point, point_label):
    global current_point_index
    if current_point_index < len(timeseries_refs) - 1:
        current_point_index += 1
        load_point(current_point_index, point_label)
    else:
        messagebox.showinfo("Completion", "All points have been processed.")
        log_text.insert(tk.END, "All points have been processed.\n")


def save_rdf(log_text):
    if conn is None:
        messagebox.showerror("Error", "Please connect to the database first.")
        return

    g.serialize("brick_model_with_timeseries.ttl", format="turtle")
    log_text.insert(tk.END, "RDF model saved to 'brick_model_with_timeseries.ttl'.\n")
