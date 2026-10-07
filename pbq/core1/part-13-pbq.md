# Core 1, Part 13: PBQ practice (Troubleshooting Motherboards, RAM, CPU, Power, Drives and RAID)

Two performance-based question (PBQ) drills for **objectives 5.1 and 5.2** (220-1201). Print this page or copy the blanks into a text file. Do the tasks **before** you open [`part-13-pbq-answers.md`](part-13-pbq-answers.md). Facts come from the Part 13 [cheatsheet](../../core1/part-13-troubleshooting-hardware/cheatsheet.md) and [memorise sheet](../../core1/part-13-troubleshooting-hardware/memorize.md).

---

## C1P13-PBQ1: Fault Finder Match-up

| | |
|---|---|
| **ID** | C1P13-PBQ1 |
| **Objectives** | 5.1, 5.2 |
| **Type** | Matching (drag and drop style) |
| **Time guide** | 5 minutes |
| **Points** | 8 (1 per correct match) |

### Scenario

You work the repair bench and eight tickets have come in. Each ticket needs one best first action from the list. Two actions in the list are wrong for every ticket.

### Task

Write the action letter next to each ticket number. Each action is used at most once.

### Materials

**Actions**

| Letter | Action |
|---|---|
| A | Replace the CMOS battery, then reset the clock in firmware |
| B | Power off and unplug at once, then replace the part |
| C | Clean with compressed air and check every fan spins |
| D | Look up the beep pattern in the motherboard manual |
| E | Check the boot order in firmware, reseat cables, and see if the drive is detected |
| F | Back up now, then replace the drive |
| G | Replace the motherboard |
| H | Check the outlet, power cable and PSU switch, then test the power supply |
| I | Format the drive and reinstall Windows |
| J | Replace the RAM with a different brand |

**Tickets**

| # | Ticket | Your action letter |
|---|---|---|
| 1 | The PC starts but beeps in a pattern and shows nothing on screen | |
| 2 | The date and time reset to an old date every time the PC is unplugged | |
| 3 | A strong burning smell comes from the PC case | |
| 4 | A hard drive makes a repeated clicking sound | |
| 5 | The power button does nothing: no lights and no fans | |
| 6 | The tops of several capacitors on the motherboard are swollen and leaking | |
| 7 | The inside of the case is thick with dust and the PC overheats | |
| 8 | At startup the screen says "Bootable device not found" | |

---

## C1P13-PBQ2: RAID Rescue Table

| | |
|---|---|
| **ID** | C1P13-PBQ2 |
| **Objectives** | 5.2 |
| **Type** | Fill-in table |
| **Time guide** | 7 minutes |
| **Points** | 17 (1 per blank) |

### Scenario

A small business has several RAID arrays, and alarms went off on all of them overnight. For each array you must say whether the data can still be reached, and what to do next. Then you check the minimum number of drives for each RAID level.

### Task

**Part A.** In the "Data still available?" column write **Yes** (the array still works, though degraded) or **No** (the array is lost). In the "Next action" column write **R** or **S**:

- **R** = replace the failed drive and let the array rebuild
- **S** = restore the data from backup

**Part B.** Write the minimum number of drives for each RAID level.

### Materials

**Part A**

| # | Array | Drives failed | Data still available? | Next action |
|---|---|---|---|---|
| 1 | RAID 1, 2 drives | 1 | | |
| 2 | RAID 0, 2 drives | 1 | | |
| 3 | RAID 5, 3 drives | 1 | | |
| 4 | RAID 5, 3 drives | 2 | | |
| 5 | RAID 6, 4 drives | 2 | | |
| 6 | RAID 10, 4 drives (two mirrored pairs) | 2, both from the same mirrored pair | | |

**Part B**

| Level | Minimum drives |
|---|---|
| RAID 0 | |
| RAID 1 | |
| RAID 5 | |
| RAID 6 | |
| RAID 10 | |
