# Core 1, Part 7: Ports and Protocols: TCP, UDP and the Numbers You Must Know

**Objective 2.1** (220-1201): *Compare and contrast Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) ports, protocols, and their purposes.*
Domain: Networking (23% of the exam). Also in the kit: [`memorize/ports-and-protocols.md`](../../memorize/ports-and-protocols.md).

## The idea

- An **IP address** is the building. A **port** is the apartment number: it tells the computer which program gets the data.
- Port numbers run **0 to 65535**. Well known ports are **0 to 1023**.
- A **protocol** is a set of rules for a conversation. Each common protocol has a standard port.

## TCP vs UDP

| | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
|---|---|---|
| Connection | Sets up a connection first (connection-oriented) | No connection (connectionless) |
| Delivery | Checks every piece arrived (acknowledgments) and resends lost data | No checking, no resending |
| Speed | Slower, reliable | Faster, lightweight |
| Analogy | Registered post | Postcard |
| Used for | Web, email, file transfer, remote access | Live video and voice, streaming, games, DHCP, quick DNS lookups |

## The ports (all 14 entries in the objective)

| Port | Protocol | What it does | Transport |
|---|---|---|---|
| 20-21 | FTP (File Transfer Protocol) | Moves files. 21 is commands, 20 is data. Not encrypted | TCP |
| 22 | SSH (Secure Shell) | Encrypted remote command line | TCP |
| 23 | Telnet | Remote command line in plain text, including passwords. Replaced by SSH | TCP |
| 25 | SMTP (Simple Mail Transfer Protocol) | Sends email | TCP |
| 53 | DNS (Domain Name System) | Turns names into IP addresses | UDP (quick lookups) and TCP |
| 67/68 | DHCP (Dynamic Host Configuration Protocol) | Hands out IP addresses. 67 server, 68 client | UDP |
| 80 | HTTP (Hypertext Transfer Protocol) | Web pages, not encrypted | TCP |
| 110 | POP3 (Post Office Protocol 3) | Downloads email to one device, usually removing it from the server | TCP |
| 137-139 | NetBIOS / NetBT (NetBIOS over TCP/IP) | Old Windows naming and sharing. 137 and 138 UDP, 139 TCP | UDP and TCP |
| 143 | IMAP (Internet Mail Access Protocol) | Leaves email on the server and syncs all devices | TCP |
| 389 | LDAP (Lightweight Directory Access Protocol) | Looks up users and devices in a directory | TCP (UDP also used) |
| 443 | HTTPS (Hypertext Transfer Protocol Secure) | Encrypted web | TCP |
| 445 | SMB / CIFS (Server Message Block / Common Internet File System) | Windows file and printer sharing | TCP |
| 3389 | RDP (Remote Desktop Protocol) | Full remote Windows desktop | TCP (UDP also used) |

## Pairs and trios to learn together

- **Secure vs insecure:** HTTP 80 / HTTPS 443. Telnet 23 / SSH 22. FTP 20-21 is unencrypted.
- **Email:** send = SMTP 25, download = POP3 110, sync = IMAP 143.
- **DHCP:** 67 server, 68 client (server first).
- **Look-alikes:** LDAP 389 (directory) vs RDP 3389 (remote desktop).

## Common scenarios

| Scenario | Answer |
|---|---|
| Admin password visible on the network during remote login | Replace Telnet (23) with SSH (22) |
| Email must be identical on phone and laptop | IMAP (143), not POP3 |
| Live video call freezes waiting for lost data | UDP (it doesn't resend) |
| Firewall rule to allow remote desktop to office PCs | TCP 3389 |
| Firewall rule to allow secure web browsing | TCP 443 |
| Shared Windows folder won't connect, firewall blocking | SMB, TCP 445 |
| Looking up names in a company directory | LDAP, 389 |

Always confirm against CompTIA's current objectives, which are the authority on what's tested.
