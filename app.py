import time, os, socket, subprocess, datetime

#----------------------------------------
# Gives a human-readable uptime string
def uptime():

    try:
        f = open( "/proc/uptime" )
        contents = f.read().split()
        total_seconds = float(contents[0])
        f.close()
    except:
        try:
            result = subprocess.run(["sysctl -n kern.boottime | cut -c9-18"], shell=True, stdout=subprocess.PIPE)
            total_seconds = datetime.datetime.utcnow().timestamp() - int(result.stdout)
        except Exception as e:
            print(e)
            return "cannot open uptime file: /proc/uptime"
 
    # Helper vars:
    MINUTE  = 60
    HOUR    = MINUTE * 60
    DAY    = HOUR * 24
 
    # Get the days, hours, etc:
    days    = int( total_seconds / DAY )
    hours   = int( ( total_seconds % DAY ) / HOUR )
    minutes = int( ( total_seconds % HOUR ) / MINUTE )
    seconds = int( total_seconds % MINUTE )
 
    # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
    string = ""
    if days > 0:
        string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
    if len(string) > 0 or hours > 0:
        string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
    if len(string) > 0 or minutes > 0:
        string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
    string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
 
    return string;
 

while True:
	print(socket.gethostname() + " uptime is " + uptime())
	time.sleep(60*60)
