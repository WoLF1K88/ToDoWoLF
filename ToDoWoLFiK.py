todos =[]#пустой список дел
menu = "1. Print \n" \
       "2. Add \n" \
       "3. Change \n" \
       "4. Delete \n" \
       "0. Exit"
def print_todos():
   print(todos)#печатать список
def add_todo(text):
        text = input("Введите задачу:" )#добавление задачи
        todos.append(text)
        return text
while True:
    print(menu)
    command = input("Enter command:  " )
    if command not in ("1","2","3","4","0"):
            print("Error")
    elif command == "1": 
            print_todos()
    elif command == "2":
            add_todo
       



def change_todo(index, text):
    pass
def delete_todo(index):
    pass


#вместо ИФОВ МОЖНО ЗАВЕЗТИ СЛОВАРЬ
#dd= {"1": print_todos,
# "2:.."}
#dd[command]
