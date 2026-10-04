# Memorise list: Storage: HDD, SSD, NVMe, M.2 and RAID (Core 1, Part 3)

Understand the video first, then learn these cold. They're the facts a scenario question assumes you already know.
Flashcards: [`flashcards/core1_part03.csv`](../../flashcards/core1_part03.csv) (import into Anki or any flashcard app).


## Hard drives

| Question | Answer |
|---|---|
| HDD spindle speeds | 5400 and 7200 RPM (common PCs); 10,000 and 15,000 RPM (servers) |
| HDD form factors | 3.5-inch (desktops, servers); 2.5-inch (laptops) |

## Interfaces

| Question | Answer |
|---|---|
| SATA III speed | 6 Gbps (about 600 MB/s) |
| NVMe runs over | PCIe lanes (several GB/s) |
| SAS is used in | Enterprise servers |
| SAS vs SATA controller compatibility | A SAS controller can run SATA drives; a SATA controller cannot run SAS drives |

## SSD form factors

| Question | Answer |
|---|---|
| M.2 is a... (shape or speed?) | A shape (form factor). An M.2 drive can be SATA or NVMe |
| M.2 size 2280 means | 22 mm wide x 80 mm long |
| M.2 B key / M key | B key = SATA or PCIe x2. M key = PCIe x4 (NVMe). B+M accepts both |
| mSATA is | An older small form factor that uses the SATA interface |

## RAID

| Question | Answer |
|---|---|
| RAID 0 | Striping. Min 2 drives. 100% capacity. NO fault tolerance |
| RAID 1 | Mirroring. 2 drives. 50% capacity. Survives 1 failure |
| RAID 5 | Striping with distributed parity. Min 3 drives. Survives 1 failure. Capacity = all but one drive |
| RAID 6 | Double parity. Min 4 drives. Survives 2 failures. Capacity = all but two drives |
| RAID 10 (1+0) | Mirrored pairs striped together. Min 4 drives. 50% capacity. Survives 1 failure per mirrored pair |
| Is RAID a backup? | No. It protects against a drive failing, not deletion, malware, fire or controller failure |

## Removable and optical

| Question | Answer |
|---|---|
| CD / DVD / Blu-ray capacity (single layer) | About 700 MB / 4.7 GB / 25 GB |
