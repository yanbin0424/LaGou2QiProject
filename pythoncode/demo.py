a = 1


def fun():
    global a
    a = 2
    print(a)


print(a)
fun()
print(a)
