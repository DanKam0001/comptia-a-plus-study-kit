# Core 2, Part 3: PBQ answers

Task file: [part-03-pbq.md](part-03-pbq.md). Try the tasks first.

---

## C2P03-PBQ1: Wipe and format a USB stick with diskpart

**Correct order: E, C, F, H, A, G, D, B**

| Position | Step | Why |
|---|---|---|
| 1 | E, Open Command Prompt as administrator | `diskpart` needs administrator rights |
| 2 | C, `diskpart` | Starts the tool; its commands only work inside it |
| 3 | F, `list disk` | Shows the disks so you can confirm which one is the stick |
| 4 | H, `select disk 1` | `clean` works on the selected disk, so select first |
| 5 | A, `clean` | Erases the selected disk. Check the selection before this step |
| 6 | G, `create partition primary` | A cleaned disk has no partition |
| 7 | D, `format fs=ntfs quick` | Formatting needs a partition to format |
| 8 | B, `exit` | Leaves diskpart |

**Partial credit (8 points):** 1 point per step in the right position. 8 = full marks. 6 to 7 = close, recheck which steps depend on which. 5 or fewer = reread the diskpart row in the cheatsheet. Running `clean` on the wrong selected disk would erase the wrong disk, which is why that order matters.

---

## C2P03-PBQ2: Pick the exact command

| Ticket | Answer | Why |
|---|---|---|
| 1 | A, `ipconfig /all` | Plain `ipconfig` omits DNS servers and MAC address; `/all` adds them |
| 2 | B, `ipconfig /release` | Gives up the current address |
| 3 | C, `ipconfig /renew` | Asks for a new address |
| 4 | D, `ipconfig /flushdns` | Clears the DNS cache |
| 5 | C, `netstat -ano` | `-a` all, `-n` numbers, `-o` adds the process ID |
| 6 | C, `chkdsk /r` | `/r` also finds bad sectors and recovers readable data (it includes `/f`); plain `chkdsk` only reports |
| 7 | C, `sfc /scannow` | System File Checker repairs protected Windows files. `chkdsk` checks the drive, not Windows files |
| 8 | B, `robocopy ... /E` | `/E` copies subfolders including empty ones. `/MIR` would delete extra files at the destination |

**Partial credit (8 points):** 1 per ticket. 7 to 8 = strong. 5 to 6 = reread the switches table in memorize.md. 4 or fewer = redo the Part 3 lab.
