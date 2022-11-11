
# Docker Basics

## What is namespace and cgroup
Namespaces provide isolation of system resources, and (Control groups)cgroups allow for fine‑grained control and enforcement of limits for those resources.

In short:
- namespaces = limits what you can see
- Cgroups = limits how much you can use

![image](/images/Linux/linux-namespace.png)

![image](/images/Linux/command-namespace.JPG)

UTS (UNIX Time-Sharing) namespaces allow a single system to appear to have different host and domain names to different processes.

An interprocess communication (IPC) namespace has its own IPC resources, for example POSIX message queues.

## Docker Networking

Three types of docker network
- Bridge (Default)
- None
- Host

When a container is created there is eth0 ethernet interface created which connect to the docker0 interface.

## Docker Volume

Docker creates volume under var/lib/docker/volumes

```
docker run -v etc/sunish:etc/database nginx
```
etc/sunish is host machine location

## Difference between Docker Save and Export

## Docker Reference
https://alexander.holbreich.org/docker-components-explained/


# Docker Internals

In this section i assume readers already know about the Docker concepts
So here in my centos machine i have installed docker. So lets see where the docker is living in my centos machine.

To under where the docker lives run the below command

```
docker info
```
You will get the below information in your shell

![image](/images/dockerinfo.PNG)

So we got few information like StorageDrive used by docker and the Docker Root directory.Let's naviate to the folder
```
/var/lib/docker
```
![image](/images/dockerroot.PNG)

It have folders containers ,images ,networks ,overlay2 ,plugins ,volumes etc .Currently all the folders are empty.

Lets download the alpine image for example and see where the image will get downloaded.run the below command to download the image

```
docker pull alpine
```
```
docker images
```
![image](/images/alpineimage.PNG)

Do a docker inspect to see how many layers are there for this alpine image

```
docker inspect alpine
```
![image](/images/dockerlayer.PNG)

The above image shows the alpine image have only one layer which starts with 1411.

Here comes the concept of LowerDir , MergeDir , UpperDir , WorkDir.

if you observe the left side of the image you can see the folders and files got gernerated at /var/lib/docker/overlay2

Lets explore the alpine image layer folder.

![image](/images/explorealpineimage.PNG)

The Link file have a number which points to a folder under the I folder.

If we spin up the container wat i observered is more folder got added under the overlay2 and conatiners folder as shown below.

![image](/images/runningtheimage.PNG)

Now Create a folder inside the Docker conatiner and see where it will be created in hostmachine

![image](/images/creatingfolderinsidedocker.PNG)
