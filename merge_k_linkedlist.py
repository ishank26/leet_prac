import heapq

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None



def mergeK(lists):
 	dummy = Node(0) # temp node
 	pq = []

 	for i in range(len(lists)):
 		if lists[i]:
 			heapq.heappush(pq, (lists[i].data, lists[i], i))

 	tmp = dummy

 	while pq:
 		# heap maintains already sorted values
 		# get the minimum item and add to dummy 
 		# set old tmp next to item
 		# set tmp to item for further comparison 
 		# heappush item.next to heap
 		heap_item = heapq.heappop(pq) # (data, list, pos)
 		if heap_item:
 			tmp.next = heap_item[1]
 			tmp =  tmp.next

 			if heap_item[1].next:
 				heapq.heappush(pq, (heap_item[1].next.data, heap_item[1], heap_item[2]))
 	
 	return dummy.next








if __name__ =='__main__':
	# create first linked list: 1 -> 2 -> 8
	n3 = Node(8)
	n2 = Node(2)
	n1 = Node(1)
	n1.next = n2
	n2.next = n3
	L1 = n1

	# create second linked list: 6 -> 6 -> 9
	n6 = Node(9)
	n5 = Node(6)
	n4 = Node(6)
	n4.next = n5
	n5.next = n6
	L2 = n4

	# create third linked list: 1 -> 7 -> 10
	n9 = Node(10)
	n8 = Node(7)
	n7 = Node(1)
	n7.next = n8
	n8.next = n9
	L3 = n7

	lists = [L1,L2,L3]



	# print the linked list
	merged = mergeK(lists)
	while merged != None:
	  print(str(merged.data) + ' -> ')
	  merged = merged.next
	print('None')
