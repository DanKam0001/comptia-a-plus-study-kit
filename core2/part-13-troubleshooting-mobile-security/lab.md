# Lab: Check your phone and browser for the warning signs

**Time:** 20 to 30 minutes. **Needs:** your phone and a Windows PC. Everything here is read-only. Don't turn on developer mode, root or jailbreak anything.

Goal: look for the symptoms from this part, on your own devices.

## 1. Phone: battery and data

1. Open **Battery** settings. Which app used the most in the last 24 hours? Does that make sense?
2. Open **Mobile data** or **Data usage**. Which app used the most data? Set a data warning level if your plan has a limit.
3. Look at **storage**. Is it more than 90 percent full? A full phone makes apps crash and updates fail.

## 2. Phone: where did your apps come from?

- **Android:** Settings > Apps > Special app access > **Install unknown apps** (wording varies by phone maker). Does any app have permission to install apps? Turn it off for anything you don't need. Check whether **Developer options** is switched on (it's hidden by default).
- **iPhone:** all apps normally come from the App Store. Check **Settings > General > VPN & Device Management** for profiles you don't recognise.
- List any app you don't remember installing. Look it up before deciding.

## 3. Phone: connectivity drills

Practise each fix so it's automatic:

1. Turn Bluetooth off and on. Then **forget** one paired device and pair it again.
2. Turn on airplane mode, then off. Then **forget** your Wi-Fi network and rejoin it.
3. Check NFC is on (Android) and see how close the phone must be to a contactless reader.
4. Turn the rotation lock on, rotate the phone, then turn it off.

## 4. PC browser: look for hijack signs

1. Open your browser's **Extensions** page. Remove any you don't recognise.
2. Check your **home page and search engine** setting are what you chose.
3. Check the proxy: Windows Settings > Network and Internet > Proxy. Is a proxy turned on that you didn't set?
4. View the hosts file (read-only):

```powershell
Get-Content C:\Windows\System32\drivers\etc\hosts
```

On a clean PC it's mostly comment lines starting with `#`. Entries pointing popular sites to odd addresses are a redirection sign.

## 5. PC: update history

Open Settings > Windows Update > **Update history**. Any repeated failures? A failing update can be low disk space or, sometimes, malware.

## Check yourself

- A free app from a website, not the store, comes with ads and a fast-draining battery. What is the likely cause, and what do you do?
- What is the difference between rooting and jailbreaking?
- Your search results keep opening a different site. Name three places you check.
- A pop-up says your antivirus found 100 threats and gives a phone number. What is it?
