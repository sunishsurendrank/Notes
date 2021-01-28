import os

output = os.popen("powershell.exe Get-service").readlines()
message = "Stopped"

for line in output:
    if message in line: 
        print("Message found : {0}".format(line))