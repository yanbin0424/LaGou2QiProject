# 有参数
def add(a, b):
    c = a + b
    print(f"a +b ={c}")


# 无参数
def sub():
    A = 10
    B = 5
    C = A - B
    print(f"A - B = {C}")


# 有返回值
def mul(par1, par2):
    par = par1 * par2
    return par


# 无返回值
def div(div1, div2):
    div3 = div1 / div2
    print(f"div1/div2= {div3}")


add(1, 2)

sub()
# 无返回值的默认返回值为None
print(sub())

m = mul(6, 5)
print(m)

div(5, 3)
