#create bicycle and print the first element
bicycle=[1, 2, 'a']
print(bicycle)
print(bicycle[0])
print('---')

#add one more element to the end
bicycle.append('b')
print(bicycle)
print('---')

#insert element to the begining
bicycle.insert(0, '3')
print(bicycle)
print('---')

#delete the first element
del bicycle[0]
print(bicycle)
print('---')

#delete the last element and the seconf element
bicycle.pop()
print(bicycle)
print('---')
bicycle.pop(1)
print(bicycle)
print('---')

#find and delete the 'a' element
bicycle.remove('a')
print(bicycle)
print('---')

#use sort in bicycle
bicycle=['r', 'a', 'd']
bicycle.sort()
print(bicycle)
print('---')

#reverse sort
bicycle.sort(reverse=True)
print(bicycle)
print('---')

#use 'sorted' function
bicycle=['r', 'a', 'd']
print('original:', bicycle)
print('sorted', sorted(bicycle))
print('original:', bicycle)
print('---')

#'reverse' elements in bicycle
bicycle=['r', 'a', 'k', 'd']
print(bicycle)
bicycle.reverse()
print(bicycle)
print('---')

#finding out how many elements in bicycle
bicycle=['r', 'a', 'k', 'd']
len_variable=len(bicycle)
print(len_variable)
print('---')
