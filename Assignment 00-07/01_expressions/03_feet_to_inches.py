per_feet: int = 12
def main():
    value_in_feet: float = float(input("Enter Value in Foot/Feet:")) 
    total_inches = value_in_feet * (per_feet)
    print(f"User Input in Feet: {value_in_feet}, Convert into inches: {total_inches}")

if __name__ == "__main__":
    main()
    