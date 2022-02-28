# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Omar Nasser
# ASSIGNMENT:   Technical HW: Stacks & Queues

from Queue import Queue



def generate_binary_numbers(n):
    numbers = Queue([])
    temp_q = Queue([])

    temp_q.enq("1")

    while n > 0:
    
        temp_q.enq(temp_q.front()+"0")
        temp_q.enq(temp_q.front()+"1")
    
        numbers.enq(temp_q.deq())
        n -= 1

    return numbers

def main():
    generate_binary_numbers(2).print()
    
    generate_binary_numbers(3).print()
    
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    
    main()
