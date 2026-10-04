# Ports and protocols (Core 1 objective 2.1)

This is pure memorisation, and it's on the exam. Learn the number and the name both ways.

Flashcards: [`flashcards/ports.csv`](../flashcards/ports.csv)

| Port | Protocol | Full name / what it does | Transport |
|---|---|---|---|
| 20, 21 | FTP | File Transfer Protocol | TCP |
| 22 | SSH | Secure Shell | TCP |
| 23 | Telnet | Telnet (unencrypted remote terminal) | TCP |
| 25 | SMTP | Simple Mail Transfer Protocol (sending mail) | TCP |
| 53 | DNS | Domain Name System | UDP and TCP |
| 67, 68 | DHCP | Dynamic Host Configuration Protocol (67 server, 68 client) | UDP |
| 80 | HTTP | Hypertext Transfer Protocol | TCP |
| 110 | POP3 | Post Office Protocol 3 (downloading mail) | TCP |
| 137-139 | NetBIOS / NetBT | NetBIOS over TCP/IP (137/138 name and datagram on UDP, 139 session on TCP) | UDP and TCP |
| 143 | IMAP | Internet Message Access Protocol (syncing mail) | TCP |
| 389 | LDAP | Lightweight Directory Access Protocol | TCP (UDP also used) |
| 443 | HTTPS | Hypertext Transfer Protocol Secure | TCP |
| 445 | SMB / CIFS | Server Message Block / Common Internet File System | TCP |
| 3389 | RDP | Remote Desktop Protocol | TCP (UDP also used) |

## Quick rules

- **TCP** = reliable, connection-based (web, email, file transfer, remote access).
- **UDP** = fast, connectionless (DHCP, and DNS queries).
- Secure vs insecure pairs to know: HTTP 80 / HTTPS 443, Telnet 23 / SSH 22, FTP 20-21 (unencrypted).
- Email: SMTP 25 sends; POP3 110 downloads; IMAP 143 syncs.

Always confirm against CompTIA's current objectives, which are the authority on what's tested.
