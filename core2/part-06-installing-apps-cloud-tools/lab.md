# Lab: Check requirements, mount an ISO, and set up cloud sync (Windows)

**Time:** 20 to 30 minutes. **Needs:** any Windows PC and a free Microsoft or Google account. All steps are safe and reversible.

## 1. Is your PC 32-bit or 64-bit?

Open **Settings > System > About**. Under *Device specifications*, read **System type**. It will say something like "64-bit operating system, x64-based processor".
Write down your RAM and processor from the same screen.

## 2. Dedicated or integrated graphics?

Open **Task Manager > Performance**. If you see a **GPU** entry, click it.
- **Dedicated GPU memory** listed (and a number above zero) means a dedicated card with its own VRAM.
- Only **Shared GPU memory** means integrated graphics.

## 3. How much free storage?

Open **Settings > System > Storage**. Write down how much free space your main drive has. Would a 100 GB game fit?

## 4. Mount an ISO file

1. Download a small free ISO, for example the Core image from tinycorelinux.net (any legitimate free ISO works).
2. Right-click the ISO file and choose **Mount**.
3. Open **This PC**. A new virtual DVD drive appears, with the ISO's contents.
4. Right-click that drive and choose **Eject** when done.

You just did what Problem 2 in the video asks, with no disc and no disc drive.

## 5. Try cloud storage sync

1. Sign in to OneDrive (built into Windows) or Google Drive for desktop with a free account.
2. Open its settings and find which **folders sync**. Choose a small test folder only.
3. Add a text file to it, then open the web version of the service and confirm the file appears.
4. Edit the file on the web, and watch the change arrive on your PC.

## 6. Try a cloud collaboration tool

Create a document in Google Docs or Word on the web. Share it with a friend (or a second account of your own) and edit it at the same time.

## Write it up

```
OS type:               (32-bit or 64-bit)
RAM / CPU:
Graphics:              (dedicated or integrated)
Free storage:
Cloud sync tested:     (service name, folder chosen)
```

## Check yourself

- Would a 64-bit program install on this PC? Why or why not?
- What four kinds of impact should a company think about before rolling out a new app?
- A new employee cannot open the cloud spreadsheet app but can sign in. What is the most likely missing step?
