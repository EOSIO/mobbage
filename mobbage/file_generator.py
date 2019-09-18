import os
import random
from time import perf_counter 

t1_start = perf_counter()
for x in range(0,1000):
        fh = open(str(x), 'wb')
        fh.write(os.urandom(36000))
        fh.close()
# Stop the stopwatch / counter 
t1_stop = perf_counter() 
  
print("Elapsed time:", t1_stop, t1_start)  
  
  
print("Elapsed time during the whole program in seconds:", 
                                        t1_stop-t1_start)