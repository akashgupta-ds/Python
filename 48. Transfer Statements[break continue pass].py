# -----------Transfer Statement-----
# break:
# based on the condition if you want to break the loop then you can use 'break' as shown below :-

for i in range(10):
    if i==7 :
        print('Processing is enough , please break and exit ')
        break
    print(i)

cart=[100,150,20,30,500,23,900]
for item in cart:
    if item >=600:
        print('Sorry we can''t process the order ', item)
        break
    print('Processing Items are :', item)


# 2. Continue : Used to continue the current iteration and continue the next iteration
# Syntax :
# while condition:
#        body
#        body
#       continue
#        body
#        body

for i in range(10):
    if i%2==0:
        continue
    print(i)

# 3. else : with loop
# else means loop without break
# if break does not executed then for else: part will be executed.
cart=[100,150,20,30,500,23]
for item in cart:
    if item >=700:
        print('Sorry we can''t process the order ', item)
        break
    print('Processing Items are :', item)
else:
    print('All Items processed successfully ..')