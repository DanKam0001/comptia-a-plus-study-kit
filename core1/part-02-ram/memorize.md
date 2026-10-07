# Memorise list: RAM (Core 1, Part 2)

Understand the video first, then learn these cold.
Flashcards: [`flashcards/core1_part02.csv`](../../flashcards/core1_part02.csv) (import into Anki or any flashcard app).

## Form factors and pins

| Question | Answer |
|---|---|
| DIMM is used in | Desktops and servers (full size) |
| SODIMM is used in | Laptops, mini PCs, all-in-ones (about half length) |
| DDR3 pins: DIMM / SODIMM | 240 / 204 |
| DDR4 pins: DIMM / SODIMM | 288 / 260 |
| DDR5 pins: DIMM / SODIMM | 288 / 262 |

## DDR

| Question | Answer |
|---|---|
| DDR stands for | Double Data Rate |
| DDR3 voltage | 1.5 V (DDR3L = 1.35 V) |
| DDR4 voltage | 1.2 V |
| DDR5 voltage | 1.1 V |
| DDR5 starting speed | 4800 MT/s |
| Can DDR3, DDR4, DDR5 be mixed in one slot? | No. Different notch position, voltage and design |
| What decides which DDR you need? | The motherboard slot (and CPU support) |

## Speed labels

| Question | Answer |
|---|---|
| PC rating from DDR speed | DDR speed x 8 |
| DDR4-3200 is also called | PC4-25600 |
| Sticks of different speeds in one PC | All run at the slowest stick's speed |

## ECC and channels

| Question | Answer |
|---|---|
| ECC stands for | Error-Correcting Code |
| ECC width vs non-ECC | 72 bits vs 64 bits |
| ECC fixes what? | Single-bit errors (detects and corrects) |
| What must support ECC? | Both the CPU and the motherboard |
| ECC is used in | Servers and workstations |
| Single / dual channel path width | 64-bit / 128-bit |
| Higher channel counts | Triple and quad channel (workstations, servers) |
| How to get dual channel | Matching sticks in the slot pair the manual names |
| Volatile means | Contents lost when power is off |
