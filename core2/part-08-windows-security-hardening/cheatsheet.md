# Core 2, Part 8: Windows Security Settings and Workstation Hardening

**Objectives 2.2 and 2.7** (220-1202):
- 2.2: *Given a scenario, configure and apply basic Microsoft Windows OS security settings.*
- 2.7: *Given a scenario, apply workstation security options and hardening techniques.*

Domain: Security (28% of the exam).

## 2.2 Defender Antivirus

- Windows' built-in malware scanner (open it from the **Windows Security** app).
- **Activate/deactivate:** can be switched off (real-time protection). Windows turns it off automatically when another antivirus takes over.
- **Update definitions:** the list of known threats. Updates arrive through Windows Update, or manually from Windows Security > Virus and threat protection > Check for updates.

## 2.2 Firewall (Windows Defender Firewall)

- **Activate/deactivate** per network profile (domain, private, public). Open the advanced console with `wf.msc`.
- **Port security:** allow or block specific ports (inbound and outbound rules).
- **Application security:** allow or block specific programs through the firewall.

## 2.2 Users and groups

| Type | What it can do |
|---|---|
| **Local account** | Exists only on that one PC |
| **Microsoft account** | Online account. Signs in on many devices and syncs settings |
| **Standard account** | Run programs, use files. Cannot change system settings or install for all users |
| **Administrator** | Full control of the PC |
| **Guest** | Very limited. Disabled by default |
| **Power user** | Legacy group kept for old software. Sits between standard and administrator |

Best practice: use a **standard** account for daily work and an administrator only when needed.

**Run as administrator vs standard user:** right-click a program > *Run as administrator* starts it with full rights for that one session. A standard user will be asked for an administrator password.

**User Account Control (UAC):** dims the screen and asks permission before something makes a big change. Stops programs making changes silently.

## 2.2 Log-in OS options

| Option | Notes |
|---|---|
| Username and password | The classic |
| PIN | Personal identification number. With Windows Hello, a PIN works **only on that device** |
| Fingerprint | Biometric |
| Facial recognition | Biometric (Windows Hello Face) |
| SSO | Single sign-on: one sign-in for many apps |
| Passwordless / Windows Hello | PIN, fingerprint or face replace the password |

## 2.2 NTFS vs share permissions

| | NTFS permissions | Share permissions |
|---|---|---|
| Apply to | Files and folders on an NTFS drive | A shared folder, **over the network only** |
| Apply when sitting at the PC? | Yes | No |

- When both apply, the **most restrictive** permission wins (Full Control NTFS + Read share = Read over the network).
- **Inheritance:** a file or folder inherits permissions from its parent folder. Moving a file to a different volume makes it inherit the new folder's permissions. A move inside the same volume keeps its original permissions.
- **File and folder attributes:** read-only, hidden, archive, and similar flags.

## 2.2 Encryption

| Tool | What it does |
|---|---|
| **BitLocker** | Encrypts a whole drive. Usually uses the TPM. Save the **recovery key** somewhere safe. Needs Pro, Enterprise or Education editions (Home has a simpler "device encryption") |
| **BitLocker To Go** | Same for USB and other removable drives |
| **Encrypting File System (EFS)** | Encrypts individual files or folders for one user account. NTFS only |

**Data-at-rest encryption** (2.7) = encryption of stored data. BitLocker is the answer for a stolen laptop.

## 2.2 Active Directory

Active Directory keeps one central list of users and computers for a **domain**.
- **Joining a domain:** the PC takes its sign-ins from the domain (Settings > Accounts > Access work or school > Connect > Join this device to a local Active Directory domain).
- **Assigning a log-in script:** a script that runs when the user signs in.
- **Moving objects within organizational units (OUs):** OUs are folders for sorting users and computers.
- **Assigning home folders:** a personal network folder for each user.
- **Applying Group Policy:** settings pushed to many computers or users at once (for example a screen lock).
- **Selecting security groups:** groups of users given the same permissions.
- **Configuring folder redirection:** saves a user's folders (Documents, Desktop) on a server.

## 2.7 Workstation security options and hardening

**Password considerations:** length (longest matters most), character types, uniqueness (different on every site), complexity rules, expiration (forced change after a set time).

**BIOS/UEFI passwords:** stop others changing firmware settings or booting from USB. See Core 1 Part 1 for firmware.

**End-user best practices:** use screensaver locks; log off when not in use; secure and protect critical hardware (for example laptops); secure PII (personally identifiable information) and passwords; use password managers.

**Account management:** restrict user permissions; restrict log-in times; disable the guest account; use failed-attempts lockout; use timeout/screen lock; apply account expiration dates (temps and contractors).

**Other hardening:** change the default administrator account name and password; disable AutoRun (so a plugged-in USB cannot start a program alone); disable unused services.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Stolen laptop, files must be unreadable | BitLocker |
| Encrypt a USB stick | BitLocker To Go |
| Push the same setting to 200 PCs | Group Policy |
| Full Control NTFS, Read share, user connects over network | Read only (most restrictive wins) |
| Contractor leaves in 3 months | Account expiration date |
| Account tried 20 wrong passwords | Failed-attempts lockout |
| USB stick launches a program when plugged in | Disable AutoRun |
| Password-free sign-in with face or fingerprint | Windows Hello |
