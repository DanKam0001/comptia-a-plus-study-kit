# Core 2, Part 3: Performance-Based Questions

**Part:** The Windows Command Line (objective 1.5)
**Answers:** [part-03-pbq-answers.md](part-03-pbq-answers.md). Do not open it until you have finished both tasks.

The real 220-1202 exam has performance-based questions (PBQs). This kit cannot run a simulator, so each task is done on paper or in a text file. Try it before you look at the cheatsheet. You earn credit for each correct part, so never leave a row blank.

---

## C2P03-PBQ1: Wipe and format a USB stick with diskpart

| | |
|---|---|
| **Objectives** | 1.5 |
| **Type** | Ordering |
| **Time guide** | 4 minutes |

**Scenario.** A USB stick is full of old files that have already been backed up and checked. You must erase it and give it one NTFS partition, using Command Prompt. You do not yet know which disk number the stick has. It will turn out to be Disk 1.

**Task.** Put the eight steps in the correct order. Write the letters in order, for example `X Y Z ...`.

**Materials: the steps (shuffled)**

| Letter | Step |
|---|---|
| A | Type `clean` |
| B | Type `exit` |
| C | Type `diskpart` and press Enter |
| D | Type `format fs=ntfs quick` |
| E | Open Command Prompt with **Run as administrator** |
| F | Type `list disk` |
| G | Type `create partition primary` |
| H | Type `select disk 1` (after reading the list and confirming the stick is Disk 1) |

**Marking.** 8 points: 1 point for each step that is in the right position.

---

## C2P03-PBQ2: Pick the exact command

| | |
|---|---|
| **Objectives** | 1.5 |
| **Type** | Configure this form (choose the command for each situation) |
| **Time guide** | 6 minutes |

**Scenario.** Eight help desk tickets are waiting. For each ticket, choose the one command (with its switch) that does the job.

**Task.** Write the letter of your choice in the last column.

| Ticket | Situation | Options | Your letter |
|---|---|---|---|
| 1 | Show the IP address, mask and gateway **and also** the DNS servers and MAC address. | A `ipconfig /all`, B `ipconfig /release`, C `ipconfig /renew`, D `ipconfig /flushdns` | |
| 2 | Give up the current IP address. | A `ipconfig /all`, B `ipconfig /release`, C `ipconfig /renew`, D `ipconfig /flushdns` | |
| 3 | Ask for a new IP address from DHCP. | A `ipconfig /all`, B `ipconfig /release`, C `ipconfig /renew`, D `ipconfig /flushdns` | |
| 4 | Clear the stored DNS answers on this PC. | A `ipconfig /all`, B `ipconfig /release`, C `ipconfig /renew`, D `ipconfig /flushdns` | |
| 5 | List all connections with numbers instead of names, **and** the process ID of each. | A `netstat -a`, B `netstat -an`, C `netstat -ano`, D `netstat -n` | |
| 6 | Check a drive, find bad sectors **and** recover readable data. | A `chkdsk`, B `chkdsk /f`, C `chkdsk /r`, D `sfc /scannow` | |
| 7 | Scan the protected Windows system files and repair damaged ones. | A `chkdsk /r`, B `gpupdate /force`, C `sfc /scannow`, D `format C:` | |
| 8 | Copy the folder tree `C:\Source` to `D:\Backup`, including empty subfolders. Nothing at the destination may be deleted. | A `robocopy C:\Source D:\Backup /MIR`, B `robocopy C:\Source D:\Backup /E`, C `rmdir /s C:\Source`, D `format D:` | |

**Marking.** 8 points: 1 point per ticket.
