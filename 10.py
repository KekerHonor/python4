# n too hurtelh buh palendrom toog ol
a = int(input("Too: "))
for i in range(10,a+1):
    txt = str(i)
    txt = txt[::-1]
    too = int(txt)
    if i == too:
        print(i)