def main():
    lst = []  # Make an empty list to store things in

    val = input("\033[94mEnter a value: ")  # Get an initial value
    while val:  # While the user input isn't an empty value
        lst.append(val) # Add val to list
        val = input("\033[94mEnter a value: ")  # Get the next value to add

    print("Here's the list:\033[0m", lst)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()