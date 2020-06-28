#---------------Reserved Keywords -----------------------
# 33 Reserved Keywords
# True , False , None                                   3
# and , or , not , is                                   4
# if , else , elif                                      3
# while , for , break , continue , return , in , yield  7
# try , except , finally , raise , assert               5
# import , from ,as , class , def , pass , global       7
# nonlocal , lambda (anonymous), del , with             4

# continue : skip current iteeration only in loop
# pass : skip anywhere

# raise => Throw
# lambda => anonymous function => without name

# NOTE :
# 1. Only alphabet symbols
# 2. except first 3 , all
# 3. 33 Keywords

#O/P:
#['False', 'None', 'True',
# 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
# 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
# 'try', 'while', 'with', 'yield']

import keyword
print(keyword.kwlist)
#print(dict(keyword.kwlist))