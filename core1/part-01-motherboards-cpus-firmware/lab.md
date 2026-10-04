# Lab: Inspect your own motherboard and CPU (Windows)

**Time:** 10 to 15 minutes. **Needs:** any Windows PC. Everything here is read-only. You won't change any setting.

Goal: see for yourself the things Part 1 talks about, on a real machine.

## 1. Find your motherboard and its form-factor family

Open PowerShell (Start menu, type `powershell`) and run:

```powershell
Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product
```

Search the **Product** name online and note its form factor (ATX, microATX or Mini-ITX). On a laptop you will get a proprietary board.

## 2. Find your CPU, socket, cores and threads

```powershell
Get-CimInstance Win32_Processor | Select-Object Name, SocketDesignation, NumberOfCores, NumberOfLogicalProcessors
```

Write down:
- Is the socket **LGA** or **PGA**? (Search the socket name.)
- Is `NumberOfLogicalProcessors` bigger than `NumberOfCores`? That's hyper-threading / simultaneous multithreading.
- Is it **x64**? (Task Manager, Details tab, or Settings > System > About shows "64-bit operating system, x64-based processor".)

Also open **Task Manager > Performance > CPU** and compare the numbers with the PowerShell output.

## 3. Is virtualization turned on?

In **Task Manager > Performance > CPU**, look at the bottom right for **Virtualization: Enabled / Disabled**.
If it says Disabled and you want to run virtual machines, the setting is in the firmware (Intel VT-x / AMD-V).

## 4. BIOS or UEFI, and Secure Boot

Press **Windows key + R**, type `msinfo32`, press Enter. In **System Summary**, find:
- **BIOS Mode:** UEFI or Legacy
- **Secure Boot State:** On, Off or Unsupported
- **BIOS Version/Date**

## 5. Do you have a TPM, and which version?

Press **Windows key + R**, type `tpm.msc`, press Enter. Look for **Specification Version** (you want 2.0 for Windows 11).
If it says "Compatible TPM cannot be found", the TPM may be turned off in firmware, or the PC doesn't have one.

## 6. Write it up (this is the part that sticks)

Make a 6-line note for yourself:

```
Board:            (manufacturer + product)
Form factor:
CPU / socket:     (and LGA or PGA)
Cores / threads:
Firmware mode / Secure Boot / TPM version:
Virtualization:
```

## Check yourself

- If you wanted to upgrade this CPU, what two things must match or be supported besides the CPU itself? (socket and chipset, and possibly a firmware update)
- Which firmware setting would you change to run a virtual machine on this PC?
- If this PC were refused a Windows 11 upgrade, which two firmware features would you check first?

## Going further (optional)

If you have a spare desktop, open the case (powered off and unplugged!) and find: the CPU cooler, the DIMM slots, the PCIe x16 slot, the SATA ports, the front-panel header pins and the 24-pin main power connector.
