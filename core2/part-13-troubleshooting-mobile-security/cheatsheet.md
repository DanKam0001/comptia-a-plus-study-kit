# Core 2, Part 13: Troubleshooting Mobile OS, Apps and PC Security Issues

**Objectives 3.2, 3.3, 3.4** (220-1202):
- 3.2 *Given a scenario, troubleshoot common mobile OS and application issues.*
- 3.3 *Given a scenario, troubleshoot common mobile OS and application security issues.*
- 3.4 *Given a scenario, troubleshoot common personal computer (PC) security issues.*

Domain: Software Troubleshooting (23% of the exam).

Core 1 Part 14 (Troubleshooting Displays, Mobile Devices and Printers) covers the *hardware* side of mobile problems. This part is the *software and security* side. Core 2 Part 9 (Malware, Social Engineering and the Removal Procedure) gives the removal steps referred to below.

## 3.2 Mobile OS and application issues

| Symptom | Common causes | First things to try |
|---|---|---|
| Application fails to launch | Corrupt app, low storage, needs update | Restart the phone, update, clear cache, reinstall |
| Application fails to close / crashes | Bug, low memory, bad update | Force close, restart, update, reinstall |
| Application fails to update | Low storage, no connection, store account problem | Free space, check connection, sign in to the store, retry |
| Application fails to install | Low storage, incompatible OS, store problem | Free space, update the OS, check store account and connection |
| Slow to respond | Low storage or memory, too many background apps, malware | Close background apps, restart, free space, update, scan |
| OS fails to update | Low storage, low battery, poor connection | Free space, charge the battery, use stable Wi-Fi, retry |
| Battery life issues | Heavy app, high brightness, background activity, old battery | Check battery usage by app, lower brightness, close background apps, disable unused features, replace the battery |
| Random reboots | Bad app, overheating, failing battery, OS bug | Update the OS, remove recent apps, cool the phone, replace battery, last resort: back up and factory reset |
| Connectivity: Bluetooth | Off, out of range, stale pairing | Turn it on, move close, forget the device and pair again |
| Connectivity: Wi-Fi | Airplane mode, wrong password, stale network | Airplane mode off, forget the network and rejoin |
| Connectivity: NFC | Off, thick case, too far | Turn NFC on, remove case, hold against the reader (a few centimetres only) |
| Screen does not autorotate | Rotation lock on, app doesn't rotate, sensor | Turn off rotation lock, restart, check sensor calibration |

## 3.3 Mobile OS and application security issues

### Security concerns

| Concern | What it is |
|---|---|
| Application source / unofficial application stores | Apps outside the official store aren't checked. Installing one is sideloading |
| Developer mode | Unlocks powerful settings for app makers. Keep off unless needed |
| Root access / jailbreak | Removing the maker's restrictions. Rooting = Android, jailbreaking = iPhone. Lets malware take control and removes protections |
| Unauthorized / malicious application | Spyware, adware, trojans |
| Application spoofing | A fake app that imitates a real one |

### Common symptoms

High network traffic · degraded response time · data-usage limit notification · limited internet connectivity · no internet connectivity · high number of ads · fake security warnings · unexpected application behaviour · leaked personal files or data.

**Response:** identify and remove the suspicious app, run anti-malware, update the OS, change passwords for accounts that may have leaked, and if it persists back up and factory reset. Install only from the official store. Don't root or jailbreak.

## 3.4 Personal computer security issues

### Common symptoms

| Symptom | Likely cause / action |
|---|---|
| Unable to access the network | Malware changed network settings, or blocked access. Check settings, scan |
| Desktop alerts | Adware or fake alerts. Don't click. Scan |
| False alerts regarding antivirus protection | Rogue antivirus (scareware) pretending to be security software. Real antivirus won't ask for a phone call or payment in a pop-up |
| Altered system or personal files: missing or renamed files | Malware or ransomware |
| Altered system or personal files: inability to access files | Typical of ransomware. Isolate the PC, don't pay, restore from backup |
| Unwanted notifications within the OS | Adware or malicious site notifications. Remove the source |
| OS updates failures | Malware blocking updates, low space, corrupt update. Scan, free space, retry |

### Browser-related symptoms

| Symptom | Likely cause / action |
|---|---|
| Random or frequent pop-ups | Adware or a bad extension. Remove extensions, scan |
| Certificate warnings | Browser doesn't trust the site. May be fake, expired, an on-path attack, or a wrong PC clock. Don't proceed |
| Redirection | Malicious extension, changed proxy or DNS settings, hosts file changes. Remove, check settings |
| Degraded browser performance | Too many extensions, malware. Remove unknown extensions, clear cache, scan, reset the browser |

For a suspected infection, follow the malware removal procedure (Core 2 Part 9): investigate, quarantine, disable System Restore (Windows Home), remediate, update and scan, reimage if needed, re-enable restore and create a restore point, educate the user.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Fast battery drain plus ads after installing a downloaded app | Malicious sideloaded app. Remove, scan, install only from official store |
| Files renamed and can't be opened | Ransomware. Isolate, restore from backup |
| Browser redirects searches, pop-ups | Remove bad extensions, check proxy and DNS, scan |
| Phone won't pair with Bluetooth speaker | Forget the device and pair again |
| "Your antivirus found 100 threats, call this number" | Fake alert (rogue antivirus) |
| Screen won't rotate | Rotation lock on |
