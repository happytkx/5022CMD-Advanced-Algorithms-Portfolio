from medicine import Medicine
from hash_table import HashTable
from comparison import measure_hash_search, measure_array_search

product_ids = [
    2001, 2003, 2005, 2007, 2009,
    2011, 2013, 2015, 2017, 2019,
    2021, 2023, 2025, 2027, 2029,
    2031, 2033, 2035, 2042, 2045
]

# Create a larger dataset with 20 medicine records
large_medicines = []

for i in range(20):
    product_id = product_ids[i]

    medicine = Medicine(product_id,f"Test Medicine {i + 1}", 10.00 + i, 50 + i)

    large_medicines.append(medicine)

# Create larger Hash Table
large_table = HashTable(41)

# Insert the same records into the Hash Table
for medicine in large_medicines:
    large_table.insert(medicine)

test_cases = [
    ("First record", 2001),
    ("Collision record", 2042),
    ("Last record", 2045),
    ("Unsuccessful record", 9999)
]

print("\n====== Larger Dataset Performance Experiment ======")
print("Records: 20")
print("Hash Table size: 41")

for label, product_id in test_cases:
    result, hash_time = measure_hash_search(large_table, product_id)

    array_result, array_time = measure_array_search(large_medicines, product_id)

    print(f"\n{label} - Product ID {product_id}")
    print(f"Average Hash Table Search Time: {hash_time:.2f}ns")
    print(f"Average Array Search Time: {array_time:.2f}ns")
