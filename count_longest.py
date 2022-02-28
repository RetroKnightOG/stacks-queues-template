# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Omar Nasser
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue

# can destroy the queue & make it empty

def count_longest(q):

    iterations = q.size()

    queue = Queue([])

    longest = 0

    while iterations > 0:

        if queue.is_empty() == True:
            queue.enq(q.deq())

        elif queue.tail() == q.front():
            queue.enq(q.deq())

        if queue.is_empty() == False:
            if queue.tail() != q.front():
                if queue.size() > longest:
                    longest = queue.size()

                queue.clear()

        iterations -= 1

    return longest

def main():
    print("out 2:", count_longest( Queue( [ l for l in "hello" ] ) ))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee"])))

# Don't run main on import
if __name__ == "__main__":
    main()
