class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Check if stack is full
    def is_full(self):
        return len(self.stack) == self.capacity

    # Push element onto stack
    def push(self, item):
        if self.is_full():
            print("Stack is full, cannot push.")
        else:
            self.stack.append(item)
            print(f"Pushed: {item}")

    # Safe pop method
    def safe_pop(self):
        if self.is_empty():
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.stack.pop()

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Example usage
s = Stack(3)  # capacity = 3

s.push(10)
s.push(20)
s.push(30)
s.push(40)  # will show stack is full

s.display()

print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())
print("Popped:", s.safe_pop())  # will show stack is empty 
