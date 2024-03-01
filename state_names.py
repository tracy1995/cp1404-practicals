# State names in a dictionary
# File reformatted to follow PEP 8 convention

# Dictionary containing state codes and names
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# Function to retrieve state name from state code
def get_state_name(state_code):
    """
    Retrieve the state name corresponding to the given state code.
    :param state_code: The state code abbreviation.
    :return: The full name of the state.
    """
    try:
        return CODE_TO_NAME[state_code.upper()]  # Convert input to uppercase to handle lowercase inputs
    except KeyError:
        return "Invalid short state"  # Return error message if state code is not found in the dictionary

# Main program
def main():
    """
    Main function to interact with the user and display state names.
    """
    state_code = input("Enter short state: ").upper()  # Convert input to uppercase to handle lowercase inputs
    while state_code != "":
        state_name = get_state_name(state_code)
        print(state_code, "is", state_name)
        state_code = input("Enter short state: ").upper()  # Convert input to uppercase to handle lowercase inputs

# Execute the main function
if __name__ == "__main__":
    main()
