# Core 1, Part 5 PBQ answers

Tasks: [part-05-pbq.md](part-05-pbq.md). Facts come from the [Part 5 cheat sheet](../../core1/part-05-displays/cheatsheet.md).

---

## C1P05-PBQ1: Choose the right screen

**Part A**

| Person | Screen type | Why |
|---|---|---|
| 1 | **IPS** | Best colour accuracy, widest viewing angles |
| 2 | **TN** | Fastest response, cheapest, poor viewing angles |
| 3 | **VA** | Best contrast (about 3000:1), deep blacks |
| 4 | **OLED** | No backlight, each pixel lights itself, true black |
| 5 | **Mini-LED** | An LCD with thousands of tiny LEDs in local dimming zones |

**Part B**

| Ticket | Failed part | Why |
|---|---|---|
| 1 | **inverter** | It powers the CCFL backlight tube. Failing gives a very dim or flickering screen with a faint picture |
| 2 | **digitizer** | The see-through layer that senses touch. The picture is fine, so the display is not at fault |

**Marking (7 points):** 1 per person, 1 per ticket.
- 6 to 7: strong. 4 to 5: fine, redo the panel table. Under 4: relearn the LCD panel types and OLED sections.
- Common slip: picking IPS for person 3. IPS contrast is about 1000:1, VA is the contrast winner.

---

## C1P05-PBQ2: Fix the blurry, choppy monitor

- **A.** Resolution **2560 x 1440** (the monitor's native QHD resolution, so text is sharp again) and refresh rate **144 Hz**. A non-native resolution looks blurry, and 60 Hz is why fast action looks choppy.
- **B.** **Graphics card, cable, monitor.** All three must support the higher rate (the display setting then has to be switched to it, as in part A). A case fan and a keyboard have nothing to do with it.
- **C.**

| Screen | PPI | Working |
|---|---|---|
| 24-inch Full HD | **92** | 2203 / 24 = 91.8 |
| 27-inch QHD | **109** | 2937 / 27 = 108.8 |
| 24-inch 4K UHD | **184** | 4406 / 24 = 183.6 |

Sharpest: **the 24-inch 4K UHD** (highest PPI). The same resolution on a smaller screen is sharper.

**Marking (9 points):** A 2, B 3 (exactly three items listed, one per correct item), C 4 (three PPI values plus the sharpest screen).
- A PPI value within 1 of the answer is accepted for rounding differences.
- 8 to 9: strong. 6 to 7: fine. Under 6: reread the Resolution, Pixel density and Refresh rate sections.
