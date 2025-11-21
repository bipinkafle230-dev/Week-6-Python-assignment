from moduleofqn4 import multiplication_table

def table():
    try:
        n = int(input("Enter the number: "))
        limit = int(input("Enter the limit: "))
        table = multiplication_table(n, limit)
        for line in table:
            print(line)
    except ValueError:
        print("Please enter valid integers only.")

def main():
    table()

main()

# completion of program