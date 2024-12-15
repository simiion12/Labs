# Signal Handling and Producer-Consumer Implementation in Python

## Overview
This document details three interconnected programming implementations:

1. **UNIX Signal Management (`SIGUSR1` and `SIGUSR2`)**:
   - A demonstration of handling system signals in Python, showing how to respond to SIGUSR1 and SIGUSR2 events.
   
2. **Basic Producer-Consumer Implementation**:
   - An exploration of concurrent programming using Python's multiprocessing capabilities and semaphore-based synchronization.

3. **Scaled Producer-Consumer System**:
   - An expanded version of the producer-consumer model featuring increased concurrent processing capabilities.

---

## Implementation 1: UNIX Signal Management

### Purpose
Create a system that responds to UNIX signals by either displaying information or generating random data before termination.

### Code Implementation

```python
import signal
import random
import string
import sys

# Handler for SIGUSR1
def handle_sigusr1(signum, frame):
    print("SIGUSR1 received")

# Handler for SIGUSR2
def handle_sigusr2(signum, frame):
    # Generate and print 100 random ASCII characters
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    print(random_string)
    sys.exit(0)  # Terminate the program

# Register the signal handlers
signal.signal(signal.SIGUSR1, handle_sigusr1)
signal.signal(signal.SIGUSR2, handle_sigusr2)

# Keep the program running to handle signals
print("Program running, send SIGUSR1 or SIGUSR2 to test")
while True:
    pass
```

### Technical Details
The implementation features two distinct signal handlers:
- A SIGUSR1 handler that outputs a confirmation message
- A SIGUSR2 handler that creates a random string and ends execution

The program uses Python's signal module to establish these handlers and runs continuously while waiting for incoming signals.

---

## Implementation 2: Basic Producer-Consumer System

### Purpose
Create a synchronized system where multiple processes can safely produce and consume data using shared resources.

### Code Implementation

```python
import multiprocessing as mp
import os
import random
import time
from datetime import datetime

# Producer function
def producer(producer_id, pipe_name, semaphore):
    with open(pipe_name, 'wb') as pipe:
        while True:
            semaphore.acquire()  # Control overproduction
            items = [random.randint(1, 100) for _ in range(3)]
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] Producer {producer_id} produced items: {items}")
            pipe.write(bytes(f"{producer_id}:{items}\n", 'utf-8'))
            pipe.flush()
            semaphore.release()
            time.sleep(random.uniform(1, 3))  # Simulate work

# Consumer function
def consumer(consumer_id, pipe_name, semaphore):
    while True:
        with open(pipe_name, 'rb') as pipe:
            while True:
                line = pipe.readline().decode('utf-8').strip()
                if not line:  # If no data is available, reopen the pipe
                    time.sleep(0.5)  # Wait before retrying
                    break
                producer_id, items = line.split(':')
                items = eval(items)  # Convert string representation to list
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"[{timestamp}] Consumer {consumer_id} consumed items from Producer {producer_id}: {items}")
                time.sleep(random.uniform(0.5, 1.5))  # Simulate work

if __name__ == "__main__":
    pipe_name = "/tmp/producer_consumer_pipe"

    # Ensure the named pipe exists
    try:
        os.mkfifo(pipe_name)
    except FileExistsError:
        pass

    # Semaphore to control production and consumption limits
    producer_semaphore = mp.Semaphore(3)  # Producer limit
    consumer_semaphore = mp.Semaphore(5)  # Consumer limit

    # Start producers
    producers = [mp.Process(target=producer, args=(i, pipe_name, producer_semaphore)) for i in range(3)]
    for p in producers:
        p.start()

    # Start consumers
    consumers = [mp.Process(target=consumer, args=(i, pipe_name, consumer_semaphore)) for i in range(2)]
    for c in consumers:
        c.start()

    # Join processes
    for p in producers:
        p.join()
    for c in consumers:
        c.join()
```

### Technical Details
The system employs:
- Named pipes for inter-process data transfer
- Semaphores to regulate resource access
- Multiple producer and consumer processes running simultaneously
- Timestamp-based logging for monitoring data flow

---

## Implementation 3: Scaled Producer-Consumer System

### Purpose
Enhance processing throughput by increasing the number of concurrent consumers while maintaining system stability.

### Code Modification

```python
# The code remains identical to Implementation 2, with this key change:

# Start consumers
consumers = [mp.Process(target=consumer, args=(i, pipe_name, consumer_semaphore)) for i in range(3)]  # Changed to 3 consumers
for c in consumers:
    c.start()
```

### Technical Details
This version increases system throughput by:
- Adding an additional consumer process
- Maintaining the existing synchronization mechanisms
- Preserving the original producer configuration

---

## Summary

This collection of implementations showcases different aspects of system programming in Python:

The signal handling system demonstrates low-level system interaction capabilities, allowing programs to respond to external triggers in a controlled manner. The producer-consumer implementations highlight concurrent programming principles, showing how to manage shared resources and parallel processing effectively.

The progression from basic to scaled implementations illustrates how such systems can be enhanced while maintaining stability. These examples serve as practical templates for building larger-scale concurrent applications where resource management and process synchronization are crucial.