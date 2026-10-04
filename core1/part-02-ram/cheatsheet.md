# Core 1, Part 2: RAM

**Objective 3.3** (220-1201): *Compare and contrast RAM characteristics.*
Domain: Hardware (25% of the exam).

## What RAM is

- Working memory: whatever is open right now. **Volatile**, so contents are lost when power is off.
- Far faster than storage. More RAM = more can stay open before the system leans on storage.

## Form factors

| | DIMM | SODIMM |
|---|---|---|
| Used in | Desktops, servers | Laptops, mini PCs, all-in-ones |
| Size | Full length | About half the length |
| DDR3 pins | 240 | 204 |
| DDR4 pins | 288 | 260 |
| DDR5 pins | 288 | 262 |

## DDR generations

| | Voltage | Notes |
|---|---|---|
| DDR3 | 1.5 V (1.35 V low-voltage) | Oldest in scope |
| DDR4 | 1.2 V | Very common |
| DDR5 | 1.1 V | Starts at 4800 MT/s |

- Generations are **not interchangeable**: the notch sits in a different place on each, so the wrong stick won't seat.
- The motherboard slot decides the generation.

## Reading a label

- **PC rating = DDR speed x 8**. Example: DDR4-3200 = PC4-25600 (25,600 MB/s peak).
- Mixed-speed modules all run at the **slowest** module's speed.

## ECC vs non-ECC

| | ECC | Non-ECC |
|---|---|---|
| Width | 72 bits | 64 bits |
| Does | Detects and corrects single-bit errors | Nothing for errors |
| Cost / speed | Costs more, slightly slower | Standard |
| Needs | CPU **and** motherboard support | Anything |
| Used in | Servers, workstations | Everyday PCs |

## Channels

- Single channel = 64-bit path. **Dual channel = 128-bit path.** Workstations and servers also use triple and quad channel.
- Install **matching modules in the slot pair the motherboard manual designates** (often the same-colored slots). Wrong slots = single channel.

## Installing

Power off and unplug, anti-static strap, open the clips, align the notch, press both ends until the clips click, then check the total in firmware or Task Manager. If short, reseat before blaming the board.

## Pre-purchase checklist

Generation, form factor, ECC support, maximum capacity and speed the board supports, free slots.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| New memory too long for a laptop | It's a DIMM; laptops use SODIMM |
| Second stick gave no speed boost | Wrong slots, running single channel |
| Server crashes with silent data errors | Needs ECC on a supporting board and CPU |
| Memory won't seat in the slot | Wrong DDR generation (notch mismatch) |
