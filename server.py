from flask import Flask, request, jsonify, make_response
from tinydb import TinyDB
import re

app = Flask(__name__)
db = TinyDB('database.json')


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.values
    valid_data = create_dict(data)
    result = check_data_base(valid_data)
    return jsonify(result)


def check_data_base(valid_data):
    temporary = {}
    bd_data = db.all()
    for i in bd_data:
        for j in i.items():
            if j[0] == 'form_name' and not temporary:
                temporary.update({j[0]: j[1]})
                print(temporary)

            elif not i.get(j[0]) == valid_data.get(j[0]) and j[0] in valid_data:
                temporary = {}

    if temporary:
        return temporary
    else:
        return valid_data


def create_dict(data):
    validated_dict = {}
    for key, value in data.items():
        validated_value = validate_data(key, value)
        validated_dict[validated_value[0]] = validated_value[1]
    return validated_dict


def validate_data(key, value):
    if is_valid_date(value) and key == "user_order_date":
        return (key := "user_order_date", value := "date")

    elif is_valid_phone(value) and key == "user_phone":
        return (key := "user_phone", value := "phone")

    elif is_valid_email(value) and key == "user_email":
        return (key := "user_email", value := "email")

    elif key == "user_text":
        return (key := "user_text", value := "text")
    else:
        return (key, value)


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
