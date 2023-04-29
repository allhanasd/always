h, m = input().split()
h = int(h)
m = int(m)
mm = h * 60 + m + gap
print(mm//60 % 24, mm % 60)