have_girl = False


def send():
    global have_girl
    print("发女朋友了。。。")
    have_girl = True
    print(f"have_girl ={have_girl}")


def show():
    if have_girl == True:
        print("有女朋友了，好开森。。。")
    else:
        print("单身贵族 *_*")


send()
show()
