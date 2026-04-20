from collections import deque

class Queue:
    def _init_(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to queue")

    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        else:
            return self.queue.popleft()

    def display(self):
        print("Queue:", list(self.queue))


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())
print("Dequeued element:", q.safe_dequeue())

print("Dequeued element:", q.safe_dequeue())