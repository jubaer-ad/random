# class Tree:
#     m = 5
#     l = ["a", "b"]
#     pass

# t001 = Tree()
# t002 = Tree()

# t001.name = "t001"
# t002.name = "t002"
# print(t001.name)
# # print(t001.m)
# # print(t001.l)
# print(t001.__dict__)
# t002.l = ["c", "d"]
# t001.m = 7
# print(t002.name)
# # print(t002.m)
# # print(t002.l)
# print(t002.__dict__)
# print(Tree.__name__)
# print(Tree.__dict__)

# class A(object):
#     def foo(self):
#         self.foo = 'foo'
#     def bar(self):
#         self.bar = 'bar'

# a = A()
# a.val = 6
# print(a.__dict__)
# a.foo()
# print(a.__dict__)
# print(A.__dict__)

a = 7
print("a is: {}".format(a))
del a
# a.__del__()
print("a is: {}".format(a))