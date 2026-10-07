# Core 2, Part 12: PBQ answers and marking

Questions are in `part-12-pbq.md`. One point per correct item, nothing for a wrong item. This kit marks each item separately. CompTIA does not publish its PBQ scoring rules, so treat this as practice marking, not the real formula.

---

## C2P12-PBQ1: Match the symptom to the first fix (8 points)

| # | Letter | Why |
|---|---|---|
| 1 | A | A bad driver update causes the blue screen. Safe mode loads only basic drivers, so you can roll it back. |
| 2 | B | A USB stick or disc left in the PC can make firmware boot from it. Remove it, then check the boot order. |
| 3 | C | A dead CMOS battery loses the clock when power is removed. |
| 4 | D | A service fails to start when something it depends on is not running. |
| 5 | E | Too many devices on one controller. Use a powered hub and fewer devices. |
| 6 | F | Domain sign-in needs the clock within 5 minutes by default, so sync with a time server. |
| 7 | G | Dust causes overheating, and overheating causes shutdowns under load. |
| 8 | H | Task Manager shows what is using CPU, memory, disk and network. |

Not used: **I** (reinstalling is a last resort, not a first fix) and **J** (nothing in these symptoms points to the keyboard).

**Marking:** 8 = full marks. 6 to 7 = good. Below 6 = reread the "twelve symptoms" table in the Part 12 cheat sheet. Picking I for any item means you jumped to the last resort.

---

## C2P12-PBQ2: Fix a blue screen after an update (10 points)

**Part A (5 points: one per step in the correct place)**

| Number | Step | Why |
|---|---|---|
| 4 | Restart normally and check that Windows now stays up | Test after the fix. |
| 3 | Open Device Manager and roll back the driver that was just updated | The fix, done from safe mode. |
| 1 | Write down the stop code shown on the blue screen | Note it while it is on screen. |
| 2 | Boot into safe mode | Starts with only basic drivers so the bad driver is not loaded. |
| blank | Reinstall Windows | Wrong move: far too drastic when a driver rollback can fix it. |
| 5 | Record the fix in the ticket | Documentation comes last, once you know what worked. |

The correct order of numbers reading down the table is: 4, 3, 1, 2, blank, 5.

**Part B (5 points)**

| # | Answer |
|---|---|
| 1 | Any three of `/fixmbr`, `/fixboot`, `/rebuildbcd`, `/scanos` (any order, all three right for the point) |
| 2 | `/scannow` |
| 3 | `/resync` |
| 4 | `Minidump` |
| 5 | 5 |

**Marking:** 10 = full marks. 8 to 9 = good. Below 8 = reread the "Tools by job" table. In Part A, if "Reinstall Windows" got a number, you lose that point and the one for any step you shifted.
