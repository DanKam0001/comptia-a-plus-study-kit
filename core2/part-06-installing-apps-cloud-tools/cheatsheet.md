# Core 2, Part 6: Installing Apps and Cloud Productivity Tools

**Objectives 1.10 and 1.11** (220-1202):
- 1.10: *Given a scenario, install applications according to requirements.*
- 1.11: *Given a scenario, install and configure cloud-based productivity tools.*

Domain: Operating Systems (28% of the exam).

## 1.10 System requirements for applications

Check these **before** installing anything:

| Requirement | What to check |
|---|---|
| 32-bit vs 64-bit | A 64-bit app needs a 64-bit OS. A 32-bit app usually runs on both 32-bit and 64-bit Windows. A 32-bit OS can use only about 4 GB of RAM |
| Dedicated vs integrated graphics | Dedicated = a separate card with its own memory. Integrated = built into the CPU, shares system RAM. Games, 3D and video editing want dedicated |
| VRAM | Video RAM on a dedicated card. Apps list a minimum |
| RAM | Minimum and recommended RAM, plus what else is running |
| CPU | Minimum speed and number of cores, and whether the architecture (x64 or ARM) is supported |
| External hardware tokens | A small USB key (a dongle) that proves you own a license. The app will not run without it plugged in |
| Storage | Free disk space for the install **and** for the data it creates. An SSD helps speed |
| Application-to-OS compatibility | Is the app built for this OS and this version (Windows 10 vs 11, Windows vs macOS vs Linux)? |

Core 1 Part 2 (RAM) and Part 3 (Storage) cover the hardware side of these numbers.

## 1.10 Distribution methods

| Method | What it is |
|---|---|
| Physical media | A disc (or other drive) you install from. Needs a drive that can read it |
| Mountable ISO file | One file holding a copy of a disc. Windows can **mount** it as a virtual drive (double-click or right-click > Mount), so no real disc or disc drive is needed |
| Downloadable package | A file you download and run (for example an installer file) |
| Image deployment | One prepared system image, with the OS and apps already inside, copied to many computers at once. Used by IT for rollouts |

## 1.10 Impact considerations for new applications

| Impact on | Questions to ask |
|---|---|
| **Device** | Storage used? Slows the machine? Needs more RAM or a better GPU? |
| **Network** | Large downloads or constant syncing? Bandwidth during work hours? |
| **Operation** | Does it change how people work? Training needed? Does it work with other apps? |
| **Business** | Cost, licensing, support, risk, does it break any rules? |

Good habit: test on a few computers first (a pilot), then roll out to everyone.

## 1.11 Cloud-based productivity tools

**Email systems**
- Cloud email lives on the provider's servers, so any device can reach it.
- Examples: Outlook with Microsoft 365, Gmail.
- Related ports (see Core 1 Part 7): SMTP sends mail (25, or 587 for submission), POP3 downloads (110, or 995 secure), IMAP syncs (143, or 993 secure).

**Storage**
- Cloud storage keeps files online and **syncs** them to your devices. Examples: OneDrive, Google Drive, Dropbox.
- **Sync/folder settings:** choose which folders sync; choose online-only files versus kept on the device; watch for **conflict copies** when two people edit the same file.

**Collaboration tools**

| Type | Examples |
|---|---|
| Word processing | Word, Google Docs |
| Spreadsheets | Excel, Google Sheets |
| Presentation tools | PowerPoint, Google Slides |
| Videoconferencing | Teams, Zoom |
| Instant messaging | Teams, Slack |

Several people can edit one file at the same time in a browser.

**Identity synchronization**
- Keeps one set of sign-in details the same between the on-premises directory (such as Active Directory) and the cloud, so a user has one account and one password everywhere.

**Licensing assignment**
- Cloud apps are paid per user. An admin must **assign a license** to each user's account. Account but no license = apps stay locked (or show "no license").

## Common scenarios

| Symptom | Likely answer |
|---|---|
| 64-bit program will not install on this PC | PC is running a 32-bit OS |
| Program is on a disc image, laptop has no disc drive | Mount the ISO file |
| New user can sign in but the cloud spreadsheet app says no license | Admin assigns a license to the user's account |
| Same install needed on 50 identical PCs | Image deployment |
| Pro app refuses to start, no error about the PC | External hardware token not plugged in |
| Team wants to edit one spreadsheet together | Cloud collaboration tool |
