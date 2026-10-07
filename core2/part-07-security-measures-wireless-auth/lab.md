# Lab: Audit your own security (Windows and a phone)

**Time:** 20 to 30 minutes. **Needs:** a Windows PC on your own Wi-Fi, a phone, and an online account you own (email, Microsoft, Google). Everything here is on your own devices and accounts. Do not test anyone else's doors or networks.

## 1. What Wi-Fi security are you using?

Open PowerShell (Start menu, type `powershell`) while connected to Wi-Fi:

```powershell
netsh wlan show interfaces
```

Look at **Authentication** (for example WPA2-Personal or WPA3-Personal) and **Cipher** (CCMP means AES).
- Is it WPA3? WPA2? Anything older?
- If your router's admin page offers WPA3 and your devices support it, note it. Changing it is optional, and can lock out older devices.

## 2. Turn on multifactor authentication

1. Pick one account you own (email is best).
2. Open its security settings and turn on **2-step verification / MFA**.
3. Choose an **authenticator app** (rather than SMS) if the service offers one.
4. Sign out and back in to see the code prompt.
5. Save the backup codes somewhere safe.

Which of the seven MFA methods from the cheat sheet did you use?

## 3. A physical security walk-through (observe only)

Walk through a building you are allowed in (home, college, workplace). On paper, tick every control you can see: bollards, fences, lighting, door locks, badge readers, cameras, alarm signs, a vestibule. Note one gap. Do not try to bypass anything.

## 4. Check what signs you in

On your phone, find which sign-in methods are enabled (PIN, fingerprint, face). Sort them into *something you know / have / are*.

## 5. Write it up

```
Wi-Fi security type:         (WPA2 / WPA3 / other)
Cipher:                      (CCMP = AES)
MFA turned on for:           (account) using (method)
Physical controls spotted:
Biggest gap I noticed:
```

## Check yourself

- Which control stops one person following another through a secure door?
- Why is an authenticator app stronger than SMS?
- Which central server would check Wi-Fi and VPN logins in a company?
