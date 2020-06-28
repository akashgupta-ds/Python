# ---------------------Range() Data Type --------------------------
# 1. This represents a sequence of values
# 2. Immutable
# 3. Form-1 : range(10)         range(end)
# 4. It represents values from 0-9 (end - 1)

print(range(10))        # range(0, 10)
print(type(range(10)))  # <class 'range'>

for i in range(10):
    print(i)

r=range(10)
print('r[0] is :',r[0])     # 0
print('r[4] is :',r[4])     # 4
print('r[0:3] is :',r[0:3]) # range(0, 3)
# immutable
#r[0]=777                    #TypeError: 'range' object does not support item assignment

# form - 2 range(x,y)/ range(start,end)
# to represent numbers from 10,29 (end-1)
print(range(10,30))
for i in range(10,30):
    print('Range is :',i)

# form - 3 range(x,y,steps)/ range(start,end,steps)
# to represent numbers from 10,50 (end-1)
print(range(10,50))
for i in range(10,50,5):
    print('Range is :',i)

# float range does not work
#print(range(10.5,20.6)) #TypeError: 'float' object cannot be interpreted as an integer
