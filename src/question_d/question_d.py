num = 0

def use_global():
    global num
    num = 2

def main():
    global num
    print("initial num: " , num)
    use_global()
    print("modified num: " , num)





