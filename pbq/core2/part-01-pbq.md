# Core 2, Part 1: Performance-Based Questions

**Part:** Operating Systems, Windows Editions and Installing Them (objectives 1.1, 1.2, 1.3)
**Answers:** [part-01-pbq-answers.md](part-01-pbq-answers.md). Do not open it until you have finished both tasks.

The real 220-1202 exam has performance-based questions (PBQs): hands-on tasks instead of four-option choices. This kit cannot run a simulator, so each task here is done on paper or in a text file. Use the cheatsheet and memorize sheet **after** you try it, not during. Like the real exam, you earn credit for each correct part, so never leave a row blank.

---

## C2P01-PBQ1: Pick the file system

| | |
|---|---|
| **Objectives** | 1.1 |
| **Type** | Matching |
| **Time guide** | 5 minutes |

**Scenario.** You are the help desk person at a small design studio. The studio has Windows PCs, Macs, a Linux server and some USB drives. Your manager sends you seven short questions about which file system fits each job.

**Task.** Match each situation (1 to 7) to **one** file system (A to G). Each file system is used **exactly once**.

**Materials: file systems**

| Letter | File system |
|---|---|
| A | APFS |
| B | ext4 |
| C | exFAT |
| D | FAT32 |
| E | NTFS |
| F | ReFS |
| G | XFS |

**Situations**

1. A USB drive shared between Windows PCs and Macs. It must hold single video files of 10 GB.
2. The default file system on a Windows system drive.
3. The file system used by Apple's Macs, iPhones and iPads.
4. The common default file system on Linux.
5. An old file system that works on almost everything, but a single file can never be bigger than 4 GB.
6. A Windows file system built to resist data damage on very large storage. It is not the everyday default for a normal Windows drive.
7. A high-performance Linux file system made for large files and large volumes.

**Marking.** 7 points: 1 point per correct match. Wrong answers do not lose points.

---

## C2P01-PBQ2: Can it run Windows 11, and how do we install it?

| | |
|---|---|
| **Objectives** | 1.2, 1.3 |
| **Type** | Configure this form (fill-in table) |
| **Time guide** | 8 minutes |

**Scenario.** A school is deciding which PCs can move to Windows 11. You check four PCs against the requirements, then pick the install method for five jobs.

**Materials: Windows 11 requirements**

| # | Requirement |
|---|---|
| 1 | 64-bit processor, 1 GHz or faster, 2 or more cores |
| 2 | 4 GB RAM |
| 3 | 64 GB storage |
| 4 | UEFI firmware with Secure Boot |
| 5 | TPM 2.0 |

**Part A.** For each PC, write **Yes** (meets every requirement) or **No**. If No, write the **number (1 to 5)** of the one requirement it fails.

| PC | Processor | RAM | Storage | Firmware | TPM | Runs Windows 11? | Failed requirement # |
|---|---|---|---|---|---|---|---|
| PC1 | 64-bit, 2.6 GHz, 4 cores | 8 GB | 256 GB | UEFI, Secure Boot on | 2.0 | | |
| PC2 | 64-bit, 3.0 GHz, 6 cores | 16 GB | 1 TB | UEFI, Secure Boot on | 1.2 | | |
| PC3 | 64-bit, 2.4 GHz, 4 cores | 8 GB | 256 GB | Legacy BIOS mode, no Secure Boot | 2.0 | | |
| PC4 | 64-bit, 2.0 GHz, 2 cores | 8 GB | 32 GB | UEFI, Secure Boot on | 2.0 | | |

**Part B.** Pick **one** method (A to G) for each job. Each method is used **at most once**, and two are not needed.

| Letter | Method |
|---|---|
| A | Clean install |
| B | Upgrade (in-place) |
| C | Image deployment |
| D | Zero-touch deployment |
| E | Repair installation |
| F | Recovery partition |
| G | Load a third-party driver during setup |

| Job | Your letter |
|---|---|
| a. A Windows 10 PC that meets the requirements. The owner wants Windows 11 and wants to keep files, apps and settings. | |
| b. IT must put the same Windows and apps on 40 identical PCs by copying one ready-made copy. | |
| c. New PCs are shipped straight to staff. Nobody at IT touches them, and they set themselves up. | |
| d. Windows system files are damaged. The user wants them fixed and wants to keep files and apps. | |
| e. Windows setup shows no drive to install to, because the PC uses a RAID controller. | |

**Marking.** 9 points. Part A: 1 point for PC1, and 1 point each for PC2 to PC4 only when both the No and the requirement number are right (4 points). Part B: 1 point per row (5 points).
