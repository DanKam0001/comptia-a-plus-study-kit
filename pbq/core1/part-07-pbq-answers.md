# Core 1, Part 7 PBQ answers

Tasks: [part-07-pbq.md](part-07-pbq.md). Facts come from the [Part 7 cheat sheet](../../core1/part-07-ports-protocols/cheatsheet.md) and the [ports and protocols memorise sheet](../../memorize/ports-and-protocols.md).

---

## C1P07-PBQ1: Drag each protocol to its port

| # | Protocol | Port | Why |
|---|---|---|---|
| 1 | FTP | **A** 20-21 | 21 is commands, 20 is data. Not encrypted |
| 2 | SSH | **B** 22 | Encrypted remote command line |
| 3 | Telnet | **C** 23 | Plain-text remote command line |
| 4 | SMTP | **D** 25 | Sends email |
| 5 | DNS | **E** 53 | Names to IP addresses |
| 6 | DHCP | **F** 67/68 | 67 server, 68 client |
| 7 | HTTP | **G** 80 | Web, not encrypted |
| 8 | POP3 | **H** 110 | Downloads email |
| 9 | NetBIOS / NetBT | **I** 137-139 | Old Windows naming and sharing |
| 10 | IMAP | **J** 143 | Leaves email on the server and syncs |
| 11 | LDAP | **K** 389 | Directory lookups |
| 12 | HTTPS | **L** 443 | Encrypted web |
| 13 | SMB / CIFS | **M** 445 | Windows file and printer sharing |
| 14 | RDP | **N** 3389 | Full remote Windows desktop |

**Marking (14 points):** 1 per protocol.
- 13 to 14: exam ready on this objective. 10 to 12: fine, drill the misses with the flashcards. Under 10: learn the table pair by pair (secure vs insecure, email trio, DHCP 67 then 68).
- Common slips: LDAP 389 and RDP 3389 swapped, and POP3 110 against IMAP 143.

---

## C1P07-PBQ2: Build the firewall rules

| Rule | Action | Protocol | Port | Why |
|---|---|---|---|---|
| 1 | Allow | TCP | **3389** | RDP (accept UDP too: modern RDP also uses UDP 3389) |
| 2 | Allow | TCP | **443** | HTTPS |
| 3 | Block | TCP | **23** | Telnet, plain text, passwords visible |
| 4 | Allow | TCP | **22** | SSH |
| 5 | Allow | TCP | **445** | SMB |
| 6 | Allow | UDP | **67** | DHCP server side, UDP |
| 7 | Allow | TCP | **25** | SMTP |
| 8 | Block | TCP | **80** | HTTP, unencrypted web |

- **B1.** **UDP.** It does not resend lost data, so the call keeps going instead of freezing.
- **B2.** **TCP.** It checks every piece arrived and resends lost data.

**Marking (18 points):** per rule 1 for the port and 1 for the protocol (16 points), 1 each for B1 and B2.
- 16 to 18: strong. 12 to 15: fine, recheck the weak rows. Under 12: relearn the TCP vs UDP table and the ports.
- Port and protocol are marked separately, so a right port with a wrong protocol still earns 1.
