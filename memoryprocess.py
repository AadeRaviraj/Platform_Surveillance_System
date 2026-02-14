import psutil
import time

# 3. Add Actual Memory Allocation Feature
# Display real memory usage of each process:
# RSS (Resident Set Size-actual RAM used)
# . VMS (Virtual Memory)
# Memory Percentage
# Requirement
# Show:
# Top 10 memory consuming processes 

def RealmemoryUse():
    top10usage = []
    for  proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    time.sleep(0.2)
    for  proc in psutil.process_iter():
        try:
            # print(proc.memory_info().rss  )
            
            top10usage.append(proc.memory_info().rss)
            
        except:
            pass
    
    print(f"Ram usage : {psutil.virtual_memory().percent}")       
        
    top10usage.sort()
    top10 = 10
    print(f"Top 10 memory use : {top10usage[-top10:]}") 
    # process = psutil.Process()
    # print(process.memory_info().rss / 1024 ** 2 )


RealmemoryUse()