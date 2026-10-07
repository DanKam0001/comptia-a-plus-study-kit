# Core 1, Part 2 PBQs: RAM

Performance-based question (PBQ) practice for **Objective 3.3** (220-1201). Do each task on paper or in a text file. Answers are in a separate file ([part-02-pbq-answers.md](part-02-pbq-answers.md)), so don't open it until you have finished.

If you are stuck, check the [Part 2 cheat sheet](../../core1/part-02-ram/cheatsheet.md), mark that item, and lose the point.

---

## C1P02-PBQ1: Name that memory stick

- **Objective:** 3.3
- **Type:** Fill-in table
- **Time guide:** 5 minutes

### Scenario

You are sorting a box of loose memory sticks at a repair shop. The labels are worn off, so all you can read are the number of pins, the voltage and which kind of machine each stick came out of. Work out what each one is, and fill in the speed-rating names on the shelf labels.

### Materials

**Part A: the sticks**

| Stick | Pins | Voltage | Came out of |
|---|---|---|---|
| 1 | 204 | 1.5 V | a laptop |
| 2 | 240 | 1.5 V | a desktop |
| 3 | 260 | 1.2 V | a laptop |
| 4 | 262 | 1.1 V | a laptop |
| 5 | 288 | 1.2 V | a desktop |
| 6 | 288 | 1.1 V | a desktop |

**Part B: shelf labels** (rule: the PC rating is the DDR speed multiplied by 8)

| Stick label | PC rating |
|---|---|
| DDR3-1600 | |
| DDR4-2400 | |
| DDR4-3200 | PC4-25600 (given, as the example) |
| DDR5-4800 | |

### Task

**Part A.** For each stick write the **DDR generation** (DDR3, DDR4 or DDR5) and the **form factor** (DIMM or SODIMM).

**Part B.** Fill in the three blank PC ratings. Use the right prefix for the generation (PC3, PC4 or PC5).

### Marking

9 points: Part A 6 (one per stick, generation and form factor both right), Part B 3. A stick with only one of the two right scores no point.

---

## C1P02-PBQ2: Get dual channel working

- **Objective:** 3.3
- **Type:** Scenario fix (diagram and short answers)
- **Time guide:** 5 minutes

### Scenario

A customer put two matching 8 GB DDR4 sticks into a desktop. The PC starts, but benchmark software says memory bandwidth is only half of what the sticks should give. The motherboard manual says: "To run two modules in dual channel, install them in slots 2 and 4 (the black slots). Any other pair runs in single channel."

### Materials

The board as the customer installed it (X = a stick is fitted):

```
CPU   [Slot 1 grey: X]  [Slot 2 black: X]  [Slot 3 grey: empty]  [Slot 4 black: empty]
```

### Task

1. Which two slots should the sticks be in? Write the slot numbers.
2. How wide is the data path in single channel, and how wide in dual channel? (Write both in bits.)
3. The customer later adds a third stick: DDR4-2666. The other two are DDR4-3200. At what speed will all of them run?
4. After fitting the new memory, the PC reports 16 GB when 24 GB is installed. Write the first thing you should try, in a few words. Pick one from this list: `reseat the stick` / `replace the motherboard` / `buy ECC memory` / `change to a SODIMM`.

### Marking

5 points: 1 for question 1 (both slot numbers), 1 for question 2 (both widths), 1 for question 3, 1 for question 4, plus 1 for writing the dual-channel result in your own words ("two channels at once, so about double the bandwidth").
