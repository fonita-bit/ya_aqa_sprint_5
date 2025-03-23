# helpers/data.py

import random
import string

# Генерация уникального email
def generate_email():
    email = f"svetlanabratchenko19123{random.randint(100, 999)}@yandex.ru"
    return email

# Генерация пароля
def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # Длина пароля 8 символов
    return password
