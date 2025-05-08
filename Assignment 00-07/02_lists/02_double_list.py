# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# # numbers = [2, 4, 6, 8]
def main():
    
    numbers : list[int] = [1,2,3,4,5] #loop through the indices of the list.
    for i in range(len(numbers)):
        element_at_index = numbers[i] #Get the element at index i in the numbers list.
        numbers[i] = element_at_index * 2
    print(f"\033[1;3m your list is now doubled:\033[0m", numbers) #it will print the double number list

if __name__ == "__main__":
    main()