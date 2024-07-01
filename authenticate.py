from conf import host, user, password, db_name
import psycopg2
def connect():
    global connection
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    global cursor
    cursor = connection.cursor()


# Функция регистрации нового пользователя
def register_user(email, username, password):
    #     hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (email, name, password) VALUES (%s, %s, %s)",
                   (email, username, password))
    connection.commit()


# Функция проверки аутентификации пользователя
def authenticate_user(username, password):
    # hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE name=%s AND password=%s",
                   (username, password))
    if cursor.fetchone():
        return True
    else:
        return False


def start():
    connect()
    choice = int(input('Выберете варриант:\n 1.Войти \n2.Зарегистрироваться:\n  '))

    if choice == 2:
        register_user(input('Введите свой email'), input('Введите свое имя '), input('Введите свой пароль '))
    elif choice == 1:
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        if authenticate_user(username, password):
            print("Аутентификация успешна!")
        else:
            print("Неверные имя пользователя или пароль.")

print(__name__)
if __name__ == '__main__':
    start()