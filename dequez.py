
import array
class Deque:
    max_size = 20

    def __init__(self):
        self._data = [None]*Deque.max_size
        self._size = 0
        self._front = -1
        self._rear = -1

    def add_to_front(self, val):
        if (self._front == 0 and self._rear == len(self._data) - 1) or (self._front == self._rear + 1):
            print("queue is full")

        elif self._front == -1 and self._rear == -1:
            self._front = 0
            self._rear = 0
            self._data[self._front] = val

        elif self._front == 0:
            self._front = len(self._data) - 1
            self._data[self._front] = val

        else:
            self._front -= 1
            self._data[self._front] = val

    def add_to_rear(self, val):
        if (self._front == 0 and self._rear == len(self._data) - 1) or (self._front == self._rear + 1):
            print("queue is full")

        elif self._front == -1 and self._rear == -1:
            self._front = 0
            self._rear = 0
            self._data[self._rear] = val

        elif self._rear == len(self._data) -1:
            self._rear = 0

        else:
            self._rear += 1
            self._data[self._rear] = val

    def display(self):
        i = self._front
        while i != self._rear:
            print(self._data[i], end = ",")
            i = (i+1)% len(self._data)

        print(self._data[i])

    def get_front(self):
        return self._data[self._front]

    def get_rear(self):
        return self._data[self._rear]

    def remove_front(self):
        if self._front == -1 and self._rear == -1:
            print("deque is empty")

        elif self._front == self._rear:
            self._front = -1
            self._rear = -1

        elif self._front == len(self._data) - 1:
            print("removed value is", self._data[self._front])
            self._front = 0

        else:
            print("removed value is", self._data[self._front])
            self._front += 1

    def remove_rear(self):
        if self._front == -1 and self._rear == -1:
            print("deque is empty")

        elif self._front == self._rear:
            self._front = -1
            self._rear = -1

        elif self._rear == 0:
            print("removed value is", self._data[self._rear])
            self._rear = len(self._data) - 1

        else:
            print("removed value is", self._data[self._rear])
            self._rear -= 1

    def is_empty(self):
        return (self._front == -1 and self._rear == -1)

    def is_full(self):
        return (self._front == 0 and self._rear == len(self._data) - 1) or (self._front == self._rear + 1)

    def length(self):
        return len(self._data)


        

        
            
            
            
        

    

        
    
