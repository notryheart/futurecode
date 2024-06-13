class Node:
    def __init__(self, val: int, next = None) -> None:
        self.val = val
        self.next = next

class linked_list:
    def __init__(self, root) -> None:
        self.root = root

    def append(self, val: int) -> None:
        tmp = self.root
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val = val)

    def output(self) -> None:
        tmp = self.root
        while tmp:
            print(tmp.val, end = " ")
            tmp = tmp.next
    
    def search(self,val) -> bool:
        tmp = self.root
        while tmp:
            if tmp.val == val:
                return True
            tmp = tmp.next
        return False

    def pop(self):
        tmp = self.root
        while tmp.next.next:
            tmp = tmp.next
        tmp.next = None

    def remove(self):
        tmp = self.root
        while tmp.next.next:
            tmp = tmp.next
        tmp.next = None

root = Node(10)
ll = linked_list(root = root)
ll.append(15)
ll.append(30)
ll.pop()
ll.remove()
