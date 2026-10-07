# Core 2, Part 5: PBQ answers

Task file: [part-05-pbq.md](part-05-pbq.md). Try the tasks first.

---

## C2P05-PBQ1: Learn your way around a Mac

| # | Answer | Why |
|---|---|---|
| 1 | G, Keychain | Stores passwords and certificates |
| 2 | F, Force Quit | Option + Command + Esc ends a frozen app |
| 3 | I, Spotlight | Command + Space searches apps, files and the web |
| 4 | J, Time Machine | Automatic backups to an external drive, with older versions restorable |
| 5 | K, .dmg file | A disk image: open it, drag the app into Applications, eject the disk |
| 6 | E, FileVault | Encrypts the whole startup drive |
| 7 | A, Dock | The Mac's taskbar equivalent |
| 8 | H, Mission Control | Shows all open windows and desktops at once |
| 9 | L, .pkg file | An installer package that runs a step-by-step wizard |
| 10 | D, Disk Utility | First Aid checks and repairs; also erases and formats drives |

Not used: B (Finder browses files and folders) and C (Continuity makes a Mac and iPhone work together).

**Partial credit (10 points):** 1 per match. 9 to 10 = strong. 7 to 8 = pass-level. 6 or fewer = reread Part A of the cheatsheet.

---

## C2P05-PBQ2: The Linux admin sheet

**Part A**

| # | Answer | Why |
|---|---|---|
| 1 | `750` | rwx = 4+2+1 = 7, r-x = 4+1 = 5, --- = 0 |
| 2 | `664` | rw- = 4+2 = 6, rw- = 6, r-- = 4 |
| 3 | `700` | rwx = 7, then 0 and 0 |
| 4 | `444` | r-- = 4 for each of the three groups |
| 5 | owner `rw-`, group `r--`, others `---` | 6 = 4+2 (rw-), 4 = r--, 0 = nothing |
| 6 | owner `rwx`, group `r-x`, others `r-x` | 7 = rwx, 5 = r-x, 5 = r-x |

**Part B**

| # | Answer | Why |
|---|---|---|
| 7 | D, `/etc/resolv.conf` | Lists DNS servers |
| 8 | E, `/etc/shadow` | Hashed passwords; only root can read it |
| 9 | B, `/etc/hosts` | Name to IP address map |
| 10 | C, `/etc/passwd` | User accounts, no passwords |
| 11 | A, `/etc/fstab` | Which drives to mount at startup |

**Partial credit (11 points):** 1 per row (rows 5 and 6 need all three groups right). 10 to 11 = strong. 8 to 9 = pass-level. 7 or fewer = reread the `chmod` row and the configuration files table.
