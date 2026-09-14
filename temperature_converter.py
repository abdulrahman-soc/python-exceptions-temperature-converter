conversion_history = []


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def show_history():
    if not conversion_history:
        print("No conversion history available.")
        return

    print("\nConversion History:")

    for conversion in conversion_history:
        print(conversion)


def main():
    while True:
        try:
            user_input = input(
                "Enter temperature and unit (e.g., 25 C or 77 F): "
            ).strip()

            if user_input.upper() == "H":
                show_history()
                continue

            value, unit = user_input.split()

            temperature = float(value)
            unit = unit.upper()

            if unit == "C":
                result = celsius_to_fahrenheit(temperature)
                message = f"{temperature} C = {result:.2f} F"

            elif unit == "F":
                result = fahrenheit_to_celsius(temperature)
                message = f"{temperature} F = {result:.2f} C"

            else:
                raise TypeError("Invalid temperature unit.")

            print(message)
            conversion_history.append(message)

        except ValueError:
            print("Invalid input. Please enter a number followed by C or F.")

        except TypeError as error:
            print(error)


if __name__ == "__main__":
    main()
    