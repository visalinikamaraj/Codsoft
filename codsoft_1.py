todos=[]
def get_from_file(a):
   with open(a,"r")as file:
    todos=file.readlines()
        

def put_into_file(a):

   with open(a,'w')as file:
    file.writelines(todos)
     
   
while (True):
    user_option=input("ADD:SHOW:REPLACE:COMPLETE:EXIT:")
    
    
    if 'add' in user_option:
        todo=user_option[4:]+"\n"
        todos.append(todo)
        put_into_file("list.txt")
   

    elif 'show' in user_option:
        get_from_file("list.txt")
        
        new_todos=[item.strip('\n')for item in todos ]

        for index,item in enumerate(new_todos):
            myitem=f"{index+1}---{item}"
            print(myitem)


    elif 'replace' in user_option:
     try:
        lastindex=int(user_option[8:])
        lastindex=lastindex-1

        replaceditem=input("newone:")
        todos[lastindex]=replaceditem
        put_into_file("list.txt")
     except Exception as e:
        print (e)       
            

    elif 'complete' in user_option:
     try:
        removeindex=int(user_option[9:])
        todos.pop(removeindex-1)
        put_into_file("list.txt")
        print(todos)    
     except Exception as e:
        print (e)               
        
    
    elif 'exit' in user_option:
        break  
    
    
    else:
        print("invalid option")   
        user_option=input("ADD\tSHOW\tREPLACE\tCOMPLETE\tEXIT:")
                
print("quit")                    