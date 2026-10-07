# Core 2, Part 16: PBQ practice (Scripting, remote access, AI)

Objectives 4.8, 4.9, 4.10 (220-1202). Print this page or copy it into a text file and fill it in. Do not open `part-16-pbq-answers.md` until you have finished both tasks.

---

## C2P16-PBQ1: Pick the remote tool and its port

| | |
|---|---|
| **ID** | C2P16-PBQ1 |
| **Objectives** | 4.9 |
| **Type** | Two-column matching table (choose a tool and a port for each job) |
| **Time guide** | 6 minutes |

**Scenario.** You are the IT person for a company that has staff working from home, Linux servers, and an outside support firm. Seven different remote jobs need the right tool.

**Task.** For each job, write the number of the tool and the letter of the port. A tool or port can be used more than once, but each job has one right pair. If the kit gives no port to memorise, choose letter **n/a**.

| Number | Tool |
|---|---|
| 1 | RDP |
| 2 | VPN |
| 3 | VNC |
| 4 | SSH |
| 5 | RMM |
| 6 | SPICE |
| 7 | WinRM |

| Letter | Port |
|---|---|
| a | 22 |
| b | 3389 |
| c | 5900 |
| d | 5986 |
| n/a | No port to memorise |

| # | Job | Tool (number) | Port (letter) |
|---|---|---|---|
| 1 | A technician needs the full Windows desktop of a remote office PC. | | |
| 2 | An admin needs an encrypted command line on a remote Linux server. | | |
| 3 | Staff at home need an encrypted tunnel so their laptops act as if they are on the office network. | | |
| 4 | Graphical screen sharing across many different system types, not encrypted by default. | | |
| 5 | An IT support company watches and fixes hundreds of client PCs from one console. | | |
| 6 | Run commands on remote Windows computers over an encrypted (HTTPS) connection. | | |
| 7 | A remote display protocol for virtual machines. | | |

**Bonus (one blank).** The safest way to offer RDP is behind a ________ , never open directly to the internet.

---

## C2P16-PBQ2: Check the script, match the file types, spot the AI risk

| | |
|---|---|
| **ID** | C2P16-PBQ2 |
| **Objectives** | 4.8, 4.10 |
| **Type** | Checklist (tick the safe actions) plus matching |
| **Time guide** | 8 minutes |

**Scenario.** A colleague emails a PowerShell script found on a forum. They say it "speeds up Windows" and want you to run it on all 200 office PCs. Later the same day, staff start asking about AI tools.

**Task.**

**Part A.** Tick the THREE safe actions.

- [ ] Read the script before you run it
- [ ] Run it on all 200 PCs at once to save time
- [ ] Run it as administrator without reading it
- [ ] Run it on one machine first
- [ ] Turn off antivirus because the script asks you to
- [ ] Email it to everyone so they can try it
- [ ] Only use scripts from a trusted source

**Part B.** Write the letter of the right file type beside each description.

| Letter | File type |
|---|---|
| A | `.bat` |
| B | `.ps1` |
| C | `.vbs` |
| D | `.sh` |
| E | `.js` |
| F | `.py` |

| # | Description | Your letter |
|---|---|---|
| 1 | Windows batch file | |
| 2 | PowerShell script | |
| 3 | VBScript, older Windows scripting | |
| 4 | Shell script for Linux and macOS | |
| 5 | JavaScript, used in browsers and on servers | |
| 6 | Python, works on any system with Python installed | |

**Part C.** Write the letter of the right term beside each AI situation. Two terms are not used.

| Letter | Term |
|---|---|
| P | Hallucination |
| Q | Bias |
| R | Plagiarism |
| S | Data privacy risk |
| T | Data source |
| U | Application integration |

| # | Situation | Your letter |
|---|---|---|
| 1 | An AI confidently cites a report that does not exist. | |
| 2 | An AI leans unfairly because of the data it was trained on. | |
| 3 | A staff member passes off AI-written work as their own. | |
| 4 | A staff member pastes customer data into a public chatbot. | |
