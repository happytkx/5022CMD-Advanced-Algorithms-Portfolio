import time

# Measure Hash Table search time
def measure_hash_search(table, product_id, repetitions=10000):
    start_hash = time.perf_counter_ns()

    # Repeat the search
    for i in range(repetitions):
        result = table.search(product_id)

    end_hash = time.perf_counter_ns()

    # Calculate average search time
    hash_time = (end_hash - start_hash) / repetitions

    return result, hash_time

# Perform a sequential search through the one-dimensional list
def array_search(medicine_list, target_id):
    for item in medicine_list:
        if item.product_id == target_id:
            return item

    return None

# Measure the array search time
def measure_array_search(medicine_list, product_id, repetitions=10000):
    start_array = time.perf_counter_ns()

    # Repeat the search
    for i in range(repetitions):
        result = array_search(medicine_list, product_id)

    end_array = time.perf_counter_ns()

    # Calculate the average search time
    array_time = (end_array - start_array) / repetitions

    return result, array_time


