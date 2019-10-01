data = [1,2,8,3]

largest = 0
second_largest = 0

for a in data:
    if a > largest:
        second_largest = largest
        largest = a
    elif a < largest and a > second_largest:
        second_largest = a
print(second_largest)

print("largest: {}".format(largest))
print("second_largest: {}".format(second_largest))
L= [1,2,8,3]
maxL = max(L)
#list comprehension for remove all occurrences of max(L)
L_filter = [e for e in L if e!=maxL]
print (L)
#print max of L_filter, second maximum of L
print (max(L_filter))

lq= [1,4,8,3]
lq.remove(max(lq))
print(max(lq))

a = [0, 2, 3, 2]
a.remove(3)
print(a)

from functools import reduce
ly= [1,4,8,3]
s= reduce(lambda x,y: x if x>y else y, ly )
print(s)
# remove duplicate
mylist = [3, 2, 1, 3, 4, 4, 4, 5, 5, 3]

print( list({x:1 for x in mylist}.keys()))
 # to sort by values
# sorted(d.items(), key=lambda x: x[1])

i = ['cat','atc','ret','ter','cta','act']
d = []
# p = {x:''.join(x) for x in sorted(i)}
word_list = ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"]
anagram_list = []
for word_1 in word_list:
    for word_2 in word_list:
        if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
            anagram_list.append(word_1)
print(anagram_list)


# print(p)

#["cat","atc","cts","act"]
#[