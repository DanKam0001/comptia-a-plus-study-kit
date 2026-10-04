# CompTIA A+ Core 2 (220-1202): Practice Exam 1

90 questions, 90 minutes. Pass mark on the real exam: 700 out of 900 (scaled). Answers are in a separate file.

**1.** A user needs to move 6 GB video files between a Windows laptop and a macOS laptop using a USB flash drive. Which file system should the drive be formatted with?

- A. NTFS
- B. ext4
- C. exFAT
- D. FAT32

**2.** A small office still runs several workstations on an operating system that reached end of life eighteen months ago. Which consequence is the most significant security concern?

- A. Existing installed applications are automatically uninstalled
- B. The vendor no longer issues security patches for newly discovered vulnerabilities
- C. The operating system will stop booting after the end-of-life date
- D. The systems lose the ability to join a workgroup

**3.** A technician is installing Windows 11 on a 4 TB drive and needs the entire capacity available in a single volume. Which partitioning scheme and firmware mode are required?

- A. GPT with legacy BIOS
- B. GPT with UEFI
- C. MBR with legacy BIOS
- D. MBR with UEFI

**4.** A company is deploying 200 identical laptops and wants each to arrive at the user's desk already configured, with no technician touching the device. Which installation type best describes this?

- A. Zero-touch deployment
- B. Clean installation
- C. In-place upgrade
- D. Recovery partition restore

**5.** Before performing an in-place upgrade of Windows on a user's workstation, which two steps should the technician take first?  *(Choose TWO.)*

- A. Disable the built-in administrator account
- B. Convert the system drive from GPT to MBR
- C. Back up the user's data and verify the backup is restorable
- D. Confirm the hardware meets the new version's minimum requirements

**6.** A home user wants to connect to their work computer using Remote Desktop and also wants other staff to connect inbound to their own machine, which runs Windows 11 Home. What is the limitation?

- A. Windows Home supports neither inbound nor outbound RDP
- B. Windows Home supports both, but only one session at a time
- C. Windows Home can initiate an RDP connection but cannot host one
- D. Windows Home can host an RDP connection but cannot initiate one

**7.** A technician needs to open the Local Group Policy Editor on a workstation but finds the command does not exist. Which is the most likely explanation?

- A. The user account is not a member of the Users group
- B. The machine runs a Home edition, which does not include gpedit.msc
- C. The machine is not joined to a domain
- D. The Group Policy Client service has been stopped

**8.** A user reports that their computer restarted overnight without warning. Which tool shows the logged reason and lets the technician filter to critical system events?

- A. Disk Management
- B. Event Viewer
- C. Device Manager
- D. Task Manager

**9.** A technician wants a single console containing Event Viewer, Device Manager, and Performance Monitor together. Which tool creates it?

- A. Registry Editor (regedit.exe)
- B. System Configuration (msconfig.exe)
- C. System Information (msinfo32.exe)
- D. Microsoft Management Console (mmc.exe)

**10.** A graphics driver update has left a workstation with display corruption. Which Device Manager option returns the previously working driver?

- A. Scan for hardware changes
- B. Update Driver
- C. Roll Back Driver
- D. Disable device

**11.** A technician suspects corrupted Windows system files are causing application crashes. Which command scans protected system files and repairs them from a cached copy?

- A. diskpart clean
- B. chkdsk /f
- C. gpupdate /force
- D. sfc /scannow

**12.** A technician needs to identify which process is holding TCP port 443 open on a workstation. Which two commands, used together, provide the answer?  *(Choose TWO.)*

- A. netstat -ano
- B. tasklist
- C. ipconfig /all
- D. nslookup

**13.** A technician runs a command that copies a folder tree to a backup location and deletes files in the destination that no longer exist in the source. Which command does this?

- A. robocopy source destination /MIR
- B. move source destination
- C. xcopy source destination /s
- D. copy source destination

**14.** A user reports that a website resolves correctly on their phone but not on their Windows laptop, which returns an old address. Which command clears the locally cached name resolution data?

- A. netstat -r
- B. ipconfig /release
- C. nslookup -clear
- D. ipconfig /flushdns

**15.** A user on a metered cellular connection reports that large background downloads are consuming their data allowance. Where should the technician mark the connection to limit this behavior?

- A. Internet Options, by configuring a proxy server
- B. Device Manager, by disabling the network adapter
- C. Network and Internet settings, by setting the connection as metered
- D. Power Options, by enabling battery saver

**16.** Users report that their desktops take a long time to fully shut down and start up, and a technician wants to reduce boot time by having Windows save the kernel session to disk at shutdown. Which setting controls this?

- A. Hibernate, under Sleep settings
- B. Startup apps, in Task Manager
- C. Fast startup, under Power Options
- D. Boot logging, in System Configuration

**17.** A technician assigns a workstation a static IP address. Afterward the user can ping and reach other machines on the same subnet, but cannot ping any external IP address such as 8.8.8.8. Which setting is most likely wrong?

- A. The default gateway
- B. The DNS suffix
- C. The MAC address
- D. The computer hostname

**18.** A technician connects a laptop to a coffee-shop Wi-Fi network. Internet access works, but the laptop cannot discover or reach a colleague's shared folder on that same network, although sharing worked on the office network. What is the most likely cause?

- A. The network is set to Public, which blocks network discovery and file sharing
- B. The wireless adapter does not support the shop's frequency band
- C. The laptop has been removed from the domain
- D. The default gateway is unreachable

**19.** A workstation shows an IPv4 address of 169.254.18.44. What does this indicate?

- A. The client has been assigned a valid public address
- B. The client is configured with a static address outside its subnet
- C. The client's network adapter has been disabled
- D. The client could not reach a DHCP server and self-assigned an APIPA address

**20.** A macOS user needs to recover a document as it existed three days ago. Which built-in utility should they use?

- A. Time Machine
- B. Disk Utility
- C. Keychain Access
- D. Mission Control

**21.** Which macOS feature provides full-disk encryption?

- A. FileVault
- B. Gatekeeper
- C. Finder
- D. Spotlight

**22.** A Linux administrator needs to give the owner of a script read, write, and execute rights while giving group and others read and execute only. Which command achieves this?

- A. chmod 755 script.sh
- B. chmod 777 script.sh
- C. chmod 644 script.sh
- D. chown 755 script.sh

**23.** Which Linux file stores hashed user passwords, readable only by privileged accounts?

- A. /etc/passwd
- B. /etc/shadow
- C. /etc/hosts
- D. /etc/fstab

**24.** A user reports that a newly purchased application will not install, reporting an incompatible architecture. Which system characteristic should the technician verify first?

- A. The monitor's native resolution
- B. Whether the operating system is 32-bit or 64-bit
- C. The amount of free space on the recovery partition
- D. The installed antivirus vendor

**25.** An organization moving to a cloud productivity suite wants staff to sign in to cloud applications with the same credentials they already use on-premises. Which capability provides this?

- A. Content filtering
- B. File versioning
- C. Data loss prevention
- D. Identity synchronization

**26.** A company wants to ensure that only one person passes through a secure entrance at a time, preventing someone from following an authorized employee inside. Which control addresses this?

- A. Access control vestibule
- B. Motion sensor
- C. Bollards
- D. Badge reader

**27.** Under the principle of least privilege, what access should a new accounts-payable clerk receive?

- A. The same permissions as their manager, for continuity
- B. Local administrator rights, to avoid support tickets
- C. Full access initially, tightened after the probation period
- D. Only the permissions required to perform their specific job duties

**28.** A folder's NTFS permissions grant a user Modify, while the share permissions grant Read. What can the user do when connecting to the folder over the network?

- A. Read only
- B. Modify
- C. Nothing, because the permissions conflict
- D. Full Control

**29.** A user is logged in with an administrator account and launches an application that requires elevation. What does User Account Control do?

- A. Prompts for consent before granting the process the administrative token
- B. Logs the user out and back in with elevated rights
- C. Silently grants administrative rights because the user is already an administrator
- D. Blocks the application and requires a different account

**30.** Which two statements about BitLocker are correct?  *(Choose TWO.)*

- A. It can use a TPM to protect the encryption key
- B. It provides full-volume encryption
- C. It is included in all Windows editions, including Home
- D. It encrypts individual files chosen by the user

**31.** A technician is configuring a new wireless access point and wants the strongest available encryption. Which should be selected?

- A. WPA3
- B. WEP
- C. WPA
- D. WPA2 with TKIP

**32.** A medium-sized company wants wireless users authenticated against a central directory with individual credentials rather than one shared passphrase. Which should be implemented?

- A. WPA3-Enterprise with a RADIUS server
- B. MAC address filtering
- C. WPA3-Personal with a long passphrase
- D. A hidden SSID

**33.** A user's files have been renamed with an unfamiliar extension and a text file demanding payment appears in every folder. Which malware type is this?

- A. Adware
- B. Rootkit
- C. Ransomware
- D. Keylogger

**34.** Which malware type is specifically designed to conceal its presence by subverting the operating system itself, often surviving standard antivirus scans?

- A. Trojan
- B. Worm
- C. Rootkit
- D. Spyware

**35.** A workstation is fully patched and running current antivirus, yet is compromised by malware that runs entirely in memory and writes no file to disk. Which detection approach is most likely to identify it?

- A. Checking file hashes against a known-good baseline
- B. Behavior-based detection through an EDR platform
- C. A scheduled full disk scan
- D. Signature-based file scanning

**36.** An executive receives a personalized email appearing to come from the company's CEO, requesting an urgent wire transfer. Which attack is this?

- A. Whaling
- B. Dumpster diving
- C. Tailgating
- D. Shoulder surfing

**37.** A caller claims to be from the IT department and asks an employee to read back the six-digit code just sent to their phone. Which two describe this situation?  *(Choose TWO.)*

- A. The employee should never share the code, as it is an authentication factor
- B. This is acceptable if the caller knows the employee's job title
- C. This is a legitimate procedure for verifying identity over the phone
- D. This is a vishing attack

**38.** In the standard malware removal procedure, what must be done immediately after quarantining the infected system?

- A. Educate the end user
- B. Create a new restore point
- C. Disable System Restore
- D. Schedule future scans

**39.** During malware remediation, why is the infected machine disconnected from the network before cleaning begins?

- A. To prevent the malware from spreading to other systems or contacting external hosts
- B. To force the operating system into Safe Mode automatically
- C. To preserve the contents of the page file
- D. To allow antivirus definitions to update more quickly

**40.** Which setting limits the effectiveness of automated password-guessing attacks against local accounts?

- A. Password history length
- B. Screen saver timeout
- C. Account lockout threshold
- D. Maximum password age

**41.** A technician wants to prevent a stolen laptop from being booted to a USB device so its drive can be read. Which control addresses this most directly?

- A. Disabling the guest account
- B. A BIOS/UEFI password with boot order locked to the internal drive
- C. A complex Windows logon password
- D. A screen saver lock with a short timeout

**42.** Which two practices are appropriate when configuring a workstation for a user who handles sensitive client records?  *(Choose TWO.)*

- A. Disable automatic updates to avoid interrupting their work
- B. Configure a screen lock that activates after a short idle period
- C. Enable data-at-rest encryption on the system drive
- D. Grant the user local administrator rights so they can manage their own security

**43.** A company issues smartphones and needs the ability to enforce passcode policy and remotely wipe a lost device. Which solution provides this?

- A. A host-based firewall
- B. A password manager
- C. Full-disk encryption alone
- D. Mobile device management

**44.** Which mobile device condition most increases the risk of installing malicious applications?

- A. The device has automatic updates enabled
- B. The device is enrolled in mobile device management
- C. The device has been rooted or jailbroken
- D. The device uses biometric authentication

**45.** A hospital is disposing of failed solid-state drives that held patient records and cannot be reliably overwritten. Which disposal method is appropriate?

- A. Performing a standard quick format
- B. Degaussing the drives
- C. Deleting the partitions and reinstalling the operating system
- D. Physical destruction, such as shredding, with a certificate of destruction

**46.** What distinguishes a standard quick format from a low-level or full format?

- A. A quick format rewrites only the file system structures, leaving the underlying data recoverable
- B. A quick format overwrites every sector with zeros
- C. A quick format encrypts the volume before erasing it
- D. A quick format physically remaps bad sectors

**47.** A technician is hardening a new SOHO router. Which action should be taken first?

- A. Change the default administrator password
- B. Disable the SSID broadcast
- C. Configure port forwarding for remote access
- D. Enable MAC address filtering

**48.** Why should WPS be disabled on a SOHO wireless router?

- A. Its PIN is validated in two halves, making it feasible to brute force
- B. It broadcasts the wireless passphrase in plaintext
- C. It disables the router's built-in firewall
- D. It prevents WPA3 from being enabled

**49.** A user reports a browser warning stating the connection is not private. Which cause would produce this while the site remains legitimate?

- A. The site's certificate has expired
- B. The user's browser has pop-ups blocked
- C. The site uses a password manager extension
- D. The user's screen resolution is unsupported

**50.** A browser extension requests permission to read and change all data on every website the user visits. What is the realistic risk?

- A. It can capture credentials and modify page content on any site, including banking
- B. It can read data but cannot alter what is displayed
- C. It can only affect sites explicitly added to a whitelist
- D. The risk is limited because extensions run outside the browser

**51.** A workstation displays a stop error naming a specific .sys file, then restarts. What should the technician do first?

- A. Replace the system board
- B. Run a full antivirus scan in Safe Mode
- C. Immediately reinstall the operating system
- D. Identify the device or software associated with that driver file and check for a recent update

**52.** A user reports their computer is slow. Task Manager shows CPU at 6%, memory at 35%, and disk at 100% sustained. What is the bottleneck?

- A. Processor capacity
- B. Insufficient RAM
- C. Storage throughput
- D. Network bandwidth

**53.** A service is configured to start automatically but is not running after a reboot. Attempting to start it manually returns system error 1068. What does this indicate?

- A. The service is disabled
- B. The account running the service has an expired password
- C. A service it depends on is not running
- D. The service executable is missing

**54.** A Windows workstation fails to boot and displays an error referring to the boot configuration data. Which tool, run from the recovery environment, is most likely to repair it?

- A. diskpart clean
- B. bootrec /rebuildbcd
- C. chkdsk /r
- D. sfc /scannow

**55.** A user reports repeated low-memory warnings on a workstation with 16 GB of RAM. Which two causes should the technician investigate?  *(Choose TWO.)*

- A. An application with a memory leak consuming increasing amounts over time
- B. A page file that has been disabled or set to an unusually small fixed size
- C. An incorrect subnet mask on the network adapter
- D. A monitor running above its native resolution

**56.** An application crashes on launch for one user but works normally for another user on the same computer. What is the most likely cause?

- A. Insufficient system memory
- B. An incompatible processor architecture
- C. A failing hard drive
- D. A corrupted user profile or per-user application setting

**57.** Where should a technician look to reduce the time a Windows workstation takes to become usable after logon?

- A. The Startup apps list in Task Manager
- B. Device Manager
- C. Disk Management
- D. The Services console's dependency tab

**58.** An application reports that a required DLL is missing. Which is the most common underlying cause?

- A. A failing power supply
- B. An incorrect system date
- C. A missing runtime redistributable package the application depends on
- D. A disabled network adapter

**59.** An older business application will not run correctly on Windows 11. Which option should be tried before contacting the vendor?

- A. Changing the display to a lower color depth
- B. Disabling the page file
- C. Running the application in compatibility mode for an earlier Windows version
- D. Converting the system drive to FAT32

**60.** A user reports that a mobile application closes immediately after launching. Which step should be tried first, as it preserves the user's data within the app?

- A. Remove the device from mobile device management
- B. Clear the application's cache
- C. Clear the application's storage or data
- D. Perform a factory reset of the device

**61.** A smartphone's battery has begun draining noticeably faster than it did a month ago, with no change in usage habits. Which should the technician check first?

- A. Per-application battery usage statistics
- B. The device's screen resolution setting
- C. The Bluetooth device pairing list
- D. The SIM card seating

**62.** A technician suspects a third-party application is causing an Android device to reboot randomly. Which troubleshooting step isolates this?

- A. Clear the browser cache
- B. Enable USB debugging in developer options
- C. Boot the device into Safe Mode, which disables third-party applications
- D. Disable automatic screen rotation

**63.** A user cannot install updates on their mobile device, which reports insufficient space despite showing several gigabytes free. What is the most likely explanation?

- A. The update requires additional working space beyond the final installed size
- B. The device has exceeded its maximum number of installed applications
- C. The cellular data allowance has been exhausted
- D. The device's battery is below the required charge level

**64.** A corporate smartphone shows unusually high data usage and an application the user does not recognize. Which action should be taken first?

- A. Perform a factory reset immediately
- B. Report the device to the security team and follow the incident response procedure
- C. Uninstall the application and return the device to the user
- D. Disable cellular data and continue using the device

**65.** Which mobile application permission presents the greatest risk if granted to a malicious application?

- A. Screen rotation
- B. Flashlight control
- C. Accessibility services
- D. Calendar access

**66.** A user has enabled the option permitting installation from unknown sources on their Android device. What is the primary risk?

- A. The device's warranty is automatically voided
- B. Applications bypass the store's review process and may be malicious
- C. The device will no longer receive operating system updates
- D. Existing applications lose their granted permissions

**67.** A technician finds developer options and USB debugging enabled on a user's corporate phone. Why is this a concern?

- A. It stops the device from receiving application updates
- B. It allows a connected computer to issue privileged commands to the device
- C. It prevents the device from connecting to wireless networks
- D. It disables the device's biometric authentication

**68.** A workstation can browse most websites but Windows Update consistently fails. A technician suspects malware. Which file should be examined?

- A. The boot configuration data store
- B. The page file
- C. The registry's Run key
- D. The hosts file

**69.** A user reports a full-screen alert claiming their computer is infected and displaying a phone number to call. How can a technician recognize this as fraudulent?

- A. Legitimate alerts always appear in red
- B. Legitimate security software never provides a phone number or demands payment to remove threats
- C. Legitimate alerts always include the user's account name
- D. Legitimate alerts never appear in full screen

**70.** After cleaning adware from a workstation, the browser still opens an unfamiliar search page. Which two locations should the technician check?  *(Choose TWO.)*

- A. The browser's installed extensions
- B. The target field of the browser's desktop shortcut
- C. The printer spooler settings
- D. The workstation's BIOS boot order

**71.** Why would malware install its own root certificate into the Windows certificate store?

- A. To hide its processes from Task Manager
- B. To prevent the operating system from installing updates
- C. To allow it to intercept and decrypt the user's encrypted web traffic without warnings
- D. To grant itself local administrator rights

**72.** Which document describes the step-by-step process a technician should follow to complete a recurring task consistently?

- A. End-user license agreement
- B. Network topology diagram
- C. Standard operating procedure
- D. Acceptable use policy

**73.** What distinguishes a ticket's severity from its priority?

- A. They are interchangeable terms for the same field
- B. Severity is set by the user, while priority is set automatically
- C. Severity describes the technical impact, while priority describes the order in which work should be done
- D. Severity applies to hardware tickets and priority to software tickets

**74.** Which element of a change request describes what will be done if the change fails during the maintenance window?

- A. The risk analysis
- B. The scope of the change
- C. The end-user acceptance record
- D. The rollback plan

**75.** A pre-approved, low-risk, routine change that follows a documented procedure is classified as which change type?

- A. Emergency change
- B. Major change
- C. Normal change
- D. Standard change

**76.** A company performs a full backup on Sunday and incremental backups Monday through Thursday. A failure occurs Friday morning. What must be restored?

- A. The full backup plus all four incremental backups, in order
- B. The full backup only
- C. Thursday's incremental only
- D. The full backup plus Thursday's incremental only

**77.** What does the 3-2-1 backup rule specify?

- A. Three copies of the data, on two different media types, with one copy offsite
- B. Three servers, two data centers, one administrator
- C. Three backups per day, two retained, one verified
- D. Three full backups, two incremental, one differential

**78.** Why should backups be periodically test-restored?

- A. Test restores free space on the backup media
- B. Test restores are needed to keep the backup software licensed
- C. A backup that cannot be restored provides no protection, and failures are often discovered only during a restore
- D. Test restores are required to reset the archive attribute

**79.** A technician is preparing to replace a memory module in a desktop. Which precaution prevents electrostatic damage to the component?

- A. Wearing rubber-soled shoes while working
- B. Handling the module by its gold contact edge
- C. Wearing an anti-static wrist strap connected to a grounding point
- D. Working on a carpeted surface to absorb static

**80.** Which two practices are correct when handling and storing spare components?  *(Choose TWO.)*

- A. Store components in anti-static bags when not installed
- B. Hold expansion cards by their edges rather than their connectors
- C. Stack loose circuit boards together to save shelf space
- D. Store components in sealed plastic zip bags to keep out dust

**81.** Which document provides handling, storage, and disposal guidance for a chemical such as printer toner?

- A. Safety data sheet (SDS, formerly called MSDS)
- B. Service level agreement
- C. Asset tag record
- D. Statement of work

**82.** A server room experiences frequent brief power dips that cause equipment to restart. Which device addresses this?

- A. A power distribution unit
- B. An uninterruptible power supply
- C. A line splitter
- D. A surge suppressor

**83.** A technician discovers prohibited material on a user's workstation. What should be done first?

- A. Report it through the proper channels as defined by company policy
- B. Delete the material and inform the user
- C. Confront the user to hear their explanation
- D. Investigate the files to determine their origin

**84.** Which sequence correctly reflects the order of volatility, from most volatile to least?

- A. Disk, then RAM, then archival backups
- B. RAM, then archival backups, then disk
- C. Archival backups, then disk, then RAM
- D. RAM, then disk, then archival backups

**85.** Why is a cryptographic hash of seized media recorded before examination begins?

- A. To encrypt the media so it cannot be read by others
- B. To compress the media for faster transfer
- C. To prove afterward that the data was not altered while in the examiner's possession
- D. To recover files that were previously deleted

**86.** A user is angry and repeatedly interrupts while describing a recurring fault. What is the most appropriate response?

- A. Explain that their tone is unprofessional and ask them to calm down
- B. Transfer the call to a colleague without explanation
- C. Listen without interrupting, then restate the problem to confirm understanding
- D. Begin troubleshooting immediately to end the conversation quickly

**87.** Which file extension identifies a Windows PowerShell script?

- A. .ps1
- B. .sh
- C. .bat
- D. .vbs

**88.** Which is a recognized risk of deploying a logon script across an organization?

- A. Scripts prevent users from logging on concurrently
- B. Scripts always require local administrator rights to run
- C. Scripts cannot be tested before deployment
- D. A defect in the script is applied simultaneously to every machine that runs it

**89.** Which remote access method provides an encrypted command-line session to a Linux server?

- A. Telnet
- B. VNC
- C. SSH
- D. RDP

**90.** An employee pastes a section of a confidential client contract into a public AI chatbot to summarize it. What is the primary concern?

- A. The employee may become dependent on the tool
- B. The summary may be formatted inconsistently
- C. Confidential data has been disclosed to a third-party service outside the organization's control
- D. The chatbot may take longer than reading the document manually
