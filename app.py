from flask import Flask, render_template, request

app = Flask(__name__) # Создаём объект, который ответственен за работу сайта

@app.route('/', methods=['GET', 'POST']) # Определяем маршрут для создания главной страницы сайта
def index():
    if request.method == 'POST':
        text = request.form.get("text", '')
        print(text)
    # Возвращаем html-файл который будет отображаться по заданному маршруту
    return render_template("index.html") 

app.run()  # Даём комманду для запуска проекта 