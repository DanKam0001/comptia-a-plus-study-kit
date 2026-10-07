# Core 2, Part 14: PBQ answers and marking

Questions are in `part-14-pbq.md`. One point per correct item, nothing for a wrong item. This kit marks each item separately. CompTIA does not publish its PBQ scoring rules, so treat this as practice marking, not the real formula.

---

## C2P14-PBQ1: Plan the restore (14 points)

**Part A (6 points: 2 per plan, 1 for the correct list in the correct order, 1 for the correct count)**

| Plan | Backups to restore, in order | How many | Why |
|---|---|---|---|
| 1 Incremental | Sun full, Mon incremental, Tue incremental, Wed incremental | 4 | An incremental holds only changes since the last backup of any kind, so you need the last full plus every incremental since. |
| 2 Differential | Sun full, Wed differential | 2 | A differential holds all changes since the last full, so only the latest one is needed with the full. |
| 3 Full | Wed full | 1 | A full backup holds everything. |

**Part B (6 points: one per cell)**

| Backup type | Fastest to TAKE | Fastest to RESTORE |
|---|---|---|
| Full | 3 | 1 |
| Incremental | 1 | 3 |
| Differential | 2 | 2 |

Why: incremental copies the least each night and needs 4 backups to restore; full copies the most and needs 1; differential copies more than incremental but less than full (everything since Sunday) and needs 2. The cheat sheet states only the two extremes. The middle rank for differential follows from the counts in Part A.

**Part C (2 points)**

| # | Answer |
|---|---|
| 1 | 3, 2, 1 (one point if all three are right) |
| 2 | son, father, grandfather (one point if all three are right) |

Total: 6 + 6 + 2 = 14 points.

**Marking:** 14 = full marks. 11 to 13 = good. Below 11 = reread the backup table in the Part 14 cheat sheet. If you wrote "all the incrementals" for plan 2, you mixed up incremental and differential: differential counts from the last FULL.

---

## C2P14-PBQ2: Run a change properly (11 points)

**Part A (5 points: one per step in the correct place)**

| Your number | Step |
|---|---|
| 4 | Peer review of the finished change |
| 2 | The change board approves the request |
| blank | Make the change before approval because it is quicker |
| 5 | End-user acceptance |
| 1 | Fill in the request form |
| 3 | Implementation during the agreed time |

Why: the request form comes first (it carries the purpose, scope and risk analysis), the change board approves it, then implementation, then peer review, then end-user acceptance. Skipping approval is the wrong move for a normal change.

**Part B (4 points)**

| # | Answer | Why |
|---|---|---|
| 1 | S | Routine and pre-approved. |
| 2 | N | Planned, so it goes through the full approval process. |
| 3 | E | Urgent fix, still documented afterwards. |
| 4 | S | Routine and pre-approved. |

**Part C (2 points)**

| # | Answer |
|---|---|
| 1 | CF (change freeze) |
| 2 | MW (maintenance window) |

**Marking:** 11 = full marks. 9 to 10 = good. Below 9 = reread the change types and the "implementation, peer review, end-user acceptance" order in the cheat sheet.
