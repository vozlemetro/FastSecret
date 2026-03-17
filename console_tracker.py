#по приколу добавил
tasks = []
completed = []
while True:
    print(f'текущий список задач: {tasks}')
    print(
    '1.Добавить задачу\n' \
    '2.Удалить задачу\n' \
    '3.Просмотреть выплненные задачи\n' \
    '0.Выход')
    choice = int(input())
    if choice == 1:
        print('Какую задачу хотите добавить?')
        task = input()
        tasks.append(task)
    elif choice == 2:
        print("Какую задачу хотите удалить?")
        length = len(tasks)
        number = int(input())
        if (number <= length and number > 0):
            completed.append(tasks[number-1])
            del tasks[number-1]
        else:
            print('Вы ввели Неверное число число')
    elif choice == 3:
        print("Вот ваши выполненные задачи:")
        print(completed)    
    else:
        print('Завершение..')
        break        
