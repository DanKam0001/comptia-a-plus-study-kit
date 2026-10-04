# Core 1, Part 3: Storage

**Objective 3.4** (220-1201): *Compare and contrast storage devices.*
Domain: Hardware (25% of the exam).

## Hard disk drives (HDD)

- Magnetic spinning platters read by a moving head. Cheap per GB, slower, noisier, sensitive to shock.
- Spindle speeds: **5400** and **7200 RPM** (PCs), **10,000** and **15,000 RPM** (servers).
- Form factors: **3.5-inch** (desktops, servers), **2.5-inch** (laptops).

## Solid state drives (SSD)

- Flash memory, no moving parts. Faster, silent, shock resistant, costs more per GB.
- The classic fix for a slow boot is swapping an HDD for an SSD.

## Interfaces

| Interface | Notes |
|---|---|
| SATA | 6 Gbps (about 600 MB/s). HDDs and SSDs |
| NVMe | Built for flash. Runs over **PCIe** lanes. Several GB/s |
| SAS | Enterprise (servers). A SAS controller can run SATA drives; a SATA controller cannot run SAS |

## SSD form factors

| Form factor | Notes |
|---|---|
| 2.5-inch | Looks like a laptop HDD, SATA cable |
| **M.2** | Stick in a board slot. **A shape, not a speed**: can be SATA or NVMe. Sizes like 2280 = 22 mm x 80 mm |
| mSATA | Older small form factor, SATA signalling |

M.2 keys: **B key** = SATA or PCIe x2. **M key** = PCIe x4 (NVMe). **B+M** accepts both. Always check what the slot supports. A drive of the wrong type won't be detected.

## RAID

| Level | What | Min drives | Capacity | Survives |
|---|---|---|---|---|
| 0 | Striping | 2 | 100% | Nothing |
| 1 | Mirroring | 2 | 50% | 1 failure |
| 5 | Striping + parity | 3 | all but 1 drive | 1 failure |
| 6 | Striping + double parity | 4 | all but 2 drives | 2 failures |
| 10 (1+0) | Mirrored pairs, striped | 4 | 50% | 1 per mirrored pair |

**RAID is not a backup.** It protects against a drive failing, not deletion, malware, fire or controller failure. When a drive fails in 1/5/6/10, replace it and let the array rebuild.

## Removable and optical

- Flash drives (USB) and memory cards (SD, microSD).
- Optical, single layer: **CD about 700 MB, DVD 4.7 GB, Blu-ray 25 GB**.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Laptop with HDD boots slowly | Replace with an SSD |
| New M.2 drive not detected | Slot supports the other type (SATA vs NVMe) |
| Need speed, no redundancy needed | RAID 0 |
| Need to survive any 2 failures | RAID 6 |
| "RAID will protect us from deletions" | No: RAID is not a backup |
