# Lab: A Windows troubleshooting tour

**Time:** 20 to 30 minutes. **Needs:** a Windows PC (a virtual machine is ideal). Steps 1 to 6 are read-only or harmless. Don't change settings you don't understand.

Goal: find each troubleshooting tool and see what it shows on a healthy PC, so you recognise a sick one.

## 1. Reliability Monitor: a history of crashes

Press **Windows key + R**, type `perfmon /rel`, press Enter. The chart shows crashes and failures by day. Click a red X to see the details.

## 2. Event Viewer: find the cause

Press **Windows key + R**, type `eventvwr.msc`. Open **Windows Logs > System**. Click **Filter Current Log** and tick **Critical** and **Error**. Pick one and read the description and the source.

## 3. Task Manager: what is slow?

Open Task Manager (Ctrl + Shift + Esc). Check **Processes** (click the CPU, Memory and Disk columns to sort), **Performance**, and **Startup apps**. Which three startup apps have the highest impact?

## 4. Services and dependencies

Run `services.msc`. Double-click **Windows Time**. Look at the **General** tab (Startup type), **Log On** tab and **Dependencies** tab. Then open a service of your choice and find what it depends on.

## 5. Repair system files

Open PowerShell as administrator:

```powershell
sfc /scannow
```

It takes several minutes. Read the result: no integrity violations, or violations repaired.

## 6. Time sync

```powershell
w32tm /query /status
```

Look at **Source** and **Last Successful Sync Time**. To force a sync (needs administrator):

```powershell
w32tm /resync
```

## 7. Find the crash dumps folder and safe mode (read-only)

- In File Explorer, look for `C:\Windows\Minidump`. It may not exist if you have never had a blue screen.
- Press **Windows key + R**, type `msconfig`, open the **Boot** tab and note the **Safe boot** option. **Don't tick it**, just see where it is. (If you do tick it for practice, untick it before restarting normally.)

## 8. Optional memory test

Search **Windows Memory Diagnostic**. It restarts the PC and tests RAM. Only run it when you can spare 10 to 20 minutes.

## Check yourself

- A PC blue-screens after a new driver. Which two tools would you use, and in what order?
- Where would you look for a "dependency failed" service message?
- Which setting do you check when "Operating system not found" appears?
- What tolerance does a domain sign-in have for clock error?
