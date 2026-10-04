# Memorise list: RAM: Form Factors, DDR, ECC and Channels (Core 1, Part 2)

Understand the video first, then learn these cold. They're the facts a scenario question assumes you already know.
Flashcards: [`flashcards/core1_part02.csv`](../../flashcards/core1_part02.csv) (import into Anki or any flashcard app).


## Form factors

| Question | Answer |
|---|---|
| DIMM vs SODIMM: where each is used | DIMM: desktops and servers (full size). SODIMM: laptops, mini PCs, all-in-ones (about half the length) |
| DDR3 DIMM / SODIMM pin counts | 240 / 204 |
| DDR4 DIMM / SODIMM pin counts | 288 / 260 |
| DDR5 DIMM / SODIMM pin counts | 288 / 262 |

## DDR generations

| Question | Answer |
|---|---|
| Are DDR3, DDR4 and DDR5 interchangeable? | No. Different notch position, voltage and design |
| DDR3 voltage | 1.5 V (1.35 V low-voltage variant) |
| DDR4 voltage | 1.2 V |
| DDR5 voltage | 1.1 V |
| DDR5 starting speed | 4800 MT/s |

## Module labels

| Question | Answer |
|---|---|
| PC4-25600 equals which DDR4 speed? | DDR4-3200 (3200 x 8 = 25,600 MB/s peak bandwidth) |
| How do you get the PC rating from a DDR speed? | Multiply MT/s by 8 bytes |
| Modules of different speeds installed together run at | The speed of the slowest module |

## ECC

| Question | Answer |
|---|---|
| What ECC does | Detects and corrects single-bit errors |
| ECC module width vs non-ECC | 72 bits vs 64 bits |
| What must support ECC | Both the CPU and the motherboard |

## Channels

| Question | Answer |
|---|---|
| Single vs dual channel data path width | 64-bit vs 128-bit |
| Dual channel install rule | Matching modules in the slot pair the manual designates (often the same color) |
| Triple and quad channel are found on | Workstations and servers |
