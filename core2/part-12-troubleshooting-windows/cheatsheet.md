# Core 2, Part 12: Troubleshooting Windows

**Objective 3.1** (220-1202): *Given a scenario, troubleshoot common Windows OS issues.*
Domain: Software Troubleshooting (23% of the exam).

Core 2 Part 3 (The Windows Command Line) and Part 2 (Windows Tools) covered the tools named here (sfc, Event Viewer, Task Manager, Services, Device Manager). This part is about picking the right one for each symptom.

## The twelve symptoms

| Symptom | Common causes | First things to try |
|---|---|---|
| **Blue screen of death (BSOD)** | Bad driver, faulty update, failing RAM or drive | Note the stop code. Boot to safe mode. Roll back the driver or uninstall the update. Test RAM and check the disk. Dump files are saved (C:\Windows\Minidump) |
| **Degraded performance** | Too many startup programs, malware, nearly full drive, failing drive, low RAM | Task Manager: see what is busy (CPU, memory, disk, network). Disable startup items, scan for malware, free space, check disk health, add RAM |
| **Boot issues** | Bad update, damaged boot files, failing drive | Windows Recovery Environment: Startup Repair, safe mode, System Restore, command prompt (`bootrec /fixmbr`, `bootrec /fixboot`, `bootrec /rebuildbcd`, `sfc /scannow`) |
| **Frequent shutdowns** | Overheating (dust, dead fan, old thermal paste), failing power supply, bad RAM | Clean vents and fans, check cooler and paste, check temperatures, test the power supply, check Event Viewer |
| **Services not starting** | Stopped dependency, wrong startup type or log-on account, corrupted files | `services.msc`: check Startup type, Dependencies tab, Log On tab. Start the dependency first. Check Event Viewer |
| **Applications crashing** | Corrupt install, outdated app, bad update, bad RAM | Restart, update, repair, reinstall, check Event Viewer for the faulting module, compatibility mode |
| **Low memory warnings** | RAM nearly full, a program leaking memory | Close programs, restart, find the program in Task Manager, add RAM, check the page file (virtual memory) |
| **USB controller resource warnings** | Too many devices on one controller, not enough power | Unplug devices, use a powered hub, update or reinstall USB controller drivers in Device Manager |
| **System instability** | Corrupt system files, bad drivers, malware, faulty RAM or disk | `sfc /scannow`, update or roll back drivers, scan for malware, check Event Viewer, memory test |
| **No OS found** | Wrong boot order, USB or disc in the PC, drive not detected or failed, damaged boot files | Remove USB and discs, check boot order in firmware, check drive is detected and cables, repair boot files, replace the drive and reinstall |
| **Slow profile load** | Large or corrupt user profile, slow network server for a roaming profile | Remove big files from the profile, create a new profile and copy data, check network speed to the profile server |
| **Time drift** | Dead CMOS battery, wrong time zone, time sync failing | Replace the CMOS battery (coin cell), set time zone, sync with a time server (`w32tm /resync`). Domain sign-in (Kerberos) by default needs clocks within 5 minutes (the tolerance is a configurable policy) |

## Tools by job

| Tool | Use |
|---|---|
| Safe mode | Start with only basic drivers to remove a bad driver or update |
| Windows Recovery Environment (WinRE) | Startup Repair, System Restore, command prompt. Opens on its own after failed starts |
| Event Viewer (`eventvwr.msc`) | Errors and warnings log, the first place to look for a cause |
| Task Manager | What is using CPU, memory, disk, network. Startup apps tab |
| Services (`services.msc`) | Start, stop and set startup type of services |
| Device Manager | Update, roll back or reinstall drivers |
| `sfc /scannow` | Check and repair Windows system files |
| `bootrec` | Repair boot records (from WinRE) |
| System Restore | Roll back to an earlier working point |

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Blue screen right after a driver update | Safe mode, roll back the driver |
| "Operating system not found" | Check boot order and that the drive is detected |
| Clock resets when the PC is unplugged | Replace the CMOS battery |
| PC shuts down by itself under load | Overheating or power supply: clean dust, check cooler and paste |
| A service won't start, "dependency failed" | Start the service it depends on |
| Many USB devices, controller warning | Powered hub, fewer devices |
| Domain user can't sign in, clock is 10 minutes out | Fix the time (sync with time server) |
