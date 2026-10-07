# Core 1, Part 3 PBQs: Storage

Performance-based question (PBQ) practice for **Objective 3.4** (220-1201). Do each task on paper or in a text file. Answers are in a separate file ([part-03-pbq-answers.md](part-03-pbq-answers.md)), so don't open it until you have finished.

If you are stuck, check the [Part 3 cheat sheet](../../core1/part-03-storage/cheatsheet.md), mark that item, and lose the point.

---

## C1P03-PBQ1: Pick the RAID level

- **Objective:** 3.4
- **Type:** Matching (plus a short fill-in table)
- **Time guide:** 6 minutes

### Scenario

A small company is setting up five different storage jobs. Each job needs a different RAID level (RAID = Redundant Array of Independent Disks). Choose the level for each job, then work out how much usable space the company gets.

### Materials

**Part A: the jobs**

1. Two drives, fastest possible speed, the files are temporary scratch video and losing them is fine.
2. Exactly two drives, a live copy of everything on both, usable space is half the total.
3. Three drives, survive one drive failing, and only one drive's worth of space is lost.
4. Four drives, must survive **any** two drives failing.
5. Four drives, mirrored pairs that are then striped together, usable space is half the total.

**RAID level choices:** `RAID 0`, `RAID 1`, `RAID 5`, `RAID 6`, `RAID 10`. Each is used once.

**Part B: usable space.** Every drive is 2 TB.

| Setup | Usable space (TB) |
|---|---|
| RAID 0 on 4 drives | |
| RAID 1 on 2 drives | |
| RAID 5 on 4 drives | |
| RAID 6 on 4 drives | |
| RAID 10 on 4 drives | |

### Task

Part A: write the RAID level for each job number. Part B: fill in the five blanks.

### Marking

10 points: 1 per job (5) and 1 per row of Part B (5).

---

## C1P03-PBQ2: Spot the faults in the build sheet

- **Objective:** 3.4
- **Type:** Scenario fix (find and correct the mistakes)
- **Time guide:** 5 minutes

### Scenario

A junior technician wrote a build sheet for a server and some desktops. Some lines are fine and some contain a mistake. Mark each line **OK** or **WRONG**. For each WRONG line, pick the letter of the correct fix from the fix list.

### Materials

**Build sheet**

| Line | What the technician wrote |
|---|---|
| 1 | The new server drives are SAS, but the server only has a SATA controller. That is fine, it will run them. |
| 2 | The customer wants fast storage, so buy any M.2 SSD, because M.2 always means NVMe speed. |
| 3 | The office file server uses RAID 1 on two drives. When one dies we replace it and let the array rebuild while it keeps running. |
| 4 | We chose RAID 5, so we do not need any backups, even if staff delete files. |
| 5 | The accounting database sits on RAID 0 across two drives, so it survives a drive failure. |
| 6 | The desktops get a 3.5-inch 7200 RPM hard drive each. |

**Fix list**

- **A.** A SAS controller can run SATA drives, but a SATA controller cannot run SAS drives.
- **B.** M.2 is only a shape. The drive can be SATA or NVMe, so check what the slot supports.
- **C.** RAID only protects against drive failure, not deletion, malware or fire, so keep backups.
- **D.** RAID 0 has no fault tolerance. Use RAID 1, 5, 6 or 10 for protection.
- **E.** SATA III runs at 6 Gbps.
- **F.** Hard drives never need a spindle speed rating.

### Task

For each line write `OK`, or `WRONG` plus a fix letter (for example `WRONG D`). Two letters in the fix list are not the right fix for any line.

### Marking

6 points: 1 per line. A WRONG line needs the correct fix letter for the point.
