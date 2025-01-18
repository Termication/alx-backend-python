# Asyncio Example with `async`/`await`, Concurrency, and Random Module

This project demonstrates how to use Python's `asyncio` library to execute asynchronous programs, run concurrent coroutines, create asyncio tasks, and use the `random` module in an async context.

## Prerequisites

- Python 3.7 or later (Python 3.7+ is required for `asyncio` support)
- Basic understanding of Python async programming

## Table of Contents

- [1. `async` and `await` syntax](#async-and-await-syntax)
- [2. How to execute an async program with `asyncio`](#how-to-execute-an-async-program-with-asyncio)
- [3. How to run concurrent coroutines](#how-to-run-concurrent-coroutines)
- [4. How to create asyncio tasks](#how-to-create-asyncio-tasks)
- [5. How to use the `random` module](#how-to-use-the-random-module)

---

## 1. `async` and `await` syntax

In Python, `async` and `await` are used to define asynchronous functions and to "pause" their execution, allowing other code to run while waiting for a result.

- `async def`: Defines an asynchronous function.
- `await`: Pauses the function execution until the result of another coroutine is available.

### Example:

python
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)  # Simulates an async operation (e.g., I/O)
    print("Goodbye!")

# To run the async function
asyncio.run(say_hello())


Output:

Hello!
Goodbye!

In the above example, await asyncio.sleep(1) pauses the say_hello() function for 1 second before printing "Goodbye!".
2. How to execute an async program with asyncio

To execute an async program, we use asyncio.run(), which runs the top-level coroutine, and waits for it to finish.
Example:

import asyncio

async def main():
    print("Starting...")
    await asyncio.sleep(2)  # Simulate async work
    print("Done!")

# Execute the async program
asyncio.run(main())

Output:

Starting...
Done!

3. How to run concurrent coroutines

You can run multiple coroutines concurrently using asyncio.gather(), which allows you to run several async tasks at once.
Example:

import asyncio

async def task_1():
    print("Task 1 starting")
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task_2():
    print("Task 2 starting")
    await asyncio.sleep(2)
    print("Task 2 completed")

# Run both tasks concurrently
async def main():
    await asyncio.gather(task_1(), task_2())

asyncio.run(main())

Output:

Task 1 starting
Task 2 starting
Task 1 completed
Task 2 completed

Notice that both tasks start at the same time, and the program doesn't wait for task_1() to finish before starting task_2().
4. How to create asyncio tasks

You can create tasks using asyncio.create_task() to run them concurrently in the background.
Example:

import asyncio

async def slow_task():
    print("Starting slow task...")
    await asyncio.sleep(3)
    print("Slow task done!")

async def fast_task():
    print("Starting fast task...")
    await asyncio.sleep(1)
    print("Fast task done!")

async def main():
    task1 = asyncio.create_task(slow_task())  # Start slow task
    task2 = asyncio.create_task(fast_task())  # Start fast task

    # Wait for both tasks to finish
    await task1
    await task2

asyncio.run(main())

Output:

Starting slow task...
Starting fast task...
Fast task done!
Slow task done!

Here, asyncio.create_task() allows task1 and task2 to run concurrently. The program does not wait for one task to finish before starting the other.
5. How to use the random module

You can also use Python's random module in conjunction with asyncio to simulate random delays or other random behaviors in your async program.
Example:

import asyncio
import random

async def random_task(name):
    delay = random.uniform(1, 3)  # Random delay between 1 and 3 seconds
    print(f"Task {name} starting with a delay of {delay:.2f}s")
    await asyncio.sleep(delay)
    print(f"Task {name} completed!")

async def main():
    # Create multiple tasks with random delays
    tasks = [random_task(i) for i in range(1, 4)]
    await asyncio.gather(*tasks)

asyncio.run(main())

Output:

Task 1 starting with a delay of 2.46s
Task 2 starting with a delay of 1.87s
Task 3 starting with a delay of 2.71s
Task 2 completed!
Task 1 completed!
Task 3 completed!

In this example, each task has a random delay between 1 and 3 seconds, and the tasks are executed concurrently using asyncio.gather().
Conclusion

This project demonstrates how to use asyncio to execute asynchronous programs and run concurrent tasks. We also covered how to create asyncio tasks and incorporate randomness with the random module. Using async and await makes it easy to write concurrent programs without worrying about threads or callbacks.
