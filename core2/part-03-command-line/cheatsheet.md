# Core 2, Part 3: The Windows Command Line

**Objective 1.5** (220-1202): *Given a scenario, use the appropriate Microsoft command-line tools.*
Domain: Operating Systems (28% of the exam).

Open **Command Prompt** from the Start menu (type `cmd`). Tools that change the system need **Run as administrator** (right click, Run as administrator). A **switch** is an option added after a command, usually starting with `/`. Help for any command: `command /?`.

## Navigation

| Command | Job |
|---|---|
| `cd` | Change directory (folder). `cd ..` goes up one level. `cd \` goes to the top of the drive |
| `dir` | List the files and folders in the current folder. `dir /a` includes hidden items |

To change drive, just type the drive letter and a colon, for example `D:`.

## Network

| Command | Job | Useful forms |
|---|---|---|
| `ipconfig` | Show IP address, subnet mask and default gateway | `/all` (adds DNS servers, MAC address, DHCP info), `/release` (give up the address), `/renew` (ask for a new one), `/flushdns` (clear the DNS cache) |
| `ping` | Send test messages and time the replies. Tests whether a host answers | `ping -t` keeps going until Ctrl + C. `ping 127.0.0.1` (loopback) tests your own network software |
| `netstat` | List active connections and listening ports | `-a` all, `-n` numbers instead of names, `-o` adds the process ID, `-b` shows the program (administrator) |
| `nslookup` | Ask a DNS server to turn a name into an IP address (and back) | `nslookup example.com` |
| `net use` | Connect to or disconnect from a shared folder, giving it a drive letter | `net use Z: \\server\share`, `net use Z: /delete` |
| `tracert` | Show every router (hop) between you and a destination | `tracert example.com` |
| `pathping` | Ping plus tracert in one: shows each hop and the packet loss at each | Slow, it takes a while to gather statistics |

## Disk management

| Command | Job |
|---|---|
| `chkdsk` | Check a disk for errors. `/f` fixes errors, `/r` also finds bad sectors and recovers readable data (includes `/f`). If the drive is in use it offers to run at next restart |
| `format` | Wipe a drive and set up a file system, for example `format D: /FS:NTFS`. **Erases everything** |
| `diskpart` | Command-line version of Disk Management. Inside it: `list disk`, `select disk 1`, `clean` (erases the disk), `create partition primary`, `format fs=ntfs quick`, `assign letter=E`, `exit`. **Check the selected disk before `clean`** |

## File management

| Command | Job |
|---|---|
| `md` (or `mkdir`) | Make a new directory |
| `rmdir` (or `rd`) | Remove a directory. `/s` removes everything inside it too, `/q` is quiet (no prompts) |
| `robocopy` | Robust file copy: copy a folder tree reliably. `robocopy C:\Source D:\Backup /E` copies subfolders including empty ones. `/MIR` mirrors, **deleting files at the destination that aren't in the source**. `/Z` is restartable mode (resumes after an interrupted copy) |

## Informational

| Command | Job |
|---|---|
| `hostname` | Show the computer's name |
| `net user` | List local user accounts. `net user name /add` creates one, `net user name *` sets a password (administrator) |
| `winver` | Open a small window showing the Windows version and build |
| `whoami` | Show the account you are signed in as. `whoami /groups` lists group memberships |
| `[command name] /?` | Built-in help for any command |

## OS management

| Command | Job |
|---|---|
| `gpupdate` | Re-apply Group Policy now. `/force` re-applies everything |
| `gpresult` | Show which Group Policy settings actually applied. `/r` prints a summary, `/h file.html` makes a report |
| `sfc` | System File Checker. `sfc /scannow` scans protected Windows files and repairs damaged ones. Run as administrator |

## Exam traps

- `chkdsk` checks the **drive**. `sfc` checks **Windows system files**.
- `format` and `diskpart clean` destroy data.
- `ping` says whether one place answers. `tracert` shows every hop. `pathping` adds loss per hop.
- `ipconfig` is Windows. Linux uses `ip` (Core 2 Part 5).
- Many tools (`sfc`, `diskpart`, `chkdsk /f`, `netstat -b`) need an administrator Command Prompt.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Need the IP address, mask and gateway | `ipconfig` (add `/all` for DNS) |
| Computer has an old address after moving networks | `ipconfig /release` then `/renew` |
| Website name won't resolve but IP works | `nslookup`, then `ipconfig /flushdns` |
| Where does traffic stop on the way to a site? | `tracert` or `pathping` |
| Which program is using a port? | `netstat -ano` |
| Windows errors, suspect damaged system files | `sfc /scannow` (administrator) |
| Drive shows read errors | `chkdsk /r` |
| Copy a big folder reliably | `robocopy ... /E` |
| Policy change not applied yet | `gpupdate /force`, then `gpresult /r` |
| Map a share to a letter from the command line | `net use Z: \\server\share` |
