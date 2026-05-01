"""
CampusFind Backend — Flask API
Run: python app.py
Runs on: http://localhost:5000
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to call this API

# ── File Paths ──────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

LOST_FILE    = os.path.join(DATA_DIR, "lost_items.json")
FOUND_FILE   = os.path.join(DATA_DIR, "found_items.json")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.json")

# ── Helper: Read JSON ────────────────────────────────────────
def read_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# ── Helper: Write JSON ───────────────────────────────────────
def write_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ════════════════════════════════════════════════════════════
#  ROUTES
# ════════════════════════════════════════════════════════════

@app.route("/")
def home():
    return jsonify({
        "message": "CampusFind API is running!",
        "endpoints": {
            "GET  /api/lost"          : "All lost items",
            "GET  /api/found"         : "All found items",
            "GET  /api/students"      : "All student ID details",
            "GET  /api/lost/<id>"     : "Single lost item by ID",
            "GET  /api/found/<id>"    : "Single found item by ID",
            "GET  /api/student/<roll>": "Single student by roll number",
            "POST /api/lost"          : "Report a new lost item",
            "POST /api/found"         : "Report a new found item",
            "GET  /api/search?q=term" : "Search across lost and found"
        }
    })

# ── GET all lost items ───────────────────────────────────────
@app.route("/api/lost", methods=["GET"])
def get_lost_items():
    items = read_json(LOST_FILE)
    return jsonify({"success": True, "count": len(items), "data": items})

# ── GET all found items ──────────────────────────────────────
@app.route("/api/found", methods=["GET"])
def get_found_items():
    items = read_json(FOUND_FILE)
    return jsonify({"success": True, "count": len(items), "data": items})

# ── GET all students ─────────────────────────────────────────
@app.route("/api/students", methods=["GET"])
def get_students():
    students = read_json(STUDENTS_FILE)
    return jsonify({"success": True, "count": len(students), "data": students})

# ── GET single lost item by ID ───────────────────────────────
@app.route("/api/lost/<item_id>", methods=["GET"])
def get_lost_item(item_id):
    items = read_json(LOST_FILE)
    item = next((i for i in items if i["id"] == item_id.upper()), None)
    if item:
        return jsonify({"success": True, "data": item})
    return jsonify({"success": False, "message": "Item not found"}), 404

# ── GET single found item by ID ──────────────────────────────
@app.route("/api/found/<item_id>", methods=["GET"])
def get_found_item(item_id):
    items = read_json(FOUND_FILE)
    item = next((i for i in items if i["id"] == item_id.upper()), None)
    if item:
        return jsonify({"success": True, "data": item})
    return jsonify({"success": False, "message": "Item not found"}), 404

# ── GET student by roll number ───────────────────────────────
@app.route("/api/student/<roll_no>", methods=["GET"])
def get_student(roll_no):
    students = read_json(STUDENTS_FILE)
    student = next((s for s in students if s["roll_no"] == roll_no.upper()), None)
    if student:
        return jsonify({"success": True, "data": student})
    return jsonify({"success": False, "message": "Student not found"}), 404

# ── POST: Report new lost item ───────────────────────────────
@app.route("/api/lost", methods=["POST"])
def report_lost_item():
    body = request.get_json()
    required = ["student_id", "student_name", "item_name", "description",
                "category", "location", "date_lost", "contact"]
    for field in required:
        if field not in body:
            return jsonify({"success": False, "message": f"Missing field: {field}"}), 400

    items = read_json(LOST_FILE)
    new_id = f"L{str(len(items) + 1).zfill(3)}"
    new_item = {
        "id": new_id,
        "student_id": body["student_id"],
        "student_name": body["student_name"],
        "item_name": body["item_name"],
        "description": body["description"],
        "category": body["category"],
        "location": body["location"],
        "date_lost": body["date_lost"],
        "contact": body["contact"],
        "status": "searching",
        "image_url": body.get("image_url", ""),
        "reward": body.get("reward", "No")
    }
    items.append(new_item)
    write_json(LOST_FILE, items)
    return jsonify({"success": True, "message": "Lost item reported!", "data": new_item}), 201

# ── POST: Report new found item ──────────────────────────────
@app.route("/api/found", methods=["POST"])
def report_found_item():
    body = request.get_json()
    required = ["finder_student_id", "finder_name", "item_name", "description",
                "category", "location_found", "date_found", "contact"]
    for field in required:
        if field not in body:
            return jsonify({"success": False, "message": f"Missing field: {field}"}), 400

    items = read_json(FOUND_FILE)
    new_id = f"F{str(len(items) + 1).zfill(3)}"
    new_item = {
        "id": new_id,
        "finder_student_id": body["finder_student_id"],
        "finder_name": body["finder_name"],
        "item_name": body["item_name"],
        "description": body["description"],
        "category": body["category"],
        "location_found": body["location_found"],
        "date_found": body["date_found"],
        "contact": body["contact"],
        "status": "available",
        "image_url": body.get("image_url", ""),
        "handed_to_admin": body.get("handed_to_admin", False)
    }
    items.append(new_item)
    write_json(FOUND_FILE, items)
    return jsonify({"success": True, "message": "Found item reported!", "data": new_item}), 201

# ── GET: Search across lost and found ───────────────────────
@app.route("/api/search", methods=["GET"])
def search_items():
    query = request.args.get("q", "").lower()
    if not query:
        return jsonify({"success": False, "message": "Provide ?q=search_term"}), 400

    lost_items = read_json(LOST_FILE)
    found_items = read_json(FOUND_FILE)

    matched_lost = [
        i for i in lost_items
        if query in i["item_name"].lower()
        or query in i["description"].lower()
        or query in i["category"].lower()
        or query in i["location"].lower()
    ]
    matched_found = [
        i for i in found_items
        if query in i["item_name"].lower()
        or query in i["description"].lower()
        or query in i["category"].lower()
        or query in i["location_found"].lower()
    ]

    return jsonify({
        "success": True,
        "query": query,
        "lost_matches": matched_lost,
        "found_matches": matched_found,
        "total": len(matched_lost) + len(matched_found)
    })


if __name__ == "__main__":
    print("CampusFind API starting on http://localhost:5000")
    app.run(debug=True, port=5000)
