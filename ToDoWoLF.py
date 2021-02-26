todos =[]#пустой список дел

menu = "1. Print \n" \
       "2. Add \n" \
       "3. Change \n" \
       "4. Delete \n" \
       "0. Exit"
def print_todos():
	print(*todos, sep = "\n")#печатать список
   
def add_todo():
        text = input("Введите задачу:" )#добавление задачи
        todos.append(text)

def change_todo():
    	x = int(input('введите номер задачи, которую хотите заменить: '))
    	text = input('введите новую задачу: ')
    	todos[x-1] = text
	
def delete_todo():
        x = int(input('введите номер задачи, которую хотите удалить: '))
        todos.pop(x-1)
	
print ('Welcome in ToDo!')  
   
while True:
    print(menu)
    command = input("Enter command:  " )
    if command not in ("1","2","3","4","0"):
            print("Error")
    elif command == "1":
            print_todos()
    elif command == "2":
            add_todo()
    elif command == '3':
        	change_todo()
    elif command == '4':
            delete_todo()
    elif command =='0':
       	break
       
       
       
#def delete_todo(index):
#    x = int(input('введите номер задачи, которую хотите удалить: '))
#	todos[x-1] = ''
	


#вместо ИФОВ МОЖНО ЗАВЕЗТИ СЛОВАРЬ
#dd= {"1": print_todos,
# "2:.."}
#dd[command]