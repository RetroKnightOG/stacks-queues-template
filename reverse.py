# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Omar Nasser
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Queue import Queue
from Stack import Stack

# Return a new queue in reverse order
# Hint: can use a stack to help

def reverse(original):

    queue_n = Queue()
    stack_new = Stack()
    
    print("The original queue", original)

    while (not original.is_empty()):
        stack_new.push(original.deq())
    
    while (not stack_new.is_empty()):
        queue_n.enq(stack_new.pop())
    
    return queue_n

def main():
    reverse(Queue([l for l in "hello"])).print()
   
    reverse(Queue(list(range(1, 5)))).print()
   
    reverse(Queue([])).print()
   
    reverse(Queue([0])).print()
   
    reverse(Queue(list(range(0, 101, 5)))).print()
   
    reverse(Queue(list(range(1, -10, -1)))).print()
   
    reverse(Queue([int(i) for i in "23762304"])).print()
   
    reverse(Queue(["a"])).print()
   
    reverse(Queue([-5])).print()
   
    reverse(Queue(list(range(-5, 6)))).print()

# Don't run main on import
if __name__ == "__main__":
    main()
