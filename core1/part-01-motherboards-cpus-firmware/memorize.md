# Memorise list: Motherboards, CPUs and Firmware (Core 1, Part 1)

Understand the video first, then learn these cold. They're the facts a scenario question assumes you already know.
Flashcards: [`flashcards/core1_part01.csv`](../../flashcards/core1_part01.csv) (import into Anki or any flashcard app).


## Form factors

| Question | Answer |
|---|---|
| ATX board size and max expansion slots | 12 x 9.6 in, up to 7 slots |
| microATX board size and max expansion slots | 9.6 x 9.6 in, up to 4 slots |
| Mini-ITX board size and expansion slots | About 6.7 x 6.7 in, 1 slot |
| Can a bigger board fit a smaller case? | No. A smaller board usually fits a bigger case, never the reverse |

## Expansion slots

| Question | Answer |
|---|---|
| PCI vs PCIe in one line | PCI = shared parallel bus. PCIe = private point-to-point serial lanes |
| PCIe slot lane sizes | x1, x4, x8, x16. Graphics card normally in x16 |
| Are PCIe generations backward compatible? | Yes. A new card works in an older slot at the older speed |
| A physically x16 slot that runs slow: why? | It may be wired for fewer lanes (e.g. x4). Check the manual |

## Connectors

| Question | Answer |
|---|---|
| SATA data cable pin count / SATA power cable pin count | 7-pin data, 15-pin power |
| eSATA carries what? | Data only, no power. External version of SATA |
| M.2 size code 2280 means | 22 mm wide, 80 mm long |
| Motherboard main power connector | 24-pin |
| CPU power connector | 4-pin or 8-pin, near the processor |
| Graphics card power connector | 6-pin or 8-pin on the card |
| 3-pin vs 4-pin fan header | The 4th pin allows precise speed control (fan curves) |

## Sockets and CPUs

| Question | Answer |
|---|---|
| LGA means and where the pins are | Land Grid Array. Pins are in the motherboard socket, CPU has flat pads |
| PGA means and where the pins are | Pin Grid Array. Pins are on the CPU |
| Socket matches but new CPU still not recognised: what else? | Chipset support, and possibly a firmware update |
| Multisocket board | Two or more CPUs sharing the same memory (servers) |
| x86 memory limit | About 4 GB (32-bit) |
| x64 | 64-bit extension of x86. Nearly all Windows desktops and laptops |
| ARM is used in | Phones, tablets, Apple silicon Macs, some Windows laptops. Power efficient |
| Hyper-threading / SMT effect | One core runs two threads: 8 cores can show as 16 logical processors |
| P-cores vs E-cores | Performance cores for heavy work, efficiency cores for background work and lower power |

## Cards and cooling

| Question | Answer |
|---|---|
| Capture card direction | Takes video IN from an outside source (camera, console) |
| After removing a CPU cooler | Clean off the old thermal paste and apply fresh |
| Cause of overheating after a cooler swap | Missing or old thermal paste |

## Firmware

| Question | Answer |
|---|---|
| UEFI advantages over BIOS | Faster boot, drives larger than 2 TB, Secure Boot |
| Secure Boot does | Only allows boot loaders signed by a trusted key |
| Boot password vs BIOS password | Boot = needed to start the PC. BIOS/supervisor = needed to change firmware settings |
| Stop staff booting from USB and stop them undoing it | Disable USB boot, then set a BIOS (supervisor) password |
| VM won't start, virtualization off: setting? | Enable Intel VT-x or AMD-V in firmware |
| Windows 11 hardware requirements in firmware | TPM 2.0 and Secure Boot (UEFI) |
| TPM vs HSM | TPM = secure chip protecting one machine's keys. HSM = dedicated hardware guarding keys for many systems |
