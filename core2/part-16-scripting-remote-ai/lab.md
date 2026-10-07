# Lab: Write a safe script, try remote access and test an AI's limits (Windows)

**Time:** 20 to 25 minutes. **Needs:** a Windows PC. Everything here is harmless. You will only create a text file and read some settings.

Goal: write your first script, see what remote access looks like, and meet an AI's limits.

## 1. Write a batch file (`.bat`)

1. Open Notepad and type:

```
@echo off
echo Computer name: %COMPUTERNAME%
echo User: %USERNAME%
ipconfig | findstr /i "IPv4"
pause
```

2. Save as `info.bat` on your Desktop (set "Save as type" to **All files**).
3. Double-click it. It gathers information about the computer, which is one of the listed use cases.

## 2. Write a PowerShell script (`.ps1`)

1. In Notepad type:

```powershell
Get-Date
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version
```

2. Save as `info.ps1`. Right-click it and choose **Run with PowerShell**. If a policy error appears, that is the system protecting you from unwanted scripts, so don't change it for this lab. Instead, open PowerShell and paste the two lines in by hand.

Compare the two. Which language is newer? (PowerShell)

## 3. Look at the remote access settings (read only)

1. Open **Settings > System > Remote Desktop** (Windows 11 Pro and Enterprise can host it. Home cannot).
2. Note whether it is on or off. Leave it off unless you know why you need it.
3. Press **Windows key + R**, type `mstsc` and press Enter. That is the RDP **client**, built into every edition. You do not have to connect to anything.
4. Optional: in PowerShell run `Get-Service sshd` to see if an SSH server service exists on your machine (it usually does not by default).

## 4. Meet an AI's limits

Ask any AI chatbot: "Give me three real, published books about the history of the Windows registry, with authors." Then search for each book. Which ones exist? A made-up book that sounds real is a **hallucination**. Also ask it a question you know the answer to and check for **accuracy**.

Do not paste anything private into it. Practise by using only made-up examples.

## Check yourself

- Which file extension means PowerShell? (`.ps1`)
- Which tool gives a secure command line, and on which port? (SSH, 22)
- Why shouldn't you run a script you found on a forum without reading it? (it may bring in malware or change settings)

## Going further (optional)

Edit `info.bat` to also print the free space on `C:` (`dir C:\ | findstr "free"`). Then ask yourself which job from the "use cases" list you could script at home.
