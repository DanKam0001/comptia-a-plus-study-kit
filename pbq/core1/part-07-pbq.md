# Core 1, Part 7 PBQs: Ports and Protocols

Performance-based question (PBQ) practice for **Objective 2.1** (220-1201). Do each task on paper or in a text file. Answers are in a separate file ([part-07-pbq-answers.md](part-07-pbq-answers.md)), so don't open it until you have finished.

If you are stuck, check the [Part 7 cheat sheet](../../core1/part-07-ports-protocols/cheatsheet.md), mark that item, and lose the point.

---

## C1P07-PBQ1: Drag each protocol to its port

- **Objective:** 2.1
- **Type:** Matching (drag and drop on paper)
- **Time guide:** 6 minutes

### Scenario

A new helpdesk worker has a sticky-note list of 14 protocols and a second list of 14 port numbers. The notes got separated. Match each protocol to its standard port.

### Materials

**Protocols**

1. FTP (File Transfer Protocol)
2. SSH (Secure Shell)
3. Telnet
4. SMTP (Simple Mail Transfer Protocol)
5. DNS (Domain Name System)
6. DHCP (Dynamic Host Configuration Protocol)
7. HTTP (Hypertext Transfer Protocol)
8. POP3 (Post Office Protocol 3)
9. NetBIOS / NetBT
10. IMAP (Internet Mail Access Protocol)
11. LDAP (Lightweight Directory Access Protocol)
12. HTTPS (HTTP Secure)
13. SMB / CIFS (Server Message Block / Common Internet File System)
14. RDP (Remote Desktop Protocol)

**Port numbers** (each used once)

- **A.** 20-21
- **B.** 22
- **C.** 23
- **D.** 25
- **E.** 53
- **F.** 67/68
- **G.** 80
- **H.** 110
- **I.** 137-139
- **J.** 143
- **K.** 389
- **L.** 443
- **M.** 445
- **N.** 3389

### Task

Write the port letter next to each protocol number.

### Marking

14 points: 1 per protocol. Partial credit applies, a wrong match does not cancel a right one.

---

## C1P07-PBQ2: Build the firewall rules

- **Objective:** 2.1
- **Type:** Configure this (firewall rule form)
- **Time guide:** 6 minutes

### Scenario

You are setting up the firewall for a small office. The manager has given you the policy below. Fill in the port and the protocol (TCP or UDP) for each rule. Each rule uses a different port from the port bank.

### Materials

**Port bank** (each used once): `22`, `23`, `25`, `67`, `80`, `443`, `445`, `3389`

**The policy**

| Rule | Action | Purpose |
|---|---|---|
| 1 | Allow | Staff use full remote desktop sessions to reach office Windows PCs |
| 2 | Allow | Secure (encrypted) web browsing |
| 3 | Block | Remote login that sends passwords in plain text |
| 4 | Allow | Admins use an encrypted remote command line |
| 5 | Allow | Windows file and printer sharing |
| 6 | Allow | The DHCP server hands out IP addresses (the server side port) |
| 7 | Allow | Staff send outgoing email |
| 8 | Block | Unencrypted web pages |

**Part B** (just TCP or UDP): which transport suits each?

- **B1.** A live video call, where a late piece of data is useless.
- **B2.** Downloading a program installer that must arrive complete.

### Task

Copy the table and add two columns, **Protocol (TCP/UDP)** and **Port**. Then answer B1 and B2.

### Marking

18 points: 16 for the rules (1 for the port and 1 for the protocol, per rule, 8 rules), plus 1 each for B1 and B2.
