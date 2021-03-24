from linear_queue import LinearQueue

queue = LinearQueue(5)
queue.print()

queue.put(1)
queue.put(2)
queue.put(3)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
queue.print()

queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
queue.print()
