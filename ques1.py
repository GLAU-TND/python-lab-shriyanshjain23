class MyException(Exception):
    def __init__(self , v):
        self.v=v
    def __str__(self):
        return self.v
def Xyz(a,b):
    sum=a+b
    if(sum<150):
        raise MyException("Custom Exception Occurred")
    else:
        return sum
a=int(input())
b=int(input())
z=Xyz(a,b)
print(z)
