import time

# Calculates the nth Fibonacci number using recursion
def fibonacci(n):
    # Base case: Fibonacci(0) = 0 and Fibonacci(1) = 1
    if n <= 1:
        return n

    # Recursive case: add the two previous Fibonacci numbers
    return fibonacci(n-1) + fibonacci(n-2)

# Runs the three Fibonacci calculations sequentially
def run_sequential():
    # Record the time before the first calculation starts
    start_time = time.perf_counter_ns()

    result_35 = fibonacci(35)
    result_38 = fibonacci(38)
    result_40 = fibonacci(40)

    # Record the time after the final calculation finishes
    end_time = time.perf_counter_ns()

    # Calculate the total time taken
    sequential_elapsed_time = end_time - start_time

    return result_35, result_38, result_40, sequential_elapsed_time

# Number of experiment rounds
repetitions = 10

# Stores the elapsed time from each round
sequential_times = []

# Stores the Fibonacci results
sequential_result_35 = None
sequential_result_38 = None
sequential_result_40 = None

print("\n============== Sequential Fibonacci Experiment ==============")

for i in range(repetitions):
    sequential_result_35, sequential_result_38, sequential_result_40, round_time = run_sequential()

    # Store the elapsed time for later average calculation
    sequential_times.append(round_time)

    print("Round", i + 1, ":", round_time, "nanoseconds")

# Calculate the average time for all rounds
average_sequential_time = sum(sequential_times) / len(sequential_times)

print("\nFibonacci Results:")
print("Fibonacci(35):", sequential_result_35)
print("Fibonacci(38):", sequential_result_38)
print("Fibonacci(40):", sequential_result_40)

print("\nAverage Sequential Time:", average_sequential_time, "nanoseconds")
