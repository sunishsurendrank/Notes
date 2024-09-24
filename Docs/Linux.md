# Linux Flavours

![image](/images/Linux/linux-flavour.JPG)

# Linux Commands

## SSH to Linux Machine using Private and Public Key

### Create RSA key

If you are connecting from windows machine to linux server.

Open the powershell in windows and type the below command
```
ssh-keygen
```

The tool will create rsa key under location `C:\Users\<username>/.ssh/id_rsa`

Private Key : id_rsa
Public Key: id_rsa.pub

### Manually copy Public key to Server

In windows machine inside the powershell run the below command to view the public key
```
cat C:\Users\<username>/.ssh/id_rsa.pub
```
Copy the public key content

Login to to the linux server using username and password and go to the location .ssh

```
cd ~/.ssh 
```
You will see a file with name authorized_keys, if not create a file with name  authorized_keys and add the public key content to it and save it.

```
vi authorized_keys
```

### Try conneting from powershell

Now you can connect fom powershell console  using the below command without password.

```
ssh <userid>@<ipaddress of linux machine>
```

### Connect from Putty

- Open PuTTYgen
Open the PuTTYgen tool. You can download it if it’s not already installed (it comes with PuTTY).

- Load the Private Key
In PuTTYgen, click on Load.
In the file explorer, switch the file type to All Files since the default view is for .ppk files.
Navigate to and select your id_rsa private key file (the one without any extension).

- Save the Private Key as .ppk
After loading the key, click on Save private key.
You'll be prompted to set a passphrase for the key (optional but recommended for security).
Save the key with the .ppk extension.

- Use the .ppk File in PuTTY
Open PuTTY and go to Connection → SSH → Auth.
Under Private key file for authentication, browse and select the .ppk file you just saved.
Connect to your Linux server using this configuration.

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

# Linux Performance Observability Tools

![image](/images/Linux/linux-tools.jpg)







