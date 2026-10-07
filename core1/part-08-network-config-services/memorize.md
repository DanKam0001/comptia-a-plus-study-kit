# Memorise list: Network configuration and services (Core 1, Part 8)

Understand the video first, then learn these cold.
Flashcards: [`flashcards/core1_part08.csv`](../../flashcards/core1_part08.csv) (import into Anki or any flashcard app).

## DHCP

| Question | Answer |
|---|---|
| DHCP ports | UDP 67 (server), 68 (client) |
| Scope | Range of addresses DHCP may hand out |
| Lease | How long a device keeps an address |
| Exclusion | Addresses DHCP will not hand out |
| Reservation | Same IP always given to one MAC address |
| Static vs dynamic | Static = typed by hand. Dynamic = from DHCP |

## DNS records

| Record | Meaning |
|---|---|
| A | Name to IPv4 address |
| AAAA | Name to IPv6 address |
| CNAME | Alias to another name |
| MX | Mail server for the domain |
| TXT | Plain text. SPF, DKIM, DMARC live here |
| DNS port | 53 |

## Spam management

| Acronym | Full name | One-line job |
|---|---|---|
| SPF | Sender Policy Framework | Which servers may send for the domain |
| DKIM | DomainKeys Identified Mail | Digital signature on each message |
| DMARC | Domain-based Message Authentication, Reporting, and Conformance | What to do if SPF or DKIM fails, plus reports |

## VLAN, VPN

| Question | Answer |
|---|---|
| VLAN | Virtual LAN. One switch split into separate networks |
| What links two VLANs? | A router |
| VLAN tagging standard | IEEE 802.1Q |
| VPN | Virtual Private Network. Encrypted tunnel over an untrusted network |

## Server roles

| Role | One-liner |
|---|---|
| AAA | Authentication, Authorization, Accounting |
| Authentication | Who are you? |
| Authorization | What may you do? |
| Accounting | What did you do? |
| Syslog | Collects log messages (UDP 514) |
| NTP | Keeps clocks in sync (UDP 123) |
| Fileshare | Shared files (SMB 445) |

## Appliances and special systems

| Term | One-liner |
|---|---|
| Spam gateway | Filters email |
| UTM | Unified Threat Management: firewall, antivirus and filtering in one box |
| Load balancer | Shares traffic across servers |
| Proxy server | Makes requests for users, can filter |
| SCADA | Supervisory Control and Data Acquisition: industrial control |
| IoT | Internet of Things: smart connected devices |
