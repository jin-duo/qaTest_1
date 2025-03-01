a = int(input('請輸入數字：'))
for i in range(0,a+1):
    space = a - i
    for j in range(space):
        print(" ",end="")  
    #星星
    star = 2 * i - 1
    for k in range (star) :    #判斷是否*
        if k == 0 or k == star - 1 or a == i :
            if k % 2 == 0 :
                print("*",end="")
            else :
                print(" ",end="")
        else:
            print(" ",end="")
    print()