'''
[1->2->5->9]
[0->3->5->8]
'''



class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next   	



def merge(l1, l2):
 	l3 = Node(None, None) # temp node
 	prev = l3
 	
 	while l1 != None and l2 != None:
 		i = l1.data # get head element from l1 
 		j = l2.data # get head element from l2

 		if i<=j:
 			prev.next = l1 # get element from l1 and set to prev.next
 			l1 = l1.next
 		else:
 			prev.next = l2 # get element from l2 and set to prev.next
 			l2 = l2.next
 		prev = prev.next # update prev to point to next position

 	# If any of the items are None, merge. 
 	if l1==None:
 		prev.next = l2
 	if l2 == None:
 		prev.next = l1

 	return l3.next




if __name__ =='__main__':
	# create first linked list: 1 -> 2 -> 8
	n3 = Node(8, None)
	n2 = Node(2, n3)
	n1 = Node(1, n2)
	L1 = n1

	# create second linked list: 5 -> 6 -> 9
	n6 = Node(9, None)
	n5 = Node(6, n6)
	n4 = Node(6, n5)
	L2 = n4

	# print the linked list
	merged = merge(L1, L2)
	while merged != None:
	  print(str(merged.data) + ' -> ')
	  merged = merged.next
	print('None')





