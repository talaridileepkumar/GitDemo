# Why is Python called as interpreted language?
# Python is called an interpreted language because it goes through an interpreter,
# which turns code you write into the language understood by your computer's processor.

#1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Data types in Python:
# 1>String:(Immutable)
# s='Dileep,kumar,Talari'
# Basic Operations on string
# a)s.upper(),s.lower()s.capitalize(),s.isupper(),s.islower(),s.count(),s.split()


#2 List:(Mutable)
# l=[4,2,5,84,'Dileep']
# Basic Operations on List
#l.append(),l.insert(),l.extend(),l.pop(),l.clear(),l.reverse(),l.sort(),l.sort(reverse=True)

# D/B list and tuple ?
# list is mutable,while tuple is unmutable objects
# list is specified with [],tuple is specified by()
# tuple is more efficient than listTuples are stored in a single block of memory.
# Tuples are immutable so, It doesn't require extra space to store new objects.
# It is the reason creating a tuple is faster than List. It also explains the slight difference in indexing speed is faster than lists, because in tuples for indexing it follows fewer pointers

#3 Dictionary:(Mutable)
# det={'Name':'Dileep','age':25}
# How Dictionary works is of Hash Mapping.
# d = {3: 'd', 2: 'c', 1: 'b', 0: 'a',3:'dileep'}
# d1={'name':'dileep'}
# A dictionary is a data structure that maps keys to values.
# # A hash table is a data structure that maps keys to values by taking the hash value of the key
# # (by applying some hash function to it)
# # and mapping that to a bucket where one or more values are stored.
# # Basic Operations on Dictionary
# d.keys(),d.values(),d.items(),d.clear(),d.pop(),d.update()




'''
1. self is used to reffer the instance of the class to the method.
2. Based on self only the method will get to know for which instace it has to responce.
3. We can give any name in place of self.
'''
# class A():
#     school='SVIT'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display(self):
#         print('Name is :',self.name)
#         print('Age is :',self.age)
#'''
# 1. Using @staticmethod decorator we can create static method.
# 2. For Static method self argument doesn't required.
# 3. Using staticmethod we can provide same behavior to the all the instances of class.
# 4. staticmethod we can call through instance or without instance.'''
#     @staticmethod
#     def data():
#         print('Hi Data is being printed')
'''
# '''
# 1. Using @classmethod decorator we can create Class method.
# 2. For class method we have to give cls argument.
# 3. Using classmethod we can change class attributes.
# 4. classmethod we can call through instance or without intance.
# '''
#     @classmethod
#     def info(cls):
#         return cls.school

#
# obj=A('DIleep',25)
# obj.display()
# print(obj.school)
# print(obj.info())
# obj.data()
'''
1. An abstract method is a method that is declared, but contains no implementation.
2. By defining an abstract base class, you can define a common API for a set of subclasses.
3. By using abc module we can define abstract class.
'''
from abc import ABCMeta,abstractmethod
# from abc import ABCMeta,abstractmethod
#
# class One(metaclass=ABCMeta):
#     @abstractmethod
#     def add(self):
#         print(' \n ONE ADD ')
#
#     @abstractmethod
#     def sub(self):
#         pass
#
# # a = One()
# # a.add()
# class Two(One):
#     def add(self):
#         print(" \n TWO ADD")
#
#     def sub(self):
#         print(' \n TWO SUB')
# ins = Two()
# ins.add()
# ins.sub()
# '''
# 1. Encapsulation is wrapping data(methods) together into single uint.
#
# 2. Using encapsulation we can give protection to the class members. Using access modifiers.
# '''
# Access Modifiers:
# class A:
#     name='Dileep Public'
#     _name='Dileep Protet'
#     __name='Dileep Private'
#
# ob=A()
# print(ob.name)---To call Normal variables
# print(ob._name)-----To call Protected Variables
# print(ob._A__name)----To call Private Variables
#
# '''
# Method Overriding
# 1. If you have same method names in class A and class B, then if you Inheritence class A into class B then Class A method will override with class B method.
# '''
# class A():
#     def add(self):
#         print('\n A ADD ')
#
# class B():
#     def add(self):
#         print('\n B ADD ')
#
# class C(B, A):
#     def add(self):
#         print(' \n C ADD ')
#
# inst = C()
# inst.add()



# class Parrot:
#     def fly(self):
#         print('parrot can fly')
#
#     def swim(self):
#         print('parrot cant swim')
#
# class Penguin(Parrot):
#     def fly(self):
#         print('Penguin cant fly')
#
#     def swim(self):
#         print('Penguin can swim')
#
# def swim_test(bird):
#     bird.swim()
# # def fly_test(bird):
# #     bird.fly()
# pa=Parrot()
# pe=Penguin()
# swim_test(pe)
# swim_test(pa)

'''
1. Lambda is a another way to create a function.
2. Lambda is a one line anonymous function it doesn't contains name.
3. Using lambda we can do only one expression.
add=lambda a,b:a+b
print(add(2,4))
'''

'''
1. map is used to do operation on each iterable value and it will return all operations result in map object foramt.
2. Map taks two parameters one is function another one is iterable object
ma=map(lambda a,b:a+b,[1,2,34],[2,3,4])
print(list(ma))
'''

'''
1. The filter() method filters the given sequence with the help of a function and retun filter object.
2. filter takes two parameters one is function another one is iterable object
fi=filter(lambda a:a>2,[2,1,3,4,5,0])
print(list(fi))
'''

'''
1. reduce is used to do operation on each iterable value and its return all operations result sum.
2. reduce takes two parameters one is function another one is iterable object
from functools import reduce
fib = reduce(lambda a,b: a+b,[1,2,3,4,5])
print(fib)
'''


''' ITERATOR
1. using iterators we can get sequence of values based on demand by using next() function.
2. We can create iterators by using iter() function.
'''
# l=[0,12,3,4,4,5,56,67]
# iter_obj=iter(l)
# print(next(iter_obj))

'''
1. Using generator we can execute a block of code based on demand by using next() function.
2. using yield keyword we can create a generator.
def top_ten(n):
    for i in range(1,n):
        sq=i*i
        yield sq
values=top_ten(6)
# print(next(squares))
'''

'''
1. Using decorators we can change a behavior of function without changing any fucntion code.
2. using @ we can assign decorator to the function
def wrapper(fun):
    def inner(a,b):
        if b==0:
            print('cant be divided by zero')
            return
        fun(a,b)
    return inner
@wrapper
def mul(a,b):
    print(a/b)

mul(30,0)
'''

''' Threading Module
In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects,
preventing multiple threads from executing Python bytecodes at once.'''

# from threading import *
# import time
# class Hello(Thread):
#     def run(self):
#         for i in range(10):
#             print('Hello')
#             time.sleep(1)
#
# class Hi(Thread):
#     def run(self):
#         for i in range(10):
#             print('Hi')
#             time.sleep(1)
# t1=Hello()
# t2=Hi()
# t1.start()
# time.sleep(5)
# t2.start()
#
# t1.join()
# t2.join()
#
# print("bye")

# class A:
#     school = 'Sarada'
#
#     def display(self):
#         print('Hi How are you doing')
#     @staticmethod
#     def sum():
#         print('Hi i am sam')
#     @classmethod
#     def add(cls):
#         return cls.school
#
# obj=A()
# print(obj.add())
# alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# s='dileepkumar'
# cnt=0
# for i in s:
#     sum = alpha.index(i)
#     cnt=sum+cnt
# print(cnt)

t=186
t//=10
print(t)



