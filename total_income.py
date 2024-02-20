"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def get_income_input(months):
    """Get income input for each month and return a list of incomes."""
    incomes = []
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_income_report(incomes):
    """Print income report."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_of_months = int(input("How many months? "))

    incomes = get_income_input(num_of_months)
    print_income_report(incomes)


if __name__ == "__main__":
    main()
