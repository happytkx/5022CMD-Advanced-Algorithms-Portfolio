import time
import threading

# Calculates the nth Fibonacci number using recursion
def fibonacci(n):
    # Base case: Fibonacci(0) = 0 and Fibonacci(1) = 1
    if n <= 1:
        return n

    # Recursive case: add the two previous Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)

# Calculates a Fibonacci number for one thread
def fibonacci_worker(n, results):
    results[n] = fibonacci(n)

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

# Runs the three Fibonacci calculations using separate threads
def run_multithreaded():
    # Stores the Fibonacci results calculated by the threads
    results = {}

    # Create one thread for each Fibonacci calculation
    thread_35 = threading.Thread(
        target=fibonacci_worker,
        args=(35, results))

    thread_38 = threading.Thread(
        target=fibonacci_worker,
        args=(38, results))

    thread_40 = threading.Thread(
        target=fibonacci_worker,
        args=(40, results))

    # Record the time before the first thread starts
    start_time = time.perf_counter_ns()

    # Start all three threads
    thread_35.start()
    thread_38.start()
    thread_40.start()

    # Wait until all three threads have finished
    thread_35.join()
    thread_38.join()
    thread_40.join()

    # Record the time after the final thread finishes
    end_time = time.perf_counter_ns()

    # Calculate the total time taken
    threaded_elapsed_time = end_time - start_time

    return results[35], results[38], results[40], threaded_elapsed_time

# Number of experiment rounds
repetitions = 10

# Stores the elapsed time from each round
sequential_times = []

# Stores the Fibonacci results
sequential_result_35 = None
sequential_result_38 = None
sequential_result_40 = None

print("\n============= Sequential Fibonacci Experiment =============")

for i in range(repetitions):
    sequential_result_35, sequential_result_38, sequential_result_40, round_time = run_sequential()

    # Store the elapsed time for later average calculation
    sequential_times.append(round_time)

    print("Round", i + 1, ":", f"{round_time:,}", "nanoseconds")

# Calculate the average time for all rounds
average_sequential_time = sum(sequential_times) / len(sequential_times)

print("\nFibonacci Results:")
print("Fibonacci(35):", sequential_result_35)
print("Fibonacci(38):", sequential_result_38)
print("Fibonacci(40):", sequential_result_40)

print("\nAverage Sequential Time:", f"{average_sequential_time:,.1f}", "nanoseconds")

# Stores the elapsed time from each multithreaded round
threaded_times = []

# Stores the Fibonacci results
threaded_result_35 = None
threaded_result_38 = None
threaded_result_40 = None

print("\n=========== Multithreaded Fibonacci Experiment ===========")

for i in range(repetitions):
    threaded_result_35, threaded_result_38, threaded_result_40, round_time = run_multithreaded()

    # Store the elapsed time for later average calculation
    threaded_times.append(round_time)

    print("Round", i + 1, ":", f"{round_time:,}", "nanoseconds")

# Calculate the average time for all rounds
average_threaded_time = sum(threaded_times) / len(threaded_times)

print("\nFibonacci Results:")
print("Fibonacci(35):", threaded_result_35)
print("Fibonacci(38):", threaded_result_38)
print("Fibonacci(40):", threaded_result_40)

print("\nAverage Multithreaded Time:", f"{average_threaded_time:,.1f}", "nanoseconds")

# Display a summary of the average execution times
print("\n================= Performance Comparison =================")
print("Average Sequential Time:", f"{average_sequential_time:,.1f}", "nanoseconds")
print("Average Multithreaded Time:", f"{average_threaded_time:,.1f}", "nanoseconds")
