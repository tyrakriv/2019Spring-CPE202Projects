class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0
        self.front = None
        self.index = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True
        else:
            return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full() == True:
            raise IndexError
        else:
            self.num_items += 1
            if self.num_items == 1:
                self.front = 0
                self.index = 0
                self.items[self.index] = item
            else:
                if self.index > self.capacity-1:
                    self.index = 0
                self.items[self.index] = item
                
            self.index += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty():
            raise IndexError
        else:
            deq = self.items[self.front]
            self.items[self.front] = None
            self.front += 1
            if self.front > self.capacity-1:
                self.front = 0
            self.num_items -= 1
            return deq

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
