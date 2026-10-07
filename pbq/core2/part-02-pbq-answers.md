# Core 2, Part 2: PBQ answers

Task file: [part-02-pbq.md](part-02-pbq.md). Try the tasks first.

---

## C2P02-PBQ1: Which tool do I open?

| # | Answer | Why |
|---|---|---|
| 1 | F, `resmon.exe` | Resource Monitor is the detailed live view of which process uses CPU, memory, disk and network |
| 2 | C, `taskschd.msc` | Task Scheduler runs a program or script at a time or event |
| 3 | H, `msconfig.exe` | System Configuration controls how Windows starts, including boot options such as safe boot |
| 4 | A, `eventvwr.msc` | Event Viewer holds the logs; program errors are in the Application log |
| 5 | D, `devmgmt.msc` | Device Manager updates, rolls back, disables or uninstalls drivers; the yellow triangle means a driver problem |
| 6 | G, `perfmon.msc` | Performance Monitor records detailed counters over time |
| 7 | B, `diskmgmt.msc` | Disk Management initializes a new disk (GPT or MBR) and creates and formats volumes |
| 8 | E, `msinfo32.exe` | System Information reports hardware, drivers, BIOS mode and Secure Boot state |

Not used: I (`regedit.exe`, the Registry Editor, edits deep settings and answers none of the problems above).

**Marking:** 8 points, 1 per match. 7 to 8 = strong. 5 to 6 = review the MMC snap-in table. 4 or fewer = reread the snap-in and additional tools tables in the cheatsheet.

---

## C2P02-PBQ2: Set up a laptop's power options

| Row | Answer | Why |
|---|---|---|
| 1 | Do nothing | The choice that keeps Windows running with the lid closed |
| 2 | Hibernate | Hibernate saves work to the drive and then powers fully off, using no power |
| 3 | Sleep | Sleep keeps work in RAM, wakes in seconds and uses a little power |
| 4 | Disabled | USB selective suspend powers down idle USB ports and can make a device disappear |
| 5 | On | Fast startup saves the Windows kernel to disk at a normal shutdown for a quicker next boot |
| 6 | Balanced | Balanced is the default power plan |

**Partial credit (6 points):** 1 per row. 6 = full marks. 4 to 5 = pass-level, recheck the Power Options table. 3 or fewer = reread the Power Options section.
