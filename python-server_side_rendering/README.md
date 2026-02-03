# Python - Server Side Rendering

This project demonstrates server-side rendering concepts using Python, including templating and Flask web applications.

## Description

This repository contains tasks focused on server-side rendering techniques in Python:

1. **Task 0: Creating a Simple Templating Program**
   - Generate personalized invitation files from templates
   - Implement string templating with placeholders
   - Handle various error cases and edge conditions

2. **Task 1: Creating a Basic HTML Template in Flask**
   - Build a Flask application with Jinja templates
   - Create reusable header and footer components
   - Implement multiple pages with consistent layouts

3. **Task 2: Creating a Dynamic Template with Loops and Conditions**
   - Use Jinja's loop and conditional constructs
   - Read and parse JSON data
   - Display dynamic content based on data availability

4. **Task 3: Displaying Data from JSON or CSV Files**
   - Read and parse data from multiple file formats
   - Use query parameters to determine data sources
   - Implement filtering by product ID
   - Handle error cases for invalid inputs

5. **Task 4: Extending Dynamic Data Display to Include SQLite**
   - Set up and interact with SQLite database
   - Fetch and display data from multiple sources (JSON, CSV, SQL)
   - Implement comprehensive error handling

## Requirements

- Python 3.x
- Flask

## Installation

```bash
# Install Flask
pip install Flask
```

## Project Structure

```
python-server_side_rendering/
├── task_00_intro.py          # Templating program
├── template.txt               # Template file for invitations
├── task_01_jinja.py          # Flask application with basic templates
├── task_02_logic.py          # Flask app with dynamic content (loops/conditions)
├── task_03_files.py          # Flask app with JSON/CSV file support
├── task_04_db.py             # Flask app with SQLite database support
├── create_db.py              # Database setup script
├── items.json                # Sample items data
├── products.json             # Products data in JSON format
├── products.csv              # Products data in CSV format
├── products.db               # SQLite database (generated)
└── templates/                 # HTML templates directory
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── items.html
    └── product_display.html
```

## Usage

### Task 0: Simple Templating

```python
from task_00_intro import generate_invitations

# Read template
with open('template.txt', 'r') as file:
    template_content = file.read()

# Define attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", 
     "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", 
     "event_date": "2023-08-20", "event_location": "San Francisco"},
]

# Generate invitations
generate_invitations(template_content, attendees)
```

### Task 1: Flask Application with Basic Templates

```bash
# Run the Flask application
python task_01_jinja.py
```

Visit `http://localhost:5000` in your browser to view the application.

Available routes:
- `/` - Home page
- `/about` - About page
- `/contact` - Contact page

### Task 2: Dynamic Content with Loops and Conditions

```bash
# Run the Flask application
python task_02_logic.py
```

Visit:
- `http://localhost:5000/items` - View dynamic items list from JSON

### Task 3: Display Data from JSON or CSV Files

```bash
# Run the Flask application
python task_03_files.py
```

Visit:
- `http://localhost:5000/products?source=json` - View products from JSON
- `http://localhost:5000/products?source=csv` - View products from CSV
- `http://localhost:5000/products?source=json&id=1` - View specific product by ID

### Task 4: Display Data from SQLite Database

```bash
# First, create the database
python create_db.py

# Run the Flask application
python task_04_db.py
```

Visit:
- `http://localhost:5000/products?source=json` - View products from JSON
- `http://localhost:5000/products?source=csv` - View products from CSV
- `http://localhost:5000/products?source=sql` - View products from SQLite database
- `http://localhost:5000/products?source=sql&id=2` - View specific product by ID

## Features

### Task 0 Features
- String templating with placeholder replacement
- Error handling for invalid inputs
- Support for missing data (replaces with "N/A")
- Sequential output file generation

### Task 1 Features
- Flask web application
- Jinja template rendering
- Reusable header and footer components
- Multiple pages with consistent layout
- Navigation between pages

### Task 2 Features
- Dynamic content rendering using Jinja loops
- Conditional statements for empty data handling
- JSON file parsing
- Display items as unordered list

### Task 3 Features
- Multiple data source support (JSON and CSV)
- Query parameter routing
- Product filtering by ID
- Comprehensive error handling
- Table display format with styling

### Task 4 Features
- SQLite database integration
- Extended multi-source data display (JSON, CSV, SQL)
- Database error handling
- Consistent template rendering across all sources
- Product filtering from database queries

## Author

Holberton School Student

## Repository

- **GitHub repository**: holbertonschool-higher_level_programming
- **Directory**: python-server_side_rendering
