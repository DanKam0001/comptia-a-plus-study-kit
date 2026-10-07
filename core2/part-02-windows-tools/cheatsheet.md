# Core 2, Part 2: Windows Tools: Task Manager, MMC Snap-ins, Settings

**Objectives 1.4 and 1.6** (220-1202): *1.4 Given a scenario, use Microsoft Windows operating system features and tools. 1.6 Given a scenario, configure Microsoft Windows settings.*
Domain: Operating Systems (28% of the exam).

Core 2 Part 1 covered the Windows editions. Two tools below (Group Policy Editor and Local Users and Groups) are missing from **Home**.

## Task Manager (Ctrl + Shift + Esc)

| Tab | What it does |
|---|---|
| Processes | Every running program with its CPU, memory, disk and network use. Select one, then **End task** to close a frozen or greedy program |
| Performance | Live graphs: CPU, memory, disk, network, GPU |
| Users | Who is signed in and what each user is using |
| Startup | Programs that launch at sign in. Disable the ones you don't need to speed up boot |
| Services | Background programs. Start, stop or restart a service from here |

(Task Manager also has App history and Details tabs. They are not on the objectives list.)

## MMC snap-ins

The **Microsoft Management Console (MMC)** is a frame that holds tools called **snap-ins**. Open any of them with **Windows key + R** (the Run box), type the file name, press Enter.

| Snap-in | File name | Job |
|---|---|---|
| Event Viewer | `eventvwr.msc` | Logs of what happened: **Application** (program errors), **System** (Windows and driver events), **Security** (sign ins and audits) |
| Disk Management | `diskmgmt.msc` | Initialize a new disk (GPT or MBR), create/extend/shrink volumes, format, change drive letters |
| Task Scheduler | `taskschd.msc` | Run a program or script automatically at a time or event |
| Device Manager | `devmgmt.msc` | List hardware. Update, roll back, disable or uninstall a driver. **Yellow warning triangle** = driver problem |
| Certificate Manager | `certmgr.msc` | View and manage digital certificates (identity proofs) for the current user |
| Local Users and Groups | `lusrmgr.msc` | Create and manage local accounts and groups. **Not in Home** |
| Performance Monitor | `perfmon.msc` | Record detailed counters over time (CPU, memory, disk) |
| Group Policy Editor | `gpedit.msc` | Change security and system rules on this computer. **Not in Home** |

## Additional tools

| Tool | File name | Job |
|---|---|---|
| System Information | `msinfo32.exe` | Full report on hardware, drivers, BIOS mode, Secure Boot state |
| Resource Monitor | `resmon.exe` | Detailed live view of which process is using CPU, memory, disk and network |
| System Configuration | `msconfig.exe` | Control how Windows starts: boot options (such as safe boot) and which services load |
| Disk Cleanup | `cleanmgr.exe` | Delete temporary files, recycle bin contents and other junk |
| Disk Defragment | `dfrgui.exe` | Tidy a **hard drive** so each file sits in one piece. Do not manually defragment an SSD (Windows optimizes it with TRIM instead) |
| Registry Editor | `regedit.exe` | Edit the registry, Windows' database of deep settings. **Back up first** (File, Export). One wrong change can break Windows |

## Control Panel and Settings items (objective 1.6)

| Item | What it is for |
|---|---|
| Internet Options | Browser settings: home page, security zones, proxy, certificates |
| Devices and Printers | Connected devices, add and manage printers |
| Programs and Features | Uninstall or repair installed software, turn Windows features on or off |
| Network and Sharing Center | See and change your network connection, adapters, sharing settings |
| System | Edition, RAM, computer name, remote settings, system protection |
| Windows Defender Firewall | Allow apps through, turn the firewall on or off |
| Mail | Outlook mail profiles |
| Sound | Playback and recording devices, volume, default device |
| Device Manager | (see above) |
| Indexing Options | Which folders and file types Windows includes in search |
| Administrative Tools | A folder of the management consoles above |

### File Explorer Options

- **General**: where File Explorer opens, single or double click, privacy.
- **View**: **Show hidden files, folders and drives**, and **Hide extensions for known file types** (untick it to see extensions, which helps you spot a fake file like `photo.jpg.exe`).
- **Search**: how searches behave.

### Power Options

| Item | Meaning |
|---|---|
| Power plans | Balanced (default), Power saver, High performance |
| Sleep / suspend / standby | Low power, work kept in RAM, wakes in seconds. Uses a little power |
| Hibernate | Work saved to the drive, then fully off. Uses no power, slower to resume |
| Choose what closing the lid does | Do nothing, sleep, hibernate or shut down (separately on battery and plugged in) |
| Fast startup | A normal shutdown saves the Windows kernel to disk so the next boot is quicker |
| USB selective suspend | Windows powers down idle USB ports to save energy. Can cause a USB device to "disappear" if it is too aggressive |

### The Settings app (Windows key + I)

System, Devices, Network and Internet, Personalization, Apps, Accounts, Time and Language, Gaming, Ease of Access, Privacy, Update and Security. Rough guide:

| Category | Contains |
|---|---|
| System | Display, sound, notifications, power, storage |
| Devices | Bluetooth, printers, mouse, typing |
| Network and Internet | Wi-Fi, Ethernet, VPN, proxy, airplane mode |
| Personalization | Background, colors, themes, lock screen |
| Apps | Installed apps, default apps, startup apps |
| Accounts | Your info, sign in options, work or school accounts |
| Time and Language | Date, time, region, language |
| Gaming | Game Bar and Game Mode |
| Ease of Access | Magnifier, narrator, high contrast |
| Privacy | What apps may use (camera, microphone, location) |
| Update and Security | Windows Update, backup, recovery, Windows Security |

(Windows 11 renames some of these, for example "Privacy and security" and "Accessibility". The exam lists the names above.)

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Computer slow, one program using all the memory | Task Manager, Processes tab, End task |
| Program crashing, need the error | Event Viewer, Application log |
| New drive not in File Explorer | Disk Management: initialize, new volume, drive letter |
| Device has a yellow triangle | Device Manager: update or roll back the driver |
| Too many programs start at sign in | Task Manager Startup tab, or Apps then Startup in Settings |
| Need a script to run every night | Task Scheduler |
| Which process is hammering the disk? | Resource Monitor |
| Need to see Secure Boot state or BIOS mode | System Information |
| Laptop should keep working with the lid closed | Power Options, "Choose what closing the lid does" |
| Group Policy Editor is missing | The PC runs Windows Home |
