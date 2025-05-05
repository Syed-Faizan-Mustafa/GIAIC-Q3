import math
def main():
    # Get the two side lengths from the user and cast them to be numbers
    AB :float = float(input("\033[1;3m Enter The Length of AB:\033[0m"))
    AC :float = float(input("\033[1;3m Enter The Length of AC:\033[0m]"))
    
       # Calculate the hypotenuse using the two sides and print it out
    BC :float = math.sqrt(AB**2 + AC**2)
    print("The length of BC (The Hypotenuse) is:" + str(BC))

if __name__ == "__main__":
    main()



