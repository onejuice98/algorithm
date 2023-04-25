# tree 문제
class Node:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
class LinkedList:
    def __init__(self, size):
        self.head = Node(1)
        self.current = self.head

        for i in range(2, size+1):
            self.current.next = Node(i, prev=self.current)
            self.current = self.current.next
            
            
    def slide(self, value, target):
        value_count = 0
        target_count = 0

        current = self.head

        # value 와 맞는 move_num 위치 찾기
        while value != current.value:
            value_count += 1
            current = current.next            
        
        move_num = current
        
        # target 와 맞는 value 위치 찾기
        current = self.head
        while target != current.value:
            target_count += 1
            current = current.next
        
        end_point = current
            
        # move_num 링크 제거 후 앞뒤로 연결
        if move_num.prev != None:
            move_num.prev.next = move_num.next
        else:
            self.head = move_num.next
        if move_num.next != None:
            move_num.next.prev = move_num.prev        
        
        # end_point 링크 제거 후 move_num insert            
        move_num.next = end_point.next
        move_num.prev = end_point
        if end_point.next != None:
            end_point.next.prev = move_num
        end_point.next = move_num
        
        result = target_count - value_count
        if result < 0:
            result += 1
        return result
        
        
    def getListValue(self):
        result = []
        current = self.head
        result.append(current.value)
        while current.next != None:
            result.append(current.next.value)
            current = current.next
        return result
    
N, Q = map(int, input().split())
Q_list = []
nums = LinkedList(N)
for i in range(Q):
    a, b = map(int, input().split())
    print(nums.slide(a, b))
    

print(*nums.getListValue())