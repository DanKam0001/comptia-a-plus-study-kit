# Lab: Write a ticket, plan a change and test a restore (Windows)

**Time:** 20 to 25 minutes. **Needs:** any Windows PC, a text editor (Notepad), and a USB stick or spare folder. Nothing here changes your system settings.

Goal: practise the three habits from Part 14 on something real.

## 1. Write a proper ticket

Pick a small real problem you have had (slow boot, a Wi-Fi drop, a printer that won't print). Open Notepad and write it up like a technician:

```
User:            (you, plus contact detail)
Device:          (computer name, model)
Category:        (hardware / software / network / account)
Severity:        (low / medium / high, and why)
Issue:           (what is wrong, one or two sentences)
Progress notes:  (what you tried, in order)
Resolution:      (what fixed it, or "escalate to ...")
```

To find your computer name and model: press **Windows key + R**, type `msinfo32`, press Enter, and read **System Name** and **System Model**.

## 2. Write a change request

Imagine you want to install a big Windows update on a shared family PC. Write a request with these headings: **purpose**, **scope**, **change type** (standard, normal or emergency), **date and time** (pick a quiet evening as your maintenance window), **affected systems**, **risk level**, **rollback plan**, **backup plan**, and **who is responsible**.

## 3. Take a backup and prove it works

1. Make a folder called `LabData` on your Desktop and put five small files in it.
2. Copy the folder to a USB stick or another drive. That is your **full backup**.
3. Change two of the files, and add one new file. Copy only those three to a folder called `Incremental1`. That models an **incremental backup**.
4. Delete `LabData` from the Desktop. Now **restore**: copy the full backup back, then copy `Incremental1` over it, replacing files when asked.
5. Open the files. Are the edited versions and the new file there? That is a **test restore**.

Optional: repeat from step 3, but instead of `Incremental1`, copy every file changed since the full backup into a `Differential1` folder. Notice that to restore you need only the full copy plus that one folder.

## 4. Check the 3-2-1 rule

Write down where your most important files live. Count the copies, the media types (internal drive, USB, cloud) and the offsite copies. Do you meet **3-2-1**? What is the cheapest step that would get you there?

## Check yourself

- Which three things should a ticket's written notes always contain? (issue description, progress notes, resolution)
- Which backup type needs the full backup plus every later backup to restore? (incremental)
- What is the difference between a maintenance window and a change freeze? (a window is when changes are planned, a freeze is when they are banned)

## Going further (optional)

Windows has **File History** and **Backup and Restore** in the Control Panel. Look at their settings (do not turn anything on unless you want to) and see which backup type they use.
