log_path = "host_access_log.txt"
host_list = []
with open(log_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        host_list.append(line.split(" - - ")[0])

host_count = {}

for host in host_list:
    if host in host_count:
        host_count[host] = host_count[host]+1
    else:
        host_count[host] = 1
    
for host in host_count:
    print(f"{host} {host_count[host]}")