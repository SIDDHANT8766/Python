import gc

class Demo:
    def __init__(self):
        print("Inside Constructor ")

    def __del__(self):
        print("Inside Distructor ")

# Allocate
obj = Demo()

# Use 

# Deallocate
del obj       # free or delete      

gc.collect()  # gheun ja

print("End of application ")