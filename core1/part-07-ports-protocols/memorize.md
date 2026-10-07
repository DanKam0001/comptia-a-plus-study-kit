# Memorise list: Ports and Protocols (Core 1, Part 7)

This is pure memorisation, and it's on the exam. Learn each port in **both directions**: number to name, and name to number.
Flashcards: [`flashcards/core1_part07.csv`](../../flashcards/core1_part07.csv) (import into Anki or any flashcard app).

## Port to protocol

| Port | Protocol | Transport |
|---|---|---|
| 20-21 | FTP | TCP |
| 22 | SSH | TCP |
| 23 | Telnet | TCP |
| 25 | SMTP | TCP |
| 53 | DNS | UDP and TCP |
| 67/68 | DHCP | UDP |
| 80 | HTTP | TCP |
| 110 | POP3 | TCP |
| 137-139 | NetBIOS / NetBT | UDP and TCP |
| 143 | IMAP | TCP |
| 389 | LDAP | TCP (UDP also used) |
| 443 | HTTPS | TCP |
| 445 | SMB / CIFS | TCP |
| 3389 | RDP | TCP (UDP also used) |

## Rules and tricks

| Question | Answer |
|---|---|
| Port number range | 0 to 65535. Well known ports 0 to 1023 |
| TCP in one line | Connection first, checks delivery, resends. Reliable |
| UDP in one line | No connection, no resending. Fast |
| Which carries live video and voice? | UDP |
| Secure replacement for Telnet | SSH (22). Telnet is 23 |
| Secure version of HTTP | HTTPS (443) |
| Which mail protocol sends? | SMTP (25) |
| POP3 vs IMAP | POP3 (110) downloads to one device. IMAP (143) keeps mail on the server, synced |
| DHCP ports | 67 server, 68 client (server first) |
| LDAP vs RDP | LDAP 389 = directory. RDP 3389 = remote desktop |
| FTP data and command ports | 20 data, 21 commands. No encryption |
| SMB and CIFS | Same port, 445 |
| NetBIOS ports | 137, 138, 139 |
