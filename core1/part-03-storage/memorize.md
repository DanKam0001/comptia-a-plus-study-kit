# Memorise list: Storage (Core 1, Part 3)

Understand the video first, then learn these cold.
Flashcards: [`flashcards/core1_part03.csv`](../../flashcards/core1_part03.csv) (import into Anki or any flashcard app).

## Hard drives

| Question | Answer |
|---|---|
| HDD spindle speeds | 5400 and 7200 RPM (PCs); 10,000 and 15,000 RPM (servers) |
| HDD form factors | 3.5-inch (desktops, servers); 2.5-inch (laptops) |
| Why is an HDD fragile? | Moving parts (platters and head) |

## Interfaces

| Question | Answer |
|---|---|
| SATA III speed | 6 Gbps (about 600 MB/s) |
| NVMe runs over | PCIe lanes |
| NVMe vs SATA | NVMe is several times faster |
| SAS is used in | Servers (enterprise). SAS-3 = 12 Gbps |
| SAS controller with SATA drive? | Works |
| SATA controller with SAS drive? | Does NOT work |

## Form factors

| Question | Answer |
|---|---|
| M.2 is a... | Shape (form factor), not a speed. Can be SATA or NVMe |
| M.2 2280 means | 22 mm wide, 80 mm long |
| M.2 B key | SATA or PCIe x2 |
| M.2 M key | PCIe x4 (NVMe) |
| M.2 B+M drive | Fits both slot types |
| mSATA | Older small SSD shape (about 30 x 51 mm), SATA signalling |
| New M.2 drive not detected | The slot supports the other type (SATA vs NVMe) |

## RAID

| Question | Answer |
|---|---|
| RAID stands for | Redundant Array of Independent Disks |
| RAID 0 | Striping. Min 2 drives, 100% capacity, no fault tolerance |
| RAID 1 | Mirroring. 2 drives, 50% capacity, survives 1 failure |
| RAID 5 | Striping + parity. Min 3 drives, survives 1, capacity = all but one drive |
| RAID 6 | Double parity. Min 4 drives, survives 2, capacity = all but two drives |
| RAID 10 | Mirrored pairs striped. Min 4 drives, 50% capacity, 1 failure per pair |
| Is RAID a backup? | No |

## Removable and optical

| Question | Answer |
|---|---|
| CD / DVD / Blu-ray single-layer capacity | 700 MB / 4.7 GB / 25 GB |
| DVD / Blu-ray dual layer | 8.5 GB / 50 GB |
| SD / SDHC / SDXC maximum | 2 GB / 32 GB / 2 TB |
