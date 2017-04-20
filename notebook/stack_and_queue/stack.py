class Stack(list):
    push = list.append
    
    def is_empty(self):
        if not len(self):
            return True
        else:
            return False
        
    def peek(self):
        return self[-1]
    
# pop은 포함되어있음! delete 명령어

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    
    if s.is_empty():
        print("there is no data")
    else:
        while not s.is_empty():
            data = s.pop()
            print(data, end = '  ')