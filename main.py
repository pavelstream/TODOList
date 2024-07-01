# import conf
from authenticate import start

class Task:
    def __init__(self, task):
        pass


class TODOList:
    def __init__(self):
        self.tasks = dict()  #In future i will have to replace the sheet with the database

    def new_task(self, task):
        self.task = task

    def description_task(self, description):
        self.description = description

    def mark(self, status=False):
        self.status = status

    def add_task(self):
        self.new_task(input('Введите новую задачу: '))
        self.description_task(input('Введите описание задачи: '))
        self.mark()
        self.tasks[self.task] = {'id' : len(self.tasks), 'описание': self.description, 'статус': self.status}


    def run(self):
        start()
        while True:
            print("\nTODO List:")
            if self.tasks == False:
                print('List is empty(Список пустой)')
            else:
                self.print_tasks()

            print("\nMenu:")
            print("1. Добавить задачу")
            print("2. Изменить статус задачи")
            print("3. Выход")

            choice = input("Enter your choice : ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                new_mark = int(input('Введите номер задачи: '))
                self.tasks[list(self.tasks.keys())[new_mark]]['статус'] = True

            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Неверный выбор. Пожалуйста введите 1, 2, или 3.")


def main():
    todo_list = TODOList()
    todo_list.run()


if __name__ == "__main__":
    main()