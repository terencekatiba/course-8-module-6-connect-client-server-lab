from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample event data
events = [
    {"id": 1, "title": "Python Workshop"},
    {"id": 2, "title": "Tech Conference"},
]


# Homepage route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Event Catalog!"})


# Get all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)


# Add a new event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    # Validate request data
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    # Create a unique ID
    new_id = max(event["id"] for event in events) + 1 if events else 1

    new_event = {
        "id": new_id,
        "title": data["title"],
    }

    events.append(new_event)

    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)
