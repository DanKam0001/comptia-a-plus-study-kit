# Core 2, Part 14: Documentation, Change Management, Backup and Recovery

**Objectives 4.1, 4.2 and 4.3** (220-1202):
- 4.1 *Given a scenario, implement best practices associated with documentation and support systems information management.*
- 4.2 *Given a scenario, apply change management procedures.*
- 4.3 *Given a scenario, implement workstation backup and recovery methods.*

Domain: Operational Procedures (21% of the exam).

## 4.1 Documentation and support systems

### Ticketing systems

A **ticket** is the record of one request for help. A good ticket holds:

| Field | What it is |
|---|---|
| User information | Who reported it and how to reach them |
| Device information | Which machine (name, asset tag, model) |
| Description of the issue | What is wrong, in the user's words and yours |
| Categories | Type of problem (hardware, software, network, account...) |
| Severity | How urgent or damaging it is |
| Escalation levels | Who it goes to next if the current level cannot fix it |

**Clear, concise written communication** means three things in the notes: the **issue description**, the **progress notes** (what you tried, in order), and the **issue resolution** (what finally fixed it).

### Asset management

- **Inventory lists**: a list of everything the company owns.
- **Asset tags and IDs**: a unique sticker or number on each device, matching its record.
- **Configuration management database (CMDB)**: the database that stores the records and how assets relate.
- **Procurement life cycle**: buying a device, using it, then retiring it.
- **Warranty and licensing**: when cover or licenses end.
- **Assigned users**: who has which device.

### Types of documents

| Document | Purpose |
|---|---|
| Incident report | What happened and what was done |
| Standard operating procedure (SOP) | Step by step instructions for a routine job. Example: the software package custom installation procedure |
| New user / onboarding setup checklist | Everything to set up for a new starter |
| User off-boarding checklist | Remove access and collect equipment from a leaver |
| Service-level agreement (SLA) | A promise about response and fix times. **Internal** (between teams) or **external / third-party** (an outside company) |
| Knowledge base / articles | Written fixes and how-tos so problems are solved once |

## 4.2 Change management

### Documented business processes

- **Rollback plan**: how to undo the change.
- **Backup plan**: how data will be restored if needed.
- **Sandbox testing**: try the change on a safe copy first.
- **Responsible staff members**: named people who own the change.

### The change request

- **Request forms** carry: **purpose of the change**, **scope of the change**, **change type**, **date and time**, **affected systems / impact**, **risk analysis** (with a **risk level**).
- **Change types:** **standard** (routine, pre-approved), **normal** (goes through the full approval process), **emergency** (urgent fix, still documented).
- **Date and time:** a **maintenance window** is a planned quiet time for changes. A **change freeze** is a period when no changes are allowed.
- **Change board approvals**: a group approves or rejects the request.
- **Implementation**, then **peer review**, then **end-user acceptance**.

## 4.3 Backup and recovery

### Backup types

| Type | Copies | To restore you need |
|---|---|---|
| Full | Everything | Just that full backup |
| Incremental | Changes since the last backup of any kind | Last full + **every** incremental since |
| Differential | Changes since the last **full** backup | Last full + the **latest** differential |
| Synthetic full | Built on the backup server from the old full plus later changes (no new load on the PC) | That synthetic full |

Backup speed: incremental is quickest to take, slowest to restore. Full is slowest to take, quickest to restore.

### Recovery

- **In-place / overwrite**: restore over the original location, replacing what is there.
- **Alternative location**: restore somewhere else (to compare, or when the original is damaged).
- **Backup testing**: test restores on a regular **frequency**. An untested backup is not a backup.

### Rotation schemes

- **Onsite vs offsite**: onsite restores fast, offsite survives a fire or flood.
- **Grandfather-father-son (GFS)**: daily backups are the sons, weekly the fathers, monthly the grandfathers.
- **3-2-1 backup rule**: **3** copies of the data, on **2** different types of media, with **1** copy offsite.

## Common scenarios

| Scenario | Answer |
|---|---|
| Same fault returns, nobody knows what was tried | Poor ticket notes. Record issue, progress, resolution |
| Risky update on a live server mid-day | Change request, risk analysis, approval, rollback plan, maintenance window |
| Drive dies Thursday, full Sunday, incremental nightly | Restore Sunday's full, then Monday, Tuesday and Wednesday incrementals |
| Same, but differential nightly | Sunday's full, then only Wednesday's differential |
| Server must be fixed at once, no time for the board | Emergency change, documented |
| Which backup has the fastest restore? | Full |
