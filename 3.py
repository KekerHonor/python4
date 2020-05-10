# a-aas b hurtelh 5d huvaagdah toonuudiin niilberiig ol
a = int(input("A "))
b = int(input("B "))
c = 0
for i in range(a, b+1):
    if i // 5 != 0:
        c+=i
print(c)
