# Lab: Inspect your own memory (Windows)

**Time:** 10 minutes. **Needs:** any Windows PC. Everything here is read-only.

Goal: find out what memory your PC has, and match it to Part 2.

## 1. How much RAM, and how fast?

Open PowerShell and run:

```powershell
Get-CimInstance Win32_PhysicalMemory | Select-Object BankLabel, Capacity, Speed, Manufacturer, PartNumber, SMBIOSMemoryType
```

- `Capacity` is in bytes. Divide by 1,073,741,824 to get GB.
- `Speed` is in MT/s.
- `SMBIOSMemoryType`: 24 = DDR3, 26 = DDR4, 34 = DDR5 (a newer PC may show 0; use the part number instead).

## 2. Look at Task Manager

Open **Task Manager > Performance > Memory**. In the bottom right find:
- **Speed** and **Slots used**
- **Form factor**: DIMM or SODIMM

## 3. Work out your channel setup

Count the sticks (step 1) and compare with the **Slots used** number in Task Manager. If you have two matching sticks, search your motherboard or laptop manual for the "dual channel" slot rules. Are your sticks in the right slots?

## 4. Decode a part number

Search the `PartNumber` online. Write down: generation (DDR3/4/5), form factor, speed, whether it is ECC.

## 5. Write it up

```
Generation:
Form factor (DIMM or SODIMM):
Speed (MT/s) and PC rating (speed x 8):
Number of sticks / slots:
ECC? (almost certainly no on a home PC):
```

## Check yourself

- Why would you not buy DDR4 for a DDR5 board?
- You add a second stick and see no gain. What do you check first?
- Which two parts must support ECC?

## Going further (optional)

Powered off, unplugged and wearing an anti-static strap (or touching bare metal), open a desktop and find the DIMM slots, the clips, and the notch on a stick. Do not remove anything unless you plan to put it back.
