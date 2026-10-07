# Core 2, Part 1: PBQ answers

Task file: [part-01-pbq.md](part-01-pbq.md). Try the tasks first.

---

## C2P01-PBQ1: Pick the file system

| # | Answer | Why |
|---|---|---|
| 1 | C, exFAT | Handles large files and suits USB drives shared between Windows and macOS. FAT32 caps a file at 4 GB |
| 2 | E, NTFS | The default Windows file system |
| 3 | A, APFS | Apple's file system for macOS, iOS and iPadOS |
| 4 | B, ext4 | The common default on Linux |
| 5 | D, FAT32 | Very compatible, but the maximum single file size is 4 GB |
| 6 | F, ReFS | Built to resist data damage on large storage; not the everyday default |
| 7 | G, XFS | High-performance Linux file system for large files and volumes |

**Marking:** 7 points, 1 per match. 7 = full marks. 5 to 6 = solid, recheck the table in the cheatsheet. 4 or fewer = reread section 1.1.

---

## C2P01-PBQ2: Can it run Windows 11, and how do we install it?

**Part A**

| PC | Answer | Why |
|---|---|---|
| PC1 | Yes | Meets all five requirements |
| PC2 | No, 5 | TPM is 1.2; Windows 11 needs TPM 2.0 |
| PC3 | No, 4 | Legacy BIOS mode with no Secure Boot; Windows 11 needs UEFI with Secure Boot |
| PC4 | No, 3 | 32 GB is below the 64 GB storage requirement |

**Part B**

| Job | Answer | Why |
|---|---|---|
| a | B, Upgrade (in-place) | An upgrade keeps files, apps and settings |
| b | C, Image deployment | One ready-made image copied to many PCs |
| c | D, Zero-touch deployment | Fully automatic, nobody touches the PC (for example Windows Autopilot) |
| d | E, Repair installation | Reinstalls Windows files over the top and keeps files and apps |
| e | G, Load a third-party driver during setup | Setup cannot see a RAID or NVMe drive without the controller's driver |

Not used: A (clean install wipes everything) and F (recovery partition restores factory state).

**Partial credit (9 points):** PC1 = 1. PC2 to PC4 = 1 each only if both the No and the number are right (a right No with a wrong number earns 0). Part B = 1 per row. 8 to 9 = strong. 6 to 7 = pass-level. 5 or fewer = redo requirements and install types in section 1.2.
