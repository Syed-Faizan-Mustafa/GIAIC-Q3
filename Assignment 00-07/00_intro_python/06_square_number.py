# def main():
#     sqr_num = float(input("Enter Number:"))
#     print(str(sqr_num) + "Square is" + str(sqr_num **2))

# if __name__ == "__main__":
#     main()

def main():
    num = float(input("Enter Number: "))
    sqr_num = num * num
    print(f"\033[1;3m{num} Squared is {sqr_num}\033[0m")
if __name__ == "__main__":
    main()
