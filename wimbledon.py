"""
Game, Set, Match
Estimate: 60 minutes
Actual:   75 minutes
"""

import csv

def read_wimbledon_data(filename):
    """Reads Wimbledon data from a CSV file and returns a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            data.append(row)
    return data

def process_data(data):
    """Processes the Wimbledon data and returns a dictionary with champions and their wins."""
    champions = {}
    for row in data:
        name = row[0]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions

def display_champions(champions):
    """Displays the champions and the number of times they have won."""
    print("Wimbledon Champions:")
    for name, wins in champions.items():
        print(f"{name} {wins}")

def get_countries(champions):
    """Extracts the countries of the champions."""
    countries = set()
    for name in champions.keys():
        country = name.split()[-1]
        countries.add(country)
    return countries

def display_countries(countries):
    """Displays the countries of the champions in alphabetical order."""
    print("\nThese", len(countries), "countries have won Wimbledon:")
    country_list = sorted(countries)
    print(", ".join(country_list))

def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)
    champions = process_data(data)
    display_champions(champions)
    countries = get_countries(champions)
    display_countries(countries)

if __name__ == "__main__":
    main()
