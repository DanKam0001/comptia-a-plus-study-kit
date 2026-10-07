# Lab: Drive the Windows command line

**Time:** 25 to 30 minutes. **Needs:** any Windows PC. Everything here is safe: it only reads information or works inside one test folder you create. **Do not run `format`, `diskpart clean` or `chkdsk /f` in this lab.**

## 1. Open Command Prompt (twice)

1. Start menu, type `cmd`, press Enter. This is a normal prompt.
2. Close it, type `cmd` again, right click the result and choose **Run as administrator**. The title bar says "Administrator". You will use this one in step 5.

## 2. Move around

```
cd %USERPROFILE%
dir
cd Desktop
cd ..
```

Then try `dir /?` to read the built-in help.

## 3. Network commands

```
ipconfig
ipconfig /all
ping 127.0.0.1
ping -n 4 1.1.1.1
nslookup example.com
tracert -d example.com
netstat -ano
```

Write down:
- Your IP address, subnet mask and default gateway (from `ipconfig`).
- Your DNS server and MAC address (from `ipconfig /all`).
- How many hops `tracert` showed, and where the times jump up.
- One local port number that is LISTENING in `netstat`.

(`tracert -d` skips name lookups and runs faster. Press Ctrl + C to stop early.)

## 4. Information commands

```
hostname
whoami
whoami /groups
winver
net user
```

## 5. File commands (in an administrator prompt is fine, but not required)

```
cd %USERPROFILE%\Desktop
md LabTest
md LabTest\Source
echo hello > LabTest\Source\a.txt
md LabTest\Source\Sub
echo world > LabTest\Source\Sub\b.txt
robocopy LabTest\Source LabTest\Backup /E
dir /s LabTest\Backup
rmdir /s /q LabTest
```

Check: did `Backup` get the `Sub` folder? What would have happened without `/E`?

## 6. System file check (administrator prompt)

```
sfc /scannow
```

It can take 10 to 15 minutes. It is safe: it only repairs damaged protected files. Note whether it found any problems.

## 7. Group Policy

```
gpupdate /force
gpresult /r
```

(On Home you get limited output. That is fine.)

## Write it up

```
IP / mask / gateway:
DNS server:
Hops to example.com:
My account and groups:
Windows version and build (winver):
sfc result:
```

## Check yourself

- A user can't get online. Which command shows the IP address and gateway? (`ipconfig`)
- Which command finds where traffic stops on the way to a website? (`tracert`, or `pathping` for loss per hop)
- Which command repairs damaged Windows files? (`sfc /scannow`)
- What is the difference between `chkdsk` and `sfc`? (drive versus Windows files)

## Going further (optional)

Run `pathping example.com` and read the loss column for each hop. It takes a few minutes. Then run `robocopy` again with `/MIR` on two test folders (never your real data) and see how it deletes files from the destination.
