'''This is simple python program to create a database of switch name and its corresponding switchport name'''
print "This programs will create a switchport list based on the switch name \
which you enter"

switch=raw_input("Enter switch name: ")
stacks=raw_input("Enter number of stacks: ")
stacks=int(stacks)
for i in range(1, (stacks+1)):
	for x in range(1, 49):
		print switch + " %d/0/%d" % (i,x)
 
