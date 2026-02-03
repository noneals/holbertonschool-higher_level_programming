#!/usr/bin/python3
"""
Module for generating personalized invitation files from a template.
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendees list.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee information
    
    Returns:
        None: Writes output files or logs error messages
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees is not a list")
        return
    
    # Check if attendees is a list of dictionaries
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees is not a list of dictionaries")
        return
    
    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Start with the original template
        processed_template = template
        
        # Replace placeholders with actual values or "N/A"
        processed_template = processed_template.replace(
            "{name}", 
            str(attendee.get("name", "N/A")) if attendee.get("name") is not None else "N/A"
        )
        processed_template = processed_template.replace(
            "{event_title}", 
            str(attendee.get("event_title", "N/A")) if attendee.get("event_title") is not None else "N/A"
        )
        processed_template = processed_template.replace(
            "{event_date}", 
            str(attendee.get("event_date", "N/A")) if attendee.get("event_date") is not None else "N/A"
        )
        processed_template = processed_template.replace(
            "{event_location}", 
            str(attendee.get("event_location", "N/A")) if attendee.get("event_location") is not None else "N/A"
        )
        
        # Write to output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(processed_template)
            print(f"Generated {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
