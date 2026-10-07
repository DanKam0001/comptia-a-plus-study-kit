# Core 2, Part 11: PBQ answers and marking

Questions are in `part-11-pbq.md`. One point per correct item, nothing for a wrong item. This kit marks each item separately. CompTIA does not publish its PBQ scoring rules, so treat this as practice marking, not the real formula.

---

## C2P11-PBQ1: Choose the right method (11 points)

**Part A (3 points)**

| # | Answer | Why |
|---|---|---|
| 1 | C, Wipe | It must keep working, so overwrite the whole drive. |
| 2 | D, Maker's secure erase tool | SSDs move data around internally, so plain overwriting can miss some. |
| 3 | E, Shred | It will not power on, so it cannot be wiped, and it is an SSD so degaussing does nothing. |

**Part B (5 points, one per correct tick or correct blank)**

| Item | Tick? | Why |
|---|---|---|
| HDD | Yes | Magnetic platters, degaussing works. |
| SSD | No | Flash chips, not magnetic. |
| Backup tape | Yes | Magnetic media. |
| USB flash drive | No | Flash memory. |
| Smartphone | No | Flash storage. |

Score 1 point for each of the five rows handled correctly (ticked when it should be, left blank when it should not).

**Part C (3 points)**

Tick: serial number of each drive, the date, the method. Leave the other three blank. Why: a certificate lists the drives (usually by serial number), the date and the method, and you keep it as evidence.

**Marking:** 11 = full marks. 9 to 10 = good. Below 9 = reread the physical destruction table and the SSD note in the Part 11 cheat sheet. The most important single idea: degaussing works on magnetic media only.

---

## C2P11-PBQ2: Fix the disposal policy (8 points for T/F, plus 1 bonus point per good correction)

| # | Answer | Corrected line / why |
|---|---|---|
| 1 | F | Deleting only removes the index entry. The data stays until it is overwritten, so recovery software can bring it back. |
| 2 | F | A quick format only builds a new empty index. The data is still recoverable. Wipe the drive instead. |
| 3 | T | Drilling is cheap and quick but less thorough than shredding. |
| 4 | F | Degaussing works on magnetic media only (hard drives, tape). It does nothing to an SSD. |
| 5 | T | Burning at high temperature should be done by a licensed facility. |
| 6 | T | The certificate is signed proof of what was destroyed. |
| 7 | F | Electronics contain batteries and chemicals. Use an approved e-waste recycler. |
| 8 | T | Wiping keeps the drive usable, so it suits reuse, sale or donation. |

**Marking:** 8 T/F points. The four false lines (1, 2, 4, 7) are the ones that matter most: if you marked any of them True, reread the Part 11 core idea. A correction only earns its bonus point if it names the right fix (for example "wipe" for line 2, "approved e-waste recycler" for line 7).
