todos =[]#пустой список дел

def print_todos():
    pass #печатать текст
def add_todo(text):
    pass

#todos.append(text):
    pass

def change_todo(index, text):
    pass
def delete_todo(index):
    pass

menu = "1. Print \n" \
       "2. Add \n" \
       "3. Change \n" \
       "4. Delete \n" \
       "0. Exit"
#вместо ИФОВ МОЖНО ЗАВЕЗТИ СЛОВАРЬ
#dd= {"1": print_todos,
# "2:.."}
#dd[command]
while True:
    print (menu)
    command = input ("Enter command")
    if command not in ["1","2","3","4","0"]:
        print("Error")
        continue
    if command == "1": 
        print_todos()
    elif command == "...":
        continue
