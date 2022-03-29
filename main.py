import matplotlib.pyplot as plt

val = input("enter value")

val = int(val)

xax = []
yax = []

n = 1

while val != 1:
    if val % 2 == 0:
        val = val / 2
        xax.append(int(val))
        yax.append(n)
        n = n + 1
    else:
        val = (3 * val) + 1
        xax.append(int(val))
        yax.append(n)
        n = n + 1

plt.plot(yax, xax)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graph!')

for x, y in zip(yax, xax):
    label = "{:}".format(y)

    plt.annotate(label,
                 (x, y),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')

plt.show()
