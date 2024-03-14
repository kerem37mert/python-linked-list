from Node import Node
from creation import head

newNode = Node(data=4)
temp = head
while(temp.next != None):
    temp = temp.next

temp.next = newNode