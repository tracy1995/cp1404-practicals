def load_color_codes(file_path):
    """
    Load color codes from a file and return them as a dictionary.
    """
    color_codes = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Non-empty line
                parts = line.split('\t')
                color_name = parts[0]
                hex_code = parts[1]
                color_codes[color_name] = hex_code
    return color_codes


def main():
    color_file = "colors.txt"  # Update the file path accordingly
    color_codes = load_color_codes(color_file)

    print("Welcome to the Hexadecimal Color Code Lookup Tool!")
    print("Type 'quit' to exit.")

    while True:
        color_name = input("Enter a color name: ").strip()

        if color_name.lower() == 'quit':
            print("Exiting...")
            break

        if color_name in color_codes:
            print(f"The hexadecimal color code for {color_name} is {color_codes[color_name]}.")
        else:
            print("Color not found. Please try again.")


if __name__ == "__main__":
    main()
