# Core 1, Part 1 PBQ answers

Tasks: [part-01-pbq.md](part-01-pbq.md). Facts come from the [Part 1 cheat sheet](../../core1/part-01-motherboards-cpus-firmware/cheatsheet.md).

---

## C1P01-PBQ1: Set up the new office PC in the firmware screen

| Row | Setting | Final value | Why |
|---|---|---|---|
| 1 | TPM | **Enabled** | Windows 11 needs TPM 2.0 |
| 2 | Secure Boot | **Enabled** | Windows 11 needs a Secure Boot capable UEFI PC, and turning it on is the standard setting (it also blocks unsigned boot loaders) |
| 3 | Virtualization (VT-x / AMD-V) | **Enabled** | VMs will not start with it off (often off by default) |
| 4 | Boot from USB devices | **Disabled** | Stops staff booting from a USB stick |
| 5 | Supervisor (BIOS) password | **Set** | Needed to enter and change firmware settings |
| 6 | Fan / temperature monitoring | **Enabled** | Already correct. First place to look for shutdowns under load |

- **A.** Rows **1 and 2** (TPM 2.0 and Secure Boot).
- **B.** Disabling USB boot only works until someone goes into the firmware and turns it back on. The supervisor password stops them changing it.

**Marking (8 points):** 1 per row (6), 1 for A (both row numbers needed), 1 for B (must say the password stops staff undoing the USB setting).
- 7 to 8: pass with confidence. 5 to 6: re-read the Firmware settings table. Under 5: redo the Firmware section of the cheat sheet.
- Common slip: changing row 6 to Disabled "to save power". The scenario says IT needs it, so a needless change loses that row.

---

## C1P01-PBQ2: Will it fit? Boards, cases and slots

**Part A**

| Form factor | Size | Expansion slots |
|---|---|---|
| ATX | 12 x 9.6 in | up to 7 |
| microATX | 9.6 x 9.6 in | up to 4 |
| Mini-ITX | about 6.7 x 6.7 in | 1 |

**Part B** (a smaller board fits a bigger case, never the other way round)

| Board | Case X (up to ATX) | Case Y (up to microATX) | Case Z (up to Mini-ITX) |
|---|---|---|---|
| ATX | Yes | No | No |
| microATX | Yes | Yes | No |
| Mini-ITX | Yes | Yes | Yes |

**Part C.** **Slot C** (PCIe x16). Graphics cards normally use the x16 slot nearest the CPU, and this one is wired for all 16 lanes (so the "physically x16 but wired for fewer lanes" trap does not apply).

**Marking (16 points):** Part A 6, Part B 9, Part C 1, one point per box.
- 14 to 16: strong. 11 to 13: fine, recheck Part B if you lost points there (the direction rule is a favourite exam trap). Under 11: learn the Form factors table in the memorise sheet and redo.
- Part B is partial credit like the real exam: a wrong box does not cancel a right one.
