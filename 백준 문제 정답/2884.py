h ,m = input().split()
h = int(h)
m = int(m)

if m>=45:
    print(h, m-45)
elif h == 0 and m>45:
    print(23, m-45)
elif h == 0 and m<45:
    print(23, m+15)

else:
    print(h-1, m+15)