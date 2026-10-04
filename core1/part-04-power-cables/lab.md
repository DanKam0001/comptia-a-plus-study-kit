# Lab: Cables, connectors and power (Windows)

**Time:** 15 to 20 minutes. **Needs:** any PC and a look around your desk. Open a case only if powered off and unplugged.

## 1. What is each monitor plugged into?

Open PowerShell and run:

```powershell
Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorConnectionParams | Select-Object InstanceName, VideoOutputTechnology
```

| `VideoOutputTechnology` | Connection |
|---|---|
| 0 | VGA (HD15) |
| 4 | DVI |
| 5 | HDMI |
| 10 | DisplayPort (external) |
| 11 | DisplayPort (embedded, e.g. laptop panel) |

Then look at the back of the PC and the monitor and confirm with your own eyes.

## 2. Read your Ethernet cable

Look along the jacket of a network cable. The category is printed on it (CAT5e, CAT6, CAT6a). Is it a good match for your connection speed? Look at the plug: does it look shielded (metal) or plain plastic?

## 3. Read your power supply label (case open, **powered off and unplugged**)

Find the label on the power supply and write down:

```
Input range:     (110-120 VAC, 220-240 VAC, or both?)
Is there a voltage switch?
Output rails:    (3.3 V, 5 V, 12 V amps)
Total wattage:
80 PLUS badge:   (which level, if any)
Modular?:        (are the cables detachable?)
```

## 4. Find the connectors

On the motherboard and PSU cables, find the 24-pin (20+4) main connector, the CPU 8-pin (4+4), a SATA power cable and any PCIe power cable. If you have an old drive, look for a Molex connector.

## 5. Paper exercise: T568A and T568B

From memory, write both pin orders (pins 1 to 8). The only difference: the green and orange pairs are swapped. Then check yourself against the cheat sheet.

## Check yourself

- You need 10 Gbps over a 90 m office run. Which category? (Cat 6a.)
- Which cable do you need to join two switches directly with no uplink port? (A crossover cable, or use auto-MDI-X ports.)
- What's the first thing to check on a power supply you've brought from another country? (Its input voltage range and switch.)
