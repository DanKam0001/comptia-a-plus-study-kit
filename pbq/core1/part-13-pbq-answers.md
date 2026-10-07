# Core 1, Part 13: PBQ answers

Do the tasks in [`part-13-pbq.md`](part-13-pbq.md) first.

**Marking note:** real PBQs can earn partial credit, so each item here is marked on its own. CompTIA does not publish its PBQ scoring rules, so treat this as practice marking, not the real formula. Rough guide: all correct is a pass for this drill, 75 percent or more means you are close, below 50 percent means go back to the [cheatsheet](../../core1/part-13-troubleshooting-hardware/cheatsheet.md).

---

## C1P13-PBQ1: Fault Finder Match-up (8 points)

| # | Answer | Why |
|---|---|---|
| 1 | D | Beep codes differ by maker, so look the pattern up in the motherboard manual |
| 2 | A | A flat CMOS battery (usually a CR2032 coin cell) loses the date and time |
| 3 | B | A burning smell means power off and unplug at once, and do not power on again |
| 4 | F | Clicking means a failing HDD head: back up now, then replace |
| 5 | H | No power at all: check the outlet, cable and PSU switch, then test the PSU |
| 6 | G | Swollen or leaking capacitors on the board mean replacing the board |
| 7 | C | Dust causes overheating, and the fix is compressed air and checking the fans |
| 8 | E | Check the boot order, reseat cables, and see whether firmware detects the drive |

Wrong for every ticket: I (format and reinstall) and J (swap the RAM brand).

**Answer string:** 1D 2A 3B 4F 5H 6G 7C 8E

**Marking:** 1 point per correct match.

---

## C1P13-PBQ2: RAID Rescue Table (17 points)

**Part A** (2 points per row)

| # | Data still available? | Next action | Why |
|---|---|---|---|
| 1 | Yes | R | RAID 1 is a mirror and survives one drive. Replace and rebuild |
| 2 | No | S | RAID 0 is striping with no redundancy and survives nothing. Restore from backup |
| 3 | Yes | R | RAID 5 survives one drive. Replace and rebuild |
| 4 | No | S | RAID 5 survives only one drive, so two failed means the array is lost |
| 5 | Yes | R | RAID 6 has double parity and survives two drives. Replace and rebuild |
| 6 | No | S | RAID 10 survives one drive per mirrored pair. Both drives of one pair means that mirror is gone |

**Part B** (1 point each)

| Level | Answer |
|---|---|
| RAID 0 | 2 |
| RAID 1 | 2 |
| RAID 5 | 3 |
| RAID 6 | 4 |
| RAID 10 | 4 |

**Marking:** 12 points for Part A (1 for the Yes or No, 1 for R or S) and 5 for Part B. The two points in each row are marked independently.
