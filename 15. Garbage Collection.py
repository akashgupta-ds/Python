#------------Garbage Collector------------------
# The main objective is to detroy objects and free up memory.
# It improves the performance and memory optimization. eg. s=None available for G.C.
# If the objet does not have any object reference then that object is available for garbage collection.
# Based on our requirement We can enable and disable garbage collector.
# To destroy useless objects.
# Python prog is robust for memory problems/handling
#   1. import gc ###    module
#   2. gc.isenabled()
#   3. gc.disabled()
#   4. gc.enable()

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())



