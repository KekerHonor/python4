# 3 orontoi buh palendrom toog ol
for i in range(100,1000):
    txt = str(i)
    txt = txt[::-1]
    too = int(txt)
    if i == too:
        print(i)