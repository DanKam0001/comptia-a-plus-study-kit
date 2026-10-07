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
| 11 | DisplayPort (embedded, such as a laptop panel) |

Then look at the back of the PC and the monitor and confirm with your own eyes.

## 2. Read your Ethernet cable

Look along the jacket of a network cable. The category is printed on it (CAT5e, CAT6, CAT6a). Is it a good match for your internet speed? Is the plug plain plastic (UTP) or does it have a metal shell (STP)?

## 3. Check what your network link speed really is

```powershell
Get-NetAdapter | Select-Object Name, Status, LinkSpeed
```

A 1 Gbps link on a Cat 5e cable is normal. Would that cable do 10 Gbps?

## 4. Read your power supply label (case open, powered off and unplugged)

Do not open the power supply itself. Find its outer label and write down:

```
Input range:     (110-120 VAC, 220-240 VAC, or both?)
Is there a voltage switch?
Output rails:    (3.3 V, 5 V, 12 V amps)
Total wattage:
80 PLUS badge:   (which level, if any)
Modular?:        (are the cables detachable?)
```

## 5. Find the connectors

On the motherboard and PSU cables find the 24-pin (20+4) main connector, the CPU 8-pin (4+4), a SATA power cable and any graphics card power cable. If you have an old drive, look for a Molex connector.

## 6. Paper exercise: T568A and T568B

From memory, write both pin orders (pins 1 to 8). The only difference: the green and orange pairs are swapped. Then check yourself against the cheat sheet.

## 7. Port hunt

List every port on one laptop or PC: for each, name the connector (USB-A, USB-C, HDMI, RJ45, 3.5 mm audio...) and what it carries.

## Check yourself

- You need 10 Gbps over a 90 m office run. Which category? (Cat 6a.)
- A USB-C laptop must drive an HDMI projector. What do you need? (A USB-C to HDMI cable or adapter that supports video.)
- What is the first thing to check on a power supply brought from another country? (Its input voltage range and switch.)
