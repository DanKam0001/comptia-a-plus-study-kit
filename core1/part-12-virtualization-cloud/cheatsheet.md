# Core 1, Part 12: Virtualization and Cloud for A+

**Objectives 4.1 and 4.2** (220-1201): *Explain virtualization concepts* and *Summarize cloud computing concepts.*
Domain: Virtualization and Cloud Computing (11% of the exam).

## Virtual machines (4.1)

- A **virtual machine (VM)** is a pretend computer running inside a real one. The real computer is the **host**. The system inside the VM is the **guest**. The VM's virtual processor, memory and disk are borrowed from the host, and its disk is stored as a **file** on the host.
- Many VMs can run on one host, so one server replaces many.
- Turning on hardware virtualization in the firmware (**Intel VT-x**, **AMD-V**) is covered in Core 1 Part 1, *Motherboards, CPUs and Firmware*.

### Purpose of virtual machines

| Purpose | Meaning |
|---|---|
| **Sandbox** | A walled-off place to run risky or untrusted software. Delete the VM afterward |
| **Test and development** | Try software on many operating systems without many computers; snapshots let you roll back |
| **Application virtualization: legacy software/OS** | Keep an old program, or an old operating system, running inside a VM |
| **Application virtualization: cross-platform** | Run an app from one operating system on another (for example Windows apps on a Mac or Linux PC) |

### Requirements

| Requirement | What to remember |
|---|---|
| **Security** | Patch the host and guests, keep VMs isolated, protect the hypervisor. A VM can be attacked like any computer |
| **Network** | A VM gets a virtual network card. Typical modes: **bridged** (VM gets its own address on the real network), **NAT** (shares the host's address), **host-only** (private between host and VMs) |
| **Storage** | Each VM disk is a big file, so plan free space |
| Also | Enough RAM and CPU cores for every VM running at once, plus virtualization turned on in firmware |

### Desktop virtualization and containers

- **VDI (Virtual Desktop Infrastructure):** user desktops run as VMs on a central server. Users connect from any device, even a **thin client**, and see their own desktop. Data stays on the server.
- **Containers:** package one app with what it needs, but **share the host's operating system** instead of carrying their own. Smaller, faster to start and lighter on memory than a VM. Example: Docker. A VM carries a whole guest operating system.

### Hypervisors

| Type | Where it runs | Examples |
|---|---|---|
| **Type 1** (bare metal) | Directly on the hardware, no operating system underneath. Data centers | VMware ESXi, Microsoft Hyper-V, KVM |
| **Type 2** (hosted) | As an application on top of a normal operating system. Personal use, testing | Oracle VirtualBox, VMware Workstation |

## Cloud computing (4.2)

Cloud = renting someone else's computers over the internet and paying for what you use.

### Common cloud models (who it is for)

| Model | Meaning |
|---|---|
| **Public** | Shared by many customers, owned by a provider (Amazon Web Services, Microsoft Azure, Google Cloud) |
| **Private** | Built for one organization only |
| **Hybrid** | Public and private working together |
| **Community** | Shared by organizations with common needs, for example several hospitals or government agencies |

### Service models (what you get)

| Model | You get | You manage | Examples |
|---|---|---|---|
| **IaaS** Infrastructure as a Service | Virtual servers, storage, network | The operating system and everything on it | Amazon EC2, Azure virtual machines |
| **PaaS** Platform as a Service | A ready platform to run your own code | Your code and data only | Azure App Service, Google App Engine |
| **SaaS** Software as a Service | A finished app | Nothing, you just use it | Microsoft 365, Gmail |

Memory aid: IaaS is an empty room, PaaS is a furnished room, SaaS is a finished hotel suite.

### Cloud characteristics

| Characteristic | Meaning |
|---|---|
| **Shared resources** vs **dedicated resources** | Shared = many customers on the same hardware. Dedicated = hardware reserved for you |
| **Multitenancy** | Many customers share the same infrastructure, kept separate from each other |
| **Metered utilization** | Pay for what you use. **Ingress** = data in (usually free). **Egress** = data out (usually charged) |
| **Elasticity** | Resources grow when demand rises and shrink when it falls |
| **Availability** | The service is up and reachable. Often stated as uptime, such as 99.9 percent |
| **File synchronization** | The same files kept up to date on all devices (OneDrive, Google Drive, Dropbox) |

Backing up to the cloud is covered in Core 2 Part 14, *Documentation, Change Management, Backup and Recovery*. Cloud and virtualization security basics appear in the Core 2 security parts.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Test risky software safely | VM sandbox |
| Old app that needs an old Windows version | VM (application virtualization, legacy) |
| VM won't start, says virtualization is off | Enable VT-x or AMD-V in firmware |
| Website needs many more servers for a sale, then fewer | Elasticity |
| Staff need email with no servers to run | SaaS |
| A company wants its own cloud that nobody else shares | Private cloud |
| Staff desktops run on a central server | VDI |
| Lightweight app packaging sharing the host OS | Container |
