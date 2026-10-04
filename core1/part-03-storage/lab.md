# Lab: Inspect your own storage (Windows)

**Time:** 10 minutes. **Needs:** any Windows PC. Everything here is read-only. Don't change partitions.

## 1. What drives do you have?

Open PowerShell and run:

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, BusType, @{n='GB';e={[math]::Round($_.Size/1GB)}}, HealthStatus
```

| Column | What to look for |
|---|---|
| `MediaType` | SSD or HDD |
| `BusType` | SATA or NVMe (or USB for external drives) |
| `HealthStatus` | Healthy is what you want to see |

Search each `FriendlyName` online to find its form factor (2.5-inch, 3.5-inch, M.2) and, for HDDs, its RPM.

## 2. See the same thing in the GUI

- **Task Manager > Performance > Disk** shows each drive's type (SSD or HDD) and activity.
- **Win + R > `diskmgmt.msc`** shows partitions. Look only; don't change anything.

## 3. Work out RAID capacities (paper exercise)

Four identical **2 TB** drives. How much usable space in each level?

| Level | Usable capacity | Survives |
|---|---|---|
| RAID 0 | 8 TB | nothing |
| RAID 1 (uses exactly 2 of the drives) | 2 TB | 1 drive |
| RAID 5 | 6 TB | 1 drive |
| RAID 6 | 4 TB | 2 drives |
| RAID 10 | 4 TB | 1 per mirrored pair |

Cover the table and work them out yourself first.

## 4. Write it up

```
Drive 1: type (SSD/HDD), bus (SATA/NVMe), size, health
Drive 2: ...
Which one boots Windows?
Would swapping an HDD for an SSD help here? Why?
```

## Check yourself

- Your PC has an M.2 slot and the manual says "PCIe x4 only". Would a SATA M.2 drive work? (No. Check the slot type.)
- A friend says "I have RAID 1, so I don't need backups." What do you tell them? (It doesn't protect against deletion, malware, fire or controller failure.)
