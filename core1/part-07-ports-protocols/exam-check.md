# Exam check: Ports and Protocols

Cover the answers and try each one out loud first.

**1.** A technician logs in to a router with Telnet, and anyone watching the network can read the password. Which protocol should replace Telnet, and on which port?
<details><summary>Answer</summary>SSH on port 22. Telnet (port 23) sends plain text. SSH does the same job but encrypts everything.</details>

**2.** A new email account must keep its messages on the server, so they show up on both the phone and the laptop. Which incoming mail protocol should be used?
<details><summary>Answer</summary>IMAP on port 143. POP3 downloads mail to one device, and SMTP only sends.</details>

**3.** A live video call keeps freezing while it waits for lost data to be sent again. Which transport protocol suits live video better?
<details><summary>Answer</summary>UDP. It doesn't stop to resend lost data, so a small glitch replaces a long freeze.</details>

## More practice (written for this kit)

**4.** Which port does HTTPS use?
<details><summary>Answer</summary>443, over TCP.</details>

**5.** Which two ports does DHCP use, and which is the client?
<details><summary>Answer</summary>67 (server) and 68 (client), over UDP.</details>

**6.** A firewall must allow staff to use Remote Desktop to reach office PCs. Which port?
<details><summary>Answer</summary>3389 (RDP).</details>

**7.** Which port number do SMB and CIFS use?
<details><summary>Answer</summary>445.</details>

**8.** Which protocol on port 389 looks up users and devices in a company directory?
<details><summary>Answer</summary>LDAP, the Lightweight Directory Access Protocol.</details>

**9.** Name the protocol that sends email, and its port.
<details><summary>Answer</summary>SMTP, port 25.</details>

**10.** Which protocol uses ports 20 and 21, and is it encrypted?
<details><summary>Answer</summary>FTP. It is not encrypted.</details>
