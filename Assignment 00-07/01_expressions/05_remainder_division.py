
def main():
     # Get the numbers we want to divide
     num : int = int(input("\033[1;3m Please Enter the number to be divide \033[0m")) 
     divided_by : int = int(input("\033[1;3m Please Enter the number to be divide \033[0m"))

     quotient : int = num // divided_by # just divide the number 
     remainder : int = num % divided_by # get remiander of the division(modulas)

     print(f"The Result of this division is: {quotient} with a remiander of {remainder}")

if __name__ == "__main__":
     main()