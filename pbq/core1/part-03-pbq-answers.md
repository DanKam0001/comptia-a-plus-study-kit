# Core 1, Part 3 PBQ answers

Tasks: [part-03-pbq.md](part-03-pbq.md). Facts come from the [Part 3 cheat sheet](../../core1/part-03-storage/cheatsheet.md).

---

## C1P03-PBQ1: Pick the RAID level

**Part A**

| Job | RAID level | Why |
|---|---|---|
| 1 | **RAID 0** | Striping: fastest, no protection |
| 2 | **RAID 1** | Mirroring on 2 drives, 50% usable |
| 3 | **RAID 5** | Striping plus parity, min 3 drives, loses one drive's worth |
| 4 | **RAID 6** | Double parity survives any 2 failures (RAID 10 only survives one failure per mirrored pair) |
| 5 | **RAID 10** | Mirrored pairs striped, min 4 drives, 50% usable |

**Part B** (4 drives x 2 TB = 8 TB raw)

| Setup | Usable space | Why |
|---|---|---|
| RAID 0 on 4 drives | **8 TB** | 100% |
| RAID 1 on 2 drives | **2 TB** | 50% of 4 TB |
| RAID 5 on 4 drives | **6 TB** | all but one drive |
| RAID 6 on 4 drives | **4 TB** | all but two drives |
| RAID 10 on 4 drives | **4 TB** | 50% |

**Marking (10 points):** 1 per job, 1 per row. Partial credit applies row by row.
- 9 to 10: strong. 7 to 8: recheck the RAID table. Under 7: relearn the RAID block in the memorise sheet.
- Common slip: writing RAID 10 for job 4. It only survives one failure per pair, so "any two" means RAID 6.

---

## C1P03-PBQ2: Spot the faults in the build sheet

| Line | Answer | Why |
|---|---|---|
| 1 | **WRONG A** | A SATA controller cannot run SAS drives |
| 2 | **WRONG B** | M.2 is a shape, not a speed |
| 3 | **OK** | RAID 1 survives one failure, replace and rebuild while running |
| 4 | **WRONG C** | RAID is not a backup |
| 5 | **WRONG D** | RAID 0 survives nothing |
| 6 | **OK** | 3.5-inch drives suit desktops, 7200 RPM is a normal PC spindle speed |

E and F are the unused distractors: E is a true fact but fixes no line, F is false.

**Marking (6 points):** 1 per line. A WRONG line with the wrong letter scores nothing, and marking a correct line WRONG scores nothing.
- 6: strong. 4 to 5: fine. Under 4: reread the Interfaces, M.2 and RAID sections.
