class Stack:
    def __init__(self):
        self.items = [] 
    def push(self, item):
        self.items.append(item) 
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return (self.items == [])
class Solution:
    def isValid(self, s: str) -> bool:
        #open aithe push, close aithe pop and check
        ss = Stack()
        t = list(s)
        if len(t) == 1:
            return False
        for i in t:
            if(i == '(' or i == '[' or i == '{'):
                ss.push(i)
            else:
                if(ss.is_empty() == True):
                    return False
                k = ss.pop()
                if(k == '(' and i == ')'):
                    continue
                elif(k == '[' and i == ']'):
                    continue
                elif(k == '{' and i == '}'):
                    continue
                else:
                    return False
        if(ss.is_empty() == False):
            return False
        return True
      ##https://leetcode.com/problems/valid-parentheses/description/
