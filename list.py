user_input = 'random'
data=[]

def show_menu():
    print('Menu:\n')
    print('1. Add an item')
    print('2. Mark it as done')
    print('3. View current items')
    print('4. Exit')

while user_input !='4':

    show_menu()
    user_input=input("Enter your choice:\n")

    if user_input=='1':
        item=input("What to you want to add?\n")
        data.append(item)
        print("Added item", item)

    elif user_input=='2':
        item= input('What is to be marked as done?\n')
        if item in data:
            data.remove(item)
            print("Removed item is:",item)
        else:
            print("Item doesn't exist in the list.\n")
    elif user_input=='3':
        print('To-do list items are:\n')
        for item in data:
            print(item)
    elif user_input=='4':
        print('Goodbye\n')
    else:
        print('Please enter correct choice from 1 to 4')
