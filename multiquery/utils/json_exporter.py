import json
import os
from datetime import datetime

def export_to_json(file_path: str, query: str, responses: dict):
    """
    Exports the query and responses to a JSON file.

    :param file_path: Path to save the JSON file.
    :param query: The user query.
    :param responses: A dictionary with provider names as keys and responses as values.
    """
    # Ensure the directory exists
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    data = {
        "query": query,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "responses": responses,
    }

    # Format the datetime as a string
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path_with_timestamp = f"{file_path}_{timestamp}.json"

    with open(file_path_with_timestamp, "w") as file:
        json.dump(data, file, indent=4)