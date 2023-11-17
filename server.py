from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
import re
from typing import Tuple
import phonenumbers

app = Flask(__name__)
db = TinyDB('database.json')
User = Query()


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.values
    validated_data = [check_field(i, j) for i, j in data.items()]
    result = check_form_in_db(validated_data)
    return jsonify(result)


def check_form_in_db(validated_data) -> Tuple[str, str]:
    """эта функция проверяет есть ли совпадение у запроса '/get_form' с формами в базе данны"""
    temporary = None
    forms = db.all()
    for form in forms:
        for item in form.items():  # перебираем построчно все формы из базы данных и сравниваем с нашим запросом
            if item[0] == "form_name" and temporary is None:
                temporary = item[1]
            elif item not in validated_data:

                temporary = None
        if temporary:  # при нахождении формы отпраляем ее пользователю и на этом поиск останавливаем.
            return temporary
    else:
        return validated_data


def check_field(key: str, value: str) -> Tuple[str, str]:
    if key == "user_order_date" and is_valid_date(value):
        return "user_order_date", 'date'
    elif key == "user_phone" and is_valid_phone(value):
        return "user_phone", "phone"
    elif key == "user_email" and is_valid_email(value):
        return "user_email", "email"
    else:
        return "user_text", "text"


def is_valid_date(date: str) -> bool:
    # Поддерживаем форматы DD.MM.YYYY и YYYY-MM-DD
    pattern = r'^(?:\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$'
    return bool(re.match(pattern, date))


def is_valid_phone(value: str) -> bool:
    try:
        parsed_phone = phonenumbers.parse(value, None)
        return phonenumbers.is_valid_number(parsed_phone)
    except phonenumbers.NumberParseException:
        return False


def is_valid_email(email: str) -> bool:
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return bool(re.match(pat, email))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
