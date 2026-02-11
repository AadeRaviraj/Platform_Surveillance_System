import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border = "-" * 60
    Ret = False
    Ret = os.path.exists(FolderName)
    
    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory For log files get created successfully")
            
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Platform_%s.log" %timestamp)
    

    print("Log file gets created with name :",FileName)
    
    fobj = open(FileName,"w")
    fobj.write(Border+"\n")
    
    fobj.write("----------- Platform Surveillance System --------\n")
    fobj.write("Log created at : "+time.ctime() + "\n")
    
    fobj.write(Border+"\n\n")
    
    fobj.write("---------------------- System Report ----------------------- \n")
    
    
    # print("CPU Usage : ",psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" % mem.percent)
    fobj.write(Border+"\n")
    
    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent) )
        except:
            pass
    
    fobj.write(Border+"\n")
    
    net = psutil.net_io_counters()
    
    fobj.write(Border+"\n")
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n"% (net.bytes_sent / (1024 *1024)))
    
    fobj.write("Recv : %.2f MB\n"% (net.bytes_recv / (1024 *1024)))
    fobj.write(Border+"\n")
    
    # Process LOG
    
    Data = ProcessScan()
    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Username : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("Start Time : %s\n" %info.get("create_time"))        
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        fobj.write(Border+"\n")
        
    
    
    
    fobj.write(Border+"\n")
    fobj.write("---------------------- End of log file ---------------------\n")
    fobj.write(Border+"\n")
    

def ProcessScan(): 
    listProces = []
    
    # warm up CPU percent
    for  proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    time.sleep(0.2)
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid","name","username","status","create_time"])
            # Convert create_time 
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] ="N/A"
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            
            listProces.append(info)
        # print(info["pid"], info["name"], info["status"])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) :
            
            pass
    return listProces
    

def main():
    
    Border = "-" * 60
    print(Border)
    print("-----------  Platform Surveillance System --------")
    print(Border)
    
    if(len(sys.argv ) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to  : ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 :  Store information about processes")
            print("5 : Store information about CPU ")
            print("6 : Store information about RAM usages ")
            print("5 : Store information about secondary storage ")
            
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval: The time in minutes for periodic scheduling  ")
            print("DirectoryName : Name of decretory to create auto logs ")
            
        else:
            print("Unable tto Proceed as there is no such option ")
            print("Please use --h or --u get more details")
            
    # python demo.py 5 Marvellous
    elif (len(sys.argv) == 3):
        print("Inside projects logic")        
        print("Time interval : ", sys.argv[1])
        print("Directory name : ", sys.argv[2])
        
        # Apply the scheduler
        schedule.every(int(sys.argv[1]) ).minutes.do(CreateLog, sys.argv[2])
        
        print("Platform Surveillance System started successfully")
        print("Directory CReated ",sys.argv[2])
        print("Time Interval in minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        
        # wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    else:
        print("Invalid No of command line arguments")
        print("Unable tto Proceed as there is no such option ")
        print("Please use --h or --u get more detail")
        

    
    
    
    print(Border)
    print("--------------- Thank You for using Our script -------------")
    print(Border)

if __name__ == "__main__":
    main()