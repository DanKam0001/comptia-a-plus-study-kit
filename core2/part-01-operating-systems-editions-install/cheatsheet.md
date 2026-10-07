# Core 2, Part 1: Operating Systems, Windows Editions and Installing Them

**Objectives 1.1, 1.2 and 1.3** (220-1202):
- **1.1** Explain common operating system (OS) types and their purposes.
- **1.2** Given a scenario, perform OS installations and upgrades in a diverse environment.
- **1.3** Compare and contrast basic features of Microsoft Windows editions.

Domain: Operating Systems (28% of the exam).

Core 2 is its own course. You do not need to have watched Core 1.

## 1.1 Operating system types and purposes

An **operating system (OS)** runs the hardware and lets you run apps.

| Group | OS | Notes |
|---|---|---|
| Workstation | **Windows** | The most common desktop and laptop OS. Made by Microsoft |
| Workstation | **Linux** | Free and open source. Comes in many distributions |
| Workstation | **macOS** | Runs on Apple computers |
| Workstation | **Chrome OS** | Google's light OS, built around web apps. Runs on Chromebooks |
| Mobile | **iPadOS** | Apple iPad |
| Mobile | **iOS** | Apple iPhone |
| Mobile | **Android** | Made by Google, used by many makers |

### File system types

A **file system** decides how files are stored on a drive.

| File system | Used by | Know this |
|---|---|---|
| **NTFS** (New Technology File System) | Windows | Default for Windows. File permissions, encryption, compression, large files |
| **ReFS** (Resilient File System) | Windows | Built to resist data damage on large storage. Not the everyday default for a normal Windows drive |
| **FAT32** | Everything | Old and widely compatible. **Maximum single file size 4 GB** |
| **exFAT** (Extensible File Allocation Table) | Windows, macOS | Large files. Suits USB drives and flash storage shared between Windows and macOS |
| **ext4** (fourth extended filesystem) | Linux | Common Linux default |
| **XFS** (extended filesystem) | Linux | High-performance Linux file system for large files and volumes |
| **APFS** (Apple File System) | macOS, iOS, iPadOS | Apple's file system |

### Vendor life-cycle limitations

- **End-of-life (EOL):** the vendor stops supporting a version. No more security updates or fixes, so it becomes a risk.
- **Update limitations:** older devices may be left behind and cannot receive the newest version or updates.
- **Windows 10 support ended on October 14, 2025.**
- **Windows 11 servicing:** each version is supported for **24 months** for Home and Pro, and **36 months** for Enterprise and Education.

### Compatibility concerns between operating systems

- An app built for one OS may not exist for, or run on, another.
- Some file systems are not readable by every OS (for example, NTFS is read-only by default on macOS, and Windows cannot read ext4 or APFS without extra software).
- File formats, drivers and hardware must all be supported by the OS you move to.

## 1.2 Installations and upgrades

### Boot methods

| Method | Notes |
|---|---|
| **USB** | Most common. A bootable installer on a flash drive |
| **Network** | Boot from a server across the network (often called PXE, Preboot Execution Environment) |
| **Solid-state/flash drives** | An installer stored on flash storage |
| **Internet-based** | Download and install from the internet (for example, cloud reset or macOS recovery) |
| **External/hot-swappable drive** | An installer on an external drive |
| **Internal hard drive (partition)** | An installer or recovery tools stored on a partition of the PC's own drive |
| **Multiboot** | Two or more operating systems on one PC, chosen at startup |

Pick the boot device in the firmware, or with the boot menu key as the PC starts (see Core 1 Part 1, Motherboards, CPUs and Firmware).

### Types of installation

| Type | What it does |
|---|---|
| **Clean install** | Wipes the drive and installs fresh. No old files or apps |
| **Upgrade** | Installs the new version over the old one, keeping files, apps and settings (in-place upgrade) |
| **Image deployment** | Copies one ready-made image (OS plus apps and settings) onto many PCs |
| **Remote network installation** | Installs over the network from a server |
| **Zero-touch deployment** | Fully automatic. Nobody touches the PC. It configures itself (for example, with Windows Autopilot) |
| **Recovery partition** | A hidden copy on the drive that restores the PC to its factory state |
| **Repair installation** | Reinstalls Windows files over the top to fix problems, keeping your files and apps |
| **Other considerations: third-party drivers** | If setup cannot see the drive (RAID or NVMe controller), load a third-party driver during setup |

### Partitioning

| | MBR (Master Boot Record) | GPT (GUID Partition Table) |
|---|---|---|
| Maximum drive size used | **2 TB** | Far larger (about 9.4 ZB in theory) |
| Partitions | **4 primary** | **128** in Windows |
| Boots with | BIOS | UEFI. Windows needs GPT to boot in UEFI mode |

A new 4 TB drive showing only 2 TB was set up as MBR. Initialize it as GPT.

### Drive format

After partitioning, **format** the partition with a file system. NTFS for Windows. A quick format clears the file table. A full format also checks the drive for bad sectors, so it is slower.

### Upgrade considerations

- **Back up files and user preferences** before any upgrade.
- **Application and driver support, and backward compatibility:** check apps and drivers work with the new version.
- **Hardware compatibility:** check the PC meets the requirements (Windows 11 needs TPM 2.0 and UEFI with Secure Boot).

### Feature updates and product life cycle

- A **feature update** is a big update that adds new features. Windows 11 gets one each year.
- The **product life cycle** decides how long a version is supported. See EOL above.

## 1.3 Windows editions

| | Windows 10 | Windows 11 |
|---|---|---|
| Editions (as listed in the objectives) | Home, Pro, Pro for Workstations, Enterprise | Home, Pro, Enterprise |

**N versions** are the same edition without Windows Media Player and related media features. You can add them back with a free feature pack.

### Feature differences

| Feature | Home | Pro | Pro for Workstations | Enterprise |
|---|---|---|---|---|
| Domain vs workgroup | **Workgroup only** | Domain or workgroup | Domain or workgroup | Domain or workgroup |
| Remote Desktop (RDP) | Can connect **out** only | Can **host** and connect | Can host and connect | Can host and connect |
| BitLocker | No (device encryption on supported hardware only) | **Yes** | Yes | Yes |
| gpedit.msc (Group Policy Editor) | No | **Yes** | Yes | Yes |
| RAM limit (64-bit) | **128 GB** | **2 TB** | **6 TB** | **6 TB** |

- **Domain vs workgroup:** a **domain** is a company network with central accounts managed by a server. A **workgroup** is a small network with no central server.
- **Desktop styles/user interface:** Windows 10 has a left-aligned Start menu with live tiles. Windows 11 has a centered taskbar and Start menu and rounded corners.
- **Pro for Workstations:** for very powerful PCs. Adds the ReFS file system and supports more RAM and processors.

### Upgrade paths

- **In-place upgrade:** keeps files, apps and settings. A Windows 10 PC that meets the requirements can upgrade to Windows 11 this way.
- **Clean install:** wipes the drive and starts fresh. Needed when moving between some editions or when the old install is damaged.
- Moving up an edition (for example, Home to Pro) is done with a product key or the Microsoft Store, without reinstalling.

### Hardware requirements (Windows 11)

- 64-bit processor, 1 GHz or faster, 2 or more cores
- 4 GB RAM
- 64 GB storage
- **UEFI** firmware with **Secure Boot**
- **TPM 2.0**
