#----------------- Named Constructor -------------------
# __init__(self)
#----------------- Named Destructor --------------------
# __del__(self)

# close db connection
# close n/w connection
# GC calls destructor before destroying object to implement clean-up activity/ release memory.It calls automatically.
# GC is daemon thread which runs in background.
# GC invoked by python virtual machine (PVM).
# At the and of application GC destroys all the objects.
# if we do GC disable on one platform, it will not be considered as behaviour varies from platform to platform
# When multiple references for same object is referencing then the object only applicable for GC, if all the reference
# destroyed/deleted.

import time
class Test:
    def __init__(self):
        print('Object Initialization')
    def __del__(self):
        # close db connection
        # close n/w connection
        print('Fulfilling last wish ...')

t1=Test()
t1=None     # not pointing to any object ,available for GC.
time.sleep(10)
list=[Test(),Test(),Test()]
#print(sys.getrefcount())
time.sleep(10)
list=None
time.sleep(10)
print('End of app')
