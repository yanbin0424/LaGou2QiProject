# 只有在当前文件下__name__的名字才是'__main__'
from send import send
from show import show

if __name__ == "__main__":
    send()
    show()
