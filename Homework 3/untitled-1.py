list1 = []
list2 = []

n = 30
while n < 3000:
    n = n + 32
    list1.append(n)
m = 44
while m < 3000:
    m = m + 58
    list2.append(m)
    
n = 30
while n > -3000:
    n = n - 32
    list1.append(n)
m = 44
while m > -3000:
    m = m - 58
    list2.append(m)
    
for x in list1:
    for y in list2:
        if x == y:
            print(x)