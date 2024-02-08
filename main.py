import matplotlib.pyplot as p
import math as m

xValues = []
yValues = []
x = 0
while x <= 10:
    xValues.append(x)
    y = m.exp(-x) * m.cos(x)
    yValues.append(y)
    x += 0.01

p.plot(xValues,yValues,color="red")
p.title("A Plot Of exp(-x) cos(x)")
p.grid()
p.xlabel("X")
p.ylabel("Y")
p.axhline()
p.axvline()
p.show()

quit()