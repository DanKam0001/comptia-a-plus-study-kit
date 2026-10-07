# Core 1, Part 2: RAM: Form Factors, DDR, ECC and Channels

**Objective 3.3** (220-1201): *Compare and contrast RAM characteristics.*
Domain: Hardware (25% of the exam).

Objective bullets covered: form factors (SODIMM, DIMM), DDR iterations, ECC vs non-ECC RAM, channel configurations.

## What RAM is

- Working memory: whatever is open right now. Think of it as your desk, with storage as the cupboard.
- **Volatile**: contents are lost when power is off.
- Far faster than storage. More RAM means more can stay open before the system leans on slow storage.
- More RAM adds **capacity**, not processor speed.

## Form factors

| | DIMM | SODIMM |
|---|---|---|
| Full name | Dual In-line Memory Module | Small Outline DIMM |
| Used in | Desktops, servers | Laptops, mini PCs, all-in-ones |
| Length | 133.35 mm (5.25 in) | About 69.6 mm (DDR4 and DDR5), about half |
| DDR3 pins | 240 | 204 |
| DDR4 pins | 288 | 260 |
| DDR5 pins | 288 | 262 |

DIMM and SODIMM are never interchangeable. (Older DDR2 also existed: 240-pin DIMM, 200-pin SODIMM. It is not in the current objectives.)

## DDR iterations

| | Voltage | Notes |
|---|---|---|
| DDR3 | 1.5 V (1.35 V low-voltage DDR3L) | Oldest in scope |
| DDR4 | 1.2 V | Very common |
| DDR5 | 1.1 V | Starts at 4800 MT/s |

- DDR = **Double Data Rate**: data moves on both edges of the clock signal.
- Generations are **not interchangeable**. The **notch** sits in a different place on each, so the wrong stick will not seat. Never force it.
- The motherboard slot decides the generation. Check the board (and CPU) before buying.
- Newer generation = faster and lower voltage.

## Reading a label

- **Speed**: DDR4-3200 = 3200 million transfers per second (MT/s).
- **PC rating = DDR speed x 8**: DDR4-3200 = **PC4-25600** (25,600 MB/s peak). DDR3 modules say PC3, DDR5 say PC5.
- Mixed-speed sticks all run at the **slowest** stick's speed.

## ECC vs non-ECC

| | ECC | Non-ECC |
|---|---|---|
| Full name | Error-Correcting Code | none |
| Width | 72 bits (64 data + 8 check) | 64 bits |
| Does | Detects and corrects single-bit errors, detects some multi-bit errors | Nothing for errors |
| Cost / speed | Costs more, slightly slower | Standard |
| Needs | CPU **and** motherboard support | Anything |
| Used in | Servers, workstations | Everyday PCs |

Note: DDR5 chips have a built-in error check inside the chip, but that is not the same as full ECC modules, which still need CPU and board support.

## Channel configurations

- Single channel = 64-bit path. **Dual channel = 128-bit path**, so about twice the bandwidth.
- Workstations and servers also use **triple** and **quad** channel (more channels, more bandwidth).
- Install **matching sticks in the slot pair the motherboard manual designates** (often the same-colored slots). Wrong slots = still works, but **single channel**.

## Installing and checking

1. Power off and unplug. Touch bare metal or wear an anti-static strap.
2. Open the clips. Line the notch up with the slot.
3. Press both ends down until the clips click.
4. Start the PC and check the total in the firmware or Task Manager. If short, reseat before blaming the board.

## Pre-purchase checklist

Generation, form factor, ECC support, maximum capacity and speed the board supports, free slots.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| New memory too long for a laptop | It is a DIMM; laptops use SODIMM |
| Second stick gave no speed boost | Wrong slots, running single channel |
| Server crashes with silent data errors | ECC memory on a supporting board and CPU |
| Memory will not seat in the slot | Wrong DDR generation (notch mismatch) |
| Two different-speed sticks | Both run at the slower speed |
