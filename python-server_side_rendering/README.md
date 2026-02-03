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

## Requirements

- Python 3.x
- Flask (for Task 1)

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
├── task_01_jinja.py          # Flask application
└── templates/                 # HTML templates directory
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    └── contact.html
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

### Task 1: Flask Application

```bash
# Run the Flask application
python task_01_jinja.py
```

Visit `http://localhost:5000` in your browser to view the application.

Available routes:
- `/` - Home page
- `/about` - About page
- `/contact` - Contact page

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

## Author

Holberton School Student

## Repository

- **GitHub repository**: holbertonschool-higher_level_programming
- **Directory**: python-server_side_rendering
