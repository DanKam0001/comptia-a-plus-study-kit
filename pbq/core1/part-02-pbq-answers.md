# Core 1, Part 2 PBQ answers

Tasks: [part-02-pbq.md](part-02-pbq.md). Facts come from the [Part 2 cheat sheet](../../core1/part-02-ram/cheatsheet.md).

---

## C1P02-PBQ1: Name that memory stick

**Part A**

| Stick | Answer | Why |
|---|---|---|
| 1 | DDR3 SODIMM | 204 pins is DDR3 SODIMM (and 1.5 V is DDR3) |
| 2 | DDR3 DIMM | 240 pins is DDR3 DIMM |
| 3 | DDR4 SODIMM | 260 pins is DDR4 SODIMM |
| 4 | DDR5 SODIMM | 262 pins is DDR5 SODIMM |
| 5 | DDR4 DIMM | 288 pins on both DDR4 and DDR5 DIMMs, so the 1.2 V decides: DDR4 |
| 6 | DDR5 DIMM | 288 pins, 1.1 V is DDR5 |

**Part B**

| Stick label | PC rating | Why |
|---|---|---|
| DDR3-1600 | **PC3-12800** | 1600 x 8 = 12800, DDR3 uses PC3 |
| DDR4-2400 | **PC4-19200** | 2400 x 8 = 19200 |
| DDR5-4800 | **PC5-38400** | 4800 x 8 = 38400, DDR5 uses PC5 |

**Marking (9 points):** Part A 6 (both parts of a stick must be right for the point), Part B 3.
- Sticks 5 and 6 are the usual losers: pins alone cannot tell them apart, voltage does.
- 8 to 9: strong. 6 to 7: redo the pin table in the memorise sheet. Under 6: relearn the Form factors and DDR tables.

---

## C1P02-PBQ2: Get dual channel working

1. **Slots 2 and 4.** The manual says so, and any other pair runs single channel. (Slots 1 and 2, as installed, is the fault.)
2. **64-bit in single channel, 128-bit in dual channel.**
3. **2666 (DDR4-2666).** Mixed sticks all run at the slowest stick's speed.
4. **Reseat the stick.** If the total is short, reseat before blaming the board. Replacing the board is not a first step, ECC and SODIMM are unrelated.

Own-words point: any answer that says two channels work at once, about twice the bandwidth.

**Marking (5 points):** 1 per question 1 to 4 (question 1 needs both slot numbers, question 2 needs both widths) plus 1 for the own-words explanation.
- 5: strong. 3 to 4: fine. Under 3: reread the Channel configurations and Installing and checking sections.
