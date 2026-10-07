# Core 1, Part 3: Storage: HDD, SSD, NVMe, M.2 and RAID

**Objective 3.4** (220-1201): *Compare and contrast storage devices.*
Domain: Hardware (25% of the exam).

Objective bullets covered: hard drives (spindle speeds, 2.5-inch and 3.5-inch), solid-state drives (NVMe, SATA, PCIe, SAS; M.2, mSATA), RAID 0, 1, 5, 6, 10, removable storage (flash drives, memory cards), optical drives.

## Hard disk drives (HDD)

- Data on spinning magnetic **platters**, read by a moving **head** on an arm. Like a record player.
- Cheap per GB, but slower, noisier, and sensitive to knocks (moving parts).
- **Spindle speeds**: **5400** and **7200 RPM** (PCs), **10,000** and **15,000 RPM** (servers). Faster spin = faster access, more heat and noise.
- **Form factors**: **3.5-inch** (desktops, servers), **2.5-inch** (laptops, typically 7 mm or 9.5 mm thick).

## Solid-state drives (SSD)

- **Flash memory**, no moving parts. Faster, silent, shock resistant, costs more per GB.
- The classic fix for a slow-booting laptop: replace the HDD with an SSD.

## Communications interfaces

| Interface | Notes |
|---|---|
| SATA | SATA III = **6 Gbps** (about 600 MB/s theoretical, roughly 550 MB/s real-world). Used by HDDs and SSDs. 7-pin data cable plus separate 15-pin power |
| NVMe | Non-Volatile Memory Express. A protocol built for flash that runs over **PCIe** lanes. About 3.5 GB/s on PCIe 3.0 x4, about 7 GB/s on PCIe 4.0 x4 |
| PCIe | The fast lanes on the motherboard. NVMe drives (M.2 or add-in card) use them directly |
| SAS | Serial Attached SCSI. Enterprise/server interface (SAS-3 = 12 Gbps). A SAS controller can run SATA drives; a SATA controller **cannot** run SAS drives |

## SSD form factors

| Form factor | Notes |
|---|---|
| 2.5-inch | Looks like a laptop HDD, uses a SATA cable and power |
| **M.2** | Small stick, plugs straight into a board slot, no cables. **A shape, not a speed**: can be SATA or NVMe |
| mSATA | Older small card, about 30 x 51 mm, uses SATA signalling (older thin laptops) |

M.2 details:
- Size code: **2280 = 22 mm wide x 80 mm long**. Others: 2230, 2242, 2260, 22110.
- Keys (notch pattern): **B key** = SATA or PCIe x2. **M key** = PCIe x4 (NVMe; some M-key slots also accept SATA drives). **B+M** drives fit both.
- Always check what the slot supports (SATA, NVMe or both). A drive of the wrong type will **not be detected**.

## RAID (drive configurations)

| Level | What | Min drives | Usable capacity | Survives |
|---|---|---|---|---|
| 0 | Striping | 2 | 100% | Nothing (fastest, no protection) |
| 1 | Mirroring | 2 | 50% | 1 failure |
| 5 | Striping + parity | 3 | all but 1 drive | 1 failure |
| 6 | Striping + double parity | 4 | all but 2 drives | 2 failures |
| 10 (1+0) | Mirrored pairs, striped | 4 | 50% | 1 per mirrored pair |

- **Parity** = extra calculated data that lets a lost drive be rebuilt.
- When a drive fails in 1, 5, 6 or 10: replace it and let the array **rebuild** while the system keeps running.
- **RAID is not a backup.** It protects against drive failure, not deletion, malware, fire or controller failure. (The backup side of this is covered in Core 2 Part 14, Documentation, Change Management, Backup and Recovery.)

## Removable storage

- **Flash drives**: USB sticks.
- **Memory cards**: SD up to 2 GB; SDHC up to 32 GB; SDXC up to 2 TB. microSD is the small version (same families), used in phones and cameras.

## Optical drives

| Disc | Single layer | Dual layer |
|---|---|---|
| CD | about 700 MB | n/a |
| DVD | 4.7 GB | 8.5 GB |
| Blu-ray | 25 GB | 50 GB |

Slow and fading, but still on the exam.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Laptop with HDD boots slowly | Replace with an SSD |
| New M.2 drive not detected | Slot supports the other type (SATA vs NVMe) |
| Need speed, no redundancy needed | RAID 0 |
| Need to survive any 2 failures | RAID 6 |
| Mirrored pair, minimum 2 drives | RAID 1 |
| "RAID will protect us from deletions" | No. RAID is not a backup |
