import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from functions import (
    connect_to_db,
    load_point,
    update_sensor_options,
    add_to_rdf,
    skip_point,
    save_rdf,
)
from sensor_options import sensor_options, unit_options

# Tkinter setup
root = tk.Tk()
root.title("Brick RDF Builder")
root.geometry("800x600")  # Set larger default window size


# Function to browse for a database file
def browse_db():
    db_path = filedialog.askopenfilename(
        title="Select SQLite Database",
        filetypes=[("SQLite Database Files", "*.db"), ("All Files", "*.*")],
    )
    if db_path:
        db_entry.delete(0, tk.END)
        db_entry.insert(0, db_path)


# SQLite connection entry and buttons
db_label = tk.Label(root, text="SQLite DB Path:")
db_label.pack()

db_entry = tk.Entry(root, width=50)
db_entry.insert(0, "brick_timeseries.db")
db_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_db)
browse_button.pack()

connect_button = tk.Button(
    root,
    text="Connect to DB",
    command=lambda: connect_to_db(db_entry, log_text, point_label, load_point),
)
connect_button.pack()

# Point display label
point_label = tk.Label(root, text="No points loaded.")
point_label.pack()

# Button to skip point
skip_button = tk.Button(
    root, text="Skip Point", command=lambda: skip_point(load_point, point_label)
)
skip_button.pack()

# Dropdown for System Type
system_label = tk.Label(root, text="System Type:")
system_label.pack()
system_type = ttk.Combobox(root, values=sensor_options.keys(), width=30)
system_type.pack()

# Dropdown for Sensor Type (initially empty)
sensor_label = tk.Label(root, text="Sensor/Setpoint Type:")
sensor_label.pack()
sensor_type = ttk.Combobox(root, width=70)
sensor_type.pack()

# Dropdown for Unit
unit_label = tk.Label(root, text="Unit:")
unit_label.pack()
unit_type = ttk.Combobox(root, values=unit_options, width=70)
unit_type.pack()

system_type.bind(
    "<<ComboboxSelected>>",
    lambda event: update_sensor_options(sensor_options, system_type, sensor_type),
)

# Button to add to RDF
add_button = tk.Button(
    root,
    text="Add to RDF",
    command=lambda: add_to_rdf(
        db_entry, sensor_type, system_type, unit_type, log_text, load_point, point_label
    ),
)
add_button.pack()

# Button to save RDF
save_button = tk.Button(root, text="Save RDF", command=lambda: save_rdf(log_text))
save_button.pack()

# Log output text box (scrollable)
log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
log_text.pack()

root.mainloop()
