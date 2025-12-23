# Python Serialization Project

## 📋 Overview

This project focuses on data serialization and marshaling techniques in Python. Through hands-on implementation, students explore various serialization formats including JSON, Pickle, CSV, and XML, while understanding their practical applications in modern software development.

---

## 🎯 What You'll Learn

### Core Concepts
* **Serialization** - Converting data structures into formats suitable for storage or transmission
* **Marshaling** - Packaging complex objects for cross-platform communication
* **Data Persistence** - Maintaining object states across program executions
* **Network Communication** - Transmitting serialized data between systems

### Technical Skills
* JSON data interchange format
* Python's pickle module for object serialization
* CSV file processing and conversion
* XML structure creation and parsing
* Socket programming for network applications

---

## 🛠️ Technologies Used
```
Python 3.8.5
JSON Module
Pickle Module
CSV Module
XML ElementTree
Socket Programming
```

---

## 📁 Project Structure
```
python-serialization/
│
├── task_00_basic_serialization.py    # JSON serialization basics
├── task_01_pickle.py                 # Custom object pickling
├── task_02_csv.py                    # CSV to JSON converter
├── task_03_xml.py                    # XML serialization
└── task_04_net.py                    # Network serialization demo
```

---

## 💻 Tasks Overview

### Task 0: JSON Serialization Fundamentals
Learn to save Python dictionaries to JSON files and reload them back into memory.

**Functions:**
- `serialize_and_save_to_file(data, filename)`
- `load_and_deserialize(filename)`

### Task 1: Object Persistence with Pickle
Create a custom class that can save and restore itself using Python's pickle module.

**Class:** `CustomObject`
**Methods:** `serialize()`, `deserialize()`, `display()`

### Task 2: Data Format Conversion
Convert CSV spreadsheet data into JSON format for web applications.

**Function:** `convert_csv_to_json(csv_filename)`

### Task 3: XML Data Structures
Work with XML for enterprise-level data interchange.

**Functions:**
- `serialize_to_xml(dictionary, filename)`
- `deserialize_from_xml(filename)`

### Task 4: Network Data Transfer
Build a client-server application demonstrating serialization in network communication.

**Functions:** `start_server()`, `send_data(data)`

---

## ⚙️ Requirements

| Requirement | Details |
|------------|---------|
| **Python Version** | 3.8.5 |
| **Style Guide** | PEP 8 (pycodestyle 2.7.*) |
| **Documentation** | Required for all functions |
| **File Permissions** | All files executable |

---

## 🎓 Learning Outcomes

By completing this project, you will:

1. ✅ Understand different serialization formats and their use cases
2. ✅ Implement data persistence in Python applications
3. ✅ Convert between various data formats (JSON, CSV, XML)
4. ✅ Build network applications with serialized data transfer
5. ✅ Handle errors in file I/O and network operations

---

## 👤 Developer

**Student Developer**
- GitHub: [@noneals](https://github.com/illo888)
- Email: none.als012@gmail.com

---

## 📚 Additional Resources

- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Pickle Module Guide](https://docs.python.org/3/library/pickle.html)
- [CSV File Reading](https://docs.python.org/3/library/csv.html)
- [XML Processing](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Socket Programming](https://docs.python.org/3/library/socket.html)
