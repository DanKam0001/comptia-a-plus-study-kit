# Lab: A tour of the Windows tools

**Time:** 20 to 25 minutes. **Needs:** any Windows 10 or 11 PC. Everything here is look-only. Do not change a setting unless a step says so, and never click Apply in Registry Editor.

Goal: open every tool from Part 2 once, by its file name, so the names stick.

## 1. Task Manager

1. Press **Ctrl + Shift + Esc**.
2. On **Processes**, click the **Memory** column header to sort by memory. Which program uses the most?
3. Open **Performance** and note the CPU, memory and disk graphs.
4. Open **Startup**. How many programs are enabled? (Don't disable anything yet.)
5. Open **Services** and **Users** and see what each shows.

## 2. Open the snap-ins from the Run box

Press **Windows key + R**, type each name, press Enter, take a look, close it.

| Type | Find this |
|---|---|
| `eventvwr.msc` | Windows Logs, then the three logs: Application, Security, System. Find one red **Error** |
| `diskmgmt.msc` | Your drives. Is there any unallocated (black) space? |
| `taskschd.msc` | One task in the Task Scheduler Library |
| `devmgmt.msc` | Expand Display adapters. Any yellow triangles? |
| `certmgr.msc` | Trusted Root Certification Authorities |
| `lusrmgr.msc` | Your account under Users (not available on Home. If the window won't open, note that you are on Home) |
| `perfmon.msc` | The Performance Monitor graph |
| `gpedit.msc` | Computer Configuration (not available on Home) |

## 3. The additional tools

| Type | Find this |
|---|---|
| `msinfo32` | Your BIOS Mode and Secure Boot State |
| `resmon` | The Disk tab: which process uses the disk most? |
| `msconfig` | The Boot and Services tabs. **Cancel** when you are done |
| `cleanmgr` | How much space could be freed on C:? **Cancel** when you are done |
| `dfrgui` | Your drives and whether each is a Solid state drive or Hard disk drive |
| `regedit` | Expand `HKEY_CURRENT_USER`. Do not change anything. Close it |

## 4. Settings and Control Panel

1. Press **Windows key + I**. Count the categories. Do they match the list in the cheat sheet?
2. Open **Control Panel** from the Start menu, switch View by to **Large icons**, and find: Programs and Features, Network and Sharing Center, Indexing Options, Sound, Mail (it may be missing if Outlook isn't installed).
3. Open **Control Panel, Power Options**. Which plan is selected? Click **Choose what closing the lid does**, then close without saving.
4. Open **File Explorer, View, Options, View tab**. Find "Hide extensions for known file types" and "Show hidden files".

## 5. Write it up

Make a 6-line note:

```
Biggest memory user right now:
Startup programs enabled:
Any error in Event Viewer (Application log):
Any unallocated disk space:
Firmware mode and Secure Boot state:
Power plan:
```

## Check yourself

- Which tool would you open to see why a program crashed? (Event Viewer)
- Which tool shows what is using the disk right now, in detail? (Resource Monitor)
- A new drive doesn't appear in File Explorer. Which snap-in fixes it? (Disk Management)
- Which two snap-ins are missing on Windows Home? (Group Policy Editor, Local Users and Groups)

## Going further (optional)

Create a basic task in Task Scheduler that opens Notepad at a time two minutes from now, watch it run, then delete the task.
