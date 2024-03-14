from creation import head

temp = head
if(head.next == None):
    head = None
else:
    while(temp.next.next != None):
        temp = temp.next
    temp.next = None