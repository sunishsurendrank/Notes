[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square)](https://github.com/TheAlgorithms/Python/blob/master/CONTRIBUTING.md)&nbsp;


![image](/images/intro.PNG)


- Author of this Document : Sunish Surendran Kannembath
- Developer : Sunish Surendran Kannembath
- Reach Sunish in LinkedIn : https://www.linkedin.com/in/sunishsurendrank/
- Reach Sunish in Twitter : @sunishsurendran

# CHAPTERS
- Go Language
  - How to Install Go in Linux machine
  - Create Your First Go Lang Project
  - Comparing Datastructures GoLang and Python
- Git
  - Git Commit, Tree, Blob
  - Push code to git server
  - Difference between HEAD and heads in git
  - Difference between git push and git fetch
  - How to solve git conflicts in terminal
  - How to do branch to branch merge
  - Disable push towards the remote master branch
  - How do you squash last N commit into single commit

- Docker
  - Docker Internals
  - What is namespace and cgroup
  - Difference between Docker Save and Export

- Jenkins
  - What is the environmental varibale in which Jenkins Configuration and runtime data contains
  - Jenkins Environmental variables
  - How to secure Jenkins
  - How to move Jenkins from one server to another server

- AzureDevOps
  - How to check the pod status from the pipeline
  - How to create a custom build agent
  - How to use environmnets in the azure pipline
  - How to use secret file in azure pipeline
  

- SonarQube

- Linux
  - What is Privilihed Ports in Linux
  - What is Inode
  - Difference between Hardlink and Softlink
  - Command to create softlink
  - Maximum number of process in Linux
  - How do you get the count of open file descriptor for a process
  - What is the value returned tp the parent process if the fork() system call is executed
  - What is Collectd Tool
  - What is the responsibilty of file under root file system.
  - Which linux command is used to change the server bootup
  - How to create a crontab entry
  - What is the command to see the last exit code
  - Different type of FAT File System
  - Which Tool is used in linux to troubleshoot network issue




- Python
  - Calling Script with Parameter
  - Working with files and directories
  - Logging the Script (Creating Log file,Formating the output,Datestamp)
  - Creating Helper files
  - Working with Number and Strings (sort,reverse)
  - What is Python Comprehenisons
  - Difference between iterators and generators and what is yeild
  - What is Lambda function
  - How to add two hashtables
  - How to run linux/windows commands in Python Script.
  - What is __init__() method in python
  - What is superclass in python
  - What is Self in python class
  - What is Abstrat Class in python
  - Difference between Python 2 and Python 3
  - Range and xRange
  - Read a file and count the words init
  - Multiple inheritance 
  - Break, Continue , Pass
  - Revese Index
  - Different types of inheritance 
  - Packages and libraries 

- Kubernetes
  - Explain ControlPlane components and Ports
  - Different method to schedule a pod to Node
  - Difference between  Node Affinity and Node Selector 
  - What is the role of kube-proxy and kubelet in worker node
  - Pause container
  - Init containers
  - Differnce between Daemonset and static pod
  - Differnce between Side car Vs Ambassador Vs Adaptor
  - How the communication happens in istio
  - Difference between Liveness and Readiness Probe
  - Version support between kubeapi server, kubelet and other components
  - What is emptyDir
  - When secrets as volume mapped how the secret will be available to the container
  - Explain operator and CRD
  - Kubernetes release cycle
  - What is Endpoint kind in kubernetes
  - What is port forwarding in Kubernetes
  - Certificate rotation in kubernetes
  - Difference between deployment and statefullset and when we will use statefullset.
  - Deployment strategies in kubernetes
  - How will we implement blue green deployment, canary or dark release with kubernetes
  - What is Horizontal pod autoscaling(HPA)
  - Monitoring in kubernetes (Prometheus, Matrix server)
  - what are Expoters in kubernetes ,name some of it.
  - Difference between Service Mesh and API Gateway
  - TLS implemetation with istio
  - Secrets are just encoded, so how can we do this in secure way.
  - Cluster to cluster communication
  - Kubernetes how many times try restart by default, can we control this behaviour.
  - How many pods we can create in k8 nodes
  - What is headless service and when to use it


# How to Install Go in Linux machine

- ## Downloading the GO Package

User can download the binary release suitable for the system. Please refer to the link for latest packages

```
mkdir downloads
```
```
cd downloads
```

```
wget https://golang.org/dl/go1.14.6.linux-amd64.tar.gz
```
![image](/images/DownloadGoLang.PNG)


- ## Unzip the package to /usr/local
```
tar -C /usr/local -xzf go$VERSION.$OS-$ARCH.tar.gz
```
Once unziped navigate to the folder /usr/local/go and user can see the go lang files as shown below picture

![image](/images/GoLangInstallPath.PNG)

- ## Create a Workspace

A Go Workspace is how Go manages our source files, compiled binaries, and cached objects used for faster compilation later. It is typical, and also advised, to have only one Go Workspace, though it is possible to have multiple spaces. The GOPATH acts as the root folder of a workspace.

User can create a workspace folder for Go development.Here for this example i am creating a folder under /home

```
mkdir /home/go-workspace
```

- ## Setting GOROOT , GOPATH and PATH variable

The $GOROOT is where Go’s code, compiler, and tooling lives— this is not our source code.

The $GOPATH environment variable lists places for Go to look for Go Workspaces.

```
export GOROOT=/usr/local/go
```
```
export GOPATH=/home/go-workspace
```
```
export PATH=$PATH:$GOROOT/bin
```
User can also place a shell script under the location /etc/profile.d . Hence no need to export the GOROOT/GOPATH always.

For this documnet i have created a shell script with name go_env.sh

![image](/images/profiledPNG.PNG)

![image](/images/goenv.PNG)

## Comparing Data Structures GoLang and Python

Go Language have 2 Datastructures and Python have Built-in 4 Datastructures
```
Array  | Tuple 
Slice  | Lits
Map    | Dictionary
Struct | Sets
```
![image](/images/GoLang/GoLang_Figure1_DataStructures_Comparision.PNG)

# Git Internals
We all used the git as source code version controlling system.But how many of us explored what happens when we do a ```git add , git commit``` int our local repositories.

Here we go and explore the git commands.For this i have created a folder called git_project and under it  ran ```git init``` command ,which will initialise the git repository.

Inoder to watch the changes in the .git folder , i have used below command.
So this will watch the folder changes in every 1 second.


```
cd /.git
```
```
watch -n 1 -d find .
```

Let's add a new file called test.txt in the project folder and run the below command 

```
 git add .
```
The below figure shows the difference and extra files created by the git.

![image](/images/Git/Git_Figure1_gitaddcommand.PNG)

Under the objects folder we can see one folder called 76 created and under it there is a file created with name e579a

We can open the file using below command and see what it have.

```
git cat-file -p 76e579
```
![image](/images/Git/Git_Figure2_openobjectfile.PNG)

So this means that the above file is a copy of our test.txt file.The below figure explains how git is mapping our test.txt into the blob file.


![image](/images/Git/Git_Figure3_objectmapping.PNG)

Now we will commit the test.txt to the git and see what all files are getting generated by git in backend.
```
git commit -m "Add new file"
```
![image](/images/Git/Git_Figure4_gitcommitcommand.PNG)

The right side section shows the previous state of the .git folder and left section shows the current state of the .git folder.Hence we can easly understand the extra files git created under .git folder.

So here we can see few more folders and files got created under the objects folder.

![image](/images/Git/Git_Figure5_gitcommitfolderstructure.PNG)

This shows the concept of Blob and tree in Git.

when we commit any changes into Git , Git will store all those commit details in a Object file that is D43e9b in the above diagram and it will point to the tree which is C193f1 file ,Again the tree file points to the blob 76e579 file.

So it will be like the files will be commit --> tree --> blob

Lets checkin one more file called test1.txt and see how this object files are managing it.

![image](/images/Git/Git_Figure6_secondcommit.PNG)


The right side of the picture shows how the objects are mapped when we do a second commit.

## Push code to git server

Usually when the project starts , one of the architect start building concept of the project and keep the plans in his local git repository. When the development start , a group of developers need the plan. So the architect needs to share his plan/code with the team.The best way is to checkin the plan/code in the server repository.

So lets explore how he can do the push from his local repository to the server repository. In this example i created a repository called TestRepo in my machine and also in the server , here i am using GitHub as my server.

I commited my files to the local Repository. So now we need to link the local repository to the server repository , for this we need to run the below git command from the local repo.

```
git remote add origin https://github.com/sunishsurendrank/TestRepo.git
```

So what actually happens in the backend is this url is getting appeded to file called config under .git folder.

![image](/images/Git/Git_Figure7_configfile.PNG)

## Difference between HEAD and heads in git

If we move into the .git folder we can see a file called HEAD.
Cat that file and see what it have. It is a simple one line which points to the /refs/heads/\<branch>

For this example i have created a local repository and it default have a master branch.When i open the read the file HEAD it will be pointing to the /refs/heads/master. Now lets create a another branch called sunish. So if we open now and see the HEAD file it still point to the /refs/heads/master because we didnt checkout into sunish branch.

Now lets move to the branch sunish , now the HEAD file is pointing the folder /refs/heads/sunish . if you go through the below image you can understand much more.

![image](/images/Git/Git_Figure8_HEAD.PNG)

So now lets see what is heads means.HEAD points to the current branch and heads point to the current commit in that branch.

![image](/images/Git/Git_Figure9_heads.PNG)

In this situation we have two branch master and sunish , and in sunish branch i have changed few files and commited thats why you can see the heads/sunish moved and pointing to the new commit.But if you open the heads/master it will be pointing to the branch out commit.

## Difference between git fetch and git pull

This difference you can get by just googling , but most of the result say git pull = git fetch + git merge. This is absolutely correct , but lets explore little more in deep and see how git handles this concepts.

![image](/images/Git/Git_Figure10_gitfetch.PNG)

The both diagram is self explatory. So please go through the comments which i mentioned in the both diagram.

![image](/images/Git/Git_Figure11_gitpull.PNG)

## How to solve git conflicts in terminal
In order to learn this part we need create two branches one branch we will default master branch and second one i will be creating with name sunish.

Total two branch
```
 --> master (dafault branch) with text.txt
 --> sunish (new branch) with test.txt
```
Initially both branch have same content which is test.txt. And considering this as a example we will have content in test.txt as "abc".

![image](/images/Git/Git_Figure12_comparingtwofiles.PNG)

Now inorder to make conflict we will change the content of sunish branch test.txt to "def".

So test.txt in master branch have abc , test.txt in sunish branch have "def".

![image](/images/Git/Git_Figure13_updatingfileinsunish.PNG)

Run the below command to see the difference,this will show the difference between master and current branch that is sunish in this case.

```
git diff master
```
![image](/images/Git/Git_Figure14_gitdiff.PNG)

run the below command 
```
git merge
```
This will through the conflict message.
Now open the test.txt file your will see the conflict line.
```
<<< HEADS
>>> master
```
Remove the conflicts and do the commit again ,once that done do the merge it will work.



## How to do branch to branch merge

we can push the code into the different branch using the below command 

```
git push sunish origin/master
```


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


 ## License
 Copyright © 2020, [Sunish Surendran Kannembath](https://github.com/sunishsurendrank). 
 Released under the [MIT License](LICENSE).


 





