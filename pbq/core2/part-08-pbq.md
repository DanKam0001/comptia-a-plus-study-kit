# Core 2, Part 8: Performance-Based Questions

**Part:** Windows Security Settings and Workstation Hardening (objectives 2.2, 2.7)
**Answers:** [part-08-pbq-answers.md](part-08-pbq-answers.md). Do not open it until you have finished both tasks.

The real 220-1202 exam has performance-based questions (PBQs). This kit cannot run a simulator, so each task is done on paper or in a text file. Try it before you look at the cheatsheet. You earn credit for each correct part, so never leave a row blank.

---

## C2P08-PBQ1: What can the user actually do?

| | |
|---|---|
| **Objectives** | 2.2 |
| **Type** | Fill-in (permission calculator) |
| **Time guide** | 6 minutes |

**Scenario.** A shared folder on a Windows PC sits on an NTFS drive and is also shared across the network. NTFS permissions apply to files and folders on the drive. Share permissions apply to the shared folder **over the network only**. When both apply, the **most restrictive** one wins. Use only two levels here: **Full Control** (more access) and **Read** (less access).

**Part A.** Write the permission the user ends up with: **Full Control** or **Read**.

| # | Where the user is | NTFS permission | Share permission | Effective permission |
|---|---|---|---|---|
| 1 | Connecting over the network | Full Control | Read | |
| 2 | Connecting over the network | Read | Full Control | |
| 3 | Connecting over the network | Full Control | Full Control | |
| 4 | Sitting at the PC itself | Full Control | Read | |
| 5 | Sitting at the PC itself | Read | Full Control | |

**Part B.** The file `C:\Projects\plan.docx` has its own permissions. You move it to a new folder. Write which result happens: **Keeps its own permissions** or **Takes the new folder's permissions**.

| # | Move | Result |
|---|---|---|
| 6 | To `C:\Archive` (the same C: volume) | |
| 7 | To `D:\Archive` (a different volume) | |

**Marking.** 7 points: 1 point per row.

---

## C2P08-PBQ2: Set up a contractor and protect the data

| | |
|---|---|
| **Objectives** | 2.2, 2.7 |
| **Type** | Configure this form |
| **Time guide** | 7 minutes |

**Scenario.** A contractor starts on Monday for exactly three months. They only need to run programs and use files. They work Monday to Friday, 9 am to 5 pm. Company policy says guests are never allowed, the built-in administrator account must not be left in its default state, and repeated wrong password guesses must be stopped.

**Part A.** Choose **one option** for each row of the account form.

| Row | Setting | Options | Your choice |
|---|---|---|---|
| 1 | Account type | Standard, Administrator, Guest, Power user | |
| 2 | Account expiration | No expiry, A date at the end of the three months | |
| 3 | Allowed log-in times | Any time, Monday to Friday 9 am to 5 pm | |
| 4 | Failed-attempts lockout | Off, On | |
| 5 | Built-in Guest account | Enabled, Disabled | |
| 6 | Built-in Administrator account | Leave the default name and password, Change the name and password | |

**Part B.** Choose the encryption tool for each job.

| Row | Job | Options | Your choice |
|---|---|---|---|
| 7 | A stolen laptop must not give up any files: encrypt the whole drive. | BitLocker, BitLocker To Go, EFS | |
| 8 | A USB stick holding contractor files must be encrypted. | BitLocker, BitLocker To Go, EFS | |
| 9 | One folder on an NTFS drive must be encrypted for one user account only. | BitLocker, BitLocker To Go, EFS | |

**Marking.** 9 points: 1 point per row.
