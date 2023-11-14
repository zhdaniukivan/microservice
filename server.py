from flask import Flask, request, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('database.json')

@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form
    result = find_matching_template(data)
    return jsonify(result)

def find_matching_template(form_data):
    templates = db.all()

    for template in templates:
        template_fields = template.keys()