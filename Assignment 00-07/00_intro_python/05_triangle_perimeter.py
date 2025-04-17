def main():
    left_side = float(input("Enter left side length:"))
    right_side = float(input("Enter right side length:"))
    bottom_side = float(input("Enter bottom side length:"))

    perimeter = left_side + right_side + bottom_side

    print(f"\033[1;3m the total length of trinagle is : {perimeter}\033[0")

if __name__ == "__main__":
    main()