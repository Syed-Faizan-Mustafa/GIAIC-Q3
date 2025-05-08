def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

def main():
    message = input("\033[1;3mEnter a Message to Copy: \033[0m")
    my_list = []
    print("list before", my_list)
    add_three_copies(my_list,message)
    print("list after", my_list)
   
if __name__ == "__main__":
    main()
# list has been append due to list is mutable. before append list was epmty after append list is immutable.