# import girl 它是导入girl.py模块，导入模块里的变量的内存地址
import girl


# from...import...导入girl.py里面的have_girl这个变量，复制了一份放在本地
# from girl import have_girl


def send():
    # global have_girl
    print("发女朋友了。。。")
    girl.have_girl = True
    # print(f"have_girl ={have_girl}")
