# Core 2, Part 8: PBQ answers

Task file: [part-08-pbq.md](part-08-pbq.md). Try the tasks first.

---

## C2P08-PBQ1: What can the user actually do?

**Part A**

| # | Answer | Why |
|---|---|---|
| 1 | Read | Both apply over the network; the most restrictive (Read) wins |
| 2 | Read | Most restrictive wins, and here the NTFS permission is Read |
| 3 | Full Control | Neither permission is more restrictive |
| 4 | Full Control | Share permissions do not apply when sitting at the PC; only NTFS applies |
| 5 | Read | Only NTFS applies at the PC, and it is Read |

**Part B**

| # | Answer | Why |
|---|---|---|
| 6 | Keeps its own permissions | A move inside the same volume keeps the original permissions |
| 7 | Takes the new folder's permissions | Moving to a different volume makes the file inherit the new folder's permissions |

**Partial credit (7 points):** 1 per row. 7 = full marks. 5 to 6 = pass-level, recheck the "when does each apply" rule. 4 or fewer = reread the NTFS vs share permissions section.

---

## C2P08-PBQ2: Set up a contractor and protect the data

**Part A**

| Row | Answer | Why |
|---|---|---|
| 1 | Standard | They only run programs and use files; Administrator and Power user give too much, Guest is banned |
| 2 | A date at the end of the three months | Account expiration dates suit temps and contractors |
| 3 | Monday to Friday 9 am to 5 pm | Restricting log-in times matches their working hours |
| 4 | On | Failed-attempts lockout stops repeated password guessing |
| 5 | Disabled | Disable the Guest account |
| 6 | Change the name and password | Hardening: change the default administrator account name and password |

**Part B**

| Row | Answer | Why |
|---|---|---|
| 7 | BitLocker | Encrypts a whole drive; the answer for a stolen laptop |
| 8 | BitLocker To Go | BitLocker for USB and other removable drives |
| 9 | EFS | Encrypts individual files or folders for one user account, NTFS only |

**Partial credit (9 points):** 1 per row. 8 to 9 = strong. 6 to 7 = pass-level. 5 or fewer = reread the account management and encryption sections.
