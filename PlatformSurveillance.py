# import psutil
# import sys
# import os
# import time
# import schedule
# import smtplib
# from email.message import EmailMessage 


# # mail send 



# # 4. Add Periodic Email Reporting Feature
# # Automatically send system report through email at regular intervals.
# # Email must contain:
# # Log file attachment
# # Summary of:
# # Total processes
# # Top CPU usage processes
# # Top Memory usage processes
# # a
# # Top Thread count processes
# # Top Open file processes
# # Usage
# # PlatformSurveillance.py "MarvellousLogs" "receiver@gmail.com"  10
# # Where:
# # MarvellousLogs →→ log folder
# # receiver@gmail.com receiver mail
# # 10 interval in minutes


# # Expected Output in Log File
# # Each process entry should include:
# # Process Name
# # PID
# # CPU %
# # Memory (RSS)
# # Threads Count
# # Open Files Count
# # Timestamp


# # ==========================================
# # Program : Simple Gmail Mail Sender
# # Author  : Raviraj Aade 
# # Purpose : Send mail using Python SMTP
# # ==========================================




# # ------------------------------------------------
# # Function : send_mail
# # Description : Sends email using Gmail SMTP server
# # ------------------------------------------------
# def send_mail(Foldername ,receiver) :
    
#     CreateLog(Foldername)
    
        
#     sender_email = "ravirajade2@gmail.com"

#     app_passward = "XXXX XXXX XXXX XXXX"
    
    
#     # receive_email ="rushikeshchavhan23@gmail.com"
    
#     subject = "Test mail from python script" 
#     body = """Jay Ganesh, 
#         This is a test email sent using  Python.
#         Regards,
#         Raviraj Aade
#     """
    
#     Border = "-" * 60
    
#     LogFileName = "LogfileName.log"
#     fobj = open(LogFileName,"w")
    
    
    
#     Data = ProcessScan()
#     for info in Data:
#         # Process Name
#         # PID
#         # CPU %
#         # Memory (RSS)
#         # Threads Count
#         # Open Files Count
#         # Timestamp
#         fobj.write("Process Name : %s\n" %info.get("name")) 
#         fobj.write("PID : %s\n" %info.get("pid"))     
#         fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
#         fobj.write("Memory %% : %.2f\n" %info.get("rss"))
#         fobj.write("Thread Count : %s\n" %info.get("num_threads"))
#         fobj.write("Open Files %s:\n"%info.get("open_files"))        
#         fobj.write("Log created at : "+time.ctime() + "\n")
#         fobj.write(Border+"\n")
    
    
#     fobj.close()
    
    
#     # create Email Object 
#     msg = EmailMessage()
    
#     # Set mail header
#     msg["From"] = sender_email
#     msg["To"] = receiver
#     msg["Subject"] = subject
    
#     # Add mail body
#     msg.set_content(body)
    
#     fobj = open(LogFileName,"rb")
#     data = fobj.read()
#     print(data)
#     msg.add_attachment(data,maintype = "text",subtype ="plain", filename ="Logfile.txt")
    
#     # Create SMTP SSL Connection Manually
#     smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    
#     # Login using Gmail + App Password
#     smtp.login(sender_email,app_passward)
    
#     # Send the email
#     smtp.send_message(msg)
#     print("Mail send successfully")
    
#     # Close Connection Manually
#     smtp.quit()



# def CreateLog(FolderName):
#     Border = "-" * 60
#     Ret = False
#     Ret = os.path.exists(FolderName)
    
#     if Ret == True:
#         Ret = os.path.isdir(FolderName)
#         if Ret == False:
#             print("Unable to create folder")
#             return
#     else:
#         os.mkdir(FolderName)
#         print("Directory For log files get created successfully")
            
#     timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
#     FileName = os.path.join(FolderName,"Platform_%s.log" %timestamp)
    

#     print("Log file gets created with name :",FileName)
    
#     fobj = open(FileName,"w")
#     fobj.write(Border+"\n")
    
#     fobj.write("----------- Platform Surveillance System --------\n")
#     fobj.write("Log created at : "+time.ctime() + "\n")
    
#     fobj.write(Border+"\n\n")
    
#     fobj.write("---------------------- System Report ----------------------- \n")
    
    
#     # print("CPU Usage : ",psutil.cpu_percent())
#     fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
#     fobj.write(Border+"\n")

#     mem = psutil.virtual_memory()
#     fobj.write("RAM Usage : %s %%\n" % mem.percent)
#     fobj.write(Border+"\n")
    
#     fobj.write("\nDisk Usage Report\n")
#     fobj.write(Border+"\n")
#     for part in psutil.disk_partitions():
#         try:
#             usage = psutil.disk_usage(part.mountpoint)
#             fobj.write("%s -> %s %% used\n" %(part.mountpoint, usage.percent) )
#         except:
#             pass
    
#     fobj.write(Border+"\n")
    
#     net = psutil.net_io_counters()
    
#     fobj.write(Border+"\n")
#     fobj.write("\nNetwork Usage Report\n")
#     fobj.write("Sent : %.2f MB\n"% (net.bytes_sent / (1024 *1024)))
    
#     fobj.write("Recv : %.2f MB\n"% (net.bytes_recv / (1024 *1024)))
    
    
#     fobj.write(Border+"\n")
    
#     # Process LOG
    
#     Data = ProcessScan()
#     for info in Data:
#         fobj.write("PID : %s\n" %info.get("pid"))
#         fobj.write("Name : %s\n" %info.get("name"))
#         fobj.write("Username : %s\n" %info.get("username"))
#         fobj.write("Status : %s\n" %info.get("status"))
#         fobj.write("Start Time : %s\n" %info.get("create_time"))        
#         fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
#         fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
#         fobj.write(Border+"\n")
        
#     fobj.write(Border+"\n")
    
#     # 1. Add Thread Monitoring Feature
#     # For each running process, display:
#     # Process Name
#     # PID
#     # Number of Threads created by that process
#     # Requirement
#     # Store information in log file along with timestamp.
    
#     fobj.write(Border+"\n")
#     fobj.write("\n--------------------Thread monitoring q1--------------------\n")
#     for info in Data:
#         fobj.write("PID : %s\n" %info.get("pid"))
#         fobj.write("Name : %s\n" %info.get("name"))
        
#         fobj.write("Threads : %s\n" %info.get("threads"))
#         fobj.write("Num Of Thread : %s\n" %info.get("num_threads"))
#         fobj.write(Border+"\n")
#     fobj.write(Border+"\n")
    
    
    
#     # 2. Add Open Files Monitoring Feature
#     # For each process, display:
#     # Number of files opened by the process
#     # Requirement
#     # Count open file descriptors using system/library calls
#     # Handle permission errors properly
#     # Mention "Access Denied" in log if required
#     fobj.write(Border+"\n")
    
#     fobj.write("\n-------------------- File monitoring q2 --------------------\n")
#     for info in Data:
#         fobj.write("PID : %s\n" %info.get("pid"))
#         fobj.write("Name : %s\n" %info.get("name"))
#         fobj.write("Open files %s:\n" %info.get("open_files"))
#         fobj.write(Border+"\n")
#     fobj.write(Border+"\n")


    
#     # 3. Add Actual Memory Allocation Feature
#     # Display real memory usage of each process:
#     # RSS (Resident Set Size-actual RAM used)
#     # . VMS (Virtual Memory)
#     # Memory Percentage
#     # Requirement
#     # Show:
#     # Top 10 memory consuming processes 

    
#     fobj.write(Border+"\n")

#     top_ten_memory = sorted(Data, key=lambda x: x["rss"], reverse=True)[:10]
#     fobj.write("\n----------------Top 10 memory consuming processes q3 -------------\n\n")

#     for proc in top_ten_memory:
        
#         memory_dict = {
#             "pid": proc["pid"],
#             "name": proc["name"],
#             "rss": proc["rss"],
#             "vms": proc["vms"],
#             "memory_percent": proc["memory_percent"]
#         }

#         fobj.write(str(memory_dict))
#         fobj.write("\n\n")
#     fobj.write(f"Top 10 process : {top_ten_memory}")
#     fobj.write(Border+"\n")

    
    
    
#     fobj.write(Border+"\n")
#     fobj.write("---------------------- End of log file ---------------------\n")
#     fobj.write(Border+"\n")
#     fobj.close()






# def ProcessScan(): 
#     listProces = []
#     process_list = []
#     # warm up CPU percent
#     for  proc in psutil.process_iter():
#         try:
#             proc.cpu_percent()
#         except:
#             pass
#     time.sleep(0.2)
    
    
#     for proc in psutil.process_iter():
#         try:
#             info = proc.as_dict(attrs=["pid","name","username","status","create_time"])
#             # Convert create_time 
#             try:
#                 info["create_time"] = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(info["create_time"]))
#             except:
#                 info["create_time"] ="N/A"

#             # CPU & Memory
#             info["cpu_percent"] = proc.cpu_percent(None)
#             info["memory_percent"] = proc.memory_percent()
            
#             # Memory details
#             mem_info = proc.memory_info()
#             info["rss"] = mem_info.rss
#             info["vms"] = mem_info.vms
            
#             # Threads
#             info["threads"] = proc.threads()
#             info["num_threads"] = proc.num_threads()
            
#             # Open files (Windows)
#             try:
#                 info["open_files"] = proc.num_handles()
#             except:
#                 info["open_files"] = "Access Denied"
            
             
#             listProces.append(info)
            
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) :
#             pass
#     return listProces
    

# def main():
    
#     Border = "-" * 60
#     print(Border)
#     print("-----------  Platform Surveillance System --------")
#     print(Border)
    
#     if(len(sys.argv ) == 2):
#         if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
#             print("This Script is used to  : ")
#             print("1 : Create automatic logs")
#             print("2 : Executes periodically")
#             print("3 : Sends mail with the log")
#             print("4 :  Store information about processes")
#             print("5 : Store information about CPU ")
#             print("6 : Store information about RAM usages ")
#             print("5 : Store information about secondary storage ")
            
#         elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
#             print("Use the automation script as ")
#             print("ScriptName.py TimeInterval DirectoryName")
#             print("TimeInterval: The time in minutes for periodic scheduling  ")
#             print("DirectoryName : Name of decretory to create auto logs ")
            
#         else:
#             print("Unable tto Proceed as there is no such option ")
#             print("Please use --h or --u get more details")
            
#     # python demo.py 5 Marvellous reverver@email.com
#     elif (len(sys.argv) == 4):
#         print("Inside projects logic")        
#         print("Time interval : ", sys.argv[1])
#         print("Directory name : ", sys.argv[2])
#         print("Receiver Email: ",sys.argv[3])
        

    
#     # send_mail(sender_email,app_passward, receive_email,subject, body)
        
        
        
#         # Apply the scheduler
#         schedule.every(int(sys.argv[1]) ).minutes.do(send_mail, sys.argv[2],sys.argv[3])
        
#         print("Platform Surveillance System started successfully")
#         print("Directory CReated ",sys.argv[2])
#         print("Time Interval in minutes : ", sys.argv[1])
#         print("Press Ctrl + C to stop the execution")
        
#         # wait till abort
#         while True:
#             schedule.run_pending()
#             time.sleep(1)
          

#     else:
#         print("Invalid No of command line arguments")
#         print("Unable tto Proceed as there is no such option ")
#         print("Please use --h or --u get more detail")
        

    
    
    
#     print(Border)
#     print("--------------- Thank You for using Our script -------------")
#     print(Border)

# if __name__ == "__main__":
#     main()
    
    


# =======================================================
# Program : Automated Platform Surveillance System
# Author  : Raviraj Aade
# Purpose : Monitor system performance metrics including
#           CPU, RAM, Disk, Network, and Process details.
#           Generate timestamped log files and send
#           automated email reports at scheduled intervals.
# Date    : 14/02/2026
# =======================================================


import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage


Border = "-" * 60


#-----------------------------------------------------------------------------------------------------
#   Function name :  ProcessScan
#   Description :    Scans all currently running processes on the system and collects
#                    detailed information about each one.
#                    Performs a warm-up pass first to allow psutil to calculate accurate
#                    CPU percentages (requires two measurements with a time gap).
#                    Handles exceptions gracefully for processes that terminate mid-scan
#                    or deny access.
#                    Collects the following details per process :
#                      - PID, Name, Username, Status, Start Time
#                      - CPU Percentage, Memory Percentage
#                      - RSS (Resident Set Size) and VMS (Virtual Memory Size)
#                      - Thread count and thread list
#                      - Number of open file handles
#   Parameter :      None
#   Return :         listProces -> List of dictionaries, one dictionary per process
#   Date :           14/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def ProcessScan():

    listProces  = []
    process_list = []

    # Warm-up pass — call cpu_percent() once on all processes to initialize measurement
    # Without this, the first CPU reading will always return 0.0
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    # Wait briefly so psutil can calculate CPU usage difference between two intervals
    time.sleep(0.2)

    # Second pass — collect actual data for all running processes
    for proc in psutil.process_iter():
        try:
            # Collect basic process information
            info = proc.as_dict(attrs=["pid", "name", "username", "status", "create_time"])

            # Convert epoch timestamp to human-readable date-time format
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] = "N/A"

            # Collect CPU and memory usage percentages
            info["cpu_percent"]    = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            # Collect detailed memory info — RSS (actual RAM) and VMS (virtual memory)
            mem_info   = proc.memory_info()
            info["rss"] = mem_info.rss
            info["vms"] = mem_info.vms

            # Collect thread details and thread count
            info["threads"]     = proc.threads()
            info["num_threads"] = proc.num_threads()

            # Collect open file handle count (Windows uses num_handles)
            # Handle AccessDenied gracefully for protected system processes
            try:
                info["open_files"] = proc.num_handles()
            except:
                info["open_files"] = "Access Denied"

            listProces.append(info)

        # Gracefully handle processes that no longer exist, deny access, or are zombie processes
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listProces


#-----------------------------------------------------------------------------------------------------
#   Function name :  CreateLog
#   Description :    Creates a structured, timestamped log file inside the specified folder.
#                    Captures a full snapshot of system health at the time of the run including :
#                      - CPU usage percentage
#                      - RAM usage percentage
#                      - Disk usage per partition
#                      - Network bytes sent and received
#                      - Per-process details (PID, name, username, status, CPU %, memory %)
#                      - Thread monitoring — thread count per process
#                      - Open file monitoring — open file handles per process
#                      - Top 10 memory-consuming processes (RSS, VMS, memory %)
#                    If the log folder does not exist, it is created automatically.
#   Parameter :      FolderName -> Name of the folder to store log files (string)
#   Return :         None
#   Date :           14/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def CreateLog(FolderName):

    # Check if the log folder exists
    Ret = os.path.exists(FolderName)

    if Ret == True:
        # Confirm it is a directory and not a file with the same name
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to create folder")
            return
    else:
        # Create the log folder automatically if it does not exist
        os.mkdir(FolderName)
        print("Directory for log files created successfully.")

    # Generate a unique log file name using a timestamp
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName  = os.path.join(FolderName, "Platform_%s.log" % timestamp)

    print("Log file created with name :", FileName)

    fobj = open(FileName, "w")

    # -------------------------------------------------------------------------
    # Log File Header
    # -------------------------------------------------------------------------
    fobj.write(Border + "\n")
    fobj.write("----------- Platform Surveillance System --------\n")
    fobj.write("Log created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")
    fobj.write("---------------------- System Report ----------------------- \n")

    # -------------------------------------------------------------------------
    # CPU Usage
    # -------------------------------------------------------------------------
    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
    fobj.write(Border + "\n")

    # -------------------------------------------------------------------------
    # RAM Usage
    # -------------------------------------------------------------------------
    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %s %%\n" % mem.percent)
    fobj.write(Border + "\n")

    # -------------------------------------------------------------------------
    # Disk Usage — reports usage percentage for each mounted partition
    # -------------------------------------------------------------------------
    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border + "\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" % (part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border + "\n")

    # -------------------------------------------------------------------------
    # Network Usage — total bytes sent and received since system boot
    # -------------------------------------------------------------------------
    net = psutil.net_io_counters()
    fobj.write(Border + "\n")
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border + "\n")

    # Scan all running processes once — reused across all sections below
    Data = ProcessScan()

    # -------------------------------------------------------------------------
    # Process Report — basic info for all running processes
    # -------------------------------------------------------------------------
    for info in Data:
        fobj.write("PID : %s\n"         % info.get("pid"))
        fobj.write("Name : %s\n"        % info.get("name"))
        fobj.write("Username : %s\n"    % info.get("username"))
        fobj.write("Status : %s\n"      % info.get("status"))
        fobj.write("Start Time : %s\n"  % info.get("create_time"))
        fobj.write("CPU %% : %.2f\n"    % info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
        fobj.write(Border + "\n")

    # -------------------------------------------------------------------------
    # Thread Monitoring — thread count and thread list per process
    # -------------------------------------------------------------------------
    fobj.write(Border + "\n")
    fobj.write("\n--------------------Thread monitoring --------------------\n")
    for info in Data:
        fobj.write("PID : %s\n"           % info.get("pid"))
        fobj.write("Name : %s\n"          % info.get("name"))
        fobj.write("Threads : %s\n"       % info.get("threads"))
        fobj.write("Num Of Thread : %s\n" % info.get("num_threads"))
        fobj.write(Border + "\n")
    fobj.write(Border + "\n")

    # -------------------------------------------------------------------------
    # Open File Monitoring — open file handle count per process
    # Processes that deny access are labelled "Access Denied"
    # -------------------------------------------------------------------------
    fobj.write(Border + "\n")
    fobj.write("\n-------------------- File monitoring --------------------\n")
    for info in Data:
        fobj.write("PID : %s\n"        % info.get("pid"))
        fobj.write("Name : %s\n"       % info.get("name"))
        fobj.write("Open files %s:\n"  % info.get("open_files"))
        fobj.write(Border + "\n")
    fobj.write(Border + "\n")

    # -------------------------------------------------------------------------
    # Top 10 Memory-Consuming Processes — sorted by RSS (actual RAM used)
    # -------------------------------------------------------------------------
    fobj.write(Border + "\n")
    top_ten_memory = sorted(Data, key=lambda x: x["rss"], reverse=True)[:10]
    fobj.write("\n----------------Top 10 memory consuming processes -------------\n\n")

    for proc in top_ten_memory:
        memory_dict = {
            "pid"            : proc["pid"],
            "name"           : proc["name"],
            "rss"            : proc["rss"],
            "vms"            : proc["vms"],
            "memory_percent" : proc["memory_percent"]
        }
        fobj.write(str(memory_dict))
        fobj.write("\n\n")

    fobj.write(Border + "\n")

    # -------------------------------------------------------------------------
    # Log File Footer
    # -------------------------------------------------------------------------
    fobj.write(Border + "\n")
    fobj.write("---------------------- End of log file ---------------------\n")
    fobj.write(Border + "\n")
    fobj.close()


#-----------------------------------------------------------------------------------------------------
#   Function name :  send_mail
#   Description :    Generates a system report log file, then sends it as an email attachment
#                    to the specified receiver using Gmail SMTP SSL.
#                    Internally calls CreateLog() to generate the latest log snapshot,
#                    then calls ProcessScan() to write a detailed process report into a
#                    separate attachment file (LogfileName.log).
#                    Uses Gmail SMTP SSL on port 465 with a Google App Password.
#                    NOTE : Replace sender_email and app_passward with your own credentials.
#                           Never push your real App Password to a public repository.
#   Parameter :      Foldername -> Name of the log folder to write logs into (string)
#                    receiver   -> Receiver's email address (string)
#   Return :         None
#   Date :           14/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def send_mail(Foldername, receiver):

    # Generate the system log file before sending the email
    CreateLog(Foldername)

    # Sender credentials
    sender_email = "ravirajade2@gmail.com"

    # Gmail App Password — generated from Google Account > Security > App Passwords
    # NOTE : Use your own App Password here. 
    app_passward = "XXXX XXXX XXXX XXXX"

    subject = "Automated Platform Surveillance — System Report"
    body = """Jay Ganesh,
        This is an automated email from the Platform Surveillance System.
        Please find the system report log file attached.
        Regards,
        Raviraj Aade
    """

    # Write a process-level report to a separate log file for attachment
    LogFileName = "LogfileName.log"
    fobj = open(LogFileName, "w")

    Data = ProcessScan()

    for info in Data:
        fobj.write("Process Name : %s\n"   % info.get("name"))
        fobj.write("PID : %s\n"            % info.get("pid"))
        fobj.write("CPU %% : %.2f\n"       % info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n"    % info.get("rss"))
        fobj.write("Thread Count : %s\n"   % info.get("num_threads"))
        fobj.write("Open Files %s:\n"      % info.get("open_files"))
        fobj.write("Log created at : "     + time.ctime() + "\n")
        fobj.write(Border + "\n")

    fobj.close()

    # Create an EmailMessage object
    msg = EmailMessage()

    # Set email headers
    msg["From"]    = sender_email
    msg["To"]      = receiver
    msg["Subject"] = subject

    # Set the email body
    msg.set_content(body)

    # Read and attach the process report log file
    fobj = open(LogFileName, "rb")
    data = fobj.read()
    fobj.close()

    msg.add_attachment(data, maintype="text", subtype="plain", filename="Logfile.txt")

    # Create an SSL-encrypted SMTP connection to Gmail on port 465
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login using sender Gmail address and App Password
    smtp.login(sender_email, app_passward)

    # Send the email
    smtp.send_message(msg)
    print("Mail sent successfully")

    # Close the SMTP connection
    smtp.quit()


#-----------------------------------------------------------------------------------------------------
#   Function name :  main
#   Description :    Entry point of the Platform Surveillance System.
#                    Handles command-line arguments to control script behaviour :
#                      --h or --H                      -> Display help information
#                      --u or --U                      -> Display usage instructions
#                      <interval> <folder> <email>     -> Start scheduled surveillance
#                    Schedules send_mail() to run at the defined time interval,
#                    which internally generates a fresh log and emails it.
#                    Keeps the script running using an infinite loop.
#   Usage        :   python PlatformSurveillance.py 10 Demo receiver@gmail.com
#   Parameter :      None (reads from sys.argv)
#   Return :         None
#   Date :           14/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def main():

    print(Border)
    print("-----------  Platform Surveillance System --------")
    print(Border)

    if len(sys.argv) == 2:

        # Show help information
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Script is used to  : ")
            print("1 : Create automatic system logs")
            print("2 : Executes periodically at a set time interval")
            print("3 : Sends email with the log file attached")
            print("4 : Store information about running processes")
            print("5 : Store information about CPU usage")
            print("6 : Store information about RAM usage")
            print("7 : Store information about disk and network usage")

        # Show usage instructions
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as :")
            print("ScriptName.py TimeInterval DirectoryName ReceiverEmail")
            print("TimeInterval  : Time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to store auto logs")
            print("ReceiverEmail : Email address to receive the report")

        else:
            print("Unable to Proceed — no such option.")
            print("Please use --h or --u for more details.")

    # Start scheduled surveillance : python PlatformSurveillance.py 10 Demo receiver@gmail.com
    elif len(sys.argv) == 4:
        print("Starting Platform Surveillance System...")
        print("Time Interval  :", sys.argv[1], "minutes")
        print("Directory Name :", sys.argv[2])
        print("Receiver Email :", sys.argv[3])

        # Schedule send_mail to run automatically every N minutes
        schedule.every(int(sys.argv[1])).minutes.do(send_mail, sys.argv[2], sys.argv[3])

        print(Border)
        print("Platform Surveillance System started successfully.")
        print("Press Ctrl + C to stop the execution.")
        print(Border)

        # Keep the script alive — run scheduled tasks as they become due
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments.")
        print("Please use --h or --u for more details.")

    print(Border)
    print("--------------- Thank You for using Our script -------------")
    print(Border)


if __name__ == "__main__":
    main()