def main():
    degrees_fahrenheit = float(input("\033[1;3m Enter tenperature in fahrenheit: \033[0m"))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

if __name__ == "__main__":
    main()