class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]


s1 = Stack()
s2 = Stack()
print(s1.is_empty())
s1.push("자료구조")
print(s1.is_empty())
print(s2.is_empty())
s1.push("데이터베이스")
print(s1.size())
print(s1.peek())
print(s1.size())
print(s1.pop())
print(s1.size())
print(s1.peek())


s1 = list()
print(len(s1))
s1.append("Data structure")  # push
s1.append("DataBase")  # push
print(len(s1))  # size
print(s1[-1])  # peek
print(s1)
print(s1.pop())
print(s1)
print(s1.pop())
print(s1)
# print(s1.pop())
# print(s1)



def check_parentheses(expression : str) -> bool:  # type hint
    stack = []
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(check_parentheses("(2+3)"))
print(check_parentheses("(2+(3*9))"))
print(check_parentheses("(2+(3*9)"))  # 스택에 여는 소괄호가 하나 남아 있어서 False
print(check_parentheses(")2+(3*9)("))