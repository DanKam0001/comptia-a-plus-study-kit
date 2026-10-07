# Core 2, Part 4: Performance-Based Questions

**Part:** Windows Networking on the Client (objective 1.7)
**Answers:** [part-04-pbq-answers.md](part-04-pbq-answers.md). Do not open it until you have finished both tasks.

The real 220-1202 exam has performance-based questions (PBQs). This kit cannot run a simulator, so each task is done on paper or in a text file. Try it before you look at the cheatsheet. You earn credit for each correct part, so never leave a row blank.

---

## C2P04-PBQ1: Fix the network settings screen

| | |
|---|---|
| **Objectives** | 1.7 |
| **Type** | Fix the screen (text-described) |
| **Time guide** | 5 minutes |

**Scenario.** A small office has a Windows PC that shares a folder with the whole team. The shared folder PC must always keep the same address. A colleague typed the settings in, but the PC cannot reach anything. You are shown the screen they left behind (Internet Protocol Version 4 (TCP/IPv4) Properties).

**Materials: the screen as it is now**

```
(o) Use the following IP address:
      IP address:           192.168.1.1
      Subnet mask:          255.255.255.0
      Default gateway:      192.168.1.20
(o) Use the following DNS server addresses:
      Preferred DNS server: 255.255.255.0
```

**Materials: the IT sheet (example values for this exercise)**

| Item | Value |
|---|---|
| Address for this shared folder PC (static, must never change) | 192.168.1.20 |
| Subnet mask for the network | 255.255.255.0 |
| Router (the exit from the network) | 192.168.1.1 |
| DNS server | 8.8.8.8 |

**Task.** Write what each of the four fields **should** contain. Write "no change" for any field that is already right.

| Field | Correct value |
|---|---|
| IP address | |
| Subnet mask | |
| Default gateway | |
| Preferred DNS server | |

**Marking.** 4 points: 1 point per field.

---

## C2P04-PBQ2: Which setting solves it?

| | |
|---|---|
| **Objectives** | 1.7 |
| **Type** | Matching |
| **Time guide** | 5 minutes |

**Scenario.** Eight users send you Windows networking problems. Each one has exactly one best fix from the list.

**Task.** Match each problem (1 to 8) to **one** fix (A to H). Each fix is used **exactly once**.

**Materials: fixes**

| Letter | Fix |
|---|---|
| A | Add a VPN connection |
| B | Set the network profile to Public |
| C | Join the PC to a domain |
| D | Map a network drive |
| E | Add an exception in Windows Defender Firewall |
| F | Use a static IP address |
| G | Check the proxy settings |
| H | Turn on the metered connection setting |

**Problems**

1. A laptop at a coffee shop is visible to other people and is sharing files.
2. Large Windows updates keep eating the limited data of a phone hotspot.
3. A home worker must reach company files securely over the internet.
4. A shared folder must appear in File Explorer as the drive letter Z:, reconnecting at every sign-in.
5. One website fails only when the user is on the office network, and works at home.
6. 50 office PCs need one sign-in that works on all of them, with settings pushed from a server.
7. A device must keep the same address every day, so it cannot take whatever DHCP hands out.
8. A program on this PC cannot be reached from another computer because the firewall blocks it. The firewall must stay on.

**Marking.** 8 points: 1 point per correct match.
