import time
#Iterative
def iterative(i):
    for i in range(i,1000):
        i+1
    return(i)

#Recursive //Obsoleto
def recursive(i):
    if i >= 50:
        return(i)
    else:
        return(recursive(i+1))

start_time = time.time()
iterative(0)
print("iterative takes %s seconds\n" % (time.time() - start_time))
start_time = time.time()
recursive(0)
print("recursive takes %s seconds\n" % (time.time() - start_time))
