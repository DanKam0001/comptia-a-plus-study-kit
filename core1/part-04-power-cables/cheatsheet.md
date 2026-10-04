# Core 1, Part 4: Power Supplies, Cables and Connectors

**Objectives 3.6** (install the appropriate power supply) and **3.2** (summarize basic cable types and their connectors, features and purposes) (220-1201).
Domain: Hardware (25% of the exam).

## Power supply (3.6)

| Topic | Facts |
|---|---|
| Input | **110-120 VAC** (e.g. North America) vs **220-240 VAC** (most other countries). Manual switch set wrong can destroy the unit; many modern PSUs auto-range |
| Output rails | **3.3 V, 5 V, 12 V**. The 12 V rail powers the CPU and GPU |
| Main connector | **20+4 pin** (24 total) |
| Modular | Detachable cables, better airflow |
| Redundant | Two supplies in one chassis (servers) |
| Wattage | Maximum load. Size above peak draw with headroom |
| Efficiency | **80 PLUS**: Bronze, Silver, Gold, Platinum, Titanium |

## Copper network cables (3.2)

| Category | Speed |
|---|---|
| Cat 5e | 1 Gbps |
| Cat 6 | 1 Gbps (10 Gbps only up to about 55 m) |
| Cat 6a | 10 Gbps |

- Twisted-pair Ethernet segment maximum: **100 m**.
- **UTP** = unshielded (standard). **STP** = shielded (resists electromagnetic interference).
- **Plenum-rated**: fire-resistant, low-smoke jacket, for air-handling spaces (above ceilings).
- **Direct burial**: rated for underground.
- **Coax**: F-type connector, cable TV and broadband.

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

The green and orange pairs are swapped. **Same standard both ends = straight-through. A on one end, B on the other = crossover.**

## Fiber

- **Single-mode**: about 9 micron core, laser, long distance (kilometers).
- **Multimode**: 50 or 62.5 micron core, shorter distance (inside buildings).
- **ST** bayonet twist, **SC** square push-pull, **LC** small with an RJ45-style latch.

## Peripheral and video cables

| Cable | Facts |
|---|---|
| USB 2.0 | 480 Mbps |
| USB 3.0 | 5 Gbps (SuperSpeed) |
| Thunderbolt 3 / 4 | 40 Gbps over USB-C connector |
| Serial | DB-9 (RS-232), console access to network gear |
| HDMI | Digital video and audio |
| DisplayPort | Digital video and audio, can drive several monitors |
| DVI | DVI-D digital, DVI-A analog, DVI-I both |
| VGA | Analog, 15-pin, blue |
| USB-C | Video via DisplayPort alternate mode |

## Connectors

| Connector | Facts |
|---|---|
| RJ45 | 8-wire Ethernet |
| RJ11 | Telephone, fewer wires |
| F-type | Coax |
| ST / SC / LC | Fiber |
| Punchdown block | Terminates wires onto a patch panel |
| Micro USB / Mini USB | Older small USB connectors |
| Molex | Legacy 4-pin power (drives and fans) |
| Lightning | Apple, reversible |
| DB-9 | Serial |

An **adapter** converts one connector to another. Check it supports the signal, not just the shape.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| PC dies on plug-in after PSU swap abroad | Voltage switch on the wrong setting |
| 10 Gbps needed over 90 m | Cat 6a |
| Cable run above a ceiling | Plenum-rated |
| Join two similar devices directly | Crossover cable |
| Projector shows nothing | Port/cable mismatch, or adapter doesn't support the signal |
