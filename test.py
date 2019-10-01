from abc import ABC, abstractmethod


class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print("Some implementation!")


class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")


x = AnotherSubclass()
x.do_something()

l = [1,2,3,4,5,6,7,8,9]
print(l[2:-8:1])

class A(object):

    def __init__(self):
        print("init")
    def __new__(cls, *args, **kwargs):
        print("new")
        return super(A,cls).__new__(cls)
A()
print(dir(A()))


class B():
    @staticmethod
    def trt(data):
        print(data)
b= B()
b.trt(10)

a=[1,2,3]
b=[1,2,3]
print(id(a),id(b))

mydict = {'george':16,'amber':19}
da=list(mydict.keys())[list(mydict.values()).index(16)]
print(['george', 'amber'][0])
print(da)

def add(lst, obj, index):
    return lst[:index] + [obj] + lst[index:]
print(add([1,2,3,4],2.5,2))

# add the new item at end of list without len function
def ase(data):
    return data + [7]
    #data.index(data[-1]) + 1
data =[1,2,3,4,5,6]
print(ase(data[:-1]))

o=[1,2,3,4,5,6,7,8,9]
print(o[::-2])

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v
print(fun(data[0]))

def f(i, values = []):
    values.append(i)

    return values
print( f(1))
print( f(2))
print(f(3))

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print (sum)

init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')

print (init_tuple_a + init_tuple_b)
import copy
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)

del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)

print(id1 == id2)

l= [1,2,3]
y= l
l[0]= 7
print(l,y)

w= 10
r=w
w=20
print(w,r)


def twoSum( l1,l2):
    x= int("".join(map(str,l1[::-1])))
    y= int("".join(map(str,l2[::-1])))
    return  (x+y)


l1 = [2,4,3]
l2 = [5,6,4]
print(twoSum(l1,l2))

def lengthOfLongestSubstring(word):
    n = len(word)
    longest = 0
    longestword = {}
    for i in range(n):
        seen = []
        for j in range(i, n):
            if word[j] in seen: break
            seen.append(word[j])
        longest = max(len(seen), longest)
        longestword["".join(seen)]= longestword.get("".join(seen),0)+1
    return longest, longestword

print(lengthOfLongestSubstring("abcabcbb"))


def aa():
    print("hello")


aa()
del aa
#dir(aa())

def multiplexers ():

    return [lambda n: index * n for index in range (4)]

print( [m (2) for m in multiplexers ()])

def fast (items= []):
    items.append (1)
    return items

print (fast ())
print (fast ([10,9]))
print (fast ())

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)
f(5,[8,9])

def jin(a,b=10):
    print(a,b)
jin(10,20)
jin(40)
jin(80,50)