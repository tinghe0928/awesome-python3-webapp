class A:
    x=1
    @classmethod
    def test(cls):
        print(cls,cls.x)

class B(A):
    x=2
B.test()

'''
输出结果:
<class '__main__.B'> 2
'''
