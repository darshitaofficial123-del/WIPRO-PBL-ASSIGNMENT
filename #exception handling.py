#exception handling
try:
    file_name = input("Enter the file name: ") + ".txt"

    file = open(file_name, "r")

    total_items = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in file:
        line = line.strip()

        if line == "":
            continue

        data = line.split()

        if data[0].lower() == "discount":
            discount = int(data[1])

        else:
            total_items += 1

            if data[1].lower() == "free":
                free_items += 1
            else:
                amount += int(data[1])

    file.close()

    final_amount = amount - discount

    print("No of items purchased:", total_items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("File not found.")

except ValueError:
    print("Invalid data in file.")

except Exception as e:
    print("Error:", e)