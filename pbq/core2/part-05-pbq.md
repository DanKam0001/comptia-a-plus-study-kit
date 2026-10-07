# Core 2, Part 5: Performance-Based Questions

**Part:** macOS and Linux for Windows People (objectives 1.8, 1.9)
**Answers:** [part-05-pbq-answers.md](part-05-pbq-answers.md). Do not open it until you have finished both tasks.

The real 220-1202 exam has performance-based questions (PBQs). This kit cannot run a simulator, so each task is done on paper or in a text file. Try it before you look at the cheatsheet. You earn credit for each correct part, so never leave a row blank.

---

## C2P05-PBQ1: Learn your way around a Mac

| | |
|---|---|
| **Objectives** | 1.8 |
| **Type** | Matching |
| **Time guide** | 6 minutes |

**Scenario.** A new employee has moved from Windows to a Mac and asks you ten "what is the Mac version of this?" questions.

**Task.** Match each description (1 to 10) to **one** term (A to L). Each term is used **at most once**, and two are not needed.

**Materials: terms**

| Letter | Term |
|---|---|
| A | Dock |
| B | Finder |
| C | Continuity |
| D | Disk Utility |
| E | FileVault |
| F | Force Quit |
| G | Keychain |
| H | Mission Control |
| I | Spotlight |
| J | Time Machine |
| K | .dmg file |
| L | .pkg file |

**Descriptions**

1. Stores passwords and certificates.
2. Ends a frozen app. The shortcut is Option + Command + Esc.
3. Searches apps, files and the web. The shortcut is Command + Space.
4. Backs up automatically to an external drive and restores older versions of files.
5. A disk image. You open it, then drag the app into the Applications folder.
6. Encrypts the whole startup drive so a stolen Mac cannot be read.
7. The bar of apps along the bottom (or side) of the screen.
8. Shows all open windows and desktops at once.
9. An installer package that opens a step-by-step installer wizard.
10. Checks and repairs (First Aid), erases and formats drives.

**Marking.** 10 points: 1 point per correct match.

---

## C2P05-PBQ2: The Linux admin sheet

| | |
|---|---|
| **Objectives** | 1.9 |
| **Type** | Fill-in (permission numbers, then file paths) |
| **Time guide** | 7 minutes |

**Scenario.** You are setting up files on a Linux server. In `chmod`, each permission has a value: **r = 4, w = 2, x = 1**. You add the values for the owner, the group and others, giving three digits (for example `chmod 755` means owner rwx, group r-x, others r-x).

**Part A.** Write the three-digit number for each, or the nine-letter permission string for each number.

| # | Permissions | Your answer |
|---|---|---|
| 1 | owner `rwx`, group `r-x`, others `---` | `chmod` ______ |
| 2 | owner `rw-`, group `rw-`, others `r--` | `chmod` ______ |
| 3 | owner `rwx`, group `---`, others `---` | `chmod` ______ |
| 4 | everyone read only: `r--r--r--` | `chmod` ______ |
| 5 | `chmod 640` | owner ____, group ____, others ____ |
| 6 | `chmod 755` | owner ____, group ____, others ____ |

**Part B.** Choose the file (A to E) for each job. Each file is used exactly once.

| Letter | File |
|---|---|
| A | `/etc/fstab` |
| B | `/etc/hosts` |
| C | `/etc/passwd` |
| D | `/etc/resolv.conf` |
| E | `/etc/shadow` |

| # | Job | Letter |
|---|---|---|
| 7 | Lists the DNS servers the computer uses. | |
| 8 | Holds the scrambled (hashed) passwords. Only root can read it. | |
| 9 | A local map from names to IP addresses. | |
| 10 | Lists the user accounts, with no passwords in it. | |
| 11 | Says which drives to mount at startup. | |

**Marking.** 11 points: 1 point per row. Row 5 and row 6 need all three groups right.
