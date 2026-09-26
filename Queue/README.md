# Queue

This folder is dedicated to queue data structure programs and exercises.

## What is a queue?

A queue is a linear data structure that follows the First In, First Out (FIFO) principle.

- The first item added is the first one to be removed.
- Common operations include:
  - enqueue / insert: add an item to the rear
  - dequeue / delete: remove the front item
  - peek: view the front item without removing it
  - isEmpty: check whether the queue is empty

## Typical queue use cases

- Scheduling tasks in order
- Breadth-First Search (BFS)
- Printer and CPU job management
- Handling requests in order

## Example behavior

If you insert values 10, 20, and 30 in order, the queue will remove them in this sequence:

10
20
30

## Files in this folder

- implementation.py: basic queue implementation using a list
- doubleEndedQueue.py: deque implementation that supports insertion and deletion from both ends

## Notes

This folder is intended for queue implementations, examples, and practice problems. Add your Python files here as you learn more about queue operations and applications.
