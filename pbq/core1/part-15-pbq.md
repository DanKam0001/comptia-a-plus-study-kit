# Core 1, Part 15: PBQ practice (Troubleshooting Networks)

Two performance-based question (PBQ) drills for **objective 5.5** (220-1201). Print this page or copy the blanks into a text file. Do the tasks **before** you open [`part-15-pbq-answers.md`](part-15-pbq-answers.md). Facts come from the Part 15 [cheatsheet](../../core1/part-15-troubleshooting-networks/cheatsheet.md) and [memorise sheet](../../core1/part-15-troubleshooting-networks/memorize.md).

---

## C1P15-PBQ1: Symptom Match-up

| | |
|---|---|
| **ID** | C1P15-PBQ1 |
| **Objectives** | 5.5 |
| **Type** | Matching (drag and drop style) |
| **Time guide** | 5 minutes |
| **Points** | 8 (1 per correct match) |

### Scenario

Eight network complaints came in during one morning. Each complaint has one most likely cause on the list. Two causes on the list fit none of the complaints.

### Task

Write the cause letter next to each complaint number. Each cause is used at most once.

### Materials

**Causes**

| Letter | Cause |
|---|---|
| A | Port flapping (bad cable, connector, network card or switch port) |
| B | Authentication failure |
| C | No reply from DHCP, so the device used an APIPA address |
| D | Router, modem or internet provider fault |
| E | Jitter |
| F | High latency |
| G | Distance and thick walls |
| H | Interference from a microwave oven on the 2.4 GHz band |
| I | Out-of-date printer driver |
| J | Full hard drive |

**Complaints**

| # | Complaint | Your cause letter |
|---|---|---|
| 1 | Windows says "limited connectivity" and shows an address starting 169.254 | |
| 2 | Wi-Fi drops only while the microwave oven is running | |
| 3 | Voice calls sound choppy and robotic, but web pages load fine | |
| 4 | The light on a switch port blinks on and off again and again | |
| 5 | A video call has a long, steady delay before replies arrive | |
| 6 | A phone is refused by the Wi-Fi with "incorrect password" after the router's password was changed | |
| 7 | Wi-Fi is strong beside the router but drops two rooms away | |
| 8 | Every device in the building is offline | |

---

## C1P15-PBQ2: Order of Attack

| | |
|---|---|
| **ID** | C1P15-PBQ2 |
| **Objectives** | 5.5 |
| **Type** | Ordering, plus a Do or Never form |
| **Time guide** | 5 minutes |
| **Points** | 9 (5 for Part A, 4 for Part B) |

### Scenario

One user reports that their laptop cannot get online. You do not yet know whether anyone else is affected. You first work out how wide the problem is, then work from the bottom up, from the physical connection to the internet.

### Task

**Part A.** Write the numbers 1 to 5 next to the checks, with 1 for the first and 5 for the last. Use each number once.

**Part B.** Later that laptop is refused by the Wi-Fi network. Write **Do** or **Never** next to each possible fix.

### Materials

**Part A**

| Letter | Check | Your number |
|---|---|---|
| A | Check the laptop has a proper IP address (not one starting 169.254) | |
| B | Check the cable is plugged in and the link lights are on (or that Wi-Fi is connected) | |
| C | Check the laptop can reach the internet | |
| D | Decide whether one device or everyone is affected | |
| E | Check the laptop can reach the router | |

**Part B**

| # | Possible fix | Do or Never |
|---|---|---|
| 1 | Re-enter the Wi-Fi password | |
| 2 | Forget the network and rejoin it | |
| 3 | Turn Wi-Fi security off so devices can connect without a password | |
| 4 | Check the device's date and time | |
