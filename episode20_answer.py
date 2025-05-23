# Episode 20 Practice Questions:

# 1. What is the purpose of the `perf_counter` function in Python?
"""
The perf_counter returns the value (in seconds) of a performance counter, which is a clock with the highest available resolution to measure short durations.
"""
# 2. What do you have to be careful about when using the `perf_counter` function?
"""
You have to be careful about the fact that the perf_counter is not guaranteed to be monotonic, meaning it can go backwards in time.
This can happen due to system clock adjustments or other factors.
"""
# 3. What is the purpose of the `wrapper` function in the `my_timmer` decorator?
"""
The wrapper function in the my_timmer decorator is used to wrap the original function and add additional functionality, such as timing the execution of the function.
It allows you to measure how long the original function takes to execute without modifying its code."""
# 4. Whenever you are timing something, what do you have to be aware of?
"""
When timing something, you have to be aware of the overhead introduced by the timing mechanism itself.
This means that the time measured may not accurately reflect the actual execution time of the code being timed.
You also need to be aware that hardware and system load can affect timing results, so it's best to understand the context in which you're measuring performance.
Especially when trying to compare pieces of code and results from someone elses code.
"""