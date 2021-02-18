#GENERATING 3*3 MATRIX WITH 9 RAONDOM PRIME NUMBERS (BY USING FOR LOOP) 

list1 = [2,3,5,7,11,13,17,19,23]
for i in list1 :
	if i == 7 
	continue
	print (i)
	list1 = [2,3,5,11,13,17,19,23]
	
list1 = [2,3,5,7,13,11,19,17,23]
print (list1 [0])

max_value = list1[0]
for i in list1:
	if i > max_value 
	max_value = i 
	print("max_value: ", max_value)
        print("i: ", i)
	if i == 19 
	break
print(max_value)

          2
max_value : 3
	i:3
max_value : 5
	i:5
max_value :7
	i:7
max_value : 13
	i:13
		
		
list1 = [2,3,5,7,13,11,19,17,23]
nums = list1
print (nums)
list2 = [i*2 for i in nums if i % 13 == 0]
print(list2) 

list2 = [26]
		
