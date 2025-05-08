# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_many_numbers(numbers) -> int:
    """take a list of numbers and returns the sum of those numbers"""

    total_so_far_num : int = 0
    for number in numbers:
        total_so_far_num += number

    return total_so_far_num

def main():
    numbers : list[int] = [1,2,3,4,5,6,7,8,9,10] # make a list of number to sum.
    sum_of_numbers : int = add_many_numbers (numbers) # find the sum of the list.
    print(sum_of_numbers) # print the sum of numbers list.

if __name__ == "__main__":
    main()