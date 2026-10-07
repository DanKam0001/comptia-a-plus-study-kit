# Memorise list: Operating Systems, Windows Editions and Installing Them (Core 2, Part 1)

Understand the video first, then learn these cold. They're the facts a scenario question assumes you already know.
Flashcards: [`flashcards/core2_part01.csv`](../../flashcards/core2_part01.csv) (import into Anki or any flashcard app).

## Operating systems and file systems

| Question | Answer |
|---|---|
| Four workstation OS types | Windows, Linux, macOS, Chrome OS |
| Three mobile OS types | iOS, iPadOS, Android |
| Default Windows file system | NTFS (permissions, encryption, large files) |
| FAT32 maximum file size | 4 GB |
| File system for USB drives shared by Windows and Mac, with large files | exFAT |
| Linux file systems | ext4 and XFS |
| Apple file system | APFS |
| ReFS is built for | Resilience on large storage |
| What EOL means | End-of-life: the vendor stops updates and support |
| Windows 10 end of support | October 14, 2025 |
| Windows 11 version servicing | 24 months (Home, Pro), 36 months (Enterprise, Education) |

## Installations

| Question | Answer |
|---|---|
| Install 50 identical PCs fast | Image deployment |
| Install with nobody at the keyboard | Zero-touch deployment |
| Wipe the drive and start fresh | Clean install |
| Keep files, apps and settings | Upgrade (in-place upgrade) |
| Fix Windows but keep files and apps | Repair installation |
| Restore the PC to factory state from a hidden copy | Recovery partition |
| Two or more operating systems on one PC | Multiboot |
| Setup cannot see the drive | Load a third-party driver |
| Do first before any upgrade | Back up files and user preferences |

## Partitioning

| Question | Answer |
|---|---|
| MBR maximum drive size | 2 TB |
| MBR maximum primary partitions | 4 |
| GPT partitions in Windows | 128 |
| Windows UEFI boot needs | GPT |
| 4 TB drive shows only 2 TB | It was set up as MBR. Use GPT |

## Windows editions

| Question | Answer |
|---|---|
| Windows 10 editions | Home, Pro, Pro for Workstations, Enterprise |
| Windows 11 editions | Home, Pro, Enterprise |
| N version | Without Windows Media Player and related media features |
| Home can join a domain? | No. Workgroup only |
| Home has BitLocker? | No (Pro and above do) |
| Home has gpedit.msc? | No (Pro and above do) |
| Home and Remote Desktop | Can connect out, cannot be connected to (cannot host) |
| RAM limits (Home / Pro / Pro for Workstations / Enterprise) | 128 GB / 2 TB / 6 TB / 6 TB |
| Windows 11 hardware requirements | TPM 2.0, UEFI with Secure Boot, 4 GB RAM, 64 GB storage, 64-bit 1 GHz CPU with 2 or more cores |
