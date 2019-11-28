try:
    n=int(input('Enter a no.')) + input()
    n.count()
except(AttributeError):
    print('Attribute Error Occurred')
except(TypeError):
    print('Type Error Occurred')
except(ValueError):
    print('Value Error Occurred')
