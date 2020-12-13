class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.insert(0, item)

  def pop(self):
    return self.items.pop(0)

  def peek(self):
    return self.items[0]

  def size(self):
    return len(self.items)

def postfix(postfix_variable):
   operator_stack = Stack()
   list = postfix_variable.split()
   for index in list:
      if index in "0123456789":
         operator_stack.push(int(index))
      else:
         operand_2 = operator_stack.pop()
         operand_1 = operator_stack.pop()
         result = calculate(index, operand_1, operand_2)
         operator_stack.push(result)
   return operator_stack.pop()
def calculate(n, n1, n2):
   if n == "*":
      return n1 * n2
   elif n == "/":
      return n1 / n2
   elif n == "+":
      return n1 + n2
   else:
      return n1 - n2
print(postfix('5 1 + 9 *'))
