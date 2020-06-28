# ---------------- pass key word---------------
# To remove the error of EOF
# If no need to do anything in method then use pass
# it is an empty statement
# it is null statement
# it won't do anything


def f1(amount):
    pass
    if amount > 10000:
        print('The amount is :',amount)
    else:
        pass    # this block will not do anything

f1(100000)