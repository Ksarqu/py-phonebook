from os import system

def show_contacts():
    try:
        with open('phonebook.txt', 'r') as phonefiler:
            content = phonefiler.read()
            print(content)
    except FileNotFoundError:
        open('phonebook.txt', 'x').close()
        show_contacts()

while True:
    show_contacts()
    print("1-Add\n0-Exit")
    choice = int(input("What you want to do?"))
    if choice == 1:
        name = input("new contact name: ")
        number = input("new contact number: ")
        with open("phonebook.txt", "a") as number_file:
            number_file.write(f"{name} : {number}\n")
        system("cls")
    elif choice == 0:
        break


