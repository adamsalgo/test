class circularqueue:
    def __init__(self, size):
        self.size=size
        self.queue =[None]*size
        self.head = 0
        self.number_items = 0 
        

    def enqueue(self, item):
        if not self.is_full():
            self.queue[(self.head+self.number_items)%self.size] = item
            self.number_items = self.number_items+1
        else:
            print('the queue is full')
            
    def dequeue(self):
        if not self.is_empty():
            item = self.queue[self.head]
            self.head =(self.head+1)%self.size
            self.number_items=self.number_items-1
            return item
        else:
            print('the queue is empty')
            return None 
    def peek(self):
        return self.queue[self.head]

    def is_empty(self):
        return self.number_items == 0

    def is_full(self):
        return self.number_items==self.size
        
    def print_queue(self):
        print([self.queue[(i+self.head)%self.size] for i in range(self.number_items)])