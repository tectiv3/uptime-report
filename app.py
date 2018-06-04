import time, os, socket, subprocess, datetime, re

#----------------------------------------
# Gives a human-readable uptime string
def uptime():

    try:
        result = subprocess.run(["systeminfo"], shell=True, stdout=subprocess.PIPE)
        m = re.search("System Boot Time:\s+([^\\\\]+)\\\\r", str(result.stdout))
        if not m:
            return "unknown"
        #print("RESULT:", m.groups()[0])
        timestamp = datetime.datetime.strptime(m.groups()[0], "%m/%d/%Y, %I:%M:%S %p").timestamp()
        total_seconds = datetime.datetime.utcnow().timestamp() - timestamp
    except Exception as e:
	print(e)
        return str(e)

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
