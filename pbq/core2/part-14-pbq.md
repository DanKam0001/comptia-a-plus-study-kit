# Core 2, Part 14: PBQ practice (Documentation, change management, backup)

Objectives 4.1, 4.2, 4.3 (220-1202). Print this page or copy it into a text file and fill it in. Do not open `part-14-pbq-answers.md` until you have finished both tasks.

---

## C2P14-PBQ1: Plan the restore

| | |
|---|---|
| **ID** | C2P14-PBQ1 |
| **Objectives** | 4.3 |
| **Type** | Fill-in table and ranking |
| **Time guide** | 6 minutes |

**Scenario.** A small firm backs up its file server. There is a full backup every Sunday, and a nightly backup on Monday, Tuesday and Wednesday. The server's drive dies on Thursday morning, before any Thursday backup. The firm is comparing three plans for what the nightly backup should be.

**Task.**

**Part A.** For each plan, list the backups you must restore, in order, and how many backups that is. Use names like "Sun full", "Mon incremental", "Wed differential".

| Plan | Nightly backup type | Backups to restore, in order | How many |
|---|---|---|---|
| 1 | Incremental | | |
| 2 | Differential | | |
| 3 | Full | | |

**Part B.** Put the three backup types in order. Write 1, 2, 3 (1 = fastest). For TAKE, rank by how much data each nightly backup copies (least = fastest). For RESTORE, rank by how many backups you needed in Part A (fewest = fastest).

| Backup type | Fastest to TAKE (1 to 3) | Fastest to RESTORE (1 to 3) |
|---|---|---|
| Full | | |
| Incremental | | |
| Differential | | |

**Part C.** Fill in the blanks.

| # | Blank |
|---|---|
| 1 | The 3-2-1 rule: ___ copies of the data, on ___ different types of media, with ___ copy offsite |
| 2 | In grandfather-father-son (GFS), the daily backup is the ______ , the weekly is the ______ , the monthly is the ______ |

---

## C2P14-PBQ2: Run a change properly

| | |
|---|---|
| **ID** | C2P14-PBQ2 |
| **Objectives** | 4.1, 4.2 |
| **Type** | Ordering, classifying and matching |
| **Time guide** | 7 minutes |

**Scenario.** The IT team of a medium company follows a formal change process. Four jobs arrive this week, and you must order the process for one of them and label the rest.

**Task.**

**Part A.** The team plans to replace the file server with a new model. Number the steps 1 to 5 in the correct order. One step is wrong: leave it blank.

| Your number | Step |
|---|---|
| | Peer review of the finished change |
| | The change board approves the request |
| | Make the change before approval because it is quicker |
| | End-user acceptance |
| | Fill in the request form (purpose, scope, change type, date and time, affected systems, risk analysis) |
| | Implementation during the agreed time |

**Part B.** Label each job with S (standard), N (normal) or E (emergency).

| # | Job | S, N or E |
|---|---|---|
| 1 | The monthly routine patch run, done the same pre-approved way every month | |
| 2 | Replacing the file server with a new model, planned for next month | |
| 3 | The main file server has crashed in the middle of the working day and every user is blocked. It must be fixed right now. | |
| 4 | Creating an account for a new starter from the usual pre-approved template | |

**Part C.** Write **MW** (maintenance window) or **CF** (change freeze) beside each.

| # | Description | MW or CF |
|---|---|---|
| 1 | A period when no changes are allowed | |
| 2 | A planned quiet time for making changes | |
