# Lab: Build your first virtual machine, and try the cloud (free)

**Time:** 45 to 60 minutes. **Needs:** a Windows, Mac or Linux PC with at least 8 GB of RAM and 30 GB free disk space, and a free account for a cloud provider or email service you already use.

## 1. Check that virtualization is on

**Windows:** open Task Manager, Performance tab, CPU. At the bottom right, look for **Virtualization: Enabled**. If it says Disabled, the setting (Intel VT-x or AMD-V) is in the firmware. Core 1 Part 1 shows where.

## 2. Install a Type 2 hypervisor

Download **VirtualBox** (free, from virtualbox.org) and install it. VirtualBox is a **Type 2** hypervisor: it runs as an app on top of your normal operating system.

## 3. Create a VM

1. Download a free Linux installer (an **ISO** file), for example Ubuntu Desktop or Linux Mint, from the official site.
2. In VirtualBox choose **New**. Give it 2 CPU cores, 4 GB RAM and a 25 GB disk.
3. Under **Network**, note the default mode (usually **NAT**). Try **Bridged** and see that the VM gets its own address on your network, then put it back.
4. Start the VM and install the system inside it.

Find the VM's disk file on your host. That file **is** the VM's disk.

## 4. Be the sandbox

Inside the VM, install and try any app you would not run on your main PC. Close the VM and delete it if you like. Your host never changed.

## 5. Spot the cloud models and traits

Write down one example of each from your own life:
- **SaaS** (Gmail, Microsoft 365, Google Docs)
- **File synchronization** (OneDrive, Google Drive, Dropbox)
- Is it **public**, **private**, **hybrid** or **community** cloud?
- Where have you seen **metered** billing (a phone data plan, electricity)?
- When did a service get busier and still work (**elasticity**)?

## 6. Optional: free cloud tier

Create a free account with a major cloud provider and look at its pricing page. Find the words **ingress** and **egress** and note which one costs money.

## Check yourself

- Is VirtualBox Type 1 or Type 2? Why?
- Which firmware setting must be on for a VM to start?
- A shop needs 20 more servers for one weekend. Which cloud trait solves that?
