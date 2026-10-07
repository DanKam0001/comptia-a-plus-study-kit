# Core 2, Part 16: PBQ answers and marking

Questions are in `part-16-pbq.md`. One point per correct item, nothing for a wrong item. This kit marks each item separately. CompTIA does not publish its PBQ scoring rules, so treat this as practice marking, not the real formula.

---

## C2P16-PBQ1: Pick the remote tool and its port (15 points)

One point for the tool and one point for the port in each of the 7 rows, plus 1 for the bonus blank.

| # | Tool | Port | Why |
|---|---|---|---|
| 1 | 1, RDP | b, 3389 | Full Windows desktop over the network. |
| 2 | 4, SSH | a, 22 | Encrypted command line. |
| 3 | 2, VPN | n/a | An encrypted tunnel into a network. |
| 4 | 3, VNC | c, 5900 | Graphical screen sharing across many system types, not encrypted by default. |
| 5 | 5, RMM | n/a | One console to watch and fix many computers, used by IT support companies. |
| 6 | 7, WinRM | d, 5986 | Runs commands on remote Windows computers. 5985 is HTTP, 5986 is HTTPS, and the job says HTTPS. |
| 7 | 6, SPICE | n/a | Remote display protocol for virtual machines. |

**Bonus:** VPN (a remote desktop gateway is also acceptable).

**Marking:** 15 = full marks. 12 to 14 = good. Below 12 = reread the remote access table and memorise the ports (RDP 3389, SSH 22, VNC 5900, WinRM 5985 and 5986). The commonest slip is swapping RDP (Windows desktop) and VNC (many system types).

---

## C2P16-PBQ2: Check the script, match the file types, spot the AI risk (13 points)

**Part A (3 points)**

Tick exactly these three: **Read the script before you run it**, **Run it on one machine first**, **Only use scripts from a trusted source**. Leave the other four blank (running it everywhere at once, running it unread as administrator, turning off antivirus, and emailing it around all risk introducing malware, changing system settings or crashing machines).

Marking: 1 point per correct tick; take off 1 point for each wrong tick (never below 0). This is the one place the kit subtracts, otherwise ticking every box would score full marks.

**Part B (6 points)**

| # | Answer |
|---|---|
| 1 | A, `.bat` |
| 2 | B, `.ps1` |
| 3 | C, `.vbs` |
| 4 | D, `.sh` |
| 5 | E, `.js` |
| 6 | F, `.py` |

**Part C (4 points)**

| # | Answer | Why |
|---|---|---|
| 1 | P, Hallucination | A confident answer that is made up. |
| 2 | Q, Bias | Unfair leanings from the training data. |
| 3 | R, Plagiarism | Passing off AI-written work as your own. |
| 4 | S, Data privacy risk | Input to a public AI goes outside your control, so never paste private or customer data. |

Not used: **T** (data source is where the AI's knowledge came from) and **U** (application integration is AI built into everyday apps).

**Marking:** 13 = full marks. 10 to 12 = good. Below 10 = reread 4.8 and 4.10 in the Part 16 cheat sheet.
