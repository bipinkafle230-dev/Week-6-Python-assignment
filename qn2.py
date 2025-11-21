import csv

def write_scores():
    data = [
        ["name", "database", "account", "java"],
        ["Aadiskar", 80, 60, 55],
        ["Bipin", 50, 80, 90],
        ["Muskan", 90, 28, 63],
        ["Ramesh", 70, 66, 84],
        ["Salman", 88, 92, 79]
    ]

    with open("scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    print("CSV file 'scores.csv' created.\n")

def read_and_average_scores():
    with open("scores.csv") as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            name = row[0]
            scores = list(map(int, row[1:]))
            average = sum(scores) / len(scores)
            print(f"{name}'s average score is {average:.2f}")

def main():
    write_scores()
    read_and_average_scores()

main()

# completion of program