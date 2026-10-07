# Lab: Check your own PC's health (Windows)

**Time:** 20 minutes. **Needs:** a Windows PC. Everything here is read-only except the memory test, which restarts the PC (save your work first).

## 1. Drive health (S.M.A.R.T.)

Open PowerShell as administrator and run:

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, OperationalStatus
```

`Healthy` is what you want. Then, for a closer look, run:

```powershell
wmic diskdrive get model,status
```

`OK` means no S.M.A.R.T. failure has been reported. (Free tools such as CrystalDiskInfo show every S.M.A.R.T. attribute.)

## 2. Is a drive missing?

Press **Windows key + X** and choose **Disk Management**. Every disk should have a letter or be marked as healthy. A disk shown as **Not Initialized** or **Offline** is the "missing drive" case from the video.

## 3. Watch the temperature and load

Open **Task Manager > Performance**. Open a few heavy tabs or run a video and watch CPU use. Does the fan get louder? Is the PC slow when the CPU is near 100 percent? For temperatures, install a free monitor such as HWMonitor or look in the firmware (see Core 1 Part 1).

## 4. Check the date and clock behaviour

Note the date and time. If the PC ever loses time after being off for a while, that is a flat CMOS battery. (Only open a desktop case when it is **off and unplugged**, and take care with the battery.)

## 5. Test the RAM

Press **Windows key + R**, type `mdsched.exe`, press Enter and choose **Restart now and check for problems**. After the restart, results appear in a notification. Errors mean bad RAM.

## 6. Read the power-on beep chart

Find your motherboard's manual (search its model name from `Get-CimInstance Win32_BaseBoard`). Find the section on **beep codes**. Write down what one short beep and a repeating beep mean for your board.

## 7. Safe visual inspection (desktop only, off and unplugged)

Look at the board and power supply for bulging capacitors (swollen tops), dust on fans and fins, and whether every fan spins when you power on again.

## Check yourself

- What is the first thing to do when a PC smells of burning?
- What does a clicking hard drive mean, and what do you do first?
- A RAID 5 array is degraded with one amber drive. What next?
