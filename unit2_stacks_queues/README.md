# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Implementation Summary

I implemented the stack with a Python list and used `append()` and `pop()` to
store and remove values from the same end. This design demonstrated LIFO by
modeling a text editor's undo history: the most recently saved action was the
first action undone. I implemented the queue with `collections.deque` and used
`append()` with `popleft()` for efficient FIFO operations. The coffee-shop line
demonstrated that customers were served in the order they arrived.

Both structures returned `None` when a removal or viewing operation was
attempted while empty. I also tested empty structures and single-item
structures to confirm that boundary conditions were handled safely. Each
structure stored one additional reference for every item added, so its memory
usage grew linearly, or O(n), with the number of stored items.

## Program Output and Testing

I ran the program and verified that four stack actions were removed in reverse
order and four queued customers were removed in arrival order. I confirmed that
`pop()`, `peek()`, `dequeue()`, and `front()` returned `None` when their
structures were empty. I also verified that removing the only item from a stack
or queue caused `is_empty()` to return `True`.

## Real-World Interpretation

A stack used LIFO because only its newest item was exposed at the top, like an
undo history. A queue used FIFO because removal occurred at the front while new
items entered at the back, like customers waiting for service.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

I learned how the location used for insertion and removal determined the order
in which a linear data structure returned its elements. I implemented a stack
with a Python list because `append()` and `pop()` efficiently operated on the
same end. I implemented a queue with `deque` because `popleft()` removed the
oldest item without shifting every remaining element. The main challenge was
handling operations safely when no item existed. I overcame it by checking
`is_empty()` before each viewing or removal operation and returning `None` when
the structure was empty. I then tested empty, single-item, and reused
structures.

The text-editor scenario showed that a stack used LIFO: the most recent editing
action had to be undone first so earlier work remained in the correct order.
The coffee-shop scenario showed that a queue used FIFO: the customer who
arrived first had to receive service first. These access rules made each
structure appropriate for a different problem. Both implementations required
O(n) memory because each added item occupied another stored position. Stack
push/pop and deque enqueue/dequeue operations were O(1) in the usual case, so
the structures remained responsive as more items were added.
