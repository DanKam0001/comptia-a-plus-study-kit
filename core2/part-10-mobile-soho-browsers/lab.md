# Lab: Audit your own phone, Wi-Fi and browser

**Time:** 20 to 30 minutes. **Needs:** your phone and a Windows PC with Edge or Chrome. Everything here is read-only unless you choose to turn a setting on. Don't change your router settings on a shared or work network.

Goal: check, on your own devices, the things Part 10 talks about.

## 1. Your phone

1. Open the screen lock settings. Which type do you use: PIN, pattern, fingerprint, face or swipe? Is the PIN at least 6 digits?
2. Find the setting that says the phone is **encrypted** (usually under Security or Privacy). Most current phones are encrypted by default once a lock is set.
3. Find your **locator** feature (Apple "Find My", Google "Find My Device" or similar). Is it switched on?
4. Check your **backup** is on (iCloud or Google backup).
5. Check for updates: is the OS and every app up to date?

## 2. Your Wi-Fi encryption (Windows)

In PowerShell:

```powershell
netsh wlan show interfaces
```

Read the **Authentication** line. WPA3-Personal or WPA2-Personal is good. WEP or Open is bad.

## 3. Prove a download is genuine

1. Download any installer from its official website (for example 7-Zip or VLC). Most of these publish a SHA-256 hash on the download page. If yours doesn't, use any file and practise the command anyway.
2. In PowerShell, from the download folder:

```powershell
Get-FileHash .\installer.exe -Algorithm SHA256
```

3. Compare the result with the publisher's hash. Do they match?
4. Change one letter of the published hash in your head. A single different character means a different file.

## 4. Browser settings tour

Open your browser settings and find each of these. Write down whether it's on or off:

- Pop-up blocker
- Secure DNS (Settings > Privacy and security > Security, "Use secure DNS")
- Clear browsing data (look at the choices, don't clear anything unless you want to)
- Extensions: list them. Do you recognise every one? Remove any you don't use.
- Sign-in / sync: which data is syncing?
- Proxy: Windows Settings > Network and Internet > Proxy. Is a proxy set? Should it be?

Open a site with https and click the padlock to view the **certificate**: who issued it, and when does it expire?

## 5. Write it up

```
Phone lock type / PIN length:
Encrypted / locator on / backup on:
Wi-Fi authentication:
Hash matched? (file + result):
Secure DNS on?  Extensions I removed:
```

## Check yourself

- Which of your phone settings would let you protect the data if you lost it today?
- If your router showed a login page at 192.168.1.1 with the factory password, what would you change first?
- Why isn't hiding the SSID real security?

## Going further (optional)

Log in to your **own** home router. Check the firmware version, whether UPnP is on, whether remote management is on, and whether you have a guest network. Write down what you would change.
