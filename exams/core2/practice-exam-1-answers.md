# CompTIA A+ Core 2 (220-1202): Practice Exam 1, answer key

## Quick key

| 1: C | 2: B | 3: B | 4: A | 5: CD | 6: C | 7: B | 8: B | 9: D | 10: C |
| 11: D | 12: AB | 13: A | 14: D | 15: C | 16: C | 17: A | 18: A | 19: D | 20: A |
| 21: A | 22: A | 23: B | 24: B | 25: D | 26: A | 27: D | 28: A | 29: A | 30: AB |
| 31: A | 32: A | 33: C | 34: C | 35: B | 36: A | 37: AD | 38: C | 39: A | 40: C |
| 41: B | 42: BC | 43: D | 44: C | 45: D | 46: A | 47: A | 48: A | 49: A | 50: A |
| 51: D | 52: C | 53: C | 54: B | 55: AB | 56: D | 57: A | 58: C | 59: C | 60: B |
| 61: A | 62: C | 63: A | 64: B | 65: C | 66: B | 67: B | 68: D | 69: B | 70: AB |
| 71: C | 72: C | 73: C | 74: D | 75: D | 76: A | 77: A | 78: C | 79: C | 80: AB |
| 81: A | 82: B | 83: A | 84: D | 85: C | 86: C | 87: A | 88: D | 89: C | 90: C |

## Score yourself

- 72 or more out of 90: comfortably ready, if your practice-exam scores are consistently this high.
- 63 to 71: borderline. Drill the domain with the most misses, then retake a different paper.
- Below 63: not ready yet. Go back to the parts that cover your misses, using the objective numbers.

## Explanations

**1. Answer: C**  *[Operating Systems, objective 1.1]*

- C. exFAT

exFAT is read/write on both Windows and macOS and has no practical file-size limit. FAT32 is equally cross-platform but caps individual files at 4 GB, which the 6 GB files exceed. NTFS is read-only on macOS without third-party drivers, and ext4 is a Linux file system that neither OS mounts natively.

**2. Answer: B**  *[Operating Systems, objective 1.1]*

- B. The vendor no longer issues security patches for newly discovered vulnerabilities

End of life means the vendor stops publishing fixes, so any vulnerability found from that point onward stays permanently exploitable on those machines. The OS keeps running and applications keep working, which is exactly why the risk is easy to ignore.

**3. Answer: B**  *[Operating Systems, objective 1.2]*

- B. GPT with UEFI

MBR addresses a maximum of 2 TB, so a 4 TB volume requires GPT, and booting Windows from a GPT disk requires UEFI firmware. The remaining combinations either cap the usable space or will not boot.

**4. Answer: A**  *[Operating Systems, objective 1.2]*

- A. Zero-touch deployment

Zero-touch deployment provisions a device automatically from the network or vendor service with no hands-on configuration. A clean installation and a recovery partition restore both require someone at the machine, and an in-place upgrade applies to a system that already has an OS.

**5. Answer: C, D**  *[Operating Systems, objective 1.2]*

- C. Back up the user's data and verify the backup is restorable
- D. Confirm the hardware meets the new version's minimum requirements

A verified backup protects against an upgrade that fails partway, and a requirements check prevents starting an upgrade the hardware cannot complete. Converting to MBR would remove UEFI boot support rather than help, and the administrator account state has no bearing on an upgrade.

**6. Answer: C**  *[Operating Systems, objective 1.3]*

- C. Windows Home can initiate an RDP connection but cannot host one

The Remote Desktop client ships with every edition, so connecting out works fine. The Remote Desktop host service is a Pro and above feature, so nothing can connect in to a Home machine.

**7. Answer: B**  *[Operating Systems, objective 1.3]*

- B. The machine runs a Home edition, which does not include gpedit.msc

gpedit.msc is simply absent from Home editions. Domain membership is irrelevant, since local policy exists on standalone machines too, and a stopped service would produce an error rather than a missing file.

**8. Answer: B**  *[Operating Systems, objective 1.4]*

- B. Event Viewer

Event Viewer holds the System log, where unexpected shutdowns and kernel power events are recorded, and supports custom filtered views. Task Manager shows only current activity, Device Manager covers hardware, and Disk Management covers volumes.

**9. Answer: D**  *[Operating Systems, objective 1.4]*

- D. Microsoft Management Console (mmc.exe)

The Management Console is the host application that the individual snap-ins load into, and saved consoles can hold any combination of them. The other tools serve unrelated purposes and cannot host snap-ins.

**10. Answer: C**  *[Operating Systems, objective 1.4]*

- C. Roll Back Driver

Roll Back Driver reinstates the driver in use before the most recent update, and is available only when a previous version was retained. Updating again would not necessarily return the older build, and disabling the device removes display functionality rather than restoring it.

**11. Answer: D**  *[Operating Systems, objective 1.5]*

- D. sfc /scannow

System File Checker verifies protected operating system files and replaces damaged ones from the local component store. chkdsk repairs file system structures rather than file contents, diskpart clean destroys partition data, and gpupdate reapplies policy.

**12. Answer: A, B**  *[Operating Systems, objective 1.5]*

- A. netstat -ano
- B. tasklist

netstat with the flag set that includes the owning process identifier reveals which numeric process owns the port, and tasklist then maps that identifier to an executable name. The adapter configuration and DNS lookup tools report nothing about local port ownership.

**13. Answer: A**  *[Operating Systems, objective 1.5]*

- A. robocopy source destination /MIR

The mirror switch makes the destination an exact match of the source, which includes removing files that were deleted at the source. A recursive xcopy adds and updates but never deletes, plain copy handles single files, and move relocates rather than duplicates.

**14. Answer: D**  *[Operating Systems, objective 1.5]*

- D. ipconfig /flushdns

Flushing the resolver cache discards locally stored name-to-address mappings so the next lookup queries the DNS server fresh. ipconfig /release gives up the DHCP lease, netstat -r only displays the routing table, and nslookup has no -clear option.

**15. Answer: C**  *[Operating Systems, objective 1.6]*

- C. Network and Internet settings, by setting the connection as metered

Marking a connection as metered tells Windows and many applications to defer non-essential downloads such as optional updates. Battery saver manages power, a proxy changes routing rather than volume, and disabling the adapter removes connectivity entirely.

**16. Answer: C**  *[Operating Systems, objective 1.6]*

- C. Fast startup, under Power Options

Fast startup writes the kernel session to a hibernation file at shutdown so the next boot resumes it rather than initializing from scratch. Hibernation preserves a full user session instead, startup apps affect post-logon time, and boot logging only records what loaded.

**17. Answer: A**  *[Operating Systems, objective 1.7]*

- A. The default gateway

Traffic that stays inside the local subnet needs no gateway, so local success paired with failure to reach even a raw external IP address points at the default gateway entry. DNS is ruled out because the test uses an IP address, the hostname and DNS suffix do not affect routing, and a MAC address is not manually configured in this context.

**18. Answer: A**  *[Operating Systems, objective 1.7]*

- A. The network is set to Public, which blocks network discovery and file sharing

A newly joined network defaults to the Public profile, which turns off network discovery and file sharing, which is the intended behavior on an untrusted network. Working internet access rules out an unreachable gateway or an unsupported frequency band, and domain membership does not explain discovery being blocked.

**19. Answer: D**  *[Operating Systems, objective 1.7]*

- D. The client could not reach a DHCP server and self-assigned an APIPA address

The 169.254.0.0 range is reserved for automatic private addressing, which a client assigns itself when no DHCP server responds. It permits same-subnet communication only, and a disabled adapter would report no address at all.

**20. Answer: A**  *[Operating Systems, objective 1.8]*

- A. Time Machine

Time Machine is the built-in backup utility and supports restoring earlier versions of individual files. Disk Utility manages volumes, Mission Control arranges windows, and Keychain Access stores credentials.

**21. Answer: A**  *[Operating Systems, objective 1.8]*

- A. FileVault

FileVault encrypts the startup volume so data is unreadable without valid credentials. Gatekeeper controls which applications are permitted to run, Spotlight indexes and searches, and Finder is the file browser.

**22. Answer: A**  *[Operating Systems, objective 1.9]*

- A. chmod 755 script.sh

In octal notation the first digit covers the owner and the remaining two cover group and others, so seven grants full owner rights while five grants read and execute. Mode 644 omits execute entirely, 777 grants write to everyone, and chown changes ownership rather than permissions.

**23. Answer: B**  *[Operating Systems, objective 1.9]*

- B. /etc/shadow

Password hashes were separated out of the world-readable account file into a restricted file precisely so ordinary users could not read them. The account file holds user attributes, the hosts file maps names to addresses, and the file system table defines mounts.

**24. Answer: B**  *[Operating Systems, objective 1.10]*

- B. Whether the operating system is 32-bit or 64-bit

A 64-bit application cannot run on a 32-bit operating system, which produces exactly this class of error. Recovery partition space, antivirus choice, and display resolution do not cause architecture mismatches.

**25. Answer: D**  *[Operating Systems, objective 1.11]*

- D. Identity synchronization

Identity synchronization replicates directory accounts into the cloud provider so a single credential works in both places. Versioning retains prior copies of files, data loss prevention inspects content leaving the organization, and content filtering restricts what users can reach.

**26. Answer: A**  *[Security, objective 2.1]*

- A. Access control vestibule

An access control vestibule uses two interlocking doors so a second person cannot follow through on one authentication, which is the direct countermeasure to tailgating. Bollards stop vehicles, a badge reader authenticates but does not prevent a follower, and a motion sensor only detects.

**27. Answer: D**  *[Security, objective 2.1]*

- D. Only the permissions required to perform their specific job duties

Least privilege grants the minimum access the role actually requires, limiting the damage from both mistakes and compromised credentials. The remaining options all grant more than the role needs, which is the condition least privilege exists to prevent.

**28. Answer: A**  *[Security, objective 2.2]*

- A. Read only

When both layers apply, the more restrictive of the two wins, so the share's Read caps the effective access regardless of what the file system layer permits. Sitting at the machine locally, the share layer would not apply at all and Modify would be effective.

**29. Answer: A**  *[Security, objective 2.2]*

- A. Prompts for consent before granting the process the administrative token

An administrator's session runs with a filtered standard token, and elevation to the full token requires explicit consent. That prompt is what keeps malware running in the session from silently acquiring administrative rights.

**30. Answer: A, B**  *[Security, objective 2.2]*

- A. It can use a TPM to protect the encryption key
- B. It provides full-volume encryption

BitLocker encrypts an entire volume rather than selected files, and it commonly seals its key to the Trusted Platform Module so the drive cannot be read in another machine. Per-file encryption is what the Encrypting File System provides, and Home editions offer only the reduced Device Encryption feature.

**31. Answer: A**  *[Security, objective 2.3]*

- A. WPA3

WPA3 is the current standard and addresses weaknesses remaining in earlier versions, including offline dictionary attacks against captured handshakes. TKIP is a deprecated cipher retained for compatibility, and both WPA and WEP are broken.

**32. Answer: A**  *[Security, objective 2.3]*

- A. WPA3-Enterprise with a RADIUS server

Enterprise mode delegates authentication to a RADIUS server so each user presents their own credentials and can be revoked individually. A pre-shared key is shared by everyone, while address filtering and hiding the network name are trivially bypassed and are not authentication.

**33. Answer: C**  *[Security, objective 2.4]*

- C. Ransomware

Encrypting files and demanding payment for their return is the defining behaviour of ransomware. A keylogger captures input silently, a rootkit conceals itself and other components, and adware displays unwanted advertising.

**34. Answer: C**  *[Security, objective 2.4]*

- C. Rootkit

A rootkit operates at a privileged level and hides files, processes, and registry entries from the tools used to find it, which is why reimaging is often the only trustworthy remedy. A Trojan disguises itself as legitimate software, a worm self-propagates, and spyware gathers information.

**35. Answer: B**  *[Security, objective 2.4]*

- B. Behavior-based detection through an EDR platform

Fileless malware leaves nothing on disk for a file scanner to match, so detection depends on observing anomalous behaviour at runtime, which is what endpoint detection and response platforms provide. Every other option inspects files that in this case do not exist.

**36. Answer: A**  *[Security, objective 2.5]*

- A. Whaling

Whaling is targeted phishing aimed at a high-value individual such as a senior executive. The remaining options are physical or in-person techniques rather than a crafted email.

**37. Answer: A, D**  *[Security, objective 2.5]*

- A. The employee should never share the code, as it is an authentication factor
- D. This is a vishing attack

Voice-based social engineering is vishing, and the code in question is a possession factor that exists specifically to prove the holder is present. Knowing role details is trivially researched and proves nothing, and no legitimate process asks a user to disclose a one-time code.

**38. Answer: C**  *[Security, objective 2.6]*

- C. Disable System Restore

System Restore is disabled before remediation so infected restore points are discarded rather than preserved as a route back to the infection. Creating a restore point and educating the user both belong at the end of the procedure, after the system is clean.

**39. Answer: A**  *[Security, objective 2.6]*

- A. To prevent the malware from spreading to other systems or contacting external hosts

Quarantine contains the infection and cuts off command-and-control communication. Disconnecting actually makes updating definitions harder, which is the recognized trade-off of the step rather than a benefit.

**40. Answer: C**  *[Security, objective 2.7]*

- C. Account lockout threshold

A lockout threshold disables an account after a set number of failed attempts, which stops repeated guessing. Password history prevents reuse, screen timeout addresses unattended sessions, and maximum age forces periodic changes.

**41. Answer: B**  *[Security, objective 2.7]*

- B. A BIOS/UEFI password with boot order locked to the internal drive

Restricting firmware settings and boot order prevents booting alternate media to bypass the installed operating system entirely. A Windows password is irrelevant if the drive is read from another OS, and the remaining options address an unattended running session.

**42. Answer: B, C**  *[Security, objective 2.7]*

- B. Configure a screen lock that activates after a short idle period
- C. Enable data-at-rest encryption on the system drive

Encryption protects the records if the device is lost, and a short idle lock protects an unattended session. Granting administrative rights violates least privilege, and disabling updates leaves known vulnerabilities unpatched.

**43. Answer: D**  *[Security, objective 2.8]*

- D. Mobile device management

Mobile device management enrolls devices under central policy, which includes enforcing screen locks and issuing a remote wipe. Encryption protects data but provides no management capability, and the remaining options serve different purposes.

**44. Answer: C**  *[Security, objective 2.8]*

- C. The device has been rooted or jailbroken

Rooting or jailbreaking removes the platform's built-in restrictions, permitting installation outside the vetted store and granting applications privileges the sandbox would normally deny. The other conditions all improve the device's security posture.

**45. Answer: D**  *[Security, objective 2.9]*

- D. Physical destruction, such as shredding, with a certificate of destruction

Wear leveling means overwriting cannot guarantee every flash cell is reached, so physical destruction with documented evidence is the defensible option. Degaussing affects magnetic media only and has no effect on flash, and both remaining options leave data recoverable.

**46. Answer: A**  *[Security, objective 2.9]*

- A. A quick format rewrites only the file system structures, leaving the underlying data recoverable

A quick format replaces the index that points at the data while leaving the data itself in place, which is why recovery tools retrieve files afterward. Writing zeros across the volume is what a full format does.

**47. Answer: A**  *[Security, objective 2.10]*

- A. Change the default administrator password

Default credentials are published for every consumer model, so an unchanged password leaves the device trivially accessible regardless of other settings. Hiding the network name and filtering addresses are weak measures, and port forwarding increases exposure.

**48. Answer: A**  *[Security, objective 2.10]*

- A. Its PIN is validated in two halves, making it feasible to brute force

The PIN's design allows each half to be attacked separately, reducing the search space enough to recover it in hours and with it the wireless passphrase, no matter how strong that passphrase is. The other statements describe behaviour WPS does not have.

**49. Answer: A**  *[Security, objective 2.11]*

- A. The site's certificate has expired

Certificate validation checks the expiry date among other things, and an expired certificate triggers the warning even though encryption still functions. The remaining options have no bearing on certificate validation.

**50. Answer: A**  *[Security, objective 2.11]*

- A. It can capture credentials and modify page content on any site, including banking

That permission grants the extension the ability to observe and alter every page, which covers authentication forms and transaction details. Extensions run inside the browser with the access they were granted, not outside it.

**51. Answer: D**  *[Software Troubleshooting, objective 3.1]*

- D. Identify the device or software associated with that driver file and check for a recent update

A named driver file points directly at the component that failed, making a recent driver change the most productive first line of investigation. Reinstalling or replacing hardware discards useful diagnostic information before it has been examined.

**52. Answer: C**  *[Software Troubleshooting, objective 3.1]*

- C. Storage throughput

A disk pinned at full utilization while the processor and memory sit idle identifies storage as the constraint. Low processor and memory figures rule those out, and Task Manager's disk metric does not reflect network activity.

**53. Answer: C**  *[Software Troubleshooting, objective 3.1]*

- C. A service it depends on is not running

That specific error reports a dependency failure, so the fix is to identify and start the required service first. A disabled service returns a different error, which is why reading the number rather than the general failure matters.

**54. Answer: B**  *[Software Troubleshooting, objective 3.1]*

- B. bootrec /rebuildbcd

Rebuilding the boot configuration store addresses exactly the data the error names. System File Checker cannot run usefully against an unbootable installation from this context, chkdsk repairs file system errors, and the disk utility option would destroy data.

**55. Answer: A, B**  *[Software Troubleshooting, objective 3.1]*

- A. An application with a memory leak consuming increasing amounts over time
- B. A page file that has been disabled or set to an unusually small fixed size

A leaking process steadily consumes memory until warnings appear, and a restricted page file removes the overflow the system relies on under pressure. Display resolution and network configuration have no relationship to memory exhaustion.

**56. Answer: D**  *[Software Troubleshooting, objective 3.1]*

- D. A corrupted user profile or per-user application setting

Behaviour that differs between accounts on the same machine points to something stored per user rather than machine-wide. A hardware or architecture problem would affect every account equally.

**57. Answer: A**  *[Software Troubleshooting, objective 3.1]*

- A. The Startup apps list in Task Manager

Startup applications launch after logon and are the usual cause of a desktop that appears quickly but responds slowly. The remaining consoles manage volumes, hardware, and service relationships respectively.

**58. Answer: C**  *[Software Troubleshooting, objective 3.1]*

- C. A missing runtime redistributable package the application depends on

Applications commonly rely on shared runtime libraries distributed separately from the application itself, and a missing one produces this error. None of the other conditions cause a library load failure.

**59. Answer: C**  *[Software Troubleshooting, objective 3.1]*

- C. Running the application in compatibility mode for an earlier Windows version

Compatibility mode presents the application with an environment resembling the older version it expects, which resolves many legacy issues without vendor involvement. The remaining options would degrade the system without addressing the incompatibility.

**60. Answer: B**  *[Software Troubleshooting, objective 3.2]*

- B. Clear the application's cache

Clearing the cache discards temporary files while leaving settings and content intact, making it the least destructive first step. Clearing storage wipes the application's data, and a factory reset is far more drastic than the symptom warrants.

**61. Answer: A**  *[Software Troubleshooting, objective 3.2]*

- A. Per-application battery usage statistics

Battery usage statistics identify which application is responsible, turning a vague complaint into a specific target. The other items do not meaningfully affect battery consumption.

**62. Answer: C**  *[Software Troubleshooting, objective 3.2]*

- C. Boot the device into Safe Mode, which disables third-party applications

Safe Mode loads the operating system without third-party applications, so a symptom that disappears there confirms an installed application rather than the OS. Enabling debugging assists further diagnosis but isolates nothing on its own.

**63. Answer: A**  *[Software Troubleshooting, objective 3.2]*

- A. The update requires additional working space beyond the final installed size

Updates need temporary space for download and staging in addition to the space the installed result occupies, so the reported free figure can be misleading. A low battery produces a different and clearly worded message.

**64. Answer: B**  *[Software Troubleshooting, objective 3.3]*

- B. Report the device to the security team and follow the incident response procedure

A suspected compromise on a corporate device is an incident, and preserving evidence matters more than a quick fix. Uninstalling or resetting destroys exactly what an investigation would need.

**65. Answer: C**  *[Software Troubleshooting, objective 3.3]*

- C. Accessibility services

Accessibility services can read screen content and simulate user input across every application, which effectively grants full control of the device. Calendar access exposes limited data, and the remaining permissions are trivial.

**66. Answer: B**  *[Software Troubleshooting, objective 3.3]*

- B. Applications bypass the store's review process and may be malicious

Sideloading removes the vetting the official store performs, which is the control that ordinarily filters out malicious applications. Update delivery and existing permissions are unaffected by the setting.

**67. Answer: B**  *[Software Troubleshooting, objective 3.3]*

- B. It allows a connected computer to issue privileged commands to the device

Debugging access permits a connected host to install packages, read logs, and execute commands, which is significant exposure if the device is connected to an untrusted machine. The other described effects do not occur.

**68. Answer: D**  *[Software Troubleshooting, objective 3.4]*

- D. The hosts file

The hosts file is consulted before DNS, so entries redirecting update servers to unreachable addresses block updates while ordinary browsing continues. The Run key is worth checking for persistence but does not explain this specific symptom.

**69. Answer: B**  *[Software Troubleshooting, objective 3.4]*

- B. Legitimate security software never provides a phone number or demands payment to remove threats

Genuine endpoint protection remediates threats directly and does not route users to a call center, which makes the phone number the reliable tell. Color, size, and personalization are all easily imitated.

**70. Answer: A, B**  *[Software Troubleshooting, objective 3.4]*

- A. The browser's installed extensions
- B. The target field of the browser's desktop shortcut

A residual extension can reset the search provider on every launch, and a URL appended to the shortcut's target loads that page regardless of any browser setting. Neither firmware boot order nor print settings affect browser behaviour.

**71. Answer: C**  *[Software Troubleshooting, objective 3.4]*

- C. To allow it to intercept and decrypt the user's encrypted web traffic without warnings

A trusted root certificate lets the attacker present certificates the browser accepts, enabling silent interception of encrypted sessions. Concealing processes and obtaining privileges are achieved by other techniques.

**72. Answer: C**  *[Operational Procedures, objective 4.1]*

- C. Standard operating procedure

A standard operating procedure records how a routine task is performed so results are consistent between technicians. An acceptable use policy governs user behaviour, a topology diagram documents network layout, and a license agreement covers software terms.

**73. Answer: C**  *[Operational Procedures, objective 4.1]*

- C. Severity describes the technical impact, while priority describes the order in which work should be done

Severity measures how badly something is broken, whereas priority weighs that against business context to decide what gets attention first. A high-severity fault on a decommissioned system can legitimately carry low priority.

**74. Answer: D**  *[Operational Procedures, objective 4.2]*

- D. The rollback plan

The rollback plan states how the environment is returned to its previous working state, which is the question a change board always asks. Risk analysis assesses what could go wrong rather than what to do about it.

**75. Answer: D**  *[Operational Procedures, objective 4.2]*

- D. Standard change

A standard change is routine and pre-approved because its risk is well understood and it follows a documented procedure. A normal change goes through the full change-board approval process, and an emergency change is handled through an expedited approval path because it cannot wait for the normal schedule.

**76. Answer: A**  *[Operational Procedures, objective 4.3]*

- A. The full backup plus all four incremental backups, in order

Each incremental captures only what changed since the previous backup of any type, so the chain must be replayed in sequence. Restoring only the latest set would be sufficient if the scheme used differential backups instead.

**77. Answer: A**  *[Operational Procedures, objective 4.3]*

- A. Three copies of the data, on two different media types, with one copy offsite

The rule protects against media failure through multiple copies and formats, and against site-level loss such as fire or ransomware through the offsite copy. The other descriptions are not recognized practice.

**78. Answer: C**  *[Operational Procedures, objective 4.3]*

- C. A backup that cannot be restored provides no protection, and failures are often discovered only during a restore

Backup jobs can report success while producing unusable media, so a restore test is the only evidence the strategy actually works. The remaining statements describe effects that test restores do not have.

**79. Answer: C**  *[Operational Procedures, objective 4.4]*

- C. Wearing an anti-static wrist strap connected to a grounding point

A grounded wrist strap equalizes the technician's potential with the equipment so no discharge occurs. Carpet generates static rather than absorbing it, and touching the contacts is exactly what should be avoided.

**80. Answer: A, B**  *[Operational Procedures, objective 4.4]*

- A. Store components in anti-static bags when not installed
- B. Hold expansion cards by their edges rather than their connectors

Anti-static bags dissipate charge safely, and handling by the edges keeps skin oils and static away from contacts. Ordinary plastic bags can generate static, and stacking boards risks both physical and electrostatic damage.

**81. Answer: A**  *[Operational Procedures, objective 4.5]*

- A. Safety data sheet (SDS, formerly called MSDS)

A safety data sheet, which the CompTIA objectives still call a material safety data sheet (MSDS), details hazards, handling requirements, and correct disposal for a substance such as toner. The remaining documents cover service commitments, project deliverables, and inventory tracking.

**82. Answer: B**  *[Operational Procedures, objective 4.5]*

- B. An uninterruptible power supply

An uninterruptible power supply carries equipment through sags and short outages using its battery. A surge suppressor only protects against voltage spikes and does nothing for a dip or loss.

**83. Answer: A**  *[Operational Procedures, objective 4.6]*

- A. Report it through the proper channels as defined by company policy

First response is to report and preserve rather than to act, because independent investigation risks destroying evidence and exceeds the technician's authority. Deleting the material would compromise any subsequent process.

**84. Answer: D**  *[Operational Procedures, objective 4.6]*

- D. RAM, then disk, then archival backups

Evidence is collected most-volatile-first because the contents of memory disappear the moment the system loses power, while disk contents persist until overwritten and archived backup media persist longest.

**85. Answer: C**  *[Operational Procedures, objective 4.6]*

- C. To prove afterward that the data was not altered while in the examiner's possession

A hash taken before examination and matched afterward demonstrates integrity, which is what makes the evidence defensible. Hashing neither compresses, encrypts, nor recovers anything.

**86. Answer: C**  *[Operational Procedures, objective 4.7]*

- C. Listen without interrupting, then restate the problem to confirm understanding

Active listening followed by restating the issue defuses frustration and confirms the problem is correctly understood before work begins. Criticizing the user's tone escalates the situation.

**87. Answer: A**  *[Operational Procedures, objective 4.8]*

- A. .ps1

PowerShell scripts use the .ps1 extension. Batch files use .bat, shell scripts on Linux and macOS use .sh, and VBScript uses .vbs.

**88. Answer: D**  *[Operational Procedures, objective 4.8]*

- D. A defect in the script is applied simultaneously to every machine that runs it

The efficiency of automation cuts both ways, so an error propagates at the same scale the benefit does, which is the argument for sandbox testing beforehand. Scripts can be tested, and neither of the remaining statements is accurate.

**89. Answer: C**  *[Operational Procedures, objective 4.9]*

- C. SSH

SSH provides an encrypted shell session and is the standard for command-line administration. VNC and RDP deliver graphical desktops, and Telnet transmits everything, including credentials, in plaintext.

**90. Answer: C**  *[Operational Procedures, objective 4.10]*

- C. Confidential data has been disclosed to a third-party service outside the organization's control

Submitting confidential content to a public service is a disclosure, and the organization loses control over how that data is retained or used. This is the distinction an acceptable use policy is written to draw between public and private data submission.
