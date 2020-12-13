class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        return self.items

def palindrome(word):
    palindrome = Queue()
    for n in word:
        palindrome.enqueue(n)

    if palindrome.size() > 1 :
        First_word = palindrome.dequeue()
        Last_word = palindrome.items.pop(0)
        if First_word != Last_word:
            return False
        else:
            return True

print(palindrome("abcdefg"))
print(palindrome("radar"))
print(palindrome("123456789"))




