# Core 1, Part 4 PBQ answers

Tasks: [part-04-pbq.md](part-04-pbq.md). Facts come from the [Part 4 cheat sheet](../../core1/part-04-power-cables/cheatsheet.md).

---

## C1P04-PBQ1: Power supply workbench sheet

**Part A**

| Wire colour | Carries | Why |
|---|---|---|
| Orange | **3.3 V** | Standard PSU colour code |
| Red | **5 V** | |
| Yellow | **12 V** | The 12 V rail powers the CPU and GPU |
| Black | **ground** | |

**Part B**

| Job | Connector | Why |
|---|---|---|
| Main power to the motherboard | **20+4 pin** | 24 pins in total, the 4-pin detaches to fit 20-pin boards |
| Power to the CPU | **4+4 pin (8 pin)** | Sits near the processor |
| Power to the graphics card | **6+2 pin (8 pin)** | On the graphics card (6-pin or 6+2) |
| Power to a SATA drive | **15-pin SATA** | |
| Legacy 4-pin power | **4-pin Molex** | RJ45 is a network connector, not power |

**Part C** (lowest to highest): **Bronze, Silver, Gold, Platinum, Titanium.** Minimum efficiency at 50% load on 115 V: 85, 88, 90, 92, 94 percent.

**Part D:** **220-240 VAC.** 230 V is inside the 220-240 range. A manual switch set to 110-120 on a 230 V outlet can destroy the unit.

**Marking (15 points):** Part A 4, Part B 5, Part C 5 (1 per correct position, so the order bronze-to-titanium scores up to 5 and one swapped pair loses 2), Part D 1.
- 13 to 15: strong. 10 to 12: fine, check the Output rails table. Under 10: relearn the Power supply table.

---

## C1P04-PBQ2: Match the cable to the job

| Job | Letter | Why |
|---|---|---|
| 1 | **A** Cat 6a | 10 Gbps up to 100 m (Cat 6 only manages 10 Gbps to about 55 m) |
| 2 | **B** Plenum-rated | Fire-resistant, low-smoke jacket for air-handling spaces |
| 3 | **C** Single-mode fiber | Laser and a thin core for kilometres (multimode is for inside buildings) |
| 4 | **E** Coaxial with F-type | Screw-on F-type is the coax connector |
| 5 | **F** Serial with DB-9 | RS-232 serial for console access to network gear |
| 6 | **G** STP | Shielded copper resists electromagnetic interference |
| 7 | **H** Direct burial | Rated for underground use |

Unused: **D** (multimode, shorter-distance fiber) and **I** (Cat 5, only 100 Mbps).

**Marking (7 points):** 1 per job.
- 6 to 7: strong. 4 to 5: fine, redo the Copper and Fiber sections. Under 4: relearn the memorise sheet for cables.
- Common slip: job 3 as D. 5 km is far beyond a building-run multimode link.
