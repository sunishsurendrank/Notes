# Master Node

Follow below steps in order to install the master node of kubernetes cluster.

# Pre-requisties

### Disable Swap

In Ubuntu Linux, swap is a designated space on a storage device (usually a hard disk or SSD) that acts as "virtual" memory. When your physical RAM is fully utilized, the system can offload inactive pages of memory to this swap space, allowing for additional memory usage and potentially preventing out-of-memory errors. Swap can be configured as a swap partition or a swap file.

However, Kubernetes doesn't fully support swap space by default, as it expects that only the physical RAM will be used. Running Kubernetes commands on a system with swap enabled often leads to errors because Kubernetes node components, like the kubelet, may fail if swap is on.

Kubernetes relies on the Linux kernel’s cgroup functionality for resource isolation. By default, cgroups are designed to manage memory without swap, aligning with Kubernetes’ approach.

- You can verify if swap is enabled on your Ubuntu system with the following command:
```
swapon --show
```
This command lists active swap areas. If no output is displayed, it indicates that swap is not currently enabled.

- If it is enabled then open the /etc/fstab file:
```
vi /etc/fstab
```
- Comment out any lines related to swap by adding a # at the start of the line like below.
```
#/swap.img swap swap defaults 0 0
```
- Then, save the file and turn off swap immediately with the following command:
```
sudo swapoff -a
```

### Load br_netfilter module and enable IP Table to Bridge network

In Kubernetes clusters, the br_netfilter module is often required because Kubernetes uses iptables rules extensively to manage networking between pods and nodes. Without this module, some critical networking features might not function correctly, leading to issues with communication between containers and pods.


- Load the br_netfilter Module Manually: Load the br_netfilter kernel module:

In Linux, modules are loadable pieces of code that can be dynamically inserted into the kernel to add functionality. The command lsmod lists all currently loaded modules, showing their dependencies and usage counts. These modules enable specific functionalities, such as supporting various file systems, handling network protocols, or interacting with hardware components (e.g., USB, GPU drivers, or network cards).

In Windows, similar functionality is provided by "drivers" and "services." While Windows has its core kernel, device drivers are added separately to extend hardware support and provide system-level features. Windows services (similar to Linux daemons) also help manage background processes but are not part of the kernel itself. In contrast, Linux kernel modules are tightly integrated and can be loaded or unloaded at runtime, allowing the kernel to operate more flexibly without rebooting the system.

Some examples of Linux kernel modules:

```
br_netfilter – enables the kernel to filter bridged network traffic.
ext4 – provides support for the ext4 filesystem.
i915 – offers support for Intel integrated graphics.
```

To manage modules on Linux, you can load them with `modprobe <module_name>` and remove them with `modprobe -r <module_name>`.

```
sudo modprobe br_netfilter
```

- To check if it’s loaded, you can run:
```
lsmod | grep br_netfilter
```
- Ensure the Module Loads at Boot: Add br_netfilter to /etc/modules-load.d/kubernetes.conf to ensure it loads on system startup:

```
echo 'br_netfilter' | sudo tee /etc/modules-load.d/kubernetes.conf
```

- Set Necessary sysctl Parameters: Kubernetes requires some sysctl parameters to be enabled for networking to function correctly. Set these parameters temporarily with:

Normally, the Linux kernel doesn’t apply IP tables rules to packets traversing a bridge interface. By setting net.bridge.bridge-nf-call-iptables=1, you ensure that the firewall rules defined in IP tables are also applied to packets as they pass through the bridge interface.

```
sudo sysctl -w net.bridge.bridge-nf-call-iptables=1

sudo sysctl -w net.bridge.bridge-nf-call-ip6tables=1
```
- To make these changes permanent, add them to /etc/sysctl.conf, The /etc/sysctl.conf file in Linux is used to configure kernel parameters at runtime

```
echo 'net.bridge.bridge-nf-call-iptables=1' | sudo tee -a /etc/sysctl.conf

echo 'net.bridge.bridge-nf-call-ip6tables=1' | sudo tee -a /etc/sysctl.conf
```
- When you run sudo sysctl -p, the system reads and applies all the settings specified in /etc/sysctl.conf immediately without requiring a reboot.

```
sudo sysctl -p
```
### Check Firewall Rules

Ensure that firewalls on both the source and destination machines are not blocking the port.

ufw (Uncomplicated Firewall) is a user-friendly command-line interface in Linux designed to simplify the configuration and management of firewall rules on the system. It acts as a frontend for managing the more complex IP tables, making it easier to allow or deny access to specific ports, services, or addresses without needing deep knowledge of firewall syntax.
```
sudo ufw status
sudo ufw allow 6443/tcp

```

## Install Kubenetes

### Donwload Kubeadm, Kubelet, kubectl and start kubelet
```
mkdir /etc/apt/keyrings
```

The below command downloads the GPG release key for the Kubernetes APT repository, converts it from an ASCII-armored format to a binary format, and saves it in a specific location on the filesystem. This key will be used by the APT package manager to verify the packages' authenticity and integrity when installing or updating Kubernetes components.

```
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

Below  command adds a new APT repository for Kubernetes packages to your system's package manager configuration, ensuring that it uses a specific GPG key to verify the packages' integrity. This is a key step in setting up a system to install and manage Kubernetes components via APT.

```
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
```
```
sudo apt-get update

sudo apt-get install -y kubelet kubeadm kubectl
```
- Check the status of kubelet

```
systemctl status kubelet
```

The kubelet is now restarting every few seconds, as it waits in a crashloop for kubeadm to tell it what to do

```
sudo systemctl enable --now kubelet
```
Check the logs for the kubelet
```
journalctl -xeu kubelet
```

### Install Containerd

```
apt install -y containerd
```

```
mkdir /etc/containerd
```

```
containerd config default
```

```
cat  /etc/containerd/config.toml | grep -i SystemdCgroup -B 10
```

Systemd and cgroupfs are two ways to manage cgroups (control groups), which organize processes and control resource usage in the Linux kernel.
Systemd is the default init system in many Linux distributions and manages cgroups via its own internal mechanisms. By setting SystemdCgroup = true, containerd will use systemd to manage resources like CPU and memory.

```
containerd config default | sed 's/SystemdCgroup = false/SystemdCgroup = true/' | sudo tee /etc/containerd/config.toml
```

```
cat  /etc/containerd/config.toml | grep -i SystemdCgroup -B 10
```

```
sudo systemctl restart containerd
```

### Init kubeadm

```
ip add
```

```
sudo kubeadm init --apiserver-advertise-address 10.113.153.7 --pod-network-cidr "11.244.0.0/16" --upload-certs
```

```
sudo kubeadm reset
sudo rm -rf /var/lib/etcd
```

### Install Conatiner Network Interface - Flannel

```
wget https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
```
If you use custom podCIDR (not 10.244.0.0/16) you first need to download the above manifest and modify the network to match your one.

```
vi kube-flannel.yml
```

```
kubectl apply -f kube-flannel.yml
```

```
kubectl get pod -n kube-system
```

```
kubectl get pod -n kube-fannel
```
