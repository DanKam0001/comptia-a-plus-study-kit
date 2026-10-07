# Lab: Inspect your own storage (Windows)

**Time:** 10 to 15 minutes. **Needs:** any Windows PC. Everything here is read-only.

Goal: find out what kind of drive your PC has and how it connects.

## 1. HDD or SSD? SATA or NVMe?

Open PowerShell and run:

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, BusType, Size
```

- `MediaType`: HDD or SSD.
- `BusType`: SATA, NVMe, SAS or USB. That is the interface from the cheat sheet.

## 2. Check the form factor

Search the `FriendlyName` online. Is it 2.5-inch, 3.5-inch or M.2? If M.2, note the size (such as 2280).

## 3. Find the drive's speed in practice

Open **Task Manager > Performance** and click your disk. Note the **Type** and **Active time**. Copy a large file and watch the transfer rate.

## 4. Look at your volumes

```powershell
Get-Volume | Select-Object DriveLetter, FileSystemLabel, Size, SizeRemaining
```

## 5. Paper RAID practice

You have four 2 TB drives. Fill in this table from memory, then check the cheat sheet:

```
RAID 0 usable capacity / survives:
RAID 1 (two drives) usable capacity / survives:
RAID 5 usable capacity / survives:
RAID 6 usable capacity / survives:
RAID 10 usable capacity / survives:
```

(Answers: 8 TB / none; 2 TB / 1; 6 TB / 1; 4 TB / 2; 4 TB / 1 per mirrored pair.)

## 6. Write it up

```
Drive type (HDD or SSD):
Interface (SATA / NVMe):
Form factor:
Size:
```

## Check yourself

- Why would you swap this PC's HDD for an SSD, or not need to?
- A new M.2 drive is not detected. What do you check first?
- Which RAID level would you pick to survive two failures?

## Going further (optional)

If you have a spare desktop, powered off and unplugged, find the SATA ports, the M.2 slot and the screw or latch that holds an M.2 stick. Look for the key notch. Do not remove anything you do not plan to put back.
