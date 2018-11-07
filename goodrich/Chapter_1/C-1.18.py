lst = [0]

[lst.append(lst[-1]+1) for i in range(2,20,2)]

print(lst)
