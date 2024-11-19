import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def show_food_details(food_name):
    food_details = {
        "Пицца": "Вкусная пицца с сыром и колбасками пепперони",
        "Суши": "Свежие суши с рыбой и огурцами",
        "Бургер": "Сочный бургер с говядиной, сыром и свежими овощами."
    }

    details = food_details.get(food_name, "Информация отсутствует")

    # Окно с деталями о еде
    details_window = tk.Tk()
    details_window.title(f"Подробности о {food_name}")

    # Изображение еды
    try:
        image = Image.open(f"{food_name.lower()}.jpg")  # Ожидается, что изображение будет называться "пицца.jpg", "суши.jpg" и т.д.
        image = image.resize((200, 200))
        image = ImageTk.PhotoImage(image)

        label_image = tk.Label(details_window, image=image)
        label_image.image = image
        label_image.pack(pady=10)
    except FileNotFoundError:
        label_image = tk.Label(details_window, text="Изображение не найдено", font=("Arial", 12))
        label_image.pack(pady=10)

    label_info = tk.Label(details_window, text=details, font=("Arial", 12))
    label_info.pack(pady=10)

    # Создаем метку с выбранным блюдом
    label_selected = tk.Label(details_window, text=f"Вы выбрали {food_name}", font=("Arial", 14, "bold"), fg="green")
    label_selected.pack(pady=10)

    details_window.mainloop()

def main_app():
    app = tk.Tk()
    app.title("Приложение с едой")

    # Кнопки для выбора еды
    button_pizza = tk.Button(app, text="Пицца", command=lambda: show_food_details("Пицца"))
    button_pizza.pack(pady=10)

    button_sushi = tk.Button(app, text="Суши", command=lambda: show_food_details("Суши"))
    button_sushi.pack(pady=10)

    button_burger = tk.Button(app, text="Бургер", command=lambda: show_food_details("Бургер"))
    button_burger.pack(pady=10)

    # Цветовая раскраска
    app.config(bg="#FFE4B5")
    button_pizza.config(bg="#FF7F50")
    button_sushi.config(bg="#FF7F50")
    button_burger.config(bg="#FF7F50")

    app.mainloop()

main_app()
