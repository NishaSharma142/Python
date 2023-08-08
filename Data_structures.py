#Python Data structures

# List data structures
list=[1,2,3,4.5,"hello",6,7,8]
print(list)
print(type(list))
print(list[0])
print(list[-2])
#print(list[10])
list[0]=12
print(list)

# Tuple
tuple=(1,2,3,4.5,"hello",6,7,8)
print(tuple)
print(type(tuple))
print(tuple[0])
print(tuple[-3])
#tuple[0]=12
#print(tuple)
#print(tuple[10])

# Sets
set=list={1,1,2,3,2,3,4.5,"hello",6,7,8,"apple","banana","orange"}
print(set)
#set[0]
#set[2]=2
set.add(20)
print(set)
set.remove(2)
print(set)
set.remove("orange")
print(set)
set.add(2)
print(set)

# Dictionary
dict={1:"apple",2:"banana",3:"orange",4:"grapes",5:"mango",6:"apple"}
print(dict,type(dict))
dict[1]="coconut"
print(dict)
print(dict[3])
#dict["apple"]
dict2={1:"apple",2:True,3:"orange",4:55.6,5:"mango",6:55}
print(dict2)
dict2[10]="a"
print(dict2)
