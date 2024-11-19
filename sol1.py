import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Простой список пользователей для авторизации (с добавлением имени)
users = {
    "user1": {"password": "password1", "name": "Иван Иванов"},
    "user2": {"password": "password2", "name": "Мария Петрова"}
}


def authenticate():
    username = entry_username.get()
    password = entry_password.get()

    # Проверяем, есть ли пользователь с таким логином и паролем
    if username in users and users[username]["password"] == password:
        open_profile(username)  # Передаем имя пользователя
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")


def open_profile(username):
    # Закрываем окно авторизации
    auth_window.destroy()

    # Получаем имя пользователя
    user_name = users[username]["name"]

    # Окно профиля
    profile_window = tk.Tk()
    profile_window.title("Личный профиль")

    # Загружаем фото пользователя
    try:
        photo = Image.open("profile_picture.jpg")  # Предполагаем, что у всех пользователей одно фото
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Фото не найдено")
        return

    photo = photo.resize((150, 150))  # Уменьшаем фото до нужного размера
    photo = ImageTk.PhotoImage(photo)

    label_photo = tk.Label(profile_window, image=photo)
    label_photo.image = photo  # Сохраняем ссылку на изображение
    label_photo.pack(pady=10)

    # Текст с приветствием и именем пользователя
    label_welcome = tk.Label(profile_window, text=f"Добро пожаловать, {user_name}!", font=("Arial", 14))
    label_welcome.pack(pady=10)

    # Цветовая раскраска
    profile_window.config(bg="#ADD8E6")
    label_welcome.config(bg="#ADD8E6")

    profile_window.mainloop()


# Окно авторизации
auth_window = tk.Tk()
auth_window.title("Авторизация")

# Поля для ввода
label_username = tk.Label(auth_window, text="Логин:")
label_username.pack(pady=5)
entry_username = tk.Entry(auth_window)
entry_username.pack(pady=5)

label_password = tk.Label(auth_window, text="Пароль:")
label_password.pack(pady=5)
entry_password = tk.Entry(auth_window, show="*")
entry_password.pack(pady=5)

# Кнопка авторизации
button_login = tk.Button(auth_window, text="Войти", command=authenticate)
button_login.pack(pady=10)

# Цветовая раскраска
auth_window.config(bg="#FFEB3B")
label_username.config(bg="#FFEB3B")
label_password.config(bg="#FFEB3B")

auth_window.mainloop()
