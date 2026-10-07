# Core 1, Part 13: Troubleshooting Motherboards, RAM, CPU, Power, Drives and RAID

**Objectives 5.1 and 5.2** (220-1201): *Given a scenario, troubleshoot motherboards, RAM, CPUs, and power* and *Given a scenario, troubleshoot drive and RAID issues.*
Domain: Hardware and Network Troubleshooting (28% of the exam).

## A work habit (not tested)

The 220-1201 objectives list the six-step troubleshooting methodology but say it is **not part of the exam**. It is still how good technicians work:

1. Identify the problem.
2. Establish a theory of probable cause (question the obvious).
3. Test the theory to determine the cause.
4. Establish a plan of action and implement the solution.
5. Verify full system functionality and, if applicable, put preventive measures in place.
6. Document findings, actions and outcomes.

## 5.1 Motherboard, RAM, CPU and power symptoms

| Symptom | Common causes | What to do |
|---|---|---|
| **POST beeps** | A part failed the power-on self-test. Often RAM, graphics card or CPU | Beep codes differ by maker (AMI, Award, Dell and others). Look the pattern up in the motherboard manual. Reseat RAM and cards |
| **Proprietary crash screens** | Windows: blue screen of death (BSOD). macOS: spinning wheel (pinwheel) | Note the stop code, then test RAM, check temperatures and drivers, check the drive. See Core 2 Part 12, *Troubleshooting Windows* |
| **Blank screen** | Wrong monitor input source, loose video cable, unseated RAM or graphics card, dead display | Check the cable and input, reseat RAM and graphics card, try another monitor |
| **No power** | Unplugged, dead outlet, power supply switch off, failed power supply, loose front-panel power header | Check outlet, cable, PSU switch. Test the PSU with a power supply tester or multimeter. Check header |
| **Sluggish performance** | Heat throttling, too little RAM, failing drive, nearly full drive, malware | Check temperatures, memory use and drive health |
| **Overheating** | Dust, failed fan, missing or dried-out thermal paste, bad airflow | Clean with compressed air, check every fan spins, replace thermal paste |
| **Burning smell** | Failing power supply, burnt component, short | **Power off and unplug at once.** Do not power on again. Replace the part |
| **Random shutdown** | Overheating, failing power supply, failing RAM | Check temperatures, test the PSU |
| **Application crashes** | Bad RAM, overheating, bad drive | Run a memory test tool, check temperatures |
| **Unusual noise** | Fan bearings failing (whine, rattle, grinding), failing hard drive (clicking) | Find the source, replace the fan or back up and replace the drive |
| **Capacitor swelling** | Swollen or leaking capacitor tops on the board or PSU | Replace the board or power supply |
| **Inaccurate system date/time** | Flat **CMOS battery** (usually a CR2032 3 V coin cell on the motherboard) | Replace the battery, then reset the clock in firmware |

**Tools:** multimeter, power supply tester, POST card, compressed air, ESD strap, screwdrivers, spare known-good parts.

## 5.2 Drive and RAID symptoms

| Symptom | Common causes | What to do |
|---|---|---|
| **LED status indicators** | Drive or RAID bay lights show activity, or amber/red for a fault | Read the maker's chart. Amber or red usually means a failed or failing drive |
| **Grinding noises** | HDD moving parts failing | Back up immediately, replace the drive |
| **Clicking sounds** | HDD head failing | Back up immediately, replace the drive |
| **Bootable device not found** | Wrong boot order, loose or bad cable, dead drive, damaged boot files | Check boot order in firmware, reseat cables, check the drive appears in firmware |
| **Data loss/corruption** | Failing drive, bad cable, sudden power loss | Restore from backup, check drive health. Backups: Core 2 Part 14 |
| **RAID failure** | One or more drives failed | Replace the failed drive and rebuild. If more drives fail than the level survives, restore from backup |
| **S.M.A.R.T. failure** | Drive predicts its own failure (S.M.A.R.T. = Self-Monitoring, Analysis and Reporting Technology) | Back up now and replace the drive |
| **Extended read/write times** | Failing drive, bad sectors, full drive | Check S.M.A.R.T., back up |
| **Low IOPS** | Drive or array struggling. IOPS = Input/Output Operations Per Second | Check drive health, array state and cabling |
| **Missing drives in OS** | Drive not initialized, no drive letter, loose cable, failed drive | Check cables, firmware detection, then Disk Management |
| **Array missing** | Cable or RAID controller fault, controller settings lost | Check cables and controller, then the RAID configuration |
| **Audible alarms** | RAID controller or NAS warning of a failed or degraded array | Find the failed drive from the LED or management software and replace it |

### RAID reminder (levels covered in Core 1 Part 3, *Storage: HDD, SSD, NVMe, M.2 and RAID*)

| Level | Survives | Minimum drives |
|---|---|---|
| RAID 0 | Nothing (striping, no redundancy) | 2 |
| RAID 1 | One drive (mirror) | 2 |
| RAID 5 | One drive (parity) | 3 |
| RAID 6 | Two drives (double parity) | 4 |
| RAID 10 | One per mirror pair | 4 |

- A **degraded** array still works but has lost its protection. Replace the drive quickly. The array **rebuilds** onto the new drive, which can take hours.
- **RAID is not a backup.** It protects against a failed drive, not against deletion, malware or fire.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Beep pattern, no picture | Look up the beep code, reseat RAM |
| Clock resets when unplugged | Replace the CMOS battery |
| RAID 5 alarm, one amber drive | Replace the failed drive and let it rebuild |
| Clicking from a hard drive | Back up now, replace the drive |
| Bootable device not found | Boot order, cables, drive detected? |
| Random shutdowns under load | Overheating or failing power supply |
