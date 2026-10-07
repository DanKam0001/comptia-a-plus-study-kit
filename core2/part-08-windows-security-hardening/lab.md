# Lab: Audit your own Windows PC's security (read-only)

**Time:** 20 to 30 minutes. **Needs:** a Windows 10 or 11 PC you own. Everything here only **looks**. You will not change a setting unless a step says so.

## 1. Accounts and groups

Open PowerShell (Start menu, type `powershell`):

```powershell
Get-LocalUser | Select-Object Name, Enabled
whoami /groups
```

- Which accounts exist? Is **Guest** disabled?
- Are you in the **Administrators** group? Note it.
- Open **Settings > Accounts > Your info**. Is it a **local** or **Microsoft** account?

## 2. User Account Control

Start menu, type `UAC`, open **Change User Account Control settings**. Note the slider position. Close without changing.

## 3. Sign-in options

**Settings > Accounts > Sign-in options.** List which are available (PIN, fingerprint, facial recognition, security key). Which are set up on your PC?

## 4. Defender and the firewall

1. Open **Windows Security**. Check **Virus and threat protection**: is real-time protection on? When were definitions last updated?
2. Open **Firewall and network protection**: which profiles are on (domain, private, public)?
3. Press **Windows key + R**, type `wf.msc`, Enter. Look at **Inbound Rules** and find one rule for a program and one for a port.

## 5. Encryption

In PowerShell run **as administrator** (right-click > Run as administrator):

```powershell
manage-bde -status
```

Is the drive **Fully Encrypted**? If the command is not found you may be on Windows Home. Check **Settings > Privacy & security > Device encryption** instead.
Never turn BitLocker on without saving the recovery key somewhere off the PC.

## 6. Permissions

1. Make a folder on the Desktop called `permlab`.
2. Right-click it > **Properties > Security**. Click your user. Read the allow/deny boxes (these are **NTFS** permissions).
3. Open the **Sharing** tab > **Advanced Sharing** and read the share settings (do not share it). Note that share permissions are a separate list.
4. Delete the folder when finished.

## 7. Password and lockout policy

```powershell
net accounts
```

Read the **lockout threshold**, **minimum password length** and **maximum password age**. Those are the password considerations from the video, as set on this PC.

## 8. Hardening check

Tick each item for your PC: screen lock timeout set; BIOS/UEFI password set; AutoRun not launching anything from USB; unused services disabled; password manager in use.

## Write it up

```
Guest account:             (disabled / enabled)
My account type:           (standard / administrator, local / Microsoft)
Sign-in options in use:
Defender real-time on:     (yes / no)   Firewall profiles on:
Drive encrypted:           (yes / no / Home device encryption)
Lockout threshold / min password length:
One hardening gap:
```

## Check yourself

- If share permissions say Read and NTFS say Full Control, what do network users get?
- Which tool would you use to push a screen-lock setting to every PC in a domain?
- Which tool encrypts a whole drive, and which encrypts a USB stick?
