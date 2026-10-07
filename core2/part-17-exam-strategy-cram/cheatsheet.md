# Core 2, Part 17: Exam Strategy, PBQs and a Cram Review

**Objectives:** all of them, 1.1 to 4.10 (220-1202). This part has no new objective. It covers how to sit the exam and where to find every objective in the kit.

## The exam in numbers

| Fact | Value |
|---|---|
| Exam code | 220-1202 (Core 2) |
| Questions | At most 90 |
| Time | 90 minutes |
| Question types | Multiple choice and performance-based questions (PBQs) |
| Passing score | 700 on a scale of 100 to 900 |
| Domain 1, Operating Systems | 28% |
| Domain 2, Security | 28% |
| Domain 3, Software Troubleshooting | 23% |
| Domain 4, Operational Procedures | 21% |

## Performance-based questions (PBQs)

- A PBQ gives you a **task** on a simulated screen, such as dragging items to match them, putting steps in order, or choosing settings.
- They often appear near the start and can take longer than a multiple choice question.
- **Strategy:** read the whole task, do the parts you know, **flag** it if you're stuck, move on, and return after the multiple choice questions.
- They test things you have done, so do the labs in the kit (commands, Windows tools, settings).

## Managing time

- 90 questions in 90 minutes is about **1 minute each**. PBQs take longer, so bank time on easy questions.
- Don't sit on a hard question. Choose your best answer, **flag it**, and move on.
- Keep **10 to 15 minutes** at the end to review flagged questions.
- An unanswered question counts as wrong, so **answer every question**. Never leave one blank.

## When two answers both look right

- Re-read the question. Underline the key words: **first, best, most likely, next**.
- Cross out answers that are clearly wrong.
- Ask what is really being tested: the first step, the safest action, the fastest fix, or the most likely cause?
- Choose the answer that fits that exact word and situation. Don't change an answer without a clear reason.

## Cram map: where each objective lives

| Domain | Objectives | Parts in this series |
|---|---|---|
| 1.0 Operating Systems (28%) | 1.1 to 1.11 | Parts 1 to 6 |
| 2.0 Security (28%) | 2.1 to 2.11 | Parts 7 to 11 |
| 3.0 Software Troubleshooting (23%) | 3.1 to 3.4 | Parts 12 and 13 |
| 4.0 Operational Procedures (21%) | 4.1 to 4.10 | Parts 14, 15 and 16 |

Exact split: Part 1 = 1.1, 1.2, 1.3. Part 2 = 1.4, 1.6. Part 3 = 1.5. Part 4 = 1.7. Part 5 = 1.8, 1.9. Part 6 = 1.10, 1.11. Part 7 = 2.1, 2.3. Part 8 = 2.2, 2.7. Part 9 = 2.4, 2.5, 2.6. Part 10 = 2.8, 2.10, 2.11. Part 11 = 2.9. Part 12 = 3.1. Part 13 = 3.2, 3.3, 3.4. Part 14 = 4.1, 4.2, 4.3. Part 15 = 4.4, 4.5, 4.6, 4.7. Part 16 = 4.8, 4.9, 4.10.

## Cram: facts straight from the objectives

**Management tools (MMC snap-ins):** Event Viewer `eventvwr.msc`, Disk Management `diskmgmt.msc`, Task Scheduler `taskschd.msc`, Device Manager `devmgmt.msc`, Certificate Manager `certmgr.msc`, Local Users and Groups `lusrmgr.msc`, Performance Monitor `perfmon.msc`, Group Policy Editor `gpedit.msc`.

**Other tools:** System Information `msinfo32.exe`, Resource Monitor `resmon.exe`, System Configuration `msconfig.exe`, Disk Cleanup `cleanmgr.exe`, Disk Defragment `dfrgui.exe`, Registry Editor `regedit.exe`.

**Command line:** navigation `cd`, `dir`. Network `ipconfig`, `ping`, `netstat`, `nslookup`, `net use`, `tracert`, `pathping`. Disk `chkdsk`, `format`. Others include `gpupdate` and `sfc`. See Core 2 Part 3 for the full list.

**Malware removal, in order:**
1. Investigate and verify malware symptoms.
2. Quarantine the infected system.
3. Disable System Restore (Windows Home).
4. Remediate infected systems.
5. Update anti-malware software.
6. Scan and use removal techniques (safe mode, preinstallation environment).
7. Reimage or reinstall.
8. Schedule scans and run updates.
9. Enable System Restore and create a restore point (Windows Home).
10. Educate the end user.

**Operational procedures (Parts 14 to 16):** incremental restore = full + every incremental. Differential restore = full + latest differential. 3-2-1 = 3 copies, 2 media types, 1 offsite. Three change types: standard, normal, emergency. Disconnect power first, ESD strap. Chain of custody, order of volatility. SSH 22, RDP 3389, VNC 5900. Hallucination = confident made-up answer.

## The study loop

1. Flashcards daily.
2. Labs for hands-on practice (good PBQ prep).
3. Free practice exam in `exams/core2`, timed.
4. For every miss, find the objective, and rewatch that part.
5. Repeat until you are scoring comfortably above the pass mark.

## Common scenarios

| Scenario | Answer |
|---|---|
| PBQ you don't recognise | Do what you know, flag it, return later |
| 10 minutes left, many unanswered | Answer every one |
| Two answers look right | Re-read for first, best, most likely, next |
| Answer you are unsure of | Mark your best guess, flag it, move on |
| First thing to do on a malware question | Stop it spreading (quarantine) before cleaning |
