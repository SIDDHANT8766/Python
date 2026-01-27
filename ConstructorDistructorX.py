import gc

class Demo:
    def __init__(self):
        print("Inside Constructor ")

    def __del__(self):
        print("Inside Distructor ")

# Allocate
obj1 = Demo()
obj2 = Demo()

# Use 

# Deallocate
del obj1       # free or delete      
del obj2       # free or delete      

gc.collect()  # gheun ja

print("End of application ")