# Core 1, Part 1: Motherboards, CPUs and Firmware

**Objective 3.5** (220-1201): *Given a scenario, install and configure motherboards, central processing units (CPUs), and add-on cards.*
Domain: Hardware (25% of the exam).

## Form factors

| Form factor | Size | Expansion slots | Typical use |
|---|---|---|---|
| ATX | 12 x 9.6 in | up to 7 | Full-size desktop |
| microATX | 9.6 x 9.6 in | up to 4 | Office PC |
| Mini-ITX | about 6.7 x 6.7 in | 1 | Small and compact builds |

Mounting holes line up, so a smaller board usually fits a bigger case, never the other way round.

## Expansion slots

- **PCI**: shared parallel bus, all cards share the bandwidth.
- **PCIe**: point-to-point serial lanes, each lane is a private two-way link.
- Slot sizes: x1, x4, x8, x16. Graphics cards normally use the x16 slot nearest the CPU.
- Each PCIe generation roughly doubles per-lane speed. Generations are backward compatible (works at the older speed).
- Trap: a slot can be **physically x16 but wired for fewer lanes**. Check the manual.

## Connectors

| Connector | What to remember |
|---|---|
| SATA | 7-pin data cable plus a separate 15-pin SATA power cable |
| eSATA | External SATA. Shielded connector, data only (no power) |
| M.2 | Slot on the board, no cables. Key notch decides what fits. "2280" = 22 mm wide, 80 mm long |
| Main power | 24-pin |
| CPU power | 4 or 8-pin, near the processor |
| GPU power | 6 or 8-pin, on the graphics card |
| Headers | Front panel (power, reset, LEDs), front USB, front audio, fans |

- **Front panel header:** a reversed power-switch pair means the power button does nothing.
- **Fan headers:** 3-pin (voltage or on/off control) vs 4-pin (the fourth pin allows precise speed control, which is how fan curves work).

## CPU sockets

- **LGA (Land Grid Array):** pins are in the socket on the motherboard, the CPU has flat pads. Used by Intel desktop chips, and by AMD's current AM5.
- **PGA (Pin Grid Array):** pins are on the CPU itself. Used by AMD for years before AM5.
- A matching socket is not enough: the **chipset** must support the CPU, and sometimes the board needs a **firmware update** first.
- **Multisocket** boards (servers) hold two or more CPUs sharing the same memory.

## CPU architecture

| | Notes |
|---|---|
| x86 | 32-bit. Can only address about 4 GB of memory |
| x64 | 64-bit extension of x86. Nearly all Windows desktops and laptops |
| ARM | Simpler instruction set, power efficient. Phones, tablets, Apple silicon Macs, some Windows laptops |

Software must be built for the architecture it runs on.

## Cores

- A **core** is a complete processing unit. Chips contain several.
- **Hyper-threading / simultaneous multithreading:** one core runs two threads. 8 cores can appear as 16 logical processors.
- Many current chips mix **performance cores** (heavy work) and **efficiency cores** (background work, less power).

## Expansion cards

| Card | Does |
|---|---|
| Video card | Dedicated graphics processor and its own memory |
| Sound card | Better audio than onboard |
| Network interface card (NIC) | Wired/wireless networking, or faster than onboard |
| Capture card | Takes video IN from an outside source (camera, console) for recording/streaming |

## Cooling

- **Heat sink** (metal fins) pulls heat off the chip. **Fan** pushes air through it.
- **Thermal paste/pads** fill microscopic gaps between chip and heat sink. After removing a cooler: clean the old paste and apply fresh.
- **Liquid cooling:** pump, tubes, radiator with fans. For very hot chips or cramped cases.
- Missing or old thermal paste is a classic cause of overheating and random shutdowns.

## BIOS and UEFI

- Firmware on the motherboard that runs first: tests hardware, finds a boot device, hands over to the OS boot loader.
- UEFI replaces BIOS: faster boot, supports drives larger than 2 TB, adds Secure Boot. People (and the exam) still say "BIOS" for both.

## Firmware settings to know

| Setting | What it does |
|---|---|
| Boot options | Order of devices tried (internal drive, USB, network) |
| USB permissions | Disable USB ports or block booting from USB |
| Secure Boot | Only allows boot loaders signed by a trusted key |
| Boot password | Needed to start the computer at all |
| BIOS/supervisor password | Needed to enter and change firmware settings |
| Fan / temperature monitoring | First place to look for shutdowns under load |
| Virtualization support | Intel VT-x / AMD-V. Often off by default. Required by virtual machines |
| TPM | Trusted Platform Module: secure chip storing keys. Windows 11 needs TPM 2.0 |
| HSM | Hardware Security Module: dedicated hardware guarding keys for many systems at scale |

## Common scenarios

| Symptom | Likely answer |
|---|---|
| New CPU won't fit the board | Socket mismatch |
| Windows 11 says "not supported" on a recent PC | TPM 2.0 and/or Secure Boot disabled in firmware |
| VM refuses to start (virtualization off) | Enable VT-x / AMD-V in firmware |
| New cooler fitted, PC now overheats | No fresh thermal paste |
| Stop staff booting from USB drives | Disable USB boot, set a BIOS password so it can't be changed |
