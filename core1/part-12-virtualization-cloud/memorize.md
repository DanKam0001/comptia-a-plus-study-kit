# Memorise list: Virtualization and Cloud (Core 1, Part 12)

Understand the video first, then learn these cold.
Flashcards: [`flashcards/core1_part12.csv`](../../flashcards/core1_part12.csv) (import into Anki or any flashcard app).

## Virtualization

| Question | Answer |
|---|---|
| Host vs guest | Host = the real computer. Guest = the system inside the VM |
| Type 1 hypervisor | Runs directly on hardware (bare metal). ESXi, Hyper-V, KVM |
| Type 2 hypervisor | Runs as an app on an operating system. VirtualBox, VMware Workstation |
| Firmware settings needed for VMs | Intel VT-x or AMD-V |
| VM purposes (4) | Sandbox, test and development, legacy software or OS, cross-platform |
| VM requirements (3 named in objectives) | Security, network, storage |
| VM network modes | Bridged, NAT, host-only |
| What is a VM's disk stored as? | A file on the host |
| VDI stands for | Virtual Desktop Infrastructure |
| Thin client is | A simple device that just shows a desktop running on a server |
| Container vs VM | Container shares the host OS. VM carries its own full OS |

## Cloud models

| Question | Answer |
|---|---|
| Public cloud | Shared by many customers, run by a provider |
| Private cloud | Built for one organization |
| Hybrid cloud | Public plus private together |
| Community cloud | Shared by organizations with common needs |

## Service models

| Question | Answer |
|---|---|
| IaaS | Infrastructure as a Service. You get virtual servers and manage the OS |
| PaaS | Platform as a Service. You run your own code on a ready platform |
| SaaS | Software as a Service. A finished app, like Microsoft 365 |

## Characteristics

| Question | Answer |
|---|---|
| Multitenancy | Many customers share the same infrastructure, kept separate |
| Metered utilization | Pay for what you use |
| Ingress vs egress | Ingress = data in (usually free). Egress = data out (usually charged) |
| Elasticity | Scale up and down with demand |
| Availability | How much of the time the service is up (uptime percentage) |
| File synchronization | Same files on all devices (OneDrive, Google Drive, Dropbox) |
