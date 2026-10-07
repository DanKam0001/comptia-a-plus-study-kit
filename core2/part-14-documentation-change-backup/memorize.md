# Memorise list: Documentation, Change Management, Backup and Recovery (Core 2, Part 14)

Understand the video first, then learn these cold. They're the facts a scenario question assumes you already know.
Flashcards: [`flashcards/core2_part14.csv`](../../flashcards/core2_part14.csv) (import into Anki or any flashcard app).

## Tickets and documents

| Question | Answer |
|---|---|
| Fields in a good ticket | User info, device info, description, category, severity, escalation level |
| Three parts of good written notes | Issue description, progress notes, issue resolution |
| What does CMDB stand for? | Configuration Management Database |
| What is an asset tag for? | A unique ID on a device that matches its record |
| Procurement life cycle in one line | Buy, use, retire |
| SOP stands for / is | Standard Operating Procedure: step by step instructions for a routine job |
| SLA stands for / is | Service-Level Agreement: a promise about response and fix times (internal or external) |
| Onboarding vs off-boarding checklist | Onboarding sets up a new user. Off-boarding removes a leaver's access and collects equipment |

## Change management

| Question | Answer |
|---|---|
| Three change types | Standard (routine, pre-approved), normal (full approval), emergency (urgent, still documented) |
| Maintenance window | A planned quiet time for making changes |
| Change freeze | A period when no changes are allowed |
| Four safety nets before a change | Rollback plan, backup plan, sandbox testing, responsible staff |
| Order after approval | Implementation, peer review, end-user acceptance |
| Who approves a normal change? | The change board |

## Backups

| Question | Answer |
|---|---|
| Full backup | Copies everything |
| Incremental backup | Copies changes since the last backup of any kind |
| Differential backup | Copies changes since the last full backup |
| Synthetic full | New full built on the backup server from the old full plus later changes |
| Restore from incrementals needs | The last full + every incremental since |
| Restore from a differential needs | The last full + the latest differential only |
| In-place restore vs alternative location | In-place overwrites the original. Alternative puts the files somewhere else |
| 3-2-1 rule | 3 copies, 2 media types, 1 offsite |
| GFS | Grandfather (monthly), father (weekly), son (daily) |
| Why test backups? | A backup that has never been restored might not work |
