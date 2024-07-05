# import conf
from add_tasks import foreign_key, add_task
from authenticate import register_user, authenticate_user
from print_tasks import print_task


class Task:
    def __init__(self, task):
        pass


class TODOList:
    def __init__(self):
        # self.tasks = dict()  # In future i will have to replace the sheet with the database
        self.name = ''

    def new_task(self, task):
        self.task = task

    def description_task(self, description):
        self.description = description

    def mark(self, status=False):
        self.status = status

    def add_task(self):
        task = input('Напишите новую задачу:\n ')
        describtion = input('Напишите описание к задаче:\n ')
        name = self.name
        add_task(task=task, description=describtion, name_user=name)
        # self.new_task(input('Введите новую задачу: '))
        # self.description_task(input('Введите описание задачи: '))
        # self.mark()
        # self.tasks[self.task] = {'id': len(self.tasks), 'описание': self.description, 'статус': self.status}

    # def print_tasks(self):
    #     print(self.tasks)

    def run(self):
        choice = 0
        while choice != 1:
            choice = int(input('Выберете вариант:\n 1.Войти \n2.Зарегистрироваться:\n3. Выход:\n  '))
            if choice == 2:
                register_user(input('Введите свой email'), input('Введите свое имя '), input('Введите свой пароль '))
            elif choice == 1:
                self.name = input("Введите имя пользователя: ")
                password = input("Введите пароль: ")
                authenticate_user(self.name, password)
                print("Аутентификация успешна!")
                while True:
                    print("\nTODO List:")
                    # if self.tasks == False:
                    #     print('List is empty(Список пустой)')
                    # else:
                    #     self.print_tasks()

                    print("\nMenu:")
                    print("1. Добавить задачу")
                    # print("2. Изменить статус задачи")
                    print("3. Показать мои задачи. ")
                    print("4. Выход")

                    choice = input("Enter your choice : ")

                    if choice == '1':
                        self.add_task()
                    elif choice == '2':
                        new_mark = int(input('Введите номер задачи: '))
                        self.tasks[list(self.tasks.keys())[new_mark]]['статус'] = True
                    elif choice == '3':
                        print(*print_task(foreign_key(self.name)), sep= '\n')
                    elif choice == '4':
                        print("Exiting...")
                        break
                    else:
                        print("Неверный выбор. Введите верный номер.")


def main():
    todo_list = TODOList()
    todo_list.run()


if __name__ == "__main__":
    main()
