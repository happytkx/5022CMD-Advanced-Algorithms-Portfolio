from medicine import Medicine
from hash_table import HashTable
from comparison import measure_hash_search, measure_array_search

# Create a Hash Table with 11 available slots
table = HashTable(11)

# Create predefined medicine records
medicine1 = Medicine(1001, "Paracetamol 500mg", 5.90, 120)
medicine2 = Medicine(1012, "Ibuprofen 200mg", 8.50, 80)
medicine3 = Medicine(1023, "Cetirizine 10mg", 6.90, 60)
medicine4 = Medicine(1005, "Vitamin C 500mg", 12.90, 100)
medicine5 = Medicine(1017, "Antacid Tablets", 7.50, 50)

# Store the predefined records in the one-dimensional array
medicines = [
    medicine1,
    medicine2,
    medicine3,
    medicine4,
    medicine5
]

# Insert the records into the Hash Table
for medicine in medicines:
    table.insert(medicine)

choice = ""

# Continue displaying the menu until the user selects "4"
while choice != "4":
    print("\n~~~~~~~~ Pharmacy Inventory System ~~~~~~~~")
    print("1. Insert Product")
    print("2. Search Product")
    print("3. Display Hash Table")
    print("4. Exit")

    choice = input("Enter choice: ")

    # 1. Insert Product
    if choice == "1":
        # Collect the details of the new medicine
        product_id = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: RM"))
        stock = int(input("Enter Product Quantity: "))

        # Create a Medicine object from the user's input
        new_medicine = Medicine(product_id, name, price, stock)

        # Insert the medicine into the Hash Table
        slot = table.insert(new_medicine)

        if slot is not None:
            # Keep the one-dimensional array consistent with the Hash Table
            medicines.append(new_medicine)

            print(f"\nProduct added successfully at slot {slot}.")
        else:
            print("\nUnable to add product. Hash table is full.")

    # 2. Search Product
    elif choice == "2":
        product_id = int(input("Enter Product ID to search: "))

        # Measure the Hash Table search time
        result, hash_time = measure_hash_search(table, product_id)

        # Measure the one-dimensional array search time
        array_result, array_time = measure_array_search(medicines, product_id)

        if result is not None:
            print("\nProduct Found: ")
            print(f"ID: {result.product_id}")
            print(f"Name: {result.name}")
            print(f"Price: RM{result.price:.2f}")
            print(f"Stock: {result.stock}")
        else:
            print("\nProduct not found.")

        # Display the average execution time of both search approaches
        print(f"\nAverage Hash Table Search Time: {hash_time:.2f}ns")
        print(f"Average Array Search Time: {array_time:.2f}ns")

    # 3. Display Hash Table
    elif choice == "3":
        print("\n========== Hash Table ==========")
        table.display()

    # 4. Exit
    elif choice == "4":
        print("\nExiting Inventory System...")

    else:
        print("\nInvalid choice. Try again.")

