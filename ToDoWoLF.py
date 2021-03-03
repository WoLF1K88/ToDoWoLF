f = open("todo.txt", "a+")

todos =[]#пустой список дел
menu = "1. Print \n" \
       "2. Add \n" \
       "3. Change \n" \
       "4. Delete \n" \
       "0. Exit"
def print_todos():
        for i, text in enumerate(todos):
                print(i + 1, text)
	#	print(*todos, sep ='\n')#печатать список по строчно. * распаковывает аргументы построчно
   	 
def add_todo():
        todos.append(text)

def change_todo():
    	todos[x-1] = text
	
def delete_todo():
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
            text = input("Введите задачу:" )#добавление задачи
            add_todo()
            f.write(text)
    elif command == '3':
            x = int(input('введите номер задачи, которую хотите заменить: '))
            text = input('введите новую задачу: ')
            change_todo()
            f.write(text,'\n')
    elif command == '4':
            x = int(input('введите номер задачи, которую хотите удалить: '))
            delete_todo()
    elif command =='0':
       	break
f.writelines(todos)       
f.close()       
       


	


#вместо ИФОВ МОЖНО ЗАВЕЗТИ СЛОВАРЬ
#dd= {"1": print_todos,
# "2:.."}
#dd[command]