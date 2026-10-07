# Core 1, Part 1 PBQs: Motherboards, CPUs and Firmware

Performance-based question (PBQ) practice for **Objective 3.5** (220-1201). Do each task on paper or in a text file. Answers are in a separate file ([part-01-pbq-answers.md](part-01-pbq-answers.md)), so don't open it until you have finished.

Work from memory first. If you are stuck, look at the [Part 1 cheat sheet](../../core1/part-01-motherboards-cpus-firmware/cheatsheet.md), mark that item, and lose the point. That is how you find your weak spots.

---

## C1P01-PBQ1: Set up the new office PC in the firmware screen

- **Objective:** 3.5
- **Type:** Configure this (firmware settings form)
- **Time guide:** 5 minutes

### Scenario

You are setting up a new office PC. Its owner needs to run Windows 11 and a virtual machine (VM) for testing. The manager also wants staff unable to boot the PC from a USB stick, and unable to change these firmware settings later. IT also wants to be able to check temperatures if the PC ever shuts down under load.

### Materials

This is the firmware (UEFI) settings screen as it is now:

```
+-------------------------------------------------------------+
|  UEFI SETUP                                                 |
|-------------------------------------------------------------|
|  1. TPM (Trusted Platform Module)      [ Disabled ]         |
|  2. Secure Boot                        [ Disabled ]         |
|  3. Virtualization (Intel VT-x / AMD-V)[ Disabled ]         |
|  4. Boot from USB devices              [ Enabled  ]         |
|  5. Supervisor (BIOS) password         [ Not set  ]         |
|  6. Fan / temperature monitoring       [ Enabled  ]         |
+-------------------------------------------------------------+
```

Options for rows 1 to 4 and 6: **Enabled** or **Disabled**. Options for row 5: **Set** or **Not set**.

### Task

Copy the table below and fill in the **final** setting for each row so every need in the scenario is met. Make no unneeded changes: if a row is already correct, write its current value.

| Row | Setting | Final value |
|---|---|---|
| 1 | TPM | |
| 2 | Secure Boot | |
| 3 | Virtualization (VT-x / AMD-V) | |
| 4 | Boot from USB devices | |
| 5 | Supervisor (BIOS) password | |
| 6 | Fan / temperature monitoring | |

Then answer in one line each:

- **A.** Which two of the rows above does Windows 11 need? (Write the row numbers.)
- **B.** Why is row 5 needed as well as row 4?

### Marking

8 points: 1 point per row (6 points), plus 1 point for each of A and B. Partial credit is given per row, exactly as on the real exam.

---

## C1P01-PBQ2: Will it fit? Boards, cases and slots

- **Objective:** 3.5
- **Type:** Fill-in table (with a word bank)
- **Time guide:** 5 minutes

### Scenario

A school is rebuilding old PCs. A technician has three motherboards and three cases, and needs to know which boards fit which cases. Assume the mounting holes line up whenever the board is not bigger than the case's maximum size. The technician also needs a quick size table for the new apprentices.

### Materials

**Word bank for Part A:** `12 x 9.6 in`, `9.6 x 9.6 in`, `about 6.7 x 6.7 in`, `1`, `up to 4`, `up to 7`.

**Part B cases:**
- Case X takes boards **up to ATX** size.
- Case Y takes boards **up to microATX** size.
- Case Z takes boards **up to Mini-ITX** size only.

**Part C expansion slots on one motherboard:**

```
Slot A:  PCIe x1
Slot B:  PCIe x4
Slot C:  PCIe x16   (nearest the CPU, wired for all 16 lanes)
Slot D:  PCIe x8
```

### Task

**Part A.** Fill in the table using the word bank. Each item is used once.

| Form factor | Size | Expansion slots |
|---|---|---|
| ATX | | |
| microATX | | |
| Mini-ITX | | |

**Part B.** Write **Yes** or **No** in each box: does the board fit the case?

| Board | Case X | Case Y | Case Z |
|---|---|---|---|
| ATX | | | |
| microATX | | | |
| Mini-ITX | | | |

**Part C.** The school adds one graphics card. Which slot letter (A, B, C or D) should it go in?

### Marking

16 points: Part A 6 (one per box), Part B 9 (one per box), Part C 1. No negative marking.
