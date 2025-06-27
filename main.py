import lmstudio as lms # Подключаем скачанную библиотеку (даём псевдоним)

# Помещаем список скачанных моделей в переменную     
list_models = lms.list_downloaded_models()

with lms.Client() as client: # Устанавливает соединение с сервером модели
    model = client.llm.model("yandexgpt-5-lite-8b-instruct")
    
    while True:
        request = input("Введите запрос: ") # Ввод от пользователя
        result = model.respond(request) # Передаём ввод пользователя модели
        print(result)