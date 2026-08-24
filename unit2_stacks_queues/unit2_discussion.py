"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending makes the newest value the first one available to remove (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek examines the newest value but leaves the stack unchanged.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Appending at the back preserves arrival order for FIFO processing.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front examines the oldest value without removing it.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    print("\n=== STACK DEMO: TEXT EDITOR UNDO HISTORY ===")
    undo_history = Stack()
    actions = ["typed title", "added paragraph", "bolded heading", "inserted image"]
    for action in actions:
        undo_history.push(action)
        print(f"Saved action: {action}")

    print(f"Next action to undo (peek): {undo_history.peek()}")
    print("Undo order (most recent action first):")
    while not undo_history.is_empty():
        print(f"  Undid: {undo_history.pop()}")
    print(f"Pop on empty stack returned: {undo_history.pop()}")
    print(f"Peek on empty stack returned: {undo_history.peek()}")

    single_action = Stack()
    single_action.push("typed one word")
    print(f"Single-item stack removed: {single_action.pop()}")
    print(f"Single-item stack is empty: {single_action.is_empty()}")

    reused_stack = Stack()
    reused_stack.push("first revision")
    reused_stack.pop()
    reused_stack.push("replacement revision")
    print(f"Reused stack top after remove/add: {reused_stack.peek()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    print("\n=== QUEUE DEMO: COFFEE SHOP LINE ===")
    customer_line = Queue()
    customers = ["Amina", "Ben", "Carlos", "Dina"]
    for customer in customers:
        customer_line.enqueue(customer)
        print(f"Joined the line: {customer}")

    print(f"Next customer to be served (front): {customer_line.front()}")
    print("Service order (earliest arrival first):")
    while not customer_line.is_empty():
        print(f"  Served: {customer_line.dequeue()}")
    print(f"Dequeue on empty queue returned: {customer_line.dequeue()}")
    print(f"Front on empty queue returned: {customer_line.front()}")

    single_customer = Queue()
    single_customer.enqueue("Evan")
    print(f"Single-item queue served: {single_customer.dequeue()}")
    print(f"Single-item queue is empty: {single_customer.is_empty()}")

    reused_queue = Queue()
    reused_queue.enqueue("Farah")
    reused_queue.dequeue()
    reused_queue.enqueue("Grace")
    print(f"Reused queue front after serve/add: {reused_queue.front()}")

if __name__ == "__main__":
    main()
