# sets : unoredered,mutable,no dulipcates

myset={1,2,3,4,3}
print(myset) # {1,2,3,4}

myset2=set(["hello",23,3,4])
myset3=set("hello")
print(myset2) # {23, 'hello'}
print(myset3)
print(len(myset3))

myset.add(5) # add element to set
print(myset) # {1,2,3,4,5}

myset.remove(3) # remove element from set
print(myset) # {1,2,4,5}

myset.discard(3) # same as remove  but only remove element from set if it exists
print(myset)# 3 doesn't exist so it didn't do anything but in remove it would have raised an error

myset.pop() # remove random element from set
print(myset)

myset.clear() # clear all elements from set
print(myset)

myset.update([1,2,3,23,4]) # add multiple elements to set
print(myset)

print(myset.intersection(myset2)) # find common elements between two sets


print(myset.union(myset2) )# find all elements in both sets

myset.difference(myset2) # find elements in set1 but not in set2
# find elements in set2 but not in set1

print(myset.symmetric_difference(myset2)) # find elements in set1 or set2 but not

a={1,2,3,4,5,6,7,8}
b={2,4,6,8,10}
diff=a.difference(b)
print(diff)

a.symmetric_difference_update(b)# not common elements
print(a) # {1, 3, 5, 7, 10}

print(a.issuperset(b))
# True if all elements of b are in a

setA={1,2,3,4,5}
setB={7,8}
print(setA.isdisjoint(setB))
# True if there are no common elements between setA and setB

set3=set(setA)
print(set3)  # deep copy

a=frozenset([1,2,3,4])
# frozenset is immutable
print(a) # frozenset({1, 2, 3, 4})
##a.add(22)
# AttributeError: 'frozenset' object has no attribute 'add'
#it will give us error