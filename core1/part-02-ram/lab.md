# Lab: Inspect your own memory (Windows)

**Time:** 10 minutes. **Needs:** any Windows PC. Everything here is read-only.

## 1. Read your memory modules

Open PowerShell and run:

```powershell
Get-CimInstance Win32_PhysicalMemory | Select-Object BankLabel, @{n='GB';e={$_.Capacity/1GB}}, Speed, ConfiguredClockSpeed, SMBIOSMemoryType, FormFactor
```

Decode it:

| Column | Meaning |
|---|---|
| `SMBIOSMemoryType` | 24 = DDR3, 26 = DDR4, 34 = DDR5 |
| `FormFactor` | 8 = DIMM, 12 = SODIMM |
| `Speed` | MT/s the module is rated for |
| `ConfiguredClockSpeed` | MT/s it is actually running at (the slowest module wins) |
| `BankLabel` | Which slot position each module is in |

## 2. Work out the PC rating

Multiply your `Speed` by 8. Example: 2666 x 8 = 21,328, which is labelled PC4-21300. Check the sticker on a module if you can open the case (powered off and unplugged).

## 3. Is it ECC?

```powershell
Get-CimInstance Win32_PhysicalMemoryArray | Select-Object MemoryErrorCorrection, MemoryDevices
```

`MemoryErrorCorrection`: 3 = none, 5 = single-bit ECC, 6 = multi-bit ECC. Most desktops and laptops show 3.

## 4. Is it running dual channel?

Open **Task Manager > Performance > Memory** and note **Slots used** and **Form factor**. If you have two matching modules in two slots, check your motherboard manual for the dual-channel slot pair. A free tool such as CPU-Z also shows "Channels" on its Memory tab.

## 5. Write it up

```
Generation:        (DDR?)
Form factor:       (DIMM or SODIMM)
Modules / slots:
Speed / PC rating:
ECC:               (yes or no)
Dual channel?:
```

## Check yourself

- If you added a third stick rated for a higher speed, what speed would all three run at? (The slowest module's.)
- Could you put a DDR5 stick in this machine's slots? Why not? (Different generation and notch.)
- What would you need for ECC to work on this machine? (An ECC-capable CPU and motherboard, plus ECC modules.)
