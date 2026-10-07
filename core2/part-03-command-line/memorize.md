# Memorise list: The Windows Command Line (Core 2, Part 3)

Understand the video first, then learn these cold. They're the facts a scenario question assumes you already know.
Flashcards: [`flashcards/core2_part03.csv`](../../flashcards/core2_part03.csv) (import into Anki or any flashcard app).

## One job each

| Command | Job in one line |
|---|---|
| cd | Change directory |
| dir | List folder contents |
| ipconfig | Show IP address, mask, gateway |
| ping | Test whether a host answers |
| netstat | List connections and listening ports |
| nslookup | Look up a name in DNS |
| net use | Map or disconnect a network drive |
| tracert | Show every hop to a destination |
| pathping | Ping + tracert with loss per hop |
| chkdsk | Check a drive for errors |
| format | Wipe a drive and set up a file system |
| diskpart | Command-line disk and partition tool |
| md | Make a directory |
| rmdir | Remove a directory |
| robocopy | Robust folder copy |
| hostname | Show the computer name |
| net user | List or manage local accounts |
| winver | Show Windows version and build |
| whoami | Show the current user |
| gpupdate | Re-apply Group Policy |
| gpresult | Show which policies applied |
| sfc | Scan and repair system files |
| command /? | Help |

## Switches

| Question | Answer |
|---|---|
| Show full network details including DNS | `ipconfig /all` |
| Give up the current IP address / get a new one | `ipconfig /release` / `ipconfig /renew` |
| Clear the DNS cache | `ipconfig /flushdns` |
| Ping forever until Ctrl + C | `ping -t` |
| Loopback address to test your own network software | 127.0.0.1 |
| Show connections with process IDs, numeric | `netstat -ano` |
| Fix disk errors / also find bad sectors | `chkdsk /f` / `chkdsk /r` |
| Repair system files | `sfc /scannow` (administrator) |
| Copy folder with subfolders | `robocopy source dest /E` |
| Mirror a folder (also deletes extras at destination) | `robocopy source dest /MIR` |
| Remove a folder and everything in it | `rmdir /s` |
| Re-apply all Group Policy | `gpupdate /force` |
| Summary of applied policies | `gpresult /r` |
| Map drive Z: to a share | `net use Z: \\server\share` |

## Traps

| Question | Answer |
|---|---|
| chkdsk vs sfc | chkdsk = the drive. sfc = Windows files |
| ping vs tracert | ping = does it answer. tracert = every hop |
| Windows ipconfig equivalent on Linux | `ip` |
| Which command-line tools need an administrator prompt | sfc, diskpart, chkdsk /f, netstat -b |
