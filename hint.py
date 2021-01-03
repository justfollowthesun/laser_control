class A:
    def a(self):
        print('Class A, function a')

class B:
    def b(self):
        print('Class B, function b')

class child(A,B):
    def __init__(self):
        print('Created class child')
    def a(self):
        print('Fake a')


ch=child()
ch.a()
ch.b()

class second_child(B):
    pass

# ch2=second_child()
# ch2.a()
# ch2.b()

class third_child(child):
    def __init__(self, name1,name2):
        print(f'Hello {name1}')
        print((f'Hello {name2}')

ch3=third_child()
ch3.a()
ch3.b()
print(third_child.__mro__)

#print(ch3.__mro__)
