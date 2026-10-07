# Core 1, Part 12: PBQ practice (Virtualization and Cloud for A+)

Two performance-based question (PBQ) drills for **objectives 4.1 and 4.2** (220-1201). Print this page or copy the blanks into a text file. Do the tasks **before** you open [`part-12-pbq-answers.md`](part-12-pbq-answers.md). Facts come from the Part 12 [cheatsheet](../../core1/part-12-virtualization-cloud/cheatsheet.md) and [memorise sheet](../../core1/part-12-virtualization-cloud/memorize.md).

---

## C1P12-PBQ1: Label the Hypervisor Stacks

| | |
|---|---|
| **ID** | C1P12-PBQ1 |
| **Objectives** | 4.1 |
| **Type** | Labelled diagram (fill in the layers) |
| **Time guide** | 5 minutes |
| **Points** | 11 (1 per blank) |

### Scenario

A colleague drew two diagrams of how virtual machines (VMs) sit on a computer, but the layer names rubbed off. One diagram is a data center server, the other is a laptop where someone tests software.

### Task

**Part A.** Fill in the numbered boxes using the word bank. Layers are drawn from the top down. A word can be used more than once.

**Part B.** Write **1** or **2** next to each product to show whether it is a Type 1 or Type 2 hypervisor.

**Part C.** Fill in the blank.

### Materials

**Word bank:** Physical hardware, Hypervisor, Host operating system.

```
        TYPE 1 (data center)               TYPE 2 (laptop for testing)

   +-----------------------------+      +-----------------------------+
   |   VM   |   VM   |   VM      |      |   VM   |   VM   |   VM      |
   +-----------------------------+      +-----------------------------+
   |            [ 1 ]            |      |            [ 3 ]            |
   +-----------------------------+      +-----------------------------+
   |            [ 2 ]            |      |            [ 4 ]            |
   +-----------------------------+      +-----------------------------+
                                        |            [ 5 ]            |
                                        +-----------------------------+
```

| Box | Your label |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

**Part B**

| Product | Type (1 or 2) |
|---|---|
| VMware ESXi | |
| Oracle VirtualBox | |
| Microsoft Hyper-V | |
| VMware Workstation | |
| Citrix Hypervisor (Xen) | |

**Part C**

A VM's disk is stored on the host as a ____________.

---

## C1P12-PBQ2: Cloud Match-up

| | |
|---|---|
| **ID** | C1P12-PBQ2 |
| **Objectives** | 4.1, 4.2 |
| **Type** | Matching (drag and drop style) |
| **Time guide** | 5 minutes |
| **Points** | 8 (1 per correct match) |

### Scenario

You are helping several customers choose the right virtualization or cloud idea for their needs. Each customer matches exactly one term. Two terms in the list are not used.

### Task

Write the term letter next to each customer number. Each term is used at most once.

### Materials

**Terms**

| Letter | Term |
|---|---|
| A | IaaS |
| B | Elasticity |
| C | Hybrid cloud |
| D | Container |
| E | Community cloud |
| F | SaaS |
| G | Sandbox |
| H | PaaS |
| I | VDI |
| J | Private cloud |

**Customers**

| # | Need | Your term letter |
|---|---|---|
| 1 | A company wants its own cloud that nobody else shares | |
| 2 | A shop's website needs many extra servers for a sale, then fewer afterwards | |
| 3 | Staff need email through a web browser, and the company runs no servers | |
| 4 | A small app is packaged with what it needs but shares the host's operating system, so it is lighter than a VM | |
| 5 | Staff desktops run on a central server and are shown on thin clients | |
| 6 | A suspicious program is tested in a walled-off virtual machine that is deleted afterwards | |
| 7 | A firm rents virtual servers and installs and manages its own operating system on them | |
| 8 | Several hospitals share one cloud built for their common needs | |
