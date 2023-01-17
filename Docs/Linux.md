# Linux Flavours

![image](/images/Linux/linux-flavour.JPG)

# Linux Commands

![image](/images/Linux/linux-tools.jpg)
## Command to get the computer information

```
lscpu
```
## Disk space of file systems

```
df -H
```

List the size of each folder
 
 ```
du -sh * | sort -hr | head -n10
```

## Ram usage
```
top
```

```
free -h
```

```
cat /proc/meminfo
```

## OS details
```
hostnamectl
```
```
cat /etc/os-release
```

## SSH to another Machine

```
ssh -i id_rsa_usb user@ipaddress
```

## Copy File to remote Machine
```
scp id_rsa_usb.pub user@ipaddress:/home/sunisk/copyfolder/
```

## Cron Jobs

List
```
crontab -l
```
Creat
```
crontab -e
```

## List Open ports
```
sudo netstat -tulpn | grep LISTEN
```

## DNS server
 
/etc/resolv.conf







