from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
import re

app = Flask(__name__)
db = TinyDB('database.json')
User = Query()


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.values
    valid_data = create_dict(data)
    return jsonify(valid_data)


def create_dict(data):
    validated_dict = {}
    for key, value in data.items():
        validated_value = validate_data(key, value)
        validated_dict[key] = validated_value
    return validated_dict


def validate_data(key, value):



def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def is_valid_date(date):
    # Поддерживаем форматы DD.MM.YYYY и YYYY-MM-DD
    pattern = r'^(?:\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$'
    return bool(re.match(pattern, date))


def is_valid_phone(phone):
    pattern = r'^\+7[\s\-]?\d{3}[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$'
    return bool(re.match(pattern, phone))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
