
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