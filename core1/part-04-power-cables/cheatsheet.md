# Core 1, Part 4: Power Supplies, Cables and Connectors

**Objectives 3.6** (install the appropriate power supply) and **3.2** (summarize basic cable types and their connectors, features and purposes) (220-1201).
Domain: Hardware (25% of the exam).

Objective bullets covered: 3.6 input 110-120 VAC vs 220-240 VAC, output 3.3 V vs 5 V vs 12 V, 20+4 pin motherboard connector, redundant, modular, wattage rating, energy efficiency. 3.2 copper network cables (categories, T568A/T568B, coaxial, STP, direct burial, UTP, plenum), optical (single-mode, multimode), peripheral cables (USB 2.0, USB 3.0, serial, Thunderbolt), video cables (HDMI, DisplayPort, DVI, VGA, USB-C), hard drive cables (SATA, eSATA), adapters, connector types (RJ11, RJ45, F-type, ST, SC, LC, punchdown block, microUSB, miniUSB, USB-C, Molex, Lightning, DB9).

## Power supply (3.6)

| Topic | Facts |
|---|---|
| Job | Converts wall **AC** into the low-voltage **DC** a PC uses |
| Input | **110-120 VAC** (for example North America) vs **220-240 VAC** (most other countries). A manual voltage switch set wrong can destroy the unit. Many modern PSUs auto-range (no switch) |
| Output rails | **3.3 V, 5 V, 12 V**. The 12 V rail powers the CPU and GPU |
| Wire colors | Orange = 3.3 V, red = 5 V, yellow = 12 V, black = ground |
| Main connector | **20+4 pin** (24 total). The detachable 4-pin makes it fit 20-pin and 24-pin boards |
| CPU power | 4+4 pin (8 pin), near the processor |
| Graphics card power | 6-pin or 6+2 (8) pin |
| Drive power | 15-pin SATA power; 4-pin Molex (legacy) |
| Modular | Detachable cables. Less clutter, better airflow. Semi-modular keeps the main cables fixed |
| Redundant | Two supplies in one chassis, servers keep running if one fails |
| Wattage rating | The maximum load it can supply. Size above the system's peak draw with headroom |
| Efficiency | **80 PLUS** certification. Levels low to high: Bronze, Silver, Gold, Platinum, Titanium. Minimum efficiency at 50% load on 115 V: 85, 88, 90, 92, 94 percent (basic 80 PLUS = 80). Wasted power becomes heat |

Never open a power supply: dangerous voltages remain even when unplugged.

## Copper network cables (3.2)

| Category | Speed |
|---|---|
| Cat 5 | 100 Mbps (old) |
| Cat 5e | 1 Gbps |
| Cat 6 | 1 Gbps (10 Gbps only up to about 55 m) |
| Cat 6a | 10 Gbps, up to 100 m |
| Cat 8 | 25/40 Gbps, up to about 30 m (data centers) |

- Twisted-pair Ethernet segment maximum: **100 m**.
- **UTP** = unshielded (standard). **STP** = shielded (resists electromagnetic interference, for noisy places).
- **Plenum-rated**: fire-resistant, low-smoke jacket for air-handling spaces (above ceilings, ducts).
- **Direct burial**: rated for underground use.
- **Coaxial**: central wire plus shield. **F-type** connector. Cable TV and broadband from the provider.

## T568A vs T568B

| Pin | T568A | T568B |
|---|---|---|
| 1 | green-white | orange-white |
| 2 | green | orange |
| 3 | orange-white | green-white |
| 4 | blue | blue |
| 5 | blue-white | blue-white |
| 6 | orange | green |
| 7 | brown-white | brown-white |
| 8 | brown | brown |

The green and orange pairs are swapped. **Same standard both ends = straight-through.** **A on one end, B on the other = crossover** (joins two similar devices directly).

## Fiber optic

- Carries **light** through glass, immune to electrical interference.
- **Single-mode**: about 9 micron core, laser, long distance (kilometers).
- **Multimode**: 50 or 62.5 micron core, shorter distance (inside buildings).
- Connectors: **ST** (Straight Tip, bayonet twist-lock), **SC** (Subscriber Connector, square push-pull), **LC** (Lucent Connector, small with an RJ45-style latch).

## Peripheral cables

| Cable | Facts |
|---|---|
| USB 2.0 | 480 Mbps |
| USB 3.0 | 5 Gbps (SuperSpeed, usually blue port) |
| Thunderbolt 3 / 4 | 40 Gbps, uses the USB-C connector |
| Serial | **DB-9** connector (RS-232). Console access to network gear |

## Video cables

| Cable | Facts |
|---|---|
| HDMI | Digital video and audio. HDMI 2.0 = 18 Gbps, HDMI 2.1 = 48 Gbps |
| DisplayPort | Digital video and audio, can drive several monitors. DisplayPort 1.4 = 32.4 Gbps |
| DVI | DVI-D digital, DVI-A analog, DVI-I both |
| VGA | Analog, 15-pin, blue connector |
| USB-C | Video via DisplayPort alternate mode |

## Hard drive cables

- **SATA**: 7-pin data cable (separate 15-pin power).
- **eSATA**: external SATA, shielded connector, data only (no power).

## Connectors

| Connector | Facts |
|---|---|
| RJ45 | 8 pins, Ethernet |
| RJ11 | Telephone, fewer wires (usually 2 to 4) |
| F-type | Coax, screw-on |
| ST / SC / LC | Fiber |
| Punchdown block | Terminates cable wires (behind a wall) onto a patch panel |
| MicroUSB / MiniUSB | Older small USB connectors |
| USB-C | Small reversible connector for data, power and video |
| Molex | Legacy 4-pin power for drives and fans (yellow 12 V, red 5 V, two black) |
| Lightning | Apple, 8-pin, reversible (replaced by USB-C) |
| DB-9 | 9-pin serial |

An **adapter** converts one connector to another. Check it supports the signal, not just the shape.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| PC dies on plug-in after moving countries | Input voltage switch on the wrong setting |
| 10 Gbps needed over 90 m | Cat 6a |
| Cable run above a ceiling | Plenum-rated |
| Join two similar devices directly | Crossover cable (A on one end, B on the other) |
| USB-C laptop, HDMI projector | USB-C to HDMI cable or adapter |
| Long-distance link between buildings | Single-mode fiber |
