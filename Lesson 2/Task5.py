# Task 5
user_name = "Kseniia"
user_password = "78945qwer"

while True:
    print("Введите имя пользователя: ")
    name = input()
    print("Введите пароль: ")
    password = input()
    if name == user_name and password == user_password:
        print("Password for user:", name, "is correct")
    else:
        print("Password for user:", name, "is incorrect")
        print("Please try again...")
