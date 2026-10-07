# Core 1, Part 5 PBQs: Displays

Performance-based question (PBQ) practice for **Objective 3.1** (220-1201). Do each task on paper or in a text file. Answers are in a separate file ([part-05-pbq-answers.md](part-05-pbq-answers.md)), so don't open it until you have finished.

If you are stuck, check the [Part 5 cheat sheet](../../core1/part-05-displays/cheatsheet.md), mark that item, and lose the point.

---

## C1P05-PBQ1: Choose the right screen

- **Objective:** 3.1
- **Type:** Matching (with a short symptoms table)
- **Time guide:** 5 minutes

### Scenario

An office is buying five monitors for five different people, and also has two repair tickets on older laptops. Match each person to the best screen type, then name the failed part on each ticket.

### Materials

**Part A: the people**

1. A designer who edits photos and needs the best colour accuracy and wide viewing angles, on an LCD.
2. A gamer on a tight budget who wants the cheapest, fastest response time and does not mind poor side viewing angles.
3. A video editor who wants the best contrast ratio and deep blacks from an LCD (about 3000:1).
4. A receptionist who wants a screen with no backlight at all, where each pixel makes its own light and black is truly black.
5. A manager who wants a very bright LCD with better contrast, using thousands of tiny LEDs in local dimming zones.

**Screen type choices** (each used once): `IPS`, `TN`, `VA`, `OLED`, `Mini-LED`.

**Part B: repair tickets.** Choices for the failed part: `inverter`, `digitizer`, `graphics card`, `hinge`.

| Ticket | Failed part |
|---|---|
| 1. Old laptop with a fluorescent (CCFL) backlight: screen is very dim, and the picture is faintly visible with a flashlight | |
| 2. Tablet: picture is perfect but touches are ignored | |

### Task

Part A: write the screen type for each person. Part B: fill in the two blanks.

### Marking

7 points: 1 per person (5) plus 1 per ticket (2).

---

## C1P05-PBQ2: Fix the blurry, choppy monitor

- **Objective:** 3.1
- **Type:** Configure this (display settings form), plus a calculation
- **Time guide:** 6 minutes

### Scenario

A customer bought a 27-inch QHD monitor that supports 144 Hz. They say text looks blurry and fast action looks choppy. You open the display settings and see the screen below. Everything in the hardware chain supports 144 Hz.

### Materials

```
+--------------------------------------------------+
|  DISPLAY SETTINGS                                |
|--------------------------------------------------|
|  Monitor:        27-inch QHD, 144 Hz capable     |
|  Resolution:     [ 1920 x 1080 ]  (current)      |
|                  options: 1280 x 720             |
|                           1920 x 1080            |
|                           2560 x 1440            |
|                           3840 x 2160            |
|  Refresh rate:   [ 60 Hz ]        (current)      |
|                  options: 60 Hz, 144 Hz          |
+--------------------------------------------------+
```

**Part C: pixel density.** Use pixels per inch (PPI) = diagonal pixels divided by diagonal inches. The diagonal in pixels is shown for you:

| Screen | Diagonal pixels | Diagonal inches | PPI (round to a whole number) |
|---|---|---|---|
| 24-inch Full HD | 2203 | 24 | |
| 27-inch QHD | 2937 | 27 | |
| 24-inch 4K UHD | 4406 | 24 | |

### Task

- **A.** Write the resolution and the refresh rate you should select.
- **B.** The 144 Hz option is not listed on another customer's PC. Name the **three** things that must all support a higher refresh rate. Choose from: `graphics card`, `cable`, `monitor`, `case fan`, `keyboard`.
- **C.** Fill in the three PPI values. Then say which of the three screens is the sharpest.

### Marking

9 points: A 2 (one for each setting), B 3 (one for each correct item; list exactly three, because listing more than three scores 0 for B), C 4 (one for each PPI value plus one for the sharpest screen).
