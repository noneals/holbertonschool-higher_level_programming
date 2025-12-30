#!/usr/bin/env python3
"""
Flask-based RESTful API for basic user management.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/", methods=["GET"])
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    """Return the list of all usernames."""
    return jsonify(list(users.keys())), 200


@app.route("/status", methods=["GET"])
def status():
    """Return the status message."""
    return "OK", 200


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return user data if found."""
    if username in users:
        return jsonify(users[username]), 200
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user using JSON input."""
    new_user = request.get_json()

    if not new_user:
        return jsonify({"error": "Invalid JSON"}), 400

    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user["us]()_
