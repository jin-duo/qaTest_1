num = input ('請輸入連續數字：')
num2 = [int(a) for a in str(num)]

m1 =[]
m2 =[]
for i in num2 :
    if i % 2 ==0 :
        m1.append(i)
    else :
        m2.append(i)
    m1.sort()
    m2.sort(reverse=True)
new = ''.join(str(e) for e in m1)
m1.append(new)
h = ''.join(str(h) for h in m2)
print(h+new)
