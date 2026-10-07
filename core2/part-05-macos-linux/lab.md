# Lab: Try Linux for free, and learn macOS by comparison

**Time:** 30 to 40 minutes. **Needs:** a Windows 10 or 11 PC (no Mac needed). You'll run real Linux inside Windows using WSL (Windows Subsystem for Linux), which is free and fully removable. Everything here happens inside the Linux window. Use only the test folder in step 3.

## 1. Install Ubuntu in WSL

Open PowerShell **as administrator** and run:

```powershell
wsl --install -d Ubuntu
```

Restart if asked, then open **Ubuntu** from the Start menu and create a username and password. (Don't want to install? Use a free online Linux terminal instead. The commands are the same.)

## 2. Look around

```bash
pwd
ls
ls -l
man ls
df -h
du -sh ~
ps
top
```

Press `q` to leave `man` and `top`. Write down your current folder (`pwd`) and free space (`df`).

## 3. Make, copy, move, search, delete (test folder only)

```bash
mkdir lab
cd lab
echo "hello linux" > a.txt
cp a.txt b.txt
mv b.txt c.txt
cat c.txt
grep linux c.txt
find . -name "*.txt"
ls -l a.txt
chmod 600 a.txt
ls -l a.txt
chmod 755 a.txt
ls -l a.txt
cd ..
rm -r lab
```

Check: what did the permission string `-rw-------` become after `chmod 600`? After `chmod 755`?

## 4. sudo and apt

```bash
sudo apt update
sudo apt install -y cowsay
cowsay "I just used sudo apt"
sudo apt remove -y cowsay
```

Notice that `apt install` without `sudo` fails. That is problem three from the video.

## 5. Networking and the config files

```bash
ip a
ping -c 4 1.1.1.1
curl -I https://example.com
dig example.com
traceroute example.com
cat /etc/hosts
cat /etc/resolv.conf
cat /etc/passwd
sudo cat /etc/shadow
cat /etc/fstab
```

(`ping -c 4` sends four pings. Without `-c`, Linux ping never stops until Ctrl + C. `traceroute` may need `sudo apt install traceroute` first.) Write down: which file lists user accounts, and which holds the scrambled passwords? Why does `/etc/shadow` need `sudo`?

## 6. macOS by comparison (read-only)

If you own or can borrow a Mac, find: Finder, the Dock, Spotlight (Command + Space), Mission Control (F3 or a three or four finger swipe up), **System Settings** (Network, Printers and Scanners, Privacy and Security), **Disk Utility**, **Time Machine**, **FileVault** (in Privacy and Security) and **Terminal**. Press Option + Command + Esc to see Force Quit. If you don't have a Mac, fill in this table from the cheat sheet instead:

```
Windows           macOS             Linux
Task Manager  ->  ?                 ?
File Explorer ->  ?                 ls / cd
chkdsk        ->  ?                 ?
BitLocker     ->  ?                 -
```

## 7. Clean up (optional)

To remove Ubuntu from Windows: PowerShell, `wsl --unregister Ubuntu`.

## Check yourself

- A frozen Mac app: what do you press? (Option + Command + Esc)
- Which Mac tool does automatic backups to an external drive? (Time Machine)
- Which Linux command installs software on Ubuntu with root rights? (`sudo apt install name`)
- Which Linux command is closest to Task Manager? (`top`)
- Which file holds the DNS servers? (`/etc/resolv.conf`)
