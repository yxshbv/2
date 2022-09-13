h = int(input('h ='))
m = int(input('m ='))
s = int(input('s ='))


a = h * 30
b = m * (1/2)
c = s * (1 / 120)
result =a+b+c
while result > 360:
    result -= 360
print (result)

