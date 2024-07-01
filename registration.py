#import hashlib
import psycopg2
from conf import host, user, password, db_name

try:
    connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
    )


    cursor = connection.cursor()

except Exception as ex:
      print('ERROR ', ex)


def register_user(task, description, status, users_id):
    #     hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO tasks (task, description, status, users_id) VALUES (%s, %s, %s, %s)",
                   (task, description, status, users_id))
    connection.commit()

username ='ekt'
cursor.execute("SELECT id FROM users WHERE name='ekt'")
id = cursor.fetchone()[0]
register_user(input('task'), input('description'), 'NO', id)

