#!/usr/bin/env python3
"""
Flask-based RESTful API for basic user management.

This API provides a set of HTTP endpoints for managing a collection of
users stored in memory.

Routes:
    - GET '/'                  : Returns a welcome message.
    - GET '/data'              : Returns a list of all registered usernames.
    - GET '/status'            : Returns the plain text message 'OK'.
    - GET '/users/<username>'  : Returns user data if the username exists.
    - POST '/add_user'         : Adds a new user using JSON data.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/', methods=['GET'])
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def data():
    """Return the list of all usernames."""
    return jsonify(list(users.keys())), 200


@app.route('/status', methods=['GET'])
def status():
    """Return the status message 'OK'."""
    return "OK", 200


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Return the user's data if found, or a 404 error."""
    if username in users:
        return jsonify(users[username]), 200
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the system using JSON input."""
    new_user = request.get_json()

    if not new_user:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user["username"]

    if username in users:
        return jsonify({"error": "User already exists"}), 400
