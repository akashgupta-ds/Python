#-------Slice operator -----------------------
# slice[begin:end] => print till end-1 index
# slice[begin:end,step] => steps are jumping steps
# slice[begin:] => The end of string by default  [end index]
# slice[:end] =>   if no value at the begining then [begin index to end index -1]
# slice[:] =>      if no value at the begining & end then [begin index to end index] or entire string


s='Python Program Slicing'
# to get the substring
print(s[0:4])
# +ve index => Left to Right
# -ve index => Right to Left

# <========-ve index ===============
# <=========R to L==================
# -5    -4      -3      -2      -1
# [a  |  b   |   c  |   d   |   e]
# 0     1       2       3       4
# =========L To R =================>
# ========+ve index ===============>

s='abcde'
# s[begin : end]
# returns substring from begin index to end-1
print(s[1:4])       # bcd
print(s[2:4])       # cd
# if end is blank then begin to end string returns as follows :-
print(s[1:])        #bcde => The end of string by default [end index ]
print(s[3:])        #de => The end of string by default  [from index 3 to end index]
print(s[:4])        #abcd => returns the string till the [begin to end index - 1]
print(s[:3])        #abc => if no value at the begining then [begin index to end index -1]
print(s[:])         #abcde =>if no value at the begining & end then [begin index to end index] or entire string
print(s[-1:-4])     #'' => Empty string [always Begin index < end index]  ***imp -ve index
print(s[-4:-1])     #bcd => [always Begin index < end index]  ******** imp -ve index
print(s[-1:])       #e => last indexed character  #-ve index starts with -1
print(s[-5:])       #e => last indexed character

s='Python Program Slicing'
print(s[1:10])       # => 1 to till index 9
print(s[1:10:2])     # => 1 to till index 9 with jump of 2 steps


