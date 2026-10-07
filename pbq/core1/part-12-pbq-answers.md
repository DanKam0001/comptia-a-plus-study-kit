# Core 1, Part 12: PBQ answers

Do the tasks in [`part-12-pbq.md`](part-12-pbq.md) first.

**Marking note:** real PBQs can earn partial credit, so each item here is marked on its own. CompTIA does not publish its PBQ scoring rules, so treat this as practice marking, not the real formula. Rough guide: all correct is a pass for this drill, 75 percent or more means you are close, below 50 percent means go back to the [cheatsheet](../../core1/part-12-virtualization-cloud/cheatsheet.md).

---

## C1P12-PBQ1: Label the Hypervisor Stacks (11 points)

**Part A**

| Box | Answer | Why |
|---|---|---|
| 1 | Hypervisor | A Type 1 (bare metal) hypervisor sits directly under the VMs |
| 2 | Physical hardware | Type 1 runs directly on the hardware with no operating system underneath |
| 3 | Hypervisor | In Type 2, the hypervisor is an application that runs the VMs |
| 4 | Host operating system | Type 2 runs as an application on top of a normal operating system |
| 5 | Physical hardware | The host operating system itself sits on the hardware |

**Part B**

| Product | Answer | Why |
|---|---|---|
| VMware ESXi | 1 | Type 1 example in the kit |
| Oracle VirtualBox | 2 | Runs as an application on an operating system |
| Microsoft Hyper-V | 1 | Type 1 example in the kit |
| VMware Workstation | 2 | Runs as an application on an operating system |
| Citrix Hypervisor (Xen) | 1 | Type 1: runs directly on the hardware with no operating system underneath |

**Part C:** file. Each VM disk is stored as a big file on the host, so plan free space.

**Marking:** 1 point per blank (5 + 5 + 1 = 11). In Part A, boxes 1 and 3 both take "Hypervisor", and boxes 2 and 5 both take "Physical hardware".

---

## C1P12-PBQ2: Cloud Match-up (8 points)

| # | Answer | Why |
|---|---|---|
| 1 | J Private cloud | Built for one organization only |
| 2 | B Elasticity | Resources grow with demand and shrink again |
| 3 | F SaaS | A finished app, with nothing to manage, like Microsoft 365 or Gmail |
| 4 | D Container | Packages one app and shares the host's operating system, unlike a VM |
| 5 | I VDI | Virtual Desktop Infrastructure: desktops run as VMs on a central server, shown on thin clients |
| 6 | G Sandbox | A walled-off VM for untrusted software, deleted afterwards |
| 7 | A IaaS | Rented virtual servers where you manage the operating system and everything on it |
| 8 | E Community cloud | Shared by organizations with common needs, such as several hospitals |

Unused terms: C Hybrid cloud and H PaaS.

**Answer string:** 1J 2B 3F 4D 5I 6G 7A 8E

**Marking:** 1 point per correct match.
