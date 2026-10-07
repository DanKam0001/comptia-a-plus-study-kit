# Core 1, Part 15: PBQ answers

Do the tasks in [`part-15-pbq.md`](part-15-pbq.md) first.

**Marking note:** real PBQs can earn partial credit, so each item here is marked on its own. CompTIA does not publish its PBQ scoring rules, so treat this as practice marking, not the real formula. Rough guide: all correct is a pass for this drill, 75 percent or more means you are close, below 50 percent means go back to the [cheatsheet](../../core1/part-15-troubleshooting-networks/cheatsheet.md).

---

## C1P15-PBQ1: Symptom Match-up (8 points)

| # | Answer | Why |
|---|---|---|
| 1 | C | A 169.254 address is APIPA: DHCP did not answer, so Windows gave itself an address |
| 2 | H | A problem only while the microwave runs is interference on 2.4 GHz |
| 3 | E | Choppy, robotic calls with fine web pages point to jitter, the delay varying |
| 4 | A | A port that keeps going up and down is port flapping |
| 5 | F | A long delay before replies arrive is high latency |
| 6 | B | Being refused with a password problem is an authentication failure |
| 7 | G | Good signal near the router and a drop further away is distance and walls |
| 8 | D | If everyone is offline, check the router, modem or internet provider |

Unused causes: I (printer driver) and J (full hard drive).

**Answer string:** 1C 2H 3E 4A 5F 6B 7G 8D

**Marking:** 1 point per correct match.

---

## C1P15-PBQ2: Order of Attack (9 points)

**Part A** (5 points)

| Order | Check | Why |
|---|---|---|
| 1 | D One device or everyone? | It tells you whether to look at the device or at the router, modem and provider |
| 2 | B Cable and link lights | Work from the bottom up, starting with the physical connection |
| 3 | A Proper IP address | A 169.254 address means DHCP did not answer |
| 4 | E Reach the router | Local connection comes before the wider internet |
| 5 | C Reach the internet | The last step up the ladder |

**Answer string:** D, B, A, E, C

**Part B** (4 points)

| # | Answer | Why |
|---|---|---|
| 1 | Do | A wrong or changed password is a common cause |
| 2 | Do | Forgetting the network and rejoining clears a stale saved setup |
| 3 | Never | Never switch security off to get around an authentication failure |
| 4 | Do | A wrong date and time can break authentication that uses certificates (for example a work Wi-Fi), and it is a harmless thing to check |

**Marking:** 1 point per step in the correct position in Part A, 1 point per correct word in Part B.
