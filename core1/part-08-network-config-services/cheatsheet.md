# Core 1, Part 8: How a Network Configures Itself: IP, DHCP, DNS, VLANs, VPNs

**Objectives 2.4** (explain common network configuration concepts) and **2.3** (summarize services provided by networked hosts) (220-1201).
Domain: Networking (23% of the exam). IP addressing itself (IPv4, IPv6, APIPA, subnet mask, gateway) is objective 2.6, covered in Part 10.

## DHCP (2.4)

DHCP (Dynamic Host Configuration Protocol) hands out IP addresses automatically. Ports: UDP **67** (server), **68** (client).

| Term | Meaning |
|---|---|
| Scope | The range of addresses the DHCP server may hand out (example: 192.168.1.100 to 192.168.1.200) |
| Lease | How long a device may keep its address before it must renew |
| Exclusion | Addresses inside the scope that DHCP must never hand out (kept for devices set by hand) |
| Reservation | DHCP always gives one device (identified by its **MAC address**) the same IP address |
| Static | Address typed into the device by hand |
| Dynamic | Address handed out by DHCP |

Reservation beats a static address for printers and servers because every address stays managed in one place.

## DNS (2.4)

DNS turns names into IP addresses. Port 53.

| Record | Purpose |
|---|---|
| **A** | Name to an **IPv4** address |
| **AAAA** ("quad A") | Name to an **IPv6** address |
| **CNAME** (Canonical Name) | Alias: points one name to another name |
| **MX** (Mail Exchanger) | The server that receives email for the domain |
| **TXT** | Plain text. Used for spam management |

TXT-based spam management:

| Tool | What it does |
|---|---|
| **SPF** (Sender Policy Framework) | Lists the servers allowed to send mail for the domain |
| **DKIM** (DomainKeys Identified Mail) | Adds a digital signature to each message so receivers can check it wasn't altered and is from the domain |
| **DMARC** (Domain-based Message Authentication, Reporting, and Conformance) | Tells receivers what to do when SPF or DKIM checks fail (for example reject) and sends reports |

## VLAN and VPN (2.4)

- **VLAN** (Virtual LAN): one physical switch split into separate virtual networks. Devices on different VLANs cannot talk directly, traffic between them goes through a router. Needs a managed switch. Tagging standard: IEEE 802.1Q. Typical use: keep guests away from company devices.
- **VPN** (Virtual Private Network): an encrypted tunnel across an untrusted network such as the internet. Remote workers get safe access to the office network.

## Server roles (2.3)

| Role | What it does |
|---|---|
| DNS | Answers name lookups |
| DHCP | Hands out IP addresses |
| Fileshare | Stores shared files (SMB, port 445) |
| Print server | Manages shared printers and the print queue |
| Mail server | Sends, receives and stores email (SMTP, POP3, IMAP) |
| Syslog | Collects log messages from many devices (UDP 514, not on the 2.1 list) |
| Web server | Delivers websites (HTTP 80, HTTPS 443) |
| AAA | **A**uthentication (who are you), **A**uthorization (what may you do), **A**ccounting (what did you do) |
| Database server | Stores organised data |
| NTP (Network Time Protocol) | Keeps all clocks in step (UDP 123, not on the 2.1 list) |

## Internet appliances (2.3)

| Appliance | What it does |
|---|---|
| Spam gateway | Filters unwanted email before it arrives |
| UTM (Unified Threat Management) | Firewall, antivirus, filtering and more in one box |
| Load balancer | Spreads traffic across several servers (availability) |
| Proxy server | Makes requests on behalf of users. Can filter, cache and hide who is asking |

## Legacy, embedded and IoT (2.3)

- **Legacy / embedded:** old systems, or computers built into machines. Often cannot be patched easily.
- **SCADA** (Supervisory Control and Data Acquisition): controls industrial systems such as factories, water and power. Treat as legacy: isolate them.
- **IoT** (Internet of Things): smart connected devices such as cameras and thermostats. Often weak security, so keep them on their own VLAN and change default passwords.

## Common scenarios

| Scenario | Answer |
|---|---|
| Printer's address keeps changing | DHCP reservation |
| Company email goes to spam | SPF, DKIM and DMARC TXT records |
| Remote worker needs safe office access | VPN |
| Keep guest Wi-Fi away from company PCs | VLAN |
| Website name must reach an IPv6 address | AAAA record |
| "shop.example.com" should follow "www.example.com" | CNAME |
| Where does mail for the domain go? | MX record |
| Spread website visitors over three servers | Load balancer |
| Clocks differ between servers | NTP |
