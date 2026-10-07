# Lab: Inspect your own Windows install (Windows, free)

**Time:** 15 minutes. **Needs:** a Windows PC. Every step is read-only. You won't change or erase anything.

Goal: find the things Part 1 talks about, on a real machine.

## 1. Which edition and version are you running?

Press **Windows key + R**, type `winver`, press Enter. Write down the **edition** and **version**. Then open **Settings > System > About** and find the **Edition** and **System type**.

Is it Home, Pro or Enterprise? Which features from the cheat sheet do you have? Test one: press Windows key + R, type `gpedit.msc`, press Enter. If you get an error, you are on Home.

## 2. Is your drive MBR or GPT?

Press **Windows key + X** and choose **Disk Management**. Right-click the label of **Disk 0** (on the left), choose **Properties**, open the **Volumes** tab, and look at **Partition style**. It says **GUID Partition Table (GPT)** or **Master Boot Record (MBR)**.

Write down each partition and its **file system** (NTFS, FAT32). The small unnamed ones are usually the **EFI system partition** and the **recovery partition**.

## 3. Boot mode, Secure Boot and TPM

Press **Windows key + R**, type `msinfo32`, press Enter. In **System Summary**, find **BIOS Mode** (UEFI or Legacy) and **Secure Boot State**.

Then press **Windows key + R**, type `tpm.msc`, press Enter, and find the **Specification Version**. You want 2.0 for Windows 11. If you have a PC that Windows 11 refuses, this is the first place to look.

## 4. Can you run Windows 11?

Open **Settings > Windows Update**. If Windows 11 is on offer, the PC meets the requirements. Compare each requirement from the cheat sheet with what you found in steps 1 to 3 (and your RAM and storage under **Settings > System > About**).

## 5. Find the recovery tools (look, do not click Reset)

Open **Settings > System > Recovery**. Note the options: **Reset this PC**, **Go back** (if offered), and **Advanced startup**. Reset this PC with the "keep my files" option is close to a repair installation. With "remove everything" it acts like a clean install.

## 6. Write it up

```
Edition / version:
gpedit.msc present (yes/no):
Partition style (MBR or GPT):
File systems seen:
BIOS Mode / Secure Boot / TPM version:
Windows 11 requirements met (yes/no):
```

## Check yourself

- Your drive is MBR and 4 TB. How much can Windows use, and what would you do?
- What does Windows Home lack that a domain-joined business laptop needs?
- Which install type would you use for 50 identical laptops?

## Going further (optional)

Install a free virtual machine program such as VirtualBox and a Linux distribution, and look at which file system it uses by default (usually ext4). It is the safest way to try a second operating system.
