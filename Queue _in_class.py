class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items

customer = Queue()
while True:
    print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
    print("                                      >> List menu <<")
    print("                               1. >> Counter 1 to get customer")
    print("                               2. >> Counter 2 to get customer")
    print("                               3. >> Customer waiting...")
    print("                               4. >> Exit !")
    print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
    checker = int(input("Choose a costomer number : "))
    print('▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂')
    waiting = customer.size()
    if checker == 1:
        if waiting > 0:
            comeout = customer.dequeue()
            print("Customer({}) come in to counter 1".format(comeout))
            waiting -= 1
            print("Count number customer waiting to counter: {}".format(waiting))
            print("Customer waiting...")
            show_queue = customer.show()
            print(">>>",show_queue)
        else:
            print("Count number customer waiting to counter: {}".format(waiting))
            print("No one waiting...")
    elif checker == 2:
        if waiting > 0:
            comeout = customer.dequeue()
            print("Customer({}) come in to counter 1".format(comeout))
            waiting -= 1
            print("Count number customer waiting to counter: {}".format(waiting))
            print("Customer waiting...")
            show_queue = customer.show()
            print(">>>",show_queue)
        else:
            print("Count number customer waiting to counter: {}".format(waiting))
            print("No one waiting...")
    elif checker  == 3:
            Queue_input = input("Enter customer name : ").strip()
            customer.enqueue(Queue_input)
            print("Count number customer waiting to counter: {}".format(waiting))
            print("Customer waiting...")
            show_queue = customer.show()
            print(">>>",show_queue)
    else:
        print("Your are Exit !!!")
        break

