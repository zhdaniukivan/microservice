Описание микросервиса:
Представляю вам микросервис для обработки POST запросов по URL http://127.0.0.1:5000/get_form, где можно передавать 
неограниченное количество именованных параметров вида f_name1=value1&f_name2=value2. Микросервис обрабатывает запросы с 
встроенной валидацией данных по типам: дата, телефон, email, текст. Приложение проверяет валидность данных и подбирает 
соответствующую форму из базы данных в случае совпадения.

Установка и запуск:
git clone https://github.com/zhdaniukivan/microservice.git
переходим в директорию проекта на linux это команда:
cd microservice
если env автоматически не ативировалась то выполните следующие 4 комады:
pip install --upgrade pip 
pip install virtualenv
virtualenv venv
source venv/bin/activate

устанавливаем необходимые модули:
pip install -r requirements.txt

Запуск сервера:
python server.py

Вы можете использовать следующий URL для тестирования в Insomnia:
POST "http://127.0.0.1:5000/get_form?user_email=2819815@mail.ru&user_phone=+7 495 734-92-00&user_order_date=17.03.1988&user_text=Мне коктейль без льда.&same_data=это просто лишний текст"

Запуск автотестов:
python test_server.py

Tехнологии в проекте: Flask TinyDB Unittest

