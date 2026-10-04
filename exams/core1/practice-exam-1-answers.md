# CompTIA A+ Core 1 (220-1201): Practice Exam 1, answer key

## Quick key

| 1: CD | 2: B | 3: B | 4: A | 5: CD | 6: C | 7: B | 8: B | 9: D | 10: C |
| 11: D | 12: AB | 13: A | 14: D | 15: C | 16: C | 17: A | 18: A | 19: D | 20: A |
| 21: AB | 22: A | 23: B | 24: B | 25: D | 26: A | 27: D | 28: A | 29: A | 30: B |
| 31: A | 32: A | 33: CD | 34: C | 35: BD | 36: A | 37: AD | 38: C | 39: AB | 40: C |
| 41: B | 42: C | 43: D | 44: C | 45: D | 46: A | 47: A | 48: AD | 49: A | 50: A |
| 51: D | 52: AC | 53: C | 54: B | 55: AB | 56: D | 57: A | 58: C | 59: C | 60: BC |
| 61: A | 62: C | 63: A | 64: B | 65: C | 66: B | 67: BC | 68: D | 69: B | 70: A |
| 71: BC | 72: C | 73: C | 74: D | 75: D | 76: A | 77: AC | 78: CD | 79: C | 80: A |
| 81: A | 82: B | 83: A | 84: D |

## Score yourself

- 67 or more out of 84: comfortably ready, if your practice-exam scores are consistently this high.
- 59 to 66: borderline. Drill the domain with the most misses, then retake a different paper.
- Below 59: not ready yet. Go back to the parts that cover your misses, using the objective numbers.

## Explanations

**1. Answer: C, D**  *[Networking]*

- C. Enable a guest network with client isolation
- D. Enable WPA3 encryption

Enabling a dedicated guest network isolates visitor traffic from internal corporate resources and prevents guest devices from communicating with each other. Enabling WPA3 encryption secures wireless transmissions against eavesdropping and unauthorized access. DHCP scope exclusions prevent the DHCP server from assigning specific IPs, which does not isolate traffic or secure Wi-Fi. Static NAT mapping translates public-to-private IP addresses on firewalls/routers for inbound servers, which is irrelevant for separating wireless client traffic.

**2. Answer: B**  *[Hardware]*

- B. LC

LC (Lucent Connector) is correct because it is a popular small form factor (SFF) fiber optic connector featuring a retention latch mechanism similar to an RJ-45 ethernet plug, making it ideal for high-density network equipment. ST (Straight Tip) is incorrect because it uses a round metal bayonet twist-lock coupling mechanism. SC (Subscriber Connector) is incorrect because while it uses a push-pull mechanism, it is a larger square legacy connector format. F-type is incorrect because it is a threaded metallic connector used for coaxial copper RF cables, not optical fiber.

**3. Answer: B**  *[Hardware]*

- B. Trusted Platform Module (TPM)

The Trusted Platform Module (TPM) stores the key material BitLocker uses to unlock the drive automatically. A new motherboard brings a different TPM (or a cleared firmware TPM), so the stored binding no longer matches and Windows demands the recovery key; the technician must enable the TPM in UEFI and re-protect the drive. Secure Boot keys verify bootloader signatures but do not hold the volume key. SATA controller mode governs how the drive is presented to the OS, not key storage. A BIOS administrator password only locks access to firmware settings.

**4. Answer: A**  *[Virtualization and Cloud Computing]*

- A. Configure the VM network adapter to host-only or disconnected mode, and disable shared host-guest folders.

Isolating the virtual machine network adapter by placing it in host-only or disconnected mode prevents network-aware malware from scanning or spreading to other devices on the physical local area network. Disabling shared host-guest folders prevents file-encrypting malware or executable code from jumping out of the sandbox to infect the host filesystem. Bridged mode places the guest VM directly onto the physical local network as an active node, exposing other corporate endpoints to infection. Enabling host drive passthrough provides a direct pipeline for malware to write files onto physical host drives. Promiscuous mode allows the interface to capture all local network frames, which leaves the VM fully connected to the active production network.

**5. Answer: C, D**  *[Mobile Devices]*

- C. eSIM
- D. Over-the-air (OTA) provisioning

eSIM (embedded SIM) is a programmable integrated chip built into the device that replaces physical plastic SIM cards. Over-the-air (OTA) provisioning allows cellular operators to push carrier profile data and network subscriptions directly to the eSIM via an internet connection. Micro-SIM is a legacy physical card form factor requiring physical swapping. NFC payment profiles are used for short-range contactless payments, not cellular network registration.

**6. Answer: C**  *[Virtualization and Cloud Computing]*

- C. Community cloud

A community cloud is shared by several organizations with common concerns, such as compliance requirements or a shared mission, and is not open to the general public. A hybrid cloud combines public and private clouds. A private cloud serves one organization only, and a public cloud is open to any customer.

**7. Answer: B**  *[Hardware]*

- B. OLED

OLED (Organic Light-Emitting Diode) technology uses self-emissive organic compounds where each individual pixel produces its own light. When displaying black, the corresponding OLED pixels turn off completely, achieving true black levels, infinite contrast ratios, and zero backlight bleed. In contrast, IPS LCD, TN LCD, and VA LCD displays all rely on liquid crystals modulating a separate, continuously illuminated LED backlight, which inevitably allows minor light leakage through dark pixels.

**8. Answer: B**  *[Hardware]*

- B. Apply a thin layer of thermal compound to the top surface of the CPU integrated heat spreader.

Thermal compound (thermal paste) must be applied to the top of the CPU's integrated heat spreader (IHS) immediately before mounting the heatsink to fill microscopic air gaps between the surfaces and ensure efficient heat transfer. Connecting the CPU fan power cable occurs after physical installation of the heatsink and fan assembly onto the motherboard. Entering the UEFI setup utility can only occur after the entire hardware assembly is completed and the PC is powered on. Fastening the heatsink retention clips before applying thermal compound would result in severe CPU overheating due to inadequate heat transfer across air gaps.

**9. Answer: D**  *[Networking]*

- D. VLAN

A Virtual Local Area Network (VLAN) allows an administrator to logically segment traffic into separate broadcast domains on a single physical managed switch, isolating network groups like guest users from corporate servers. Port forwarding maps public incoming network ports to internal private IP addresses on a router. MAC filtering restricts device access based on hardware physical addresses. A DMZ (demilitarized zone) is a physical or logical subnet exposed to untrusted networks, typically managed on a firewall.

**10. Answer: C**  *[Hardware]*

- C. Plenum-rated UTP

Plenum-rated Unshielded Twisted Pair (UTP) cabling is jacketed with fire-retardant materials designed to release minimal toxic fumes and low smoke when burned, making it required by safety codes for installation in air-handling spaces like plenums. Riser-rated cabling is intended for vertical runs between floors within non-plenum spaces and lacks the stringent fire safety rating required for plenum spaces. Direct-burial Shielded Twisted Pair (STP) cable is designed for underground exterior runs and possesses a thick, moisture-resistant jacket unsuitable for indoor HVAC plenums. PVC-coated coaxial cable uses polyvinyl chloride, which releases highly toxic gases and thick smoke when exposed to flame.

**11. Answer: D**  *[Networking]*

- D. Port 445

Server Message Block (SMB) operates on TCP port 445 and is used by Windows systems for file and printer sharing over networks. Port 21 is used by FTP for file transfers. Port 143 is used by IMAP for retrieving emails from a server. Port 389 is used by LDAP for directory service queries.

**12. Answer: A, B**  *[Hardware]*

- A. A modular PSU permits unused power cable harnesses to be completely detached from the main enclosure to improve internal case airflow.
- B. The +12V rail delivers primary high-amperage power to demanding components such as the CPU and PCI Express expansion cards.

The statement regarding the +12V rail delivering primary high-amperage power to demanding components like the CPU and PCIe graphics cards is correct because modern computer architectures draw the vast majority of their power from +12V rails. The statement that a modular PSU permits unused power cable harnesses to be detached is correct because modular design allows builders to connect only required cables, reducing internal wire clutter and maximizing chassis airflow. The statement regarding the +5V rail providing primary power to GPUs is incorrect because +5V is used for minor logic circuits, USB devices, and disk controller electronics, not heavy GPU loads. The statement about fixed-cable PSUs allowing individual wires to be unplugged is incorrect because non-modular (fixed) power supplies have permanently soldered internal wiring bundles that cannot be individually detached or replaced.

**13. Answer: A**  *[Virtualization and Cloud Computing]*

- A. Type 1 hypervisor

A Type 1 (bare-metal) hypervisor installs directly onto physical server hardware without requiring a host operating system. This reduces overhead, improves performance, and increases security, making it ideal for datacenter enterprise environments. A Type 2 hypervisor runs as an application on top of an existing host operating system (such as Windows or macOS), introducing resource overhead and OS dependencies. Application container hosts run containerized engines (like Docker) on top of an existing host kernel rather than virtualizing full hardware instances. A Virtual Desktop Infrastructure (VDI) agent is software installed inside guest operating systems to coordinate remote desktop streaming to client endpoints.

**14. Answer: D**  *[Hardware and Network Troubleshooting]*

- D. Migrate the wireless network configuration to operate on the 5 GHz or 6 GHz frequency band.

Migrating the wireless network to the 5 GHz or 6 GHz frequency bands moves traffic away from the 2.4 GHz band where standard microwave ovens emit strong electromagnetic interference (RF noise). Disabling WPA3 encryption does not alter physical radio frequency interference. Replacing switch cables with lower standard Cat 5 cables degrades wired backhaul performance without resolving wireless spectrum congestion. Enabling MAC address filtering controls network access authorization but has no effect on physical RF interference.

**15. Answer: C**  *[Networking]*

- C. Syslog server

A Syslog server receives, aggregates, and stores standardized event logs and diagnostic messages sent from network devices across the infrastructure. An NTP (Network Time Protocol) server synchronizes system clocks across devices. A proxy server handles client internet requests and caches web content. A DHCP server dynamically assigns IP addresses and network configuration settings to clients.

**16. Answer: C**  *[Mobile Devices]*

- C. Geofencing policies

Geofencing relies on location services (GPS, cellular triangulation, or local Wi-Fi) to set up virtual geographical boundaries. MDM systems can use geofencing triggers to automatically enforce specific security profile restrictions—such as disabling camera hardware—when a device enters a designated secure zone. Remote wiping completely erases corporate or device data, which is an emergency procedure for lost or stolen devices. Biometric enforcement requires fingerprint or facial scans to unlock devices. Application whitelisting restricts which software programs can run, but does not dynamically toggle hardware features based on physical device coordinates.

**17. Answer: A**  *[Hardware and Network Troubleshooting]*

- A. Port flapping

Port flapping describes a physical network interface rapidly transitioning between operational link up and link down states, usually caused by a damaged cable, bent RJ45 connector pins, a failing NIC, or port autonegotiation errors. High jitter refers to variability in packet arrival delays over a network connection, impacting real-time media like voice calls. External interference affects wireless signals or unshielded copper lines by inducing noise and frame loss rather than physical link toggling. A duplex mismatch occurs when one end of a link is configured for full-duplex and the other for half-duplex, resulting in degraded speed and late collisions while the physical link state usually remains connected.

**18. Answer: A**  *[Hardware and Network Troubleshooting]*

- A. Carefully clean out accumulated lint and debris from inside the charging port.

Cleaning out accumulated lint and debris from inside the charging port using a non-conductive tool is the correct initial step because compacted pocket debris prevents charging cable pins from seating completely, causing physical looseness and poor electrical contact. Soldering hardware, performing factory resets, or replacing internal batteries and logic chips are invasive and unnecessary prior to basic physical inspection and port cleaning.

**19. Answer: D**  *[Hardware]*

- D. Replace the printer ribbon cartridge.

Replacing the printer ribbon cartridge is correct because impact dot-matrix printers transfer ink to multi-part carbon forms via an ink-soaked fabric or film ribbon struck by printhead pins; faded output indicates the ink ribbon is depleted or dried out. Cleaning the thermal printhead with isopropyl alcohol is incorrect because thermal printheads belong to direct thermal receipt printers, not impact matrix printers. Replacing the primary corona wire assembly is incorrect because corona wires are components found in laser printers. Calibrating the printhead gap using heat-sensitive paper is incorrect because heat-sensitive paper is designed for thermal printers, and incorrect paper gap settings would affect impact depth rather than ink saturation.

**20. Answer: A**  *[Hardware]*

- A. Install the official PostScript (PS) or vendor-specific driver on the workstation.

Complex vector PDFs and specialized fonts rely on a page description language the printer can interpret; a mismatched driver (for example PCL where PostScript is needed, or the reverse) produces garbled text, stray symbols and blank pages. Installing the correct PostScript or vendor driver fixes this. Plain Word documents print fine, which shows the print engine and feed path work, so replacing the fuser, cleaning the pickup rollers or swapping toner would not change garbled output.

**21. Answer: A, B**  *[Networking]*

- A. 22
- B. 443

Port 22 is used by Secure Shell (SSH) for secure, encrypted command-line management. Port 443 is used by Hypertext Transfer Protocol Secure (HTTPS) for encrypted web communications. Port 23 is used by Telnet, which sends traffic in unencrypted plain text and should be avoided. Port 80 is used by HTTP, which sends web traffic in unencrypted clear text.

**22. Answer: A**  *[Networking]*

- A. Create a DHCP reservation matching the printer's MAC address

A DHCP reservation links a specific IP address within a DHCP scope to the unique MAC address of a host interface, ensuring that host always receives the same IP address dynamically from the DHCP server. Adding the address to an exclusion pool prevents the DHCP server from issuing that address to any host, requiring static manual configuration on the device itself. Setting lease time to zero is invalid or causes immediate expiration. A CNAME record maps hostnames in DNS, not IP addresses in DHCP.

**23. Answer: B**  *[Hardware and Network Troubleshooting]*

- B. Damaged photosensitive drum

A damaged or scratched photosensitive drum cannot hold its electrostatic charge along the damaged ring or line, causing toner to continuously stick to that region and transfer onto paper as a solid vertical line. Dirty pickup rollers cause paper misfeeds or surface smudges on page edges, not continuous straight toner lines. Misaligned duplexing assemblies cause crooked double-sided printing or paper jams. Ink delivery nozzles exist on inkjet printers, not laser printers.

**24. Answer: B**  *[Mobile Devices]*

- B. Power down the device, disconnect external power, and safely remove the swollen battery.

A visibly bulging case, sticking keys, and raised trackpad indicate a swollen lithium-ion battery. This represents a severe safety hazard due to potential thermal runaway and chemical fire. The technician must immediately power off the laptop, disconnect AC power, and follow hazardous material handling procedures to remove and replace the battery. Running thermal or benchmark tests puts high electrical load and heat on the battery, increasing the explosion risk. Pressing down on a swollen battery can puncture the chemical cells, causing violent ignition.

**25. Answer: D**  *[Mobile Devices]*

- D. Background data restriction is enabled for the corporate email application.

Mobile operating systems feature data-saver settings that allow users or admins to restrict background data usage on a per-app basis over cellular networks. If restricted, the email application cannot fetch updates in the background on cellular networks, while unmanaged apps like web browsers continue to function. Blocking the IMEI would shut off all cellular data access entirely. GPS location services are not required for email protocol traffic. A misseated SIM card would prevent all cellular data connectivity, not selectively block background updates for one application.

**26. Answer: A**  *[Virtualization and Cloud Computing]*

- A. Egress data transfer fees

Egress data transfer fees are charges incurred when data leaves (exits) a cloud provider's network to be sent to an external location, such as an on-premises datacenter or another cloud. Cloud providers often offer free ingress (data coming into the cloud) but charge metered rates for network egress. Ingress metered storage charges apply to data entering the cloud, which is generally not billed per gigabyte of network movement by public providers. Rapid elasticity refers to auto-scaling system resources based on real-time application load. Multitenancy resource allocation refers to shared physical host resources among multiple customers, which is reflected in baseline instance compute costs, not outbound traffic spikes.

**27. Answer: D**  *[Hardware and Network Troubleshooting]*

- D. Separation pad

The separation pad works in tandem with the paper pickup roller to create precise friction that allows only one sheet of paper to feed into the print path at a time. When worn smooth, multiple pages slip through together. The transfer roller applies an electrical charge to draw toner from the photosensitive drum onto the paper. The fuser assembly uses heat and pressure to melt toner into paper fibers. Corona wires apply high electrostatic voltages during charging or transfer operations and do not physically regulate paper feeding.

**28. Answer: A**  *[Networking]*

- A. MAN (Metropolitan Area Network)

MAN (Metropolitan Area Network) is correct because a MAN covers a geographical area larger than a single building or localized group of buildings but smaller than a wide area network (WAN), typically spanning a city, town, or municipal region. LAN (Local Area Network) is restricted to a small geographical site, such as a single floor, office space, or single building. SAN (Storage Area Network) is a high-speed dedicated network designed specifically to connect block-level storage devices to virtual servers. PAN (Personal Area Network) covers a very short operational range centered around an individual person or device, typically using Bluetooth.

**29. Answer: A**  *[Hardware and Network Troubleshooting]*

- A. Clogged intake dust filters restricting airflow and causing thermal overload

Clogged intake dust filters restricting airflow and causing thermal overload is correct because trapped dust prevents proper air circulation, causing internal temperatures to rise until the thermal safety threshold triggers an automatic shutdown accompanied by a temperature error LED. A blown projector lamp filament is incorrect because a blown bulb prevents light output entirely and causes immediate illumination failure, not a delayed thermal shutdown. An incorrect aspect ratio setting causes image stretching, not internal projector overheating. A degraded HDMI cable causes video artifacting or signal loss, not a thermal shutdown on the projector hardware.

**30. Answer: B**  *[Hardware and Network Troubleshooting]*

- B. Check CPU thermal sensor readings in the UEFI/BIOS environment.

Checking CPU thermal sensor readings in the UEFI/BIOS environment is the best next step because the symptom of operating normally for a short period before abruptly shutting down—and then shutting down even faster upon immediate reboot—indicates thermal protection circuit triggering due to CPU overheating. Replacing the power supply unit is premature without first confirming thermal conditions versus power delivery issues. Reseating memory modules addresses POST beep errors or memory instability crashes, not delayed thermal cutoffs. Running a chkdsk scan diagnoses file system or drive sector errors, which result in blue screen errors or operating system freezes rather than sudden hardware power cutoffs.

**31. Answer: A**  *[Hardware]*

- A. Install both modules in the slot pair the motherboard manual designates for dual-channel operation (typically the same-colored slots).

Dual-channel operation requires the modules to sit on different memory channels, and the slot pair that achieves this is board-specific (often alternate, same-colored slots such as A2 and B2). The technician should follow the motherboard manual. Two modules on the same channel run single-channel. No UEFI setting can create a second channel from a single module, and distance from the CPU has no bearing on channel assignment.

**32. Answer: A**  *[Mobile Devices]*

- A. Proprietary docking station

A proprietary docking station attaches to custom bottom or side bus expansion connectors provided by specific business-class laptop lines. These offer high bandwidth for multi-monitor arrays, power delivery, and specialized peripheral connectivity. USB-C port replicators attach via standard USB ports and typically offer fewer high-bandwidth video channels and lower power pass-through compared to proprietary dock interfaces. Bluetooth expansion hubs lack the bandwidth for multiple high-resolution video streams and cannot charge a laptop. Wireless display adapters mirror video content over the air without providing wired expansion ports or power.

**33. Answer: C, D**  *[Virtualization and Cloud Computing]*

- C. Rapid elasticity
- D. High availability

Rapid elasticity is the ability of cloud environments to automatically provision (scale out) and de-provision (scale in) processing, memory, and storage resources on demand based on current workload. High availability ensures that services remain accessible without interruption through redundant systems and automatic failover mechanisms. Multitenancy describes multiple distinct customers sharing physical underlying hardware resources, which does not directly dictate automatic dynamic scaling capabilities. Measured ingress billing relates to tracking inbound network bandwidth consumption rather than compute availability or elastic resource scaling.

**34. Answer: C**  *[Networking]*

- C. AAA server

An Authentication, Authorization, and Accounting (AAA) server (such as RADIUS or TACACS+) handles centralized network access control by validating user credentials submitted via 802.1X before granting network access. A load balancer distributes incoming network traffic across multiple application servers. A spam gateway filters incoming email for junk and malicious attachments. A web proxy inspects, filters, and caches web browsing traffic for clients.

**35. Answer: B, D**  *[Hardware and Network Troubleshooting]*

- B. Run the built-in digitizer calibration utility within the operating system settings.
- D. Clean the screen surface thoroughly and inspect for dirt, moisture, or a damaged screen protector.

Running the digitizer calibration utility aligns touch input coordinates with screen pixels, while cleaning the screen surface removes dirt, oils, moisture, or trapped air bubbles under protective films that disrupt capacitive touch sensing and cause ghost touches. Replacing the graphics processing unit addresses video rendering glitches, not touch input offset. Replacing antenna cables addresses wireless connectivity drops, not digitizer accuracy.

**36. Answer: A**  *[Hardware]*

- A. RAID 6

RAID 6 is correct because it uses dual distributed parity block striping across all member drives, allowing the array to maintain full operation and data integrity even if any two drives fail simultaneously. RAID 0 is incorrect because it offers block striping with zero redundancy; a single drive failure results in total data loss. RAID 1 is incorrect because it relies on simple disk mirroring (typically across two drives) and lacks multi-drive block striping efficiency across six drives. RAID 5 is incorrect because it uses single distributed parity and can only tolerate the failure of a single drive at a time; a second simultaneous failure causes total array failure.

**37. Answer: A, D**  *[Networking]*

- A. MX
- D. TXT

MX (Mail Exchanger) records are correct because they direct incoming email traffic for a domain to the appropriate receiving mail servers. TXT (Text) records are correct because they hold arbitrary text data, which is standard for publishing DKIM public keys, SPF rules, and DMARC policies. CNAME (Canonical Name) records map alias hostnames to canonical hostnames, not incoming email delivery routes. AAAA records map hostnames directly to IPv6 addresses.

**38. Answer: C**  *[Hardware and Network Troubleshooting]*

- C. Defective or low-bandwidth video cable

A defective or low-bandwidth video cable fails to carry the required signal frequency and bandwidth for high-resolution displays, leading to screen flickering, dropping sync, and rapid display blanking. Replacing the faulty cable restores stable data transmission. An overheating graphics processing unit would impact both connected displays or cause system-wide crashes and rendering artifacts. An LCD backlight thermal shutdown would keep the screen black permanently until cooled and restarted. An incorrect refresh rate setting typically results in an 'Out of Range' warning or constant distortion rather than intermittent link loss fixed by a cable replacement.

**39. Answer: A, B**  *[Hardware and Network Troubleshooting]*

- A. The damaged capacitors are a hardware fault that software changes cannot fix, so the motherboard should be replaced or professionally repaired.
- B. The symptoms are caused by electrolyte fluid leaking, altering power filtering to system components.

Bulging or leaking capacitors reflect physical breakdown of the components that filter DC power for the CPU and other hardware. Leaking electrolyte degrades filtering, producing dirty power, spontaneous restarts and POST failures. The fault cannot be fixed with software changes, so the board should be replaced (or the capacitors replaced by a qualified repair technician). Upgrading the operating system does not affect voltage regulation, and reseating RAM or the CPU cannot restore damaged capacitors.

**40. Answer: C**  *[Hardware and Network Troubleshooting]*

- C. Stop the Print Spooler service, delete the files in the PRINTERS folder, and restart the service

Stopping the Print Spooler service, deleting the temporary spool files in the PRINTERS directory, and restarting the service is correct because stuck or corrupted print jobs locked in the Windows spooler folder prevent subsequent jobs from processing until the spooler service is reset and cleared. Performing a factory reset on the printer's network card is incorrect because the issue is isolated to the local computer's spooler software queue, not the physical printer hardware. Replacing the drum unit and toner cartridge is incorrect because physical print engine consumables do not cause software spooler file locks on the workstation. Reinstalling the driver using an LPR port does not clear locked spool files from the active spooling directory.

**41. Answer: B**  *[Networking]*

- B. ONT

An Optical Network Terminal (ONT) is used in fiber-optic communications (such as FTTP/FTTH) to convert incoming optical signals into electrical Ethernet signals suitable for connecting to a router or switch. A cable modem converts coaxial cable (DOCSIS) signals. A DSL modem converts digital signals over copper twisted-pair telephone lines. A patch panel is a passive pass-through board used to organize cable runs.

**42. Answer: C**  *[Virtualization and Cloud Computing]*

- C. Client-side file synchronization

Client-side cloud file synchronization maintains local copies of stored cloud files on client devices, allowing offline edits that automatically perform two-way updates with the cloud storage platform when an active network connection is established. Application virtualization streams software applications directly to endpoints without installing full local software packages, but it requires active network connections to stream execution logic. Virtual machine snapshotting saves a point-in-time state of an entire VM virtual disk and RAM for backup and restoration. Metered resource utilization is an administrative billing tracking feature based on active consumption.

**43. Answer: D**  *[Hardware and Network Troubleshooting]*

- D. Switch the boot mode back to UEFI in the firmware settings and save changes.

Switching the boot mode back to UEFI in firmware settings resolves the issue because modern NVMe drives holding operating system installations formatted with GUID Partition Table (GPT) require native UEFI boot mode to load the bootloader. If power loss reset firmware defaults to Legacy/CSM, the system cannot locate the UEFI boot partition. Reformatting the drive destroys data unnecessarily. Replacing the drive is unneeded since the storage controller is detected and functional. Reseating the NVMe SSD will not fix a software setting mismatch in firmware.

**44. Answer: C**  *[Hardware]*

- C. PCIe x16

PCIe x16 expansion slots provide 16 full lanes of high-speed serial communication, making them the standard installation slot for modern dedicated graphics processing units (GPUs) that require high bandwidth. PCI 32-bit is a legacy parallel bus standard with low bandwidth and is obsolete for modern video cards. PCIe x1 slots provide only a single data lane, suitable for low-bandwidth expansion cards like network interface cards or sound cards. M.2 Key E slots are compact form-factor slots typically used for Wi-Fi and Bluetooth wireless network adapters, not desktop expansion graphics cards.

**45. Answer: D**  *[Hardware and Network Troubleshooting]*

- D. CMOS battery

The CMOS battery (typically a CR2032 coin cell) supplies power to maintain system time (RTC) and retain non-volatile firmware settings when main AC power is cut off. A depleted CMOS battery causes date/time reset errors whenever wall power is removed. A main power supply failure would prevent the system from powering on altogether. The real-time clock crystal provides the frequency signal for keeping time while powered, but failure to hold time only when unplugged points directly to the battery. The TPM security module stores encryption keys, not clock backup power.

**46. Answer: A**  *[Hardware and Network Troubleshooting]*

- A. Clean off old thermal residue with isopropyl alcohol and reapply fresh thermal paste

Cleaning off old thermal residue with isopropyl alcohol and reapplying fresh thermal paste is correct because thermal paste fills microscopic air gaps between the CPU heat spreader and the heat sink, enabling effective heat transfer; missing or dried paste leads to severe thermal throttling and sluggish performance under heavy workloads. Replacing the main 24-pin ATX power connector is incorrect because power supply delivery issues typically cause immediate shutoffs or failure to power on rather than delayed thermal throttling. Clearing the motherboard CMOS memory resets system configuration settings but does not resolve physical heat dissipation issues. Upgrading from DDR4 to DDR5 RAM does not resolve CPU overheating and is structurally incompatible without replacing the motherboard.

**47. Answer: A**  *[Hardware]*

- A. EPS12V cables deliver +12V power on different pinouts than PCIe cables, and plugging the wrong cable into a motherboard or GPU can cause an electrical short circuit.

Although EPS12V (CPU power) and PCIe power connectors can both feature 8-pin physical layouts (often split as 4+4 for CPU and 6+2 for PCIe), their electrical pinouts and square/rounded keying patterns are completely different. Forcing an EPS12V cable into a GPU power slot or a PCIe cable into a motherboard CPU power socket reverses ground and +12V power pins, resulting in short circuits, melted cables, or severe hardware failure. EPS12V cables carry +12V DC power directly to the CPU power regulation circuits, not +5V DC fan power or AC wall voltage. Both CPU and GPU power cables are used regardless of whether the system uses liquid or air cooling. EPS12V connectors use an 8-pin (or 4+4 pin) layout, while 20+4 pin connectors are main ATX motherboard power cables; 34-pin ribbon connectors were used for legacy floppy disk drives.

**48. Answer: A, D**  *[Mobile Devices]*

- A. Establishing a USB tethering connection from the smartphone to the laptop
- D. Enabling Wi-Fi Mobile Hotspot on the smartphone

Enabling a Wi-Fi Mobile Hotspot configures the smartphone to act as a local wireless access point, sharing its cellular internet connection with nearby client devices. USB tethering routes the smartphone's cellular connection directly to the laptop via a USB cable. NFC peer-to-peer is designed for tiny data transfers (like contacts or URLs) over fractions of an inch, not continuous broadband network sharing. Bluetooth Low Energy beacons transmit proximity data for location tracking and do not route IP internet traffic.

**49. Answer: A**  *[Hardware]*

- A. Photosensitive image drum

A damaged or improperly discharged photosensitive image drum retains residual electrical charges from previous rotations, causing toner to stick to uncharged areas and producing faint repeating 'ghost' images down the page at regular distance intervals matching the drum's circumference. The fuser assembly uses heat and pressure to permanently melt toner into paper fibers; a fuser failure typically causes smudges, unbonded toner that rubs off, or paper jams. The primary corona wire (or charge roller) applies a uniform negative charge to the drum prior to laser writing; a failure here usually leads to all-black pages or heavy background streaking. The duplexing assembly flips paper to allow double-sided printing and has no effect on image repetition.

**50. Answer: A**  *[Networking]*

- A. 802.11ax (Wi-Fi 6E)

802.11ax (specifically Wi-Fi 6E) extends the 802.11ax standard into the 6 GHz frequency band, offering high throughput and reduced interference. 802.11ac (Wi-Fi 5) operates exclusively in the 5 GHz band. 802.11n (Wi-Fi 4) operates in both 2.4 GHz and 5 GHz bands. 802.11g operates strictly in the 2.4 GHz band.

**51. Answer: D**  *[Mobile Devices]*

- D. Containerization

Containerization creates an isolated, encrypted logical partition on a mobile device that separates corporate applications and data from personal content. This allows administrators to perform a selective enterprise wipe that removes only corporate data while leaving personal photos and applications intact. Full device disk encryption protects data at rest across the entire device but does not allow selective wiping. Remote locking prevents access to the device screen, but does not purge corporate data. Geofencing applies policies based on geographic location, not selective data separation and wiping.

**52. Answer: A, C**  *[Hardware and Network Troubleshooting]*

- A. A failing or miscalibrated touch digitizer
- C. A swollen internal lithium-ion battery exerting pressure on the display assembly

A swollen internal lithium-ion battery exerting pressure on the display assembly is correct because battery gas expansion presses against the back of the glass, placing mechanical pressure on internal components and triggering false touch events. A failing or miscalibrated touch digitizer is correct because the digitizer component interprets touch inputs, and a hardware defect or physical stress causes phantom touches and cursor drift. A damaged SIM card socket is incorrect because SIM cards handle cellular subscriber identification and do not influence screen touch registration. A high-latency Wi-Fi network connection is incorrect because network latency impacts wireless data transfers, not local touch hardware digitizer tracking.

**53. Answer: C**  *[Networking]*

- C. Cable crimper

A cable crimper is correct because it presses the metal pin contacts inside an RJ-45 modular plug into the individual conductor wires while clamping the strain-relief boot around the outer jacket. A punchdown tool is used to push individual wires into insulation displacement connector (IDC) blocks on patch panels or keystone wall jacks. A cable tester is used after termination to test pinouts and electrical continuity. A wire stripper is used beforehand to remove the protective outer jacket of the cable without cutting the internal copper conductors.

**54. Answer: B**  *[Hardware]*

- B. The dual-voltage selector switch on the power supply was left set to 115V.

Non-auto-sensing power supply units (PSUs) feature a manual dual-voltage switch toggling between 115V AC (North America) and 230V AC (Europe). Plugging a PSU set to 115V into a 230V wall outlet delivers twice the expected voltage, instantly blowing internal capacitors and damaging the unit. Unseating the main ATX power connector would prevent the system from receiving power entirely, causing no sound or smoke. Power supplies convert incoming AC power from the wall into DC power for internal components, not DC to AC. Voltage selector switches adjust input AC voltage acceptance; PCIe cables deliver 12V DC to expansion cards and do not process AC wall current or frequency.

**55. Answer: A, B**  *[Hardware]*

- A. Touchscreen digitizer panel overlay
- B. Touchscreen digitizer flex ribbon cable connection

Touch input functionality on mobile devices relies on the digitizer panel overlay (which senses physical touch) and its digitizer flex ribbon cable connection to the system motherboard. If the digitizer ribbon cable is unseated, damaged, or disconnected during assembly, touch inputs will fail entirely while image rendering remains unaffected. The display backlight inverter circuit provides high-voltage AC power to older CCFL display backlights (or controls lighting levels) and does not process touch inputs. The LCD panel data bus cable carries video signal data from the GPU to display visual pixels on screen; since the tablet shows clear visual images, this video data cable is connected and functioning properly.

**56. Answer: D**  *[Virtualization and Cloud Computing]*

- D. Virtual Desktop Infrastructure (VDI) using thin clients

Virtual Desktop Infrastructure (VDI) centralizes desktop operating system processing on servers in a datacenter, streaming screen updates down to low-power endpoints known as thin clients. Software as a Service (SaaS) provides individual web applications rather than complete remote desktop operating system sessions, and thick clients perform heavy processing locally on the client hardware. Application containerization isolates server microservices on shared OS kernels rather than hosting remote desktop sessions. Local peer-to-peer virtualization runs virtual machines on local user hardware rather than centralizing execution on server clusters.

**57. Answer: A**  *[Hardware and Network Troubleshooting]*

- A. Keep the tablet powered off, disconnect the battery if accessible, and let it dry completely before attempting to power it on.

After liquid exposure the device must stay powered off so current does not short wet circuitry; the technician should disconnect the battery if it is accessible, check the liquid contact indicators, and allow the device to dry thoroughly before trying to power it on. Charging a wet device risks shorting and corrosion, a hot oven can damage the battery, display and housing, and a factory reset requires powering the device on.

**58. Answer: C**  *[Virtualization and Cloud Computing]*

- C. The host system has insufficient RAM remaining to support hypervisor resource overhead and the host operating system.

Allocating all 32 GB of physical host RAM directly to guest virtual machines (4 VMs x 8 GB = 32 GB) leaves zero physical memory for the host operating system and hypervisor tasks. This memory starvation forces the host system to swap data out to the disk pagefile/swap file, causing severe system instability and slowdown. Type 1 hypervisors manage quad-core processors efficiently and are fully capable of distributing RAM when host overhead memory is factored in. Containers share the host kernel and do not lock dedicated guest RAM allocations in this hypervisor pattern. Disk space overcommitment affects storage drive capacity over time, not host system RAM exhaustion, and cannot corrupt motherboard firmware settings.

**59. Answer: C**  *[Mobile Devices]*

- C. Near Field Communication (NFC)

Near Field Communication (NFC) operates at short ranges (typically 1–4 centimeters), enabling secure digital transactions like Apple Pay and Google Wallet by bringing the smartphone into close proximity with the reader terminal. Infrared requires direct line-of-sight and is mostly used for remote controls. Active RFID tag broadcasting operates across much larger physical distances (up to hundreds of feet) and is used for asset tracking, not mobile payment standard protocols. Wi-Fi Direct is intended for peer-to-peer device networking and file transfer over longer distances.

**60. Answer: B, C**  *[Hardware]*

- B. Clean the thermal printhead using an isopropyl alcohol swab.
- C. Verify or replace the roll of direct thermal paper.

Direct thermal printers use heating elements on a printhead to react with heat-sensitive direct thermal paper. Over time, residue accumulates on the printhead, causing faint or streaked output; cleaning the printhead with isopropyl alcohol restores heat transfer efficiency. Additionally, thermal paper can degrade over time or be inserted incorrectly; replacing it with fresh heat-sensitive paper ensures dark, legible printing. Impact ink ribbons are used in dot-matrix/impact printers, not thermal printers. Laser transfer rollers and lasers are components of electrophotographic laser printers, not thermal receipt printers.

**61. Answer: A**  *[Hardware]*

- A. USB-C cable supporting USB 3.2 Gen 2 / Thunderbolt

USB-C cables supporting high-speed protocols (such as USB 3.2 Gen 2 or Thunderbolt) utilize Alt Modes (such as DisplayPort Alternate Mode) and USB Power Delivery (USB-PD) to stream high-resolution video, transfer fast data, and supply power to charge host laptops simultaneously over one reversible connector. HDMI 2.0 cables carry digital audio and video signals but do not support host laptop charging or high-speed USB data bus protocols. DisplayPort to DVI-D cables transmit video signals only and lack data/power capabilities. DB9 serial RS-232 cables are legacy low-speed serial diagnostic interfaces incapable of transmitting video, modern data streams, or laptop charging power.

**62. Answer: C**  *[Virtualization and Cloud Computing]*

- C. Containerization

Containerization (such as Docker or Podman) isolates applications at the OS level, allowing containers to share the host system's kernel while keeping application processes and dependencies separated. This results in extremely fast boot times, low memory overhead, and high density. Type 1 and Type 2 hypervisors create full hardware virtualization where each guest requires its own dedicated operating system kernel, resulting in higher resource overhead and slower startup times. Virtual Desktop Infrastructure (VDI) delivers full desktop environments to end-user displays rather than packaging lightweight server microservices.

**63. Answer: A**  *[Networking]*

- A. WISP

A Wireless Internet Service Provider (WISP) delivers broadband internet using fixed wireless technology, transmitting radio signals between a centralized tower and directional antennas mounted at customer premises. Satellite internet relies on geostationary or low-Earth orbit satellites in space rather than terrestrial towers. DSL delivers internet over traditional copper telephone lines. Cable uses coaxial cable infrastructure provided by cable television companies.

**64. Answer: B**  *[Hardware]*

- B. RAID 0

RAID 0 (striping) provides the highest performance by splitting data across multiple drives without parity or mirroring, resulting in 100% usable storage capacity with no overhead. However, it offers zero fault tolerance. RAID 1 uses mirroring, which cuts usable capacity in half (50% loss). RAID 5 uses block-level parity, requiring at least three drives and losing the capacity of one drive to parity overhead. RAID 10 combines mirroring and striping, sacrificing 50% of total storage capacity for redundancy.

**65. Answer: C**  *[Networking]*

- C. The workstation failed to reach a DHCP server and self-assigned an APIPA address

An IP address beginning with 169.254.x.x indicates an Automatic Private IP Addressing (APIPA) assignment. Windows automatically assigns an APIPA address when a client configured for dynamic IP addressing cannot communicate with a DHCP server. Duplicate static IP conflicts result in OS error notifications. Loss of ISP WAN connection affects internet access but does not prevent a client from receiving a valid local IP from a DHCP server. Invalid DNS entries cause name resolution failures but do not cause APIPA addresses to be assigned.

**66. Answer: B**  *[Hardware]*

- B. In-Plane Switching (IPS)

In-Plane Switching (IPS) offers the best color accuracy and widest viewing angles of the common LCD panel types, which suits graphic design. Twisted Nematic (TN) offers fast response times but poor color accuracy and narrow viewing angles. Vertical Alignment (VA) offers high contrast and deep blacks but weaker viewing angles and color precision than IPS. A resistive touch overlay is an input layer, not a display panel technology.

**67. Answer: B, C**  *[Hardware]*

- B. Mini-ITX motherboards feature only a single PCIe expansion slot, limiting internal expansion cards to a single adapter.
- C. The motherboard form factor dimensions must align with the physical mounting standoff locations inside the computer chassis.

The statement that Mini-ITX motherboards feature only a single PCIe expansion slot is correct because the standard Mini-ITX form factor specification (6.7 x 6.7 inches) physically accommodates only one expansion slot. The statement that the motherboard form factor dimensions must align with standoff locations in the chassis is correct because mounting a motherboard in an incompatible case prevents proper securing and can cause short circuits against the metal frame. The statement that MicroATX motherboards cannot accept liquid CPU cooling assemblies is incorrect because CPU liquid coolers mount to standard CPU socket brackets and fan/pump headers regardless of motherboard form factor. The statement that PCIe x1 cards cannot be installed into PCIe x16 slots is incorrect because PCI Express specifications support upward slot compatibility, allowing shorter cards (x1, x4) to function normally inside longer physical slots (x16).

**68. Answer: D**  *[Mobile Devices]*

- D. The Wi-Fi antenna cables were not properly reconnected to the internal wireless card.

Disconnected or pinched Wi-Fi antenna wires inside the display assembly are a common issue following screen replacements. Because the antenna leads run up into the display bezel to maintain range, failing to attach them firmly to the wireless card results in severely reduced Wi-Fi reception, operating only when extremely close to an access point. LCD panels do not generate RF interference that selectively blocks Wi-Fi bands. Physical disassembly of the display housing does not cause software driver corruption. Unseated RAM modules would cause boot failure or system instability, not low Wi-Fi signal strength.

**69. Answer: B**  *[Networking]*

- B. Toner probe

A toner probe (consisting of a tone generator connected to the wall outlet and an inductive probe swept across patch panel cables) is designed to trace unlabelled copper cable runs through walls and identify specific cable terminations. A cable tester checks pinout continuity and wire pairs after a connection is found. A loopback plug tests a physical port on a network interface card or switch port. A Wi-Fi analyzer measures wireless signal strength and radio frequencies.

**70. Answer: A**  *[Mobile Devices]*

- A. Replace or recharge the battery inside the active stylus and verify its Bluetooth pairing.

Active styluses contain internal electronics, pressure sensors, and Bluetooth radios that require battery power. When normal finger input works reliably on the tablet, the screen digitizer hardware is fully functional; therefore, a dead stylus battery or lost Bluetooth connection is the most likely cause. Replacing the screen digitizer is unnecessary since touch registration works. Display color calibration adjusts color reproduction, not input registration. RAM capacity does not affect active stylus connectivity or power status.

**71. Answer: B, C**  *[Hardware and Network Troubleshooting]*

- B. Initiate an array rebuild through the RAID management utility once the new drive is seated.
- C. Perform a hot-swap replacement of the failed physical drive with a compatible spare drive.

Performing a hot-swap replacement of the failed physical drive and initiating an array rebuild through the RAID management software are the correct steps to restore fault tolerance and redundancy to a degraded RAID 5 volume without data loss. Re-initializing the RAID array volume wipes all existing data from the array completely. Converting the remaining active drives to a RAID 0 configuration destroys the original volume structure and removes all fault tolerance.

**72. Answer: C**  *[Hardware and Network Troubleshooting]*

- C. Back up critical data from the drive to a secure location immediately

Backing up critical data from the drive immediately is correct because metallic clicking noises and S.M.A.R.T. threshold errors signal imminent mechanical hardware failure, making immediate data preservation the highest priority before the drive stops functioning completely. Running a full defragmentation scan is incorrect because the heavy read/write activity required for defragmentation will stress the failing mechanical components and accelerate complete drive failure. Converting the partition table from MBR to GPT is a partition management task that does not fix physical mechanical degradation. Rebuilding the drive using a SATA RAID controller is incorrect because a single standalone failing drive lacks redundancy and cannot be rebuilt without a pre-existing RAID array.

**73. Answer: C**  *[Hardware]*

- C. NVMe

Non-Volatile Memory Express (NVMe) is an open host controller interface specification designed specifically for solid-state drives (SSDs) operating over PCIe lanes, delivering massive throughput and low latency compared to legacy storage protocols. SATA III relies on the AHCI protocol designed for spinning hard drives and is bottlenecked at 6 Gbps. eSATA is an external variant of SATA III and suffers from the same throughput limits and protocol overhead. Serial Attached SCSI (SAS-3) is an enterprise storage protocol primarily used for high-availability SAS drives and storage arrays, but standard SAS interfaces do not connect directly over consumer/workstation PCIe storage host protocols with the reduced latency overhead of native NVMe.

**74. Answer: D**  *[Networking]*

- D. Network Time Protocol (NTP)

Network Time Protocol (NTP) is correct because NTP synchronizes clock timing across all client devices and servers on a network, which is critical for time-sensitive security protocols such as Kerberos and time-based multi-factor authentication (MFA). Domain Name System (DNS) resolves hostnames to IP addresses but does not synchronize clocks. Dynamic Host Configuration Protocol (DHCP) automatically assigns IP addressing configurations to network clients. Simple Network Management Protocol (SNMP) is used for monitoring and managing network hardware devices, not system clock synchronization.

**75. Answer: D**  *[Hardware]*

- D. ECC DDR4 DIMMs that the motherboard supports

Error-correcting code (ECC) memory carries extra bits and circuitry that detect and correct single-bit errors, which prevents crashes and silent data corruption in servers; the board and CPU must support ECC. Non-ECC modules cannot correct errors. SODIMMs are the smaller laptop form factor and say nothing about error correction. DDR3 modules are not compatible with a DDR4 slot.

**76. Answer: A**  *[Hardware and Network Troubleshooting]*

- A. Implement Quality of Service (QoS) prioritizing voice traffic

Implementing Quality of Service (QoS) prioritizing voice traffic is correct because VoIP audio is extremely sensitive to packet delay variation (jitter); QoS marks real-time voice packets to ensure they are queued and forwarded ahead of standard data traffic during bursts of switch activity. Changing switch port negotiation to half-duplex is incorrect because half-duplex permits collision domains, which increases packet drops and latency. Enabling Jumbo Frames is used to optimize high-throughput file or storage transfers (such as SAN traffic), not small, frequent voice packets. Configuring static IP reservations ensures consistent IP address assignment but does not prioritize or schedule traffic queues on the switch.

**77. Answer: A, C**  *[Networking]*

- A. AAAA record
- C. A record

An A record maps a domain name or hostname to a 32-bit IPv4 address, while an AAAA record maps a domain name or hostname to a 128-bit IPv6 address. An MX (Mail Exchanger) record directs domain email traffic to specified mail servers. A CNAME (Canonical Name) record creates an alias that maps one domain name to another canonical domain name rather than an IP address.

**78. Answer: C, D**  *[Mobile Devices]*

- C. Verify that the Bluetooth headset is within standard physical operating range of the phone.
- D. Place the Bluetooth headset into discovery mode by pressing and holding its power/pairing button.

For a Bluetooth host device to discover a target peripheral, the peripheral must be put into pairing/discovery mode (often indicated by a flashing LED after holding the power button). Additionally, Bluetooth devices must be within operating range (typically around 30 feet / 10 meters) to establish initial pairing. Resetting TCP/IP network stack settings targets Wi-Fi and IP address routing issues, not local Bluetooth discovery. SIM cards control cellular network authentication and have no involvement in Bluetooth connections.

**79. Answer: C**  *[Networking]*

- C. LDAP on TCP port 389

LDAP on TCP port 389 is correct because standard, unencrypted Lightweight Directory Access Protocol uses TCP port 389 to perform directory queries against Active Directory or directory services. LDAPS uses TCP port 636 for secure, encrypted directory access over TLS/SSL. SMB uses TCP port 445 for Windows file sharing and network folder access. RDP uses TCP port 3389 for remote desktop protocol sessions on Windows servers and workstations.

**80. Answer: A**  *[Mobile Devices]*

- A. Webcam wiring harness running through the display hinge

The webcam cable harness routes from the motherboard, through the screen hinge, and into the top display frame. Constant flex from opening and closing the screen lid can cause wires inside the hinge harness to fray or loosen, resulting in intermittent connections that depend on screen position. GPU failures would cause graphical artifacts across the entire LCD screen, not intermittent webcam loss tied to screen tilt. The CMOS battery retains BIOS settings and does not power webcams. The ambient light sensor adjusts display backlight brightness, not webcam video signal continuity.

**81. Answer: A**  *[Virtualization and Cloud Computing]*

- A. Platform as a Service (PaaS)

Platform as a Service (PaaS) provides developers with a pre-configured software framework, runtime environment, and database management engines where they can deploy custom code without managing operating systems, hardware provisioning, or network infrastructure. Infrastructure as a Service (IaaS) requires the customer to manage and patch operating systems, virtual machines, and installed software stack components. Software as a Service (SaaS) provides fully functional, end-user applications managed entirely by the vendor (such as Microsoft 365 or Salesforce). Desktop as a Service (DaaS) provisions full virtual desktop environments to end users rather than development execution stacks.

**82. Answer: B**  *[Hardware and Network Troubleshooting]*

- B. The projector bulb is reaching the end of its operational lifespan.

A uniformly dim image without color distortion or thermal shutdown warnings indicates that the projector lamp/bulb is degraded and reaching the end of its operational lifespan, requiring replacement. Exceeding HDMI video cable length leads to signal dropouts, screen flickering, or total loss of display output (digital sparkles or no signal), rather than uniform dimness. Setting the aspect ratio incorrectly stretches or distorts the image geometry or adds black bars. Static image burn-in causes persistent ghost outlines of static graphics, not low brightness across the whole image.

**83. Answer: A**  *[Hardware and Network Troubleshooting]*

- A. Display resolution

Adjusting the display resolution to match the monitor's native aspect ratio is correct because setting a non-native resolution forces the OS output to stretch or compress pixels, distorting visual shapes and causing text blurring. Changing color depth alters the number of bits used to represent color per pixel, not the physical aspect scaling. Modifying the refresh rate alters screen redraw frequency to eliminate flickering, not image geometry. Adjusting the contrast ratio alters light-to-dark intensity levels, which does not fix distorted or stretched proportions.

**84. Answer: D**  *[Networking]*

- D. PoE injector

A PoE injector adds electrical power to an existing Ethernet copper cable run originating from a non-PoE switch, allowing PoE-powered devices like IP cameras to operate without replacing the switch. A patch panel provides a centralized termination point for network cabling runs. An Optical Network Terminal (ONT) converts fiber optic light signals to electrical signals. A cable modem translates coaxial signals into Ethernet traffic.
