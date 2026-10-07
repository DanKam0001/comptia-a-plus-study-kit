# Lab: See why deleting isn't erasing, and plan a disposal

**Time:** 20 to 30 minutes. **Needs:** a Windows PC and, for steps 3 and 4, a **spare USB stick with nothing on it that you need**. Steps 1, 2 and 5 are read-only.

**Safety:** never run any erase or format step on your main drive. Triple-check the drive letter before you format anything.

Goal: understand which disposal method fits which drive.

## 1. What kind of drive do you have?

```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, Size
```

`MediaType` says `HDD` or `SSD`. Write down which one. Then answer: if this drive were thrown out tomorrow, which of drilling, shredding, degaussing and incineration would work on it? (Degaussing only works if it's an HDD.)

## 2. Is your data encrypted at rest?

Open PowerShell as administrator and run:

```powershell
manage-bde -status
```

If **Protection On** and **Percentage Encrypted: 100%** appear, the drive is encrypted (BitLocker). An encrypted drive whose key is gone is much harder to read, which is why some companies use encryption as part of disposal. If it says the tool isn't available, your Windows edition may not include it. That's fine.

## 3. Delete and quick format on a spare USB stick

1. Copy two or three harmless test files onto the spare USB stick.
2. Delete them.
3. Right-click the stick in File Explorer, choose **Format**, tick **Quick Format**, and format it. Note the drive letter carefully first.
4. Read the screen: Windows built a new empty index. The data blocks were not overwritten. This is why a standard or quick format is not safe disposal.

## 4. Overwrite the free space (the idea of wiping)

With the same USB stick (letter shown as `E:` here, use yours):

```powershell
cipher /w:E:\
```

This overwrites the free space on that drive in three passes (zeros, then 0xFF values, then random data), so deleted files are much harder to recover. It's the same idea as a wipe tool, but it only covers free space, not the whole drive, and it isn't reliable on flash storage such as SSDs. It takes a few minutes. Make sure the letter is the USB stick.

## 5. Write a one-page disposal plan

Make a table for an imaginary company with these devices, and choose a method for each plus a reason:

| Device | Reused? | Method | Proof you keep |
|---|---|---|---|
| 20 office laptops (SSD) being sold | Yes | | |
| Failed server hard drive | No | | |
| Old backup tapes | No | | |
| Phone returned by a leaving employee | Yes | | |

## Check yourself

- Why isn't a quick format enough before giving a PC away?
- Which destruction method is useless on an SSD?
- If an outside company destroys your drives, what document do you keep?
- Why would a company wipe a drive and then still shred it?
