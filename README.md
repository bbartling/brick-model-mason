# brick-model-mason

`brick-model-mason` is a Python application designed to assist in the creation of BRICK models from various data sources, with a focus on interactivity through a user-friendly Tkinter interface. The application connects to an existing SQLite database containing building automation system (BAS) points, allowing the user to step through each point interactively, configure it, and then construct an RDF model using the BRICK ontology. The final output is a Turtle (TTL) file representing the BRICK model. 

## Features

- **Interactive Interface:** The app uses a Tkinter-based graphical interface that allows users to step through and configure each BAS point individually.
- **Connect to SQLite Databases:** The app connects to an existing SQLite database, preventing accidental creation of new databases, and reads building automation data stored within.
- **Build Time Series References:** Supports the construction of time series references according to the BRICK schema: https://docs.brickschema.org/metadata/timeseries-storage.html.
- **RDF Model Construction:** Automatically builds an RDF model using the BRICK ontology based on user configurations.
- **Export to Turtle Format:** Users can export the final RDF model to a Turtle (.ttl) file after all points have been configured.
- **Skip and Review Points:** Allows users to skip certain points during the configuration process, ensuring only relevant data is included in the RDF model.

- TODO: Support for additional data sources (PostgreSQL, data lakes, etc.).
- TODO: BRICK model validation: https://docs.brickschema.org/metadata/timeseries-storage.html

### Prerequisites
- Python, I am using 3.12.x
- `rdflib` library

## Getting Started
```bash
pip install rdflib
```



