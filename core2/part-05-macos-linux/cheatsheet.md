# Core 2, Part 5: macOS and Linux for Windows People

**Objectives 1.8 and 1.9** (220-1202): *1.8 Explain common features and tools of the macOS/desktop operating system. 1.9 Identify common features and tools of the Linux client/desktop operating system.*
Domain: Operating Systems (28% of the exam).

# Part A: macOS (objective 1.8)

## Desktop features and their Windows twins

| macOS feature | Windows twin | What it does |
|---|---|---|
| Finder | File Explorer | Browse files and folders |
| Dock | Taskbar | Bar of apps along the bottom (or side) of the screen |
| Spotlight | Start menu search | Search apps, files and the web. **Command + Space** |
| Mission Control | Task View | Shows all open windows and desktops at once |
| Multiple desktops (Spaces) | Virtual desktops | Several desktops, switch with a gesture or Mission Control |
| Gestures | Touchpad gestures | Trackpad swipes, for example a three or four finger swipe left or right between desktops |
| Keychain | Credential Manager / password manager | Stores passwords and certificates |
| iCloud | OneDrive | Online storage and sync: **iCloud Drive**, **iMessage**, **FaceTime** |
| Continuity | (none) | A Mac and an iPhone work together (hand off tasks, share clipboard, answer calls) |
| Apple ID | Microsoft account | Signs in to the App Store and iCloud. Companies can **restrict** it on managed Macs (for example through MDM) |

## Installing and uninstalling apps

| File type | What it is | How to use it |
|---|---|---|
| **App Store** | Apple's official app shop | Click Get. Safest source |
| **.dmg** | Disk image, a file that opens like a virtual disk | Open it, **drag the app into the Applications folder**, then eject the disk |
| **.pkg** | Installer package | Opens a step by step installer wizard (may ask for an admin password) |
| **.app** | The application itself | Drag to Applications. Double click to run |

**Uninstall:** drag the app to the **Trash**, then empty it. Some apps leave settings behind in a Library folder.

## System folders

| Folder | Holds |
|---|---|
| `/Applications` | Installed apps |
| `/Users` | One home folder per user |
| `/Library` | Settings and support files for **all** users |
| `/System` | macOS itself. Protected |
| `/Users/<name>/Library` | That user's own settings and support files (hidden by default) |

## Tools and features

| Tool | Job |
|---|---|
| **Disk Utility** | Check and repair (First Aid), erase and format drives |
| **FileVault** | Encrypts the whole startup drive so a stolen Mac can't be read |
| **Time Machine** | Automatic backups to an external drive, restore older versions of files |
| **Terminal** | The command line (zsh by default on modern macOS) |
| **Force Quit** | End a frozen app: **Option + Command + Esc**, or Apple menu, Force Quit |
| **System Settings** | Displays, Network, Printers and Scanners, Privacy and Security, Accessibility, Time Machine (under General on recent macOS) |

## Best practices

- **Backups** with Time Machine. **Antivirus** is still recommended. **Updates and patches** keep it secure.
- **Rapid Security Response (RSR):** small urgent security fixes delivered between full macOS updates (introduced in macOS 13 Ventura; Apple has since replaced it with Background Security Improvements, but the exam still lists RSR).

# Part B: Linux (objective 1.9)

## OS components

| Component | Job |
|---|---|
| **Kernel** | The core. Talks to the hardware |
| **Bootloader** | Starts the kernel at power on (GRUB is common) |
| **systemd** | The first process: starts and manages services |
| **Root account** | The all powerful administrator. Don't sign in as root, use `sudo` |

## Commands

### File management

| Command | Job |
|---|---|
| `ls` | List a folder |
| `pwd` | Print working directory (where am I) |
| `mv` | Move or rename |
| `cp` | Copy |
| `rm` | Remove. **No recycle bin**. `rm -r` removes a folder and everything in it |
| `chmod` | Change permissions. r = 4, w = 2, x = 1. `chmod 755` = owner rwx, group r-x, others r-x. `chmod 644` = owner rw-, group r--, others r-- |
| `chown` | Change owner: `chown user file` |
| `grep` | Search inside files for text |
| `find` | Search for files by name and more |

### Filesystem management

| Command | Job |
|---|---|
| `fsck` | Check a filesystem for errors (like chkdsk). Run on an unmounted drive |
| `mount` | Attach a drive to the folder tree |

### Administrative

| Command | Job |
|---|---|
| `su` | Switch user (for example to root) |
| `sudo` | Run one command with root rights |

### Package management

| Command | Distribution family |
|---|---|
| `apt` | Debian, Ubuntu. `sudo apt update`, `sudo apt install name` |
| `dnf` | Fedora, Red Hat. `sudo dnf install name` |

### Network

| Command | Job |
|---|---|
| `ip` | Show and set addresses (`ip a`). Replaces older ifconfig |
| `ping` | Test a host. On Linux it keeps going until Ctrl + C |
| `curl` | Fetch a web page or file from the command line |
| `dig` | DNS lookup (like nslookup) |
| `traceroute` | Show every hop (like tracert) |

### Informational

| Command | Job |
|---|---|
| `man` | Open the manual for a command |
| `cat` | Print a file on the screen |
| `top` | Live list of processes (like Task Manager) |
| `ps` | List running processes |
| `du` | Disk usage of files and folders |
| `df` | Free space on mounted drives |

### Text editor

`nano`: a simple terminal editor. **Ctrl + O** saves, **Ctrl + X** exits.

## Common configuration files

| File | Holds |
|---|---|
| `/etc/passwd` | User accounts (no passwords) |
| `/etc/shadow` | Scrambled (hashed) passwords. Only root can read it |
| `/etc/hosts` | Name to IP address map |
| `/etc/fstab` | Which drives to mount at startup |
| `/etc/resolv.conf` | DNS servers |

## Windows to macOS to Linux

| Job | Windows | macOS | Linux |
|---|---|---|---|
| Force close an app | End task in Task Manager | Force Quit | `kill`, or end it in `top` |
| Live process list | Task Manager | Activity Monitor | `top` |
| See IP address | `ipconfig` | System Settings, Network | `ip a` |
| Check a drive | `chkdsk` | Disk Utility First Aid | `fsck` |
| Backup | File History / Backup | Time Machine | Many tools |
| Encrypt the drive | BitLocker | FileVault | Often LUKS |
| Run as admin | Run as administrator | Admin password | `sudo` |

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Mac app frozen | Force Quit (Option + Command + Esc) |
| Mac backup to external drive | Time Machine |
| Install an app from a .dmg | Drag the app to Applications |
| Stolen Mac must be unreadable | FileVault |
| Mac drive errors | Disk Utility, First Aid |
| Install a program on Ubuntu | `sudo apt install name` |
| Need to change who can run a file | `chmod` |
| Where do Linux accounts live | `/etc/passwd` (passwords in `/etc/shadow`) |
| Which Linux command is Task Manager | `top` |
