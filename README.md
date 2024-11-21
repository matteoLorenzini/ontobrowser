# Ontology Visualizer

Ontology Visualizer is a Django web application that allows users to upload and visualize ontologies in RDF and OWL formats. The application provides a hierarchical view of the ontology classes and properties, and displays detailed information about selected classes and properties.

## Features

- Upload ontology files from the local machine.
- Load existing ontologies from a predefined folder.
- Visualize ontology classes and properties in a hierarchical tree structure.
- Display detailed information about selected classes and properties.

## Setup

### Prerequisites

- Python 3.6+
- Django 3.0+
- RDFLib

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ontology_visualizer.git
    cd ontology_visualizer
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create the `ontologies` directory to store existing ontologies:

    ```bash
    mkdir ontologies
    ```

5. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

6. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

### Landing Page

The landing page provides two options:

1. **Load Ontology from Local Machine**: Upload an ontology file from your local machine.
2. **Load Existing Ontology**: Select and load an ontology from the `ontologies` directory.

### Ontology Visualization

Once an ontology is loaded, the application displays the ontology classes and properties in a hierarchical tree structure. Click on a class or property to view detailed information in the right sidebar.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.