# Core 2, Part 10: Securing Mobile Devices, SOHO Networks and Browsers

**Objectives 2.8, 2.10, 2.11** (220-1202):
- 2.8 *Given a scenario, apply common methods for securing mobile devices.*
- 2.10 *Given a scenario, apply security settings on SOHO wireless and wired networks.*
- 2.11 *Given a scenario, configure relevant security settings in a browser.*

Domain: Security (28% of the exam).

## 2.8 Securing mobile devices

### Hardening techniques

| Technique | What to remember |
|---|---|
| Device encryption | Scrambles stored data. The screen lock protects the key, so encryption without a lock is weak |
| Screen locks | PIN code, pattern, fingerprint, facial recognition, swipe |
| Swipe | Gives no security. Anyone can do it |
| PIN / password | Longer is stronger. A fingerprint or face is convenient, but needs a PIN as backup |
| Configuration profiles | A bundle of settings and security rules pushed to the phone (Wi-Fi, passcode rules, restrictions), usually by MDM |

### Patch management

- **OS updates** and **application updates** both fix security holes. Keep both current.

### Endpoint security software

- **Antivirus** and **anti-malware** to find malicious apps.
- **Content filtering** to block bad or unwanted websites.

### Locating, wiping and backing up

| Feature | Use |
|---|---|
| Locator application | Shows a lost phone on a map, can make it ring or lock it |
| Remote wipe | Erases the phone from far away when it can't be recovered |
| Remote backup application | Keeps a copy in the cloud so a wipe or loss doesn't lose data |
| Failed log-in attempts restrictions | Locks for longer after wrong guesses, or erases after a set number (for example an iPhone can erase after 10 wrong passcodes if enabled) |

### Policies and procedures

- **MDM (mobile device management):** central tool to enforce rules, push configuration profiles, locate and wipe devices.
- **BYOD:** staff use their own device. Less company control, so use profiles or containers to protect work data.
- **Corporate-owned:** the company owns and fully controls the device.
- **Profile security requirements:** the rules a device must meet (passcode length, encryption on, OS version) before it can reach company resources.

## 2.10 SOHO wireless and wired network security

### Router settings

| Setting | Why |
|---|---|
| Change default passwords | Factory logins are often listed publicly online. Change the administrator username and password first |
| IP filtering | Allow or block traffic by IP address |
| Firmware updates | Old firmware has known security holes |
| Content filtering | Block categories of websites |
| Physical placement / secure locations | Keep the router where nobody can reach its ports or reset button |
| UPnP (Universal Plug and Play) | Lets devices open ports on their own. Turn it off, malware can abuse it |
| Screened subnet | A separate zone between the internet and the inside network for public-facing servers. Formerly called a DMZ |
| Configure secure management access | Manage over HTTPS, not plain HTTP. Disable remote management if unused |

### Wireless-specific

| Setting | Notes |
|---|---|
| Change the SSID | Default name often reveals the make and model |
| Disable SSID broadcast | Hides the name from the list, but it can still be found. Weak, not real security |
| Encryption settings | Best to worst: WPA3, WPA2 (AES), WPA, WEP. Never use WEP |
| Guest access | Separate network for visitors, internet only, no access to inside devices |

### Firewall settings

- **Disable unused ports** so nothing listens that doesn't need to.
- **Port forwarding / port mapping:** sends traffic arriving at the router on one port to one inside device. Forward only what you need. Each forward is an open door.

## 2.11 Browser security

### Download and install

- Use **trusted sources** (the maker's site, an official store).
- **Hashing:** the publisher posts a hash (fingerprint) of the file. You compute your own and compare. A match means the file wasn't changed. On Windows: `Get-FileHash <file> -Algorithm SHA256`.
- **Untrusted sources** are a main way malware arrives.

### Patching, extensions and plug-ins

- Keep the browser **patched**.
- **Extensions and plug-ins** also need trusted sources. Remove those you don't use. They can read what you browse.
- Features, plug-ins and extensions can each be **enabled or disabled**.

### Password managers

- Store strong unique passwords. They only fill in a password on the matching site, which helps against fake sites.

### Secure connections and certificates

- Look for **https** and the padlock. A **valid certificate** proves the site is who it says and the connection is encrypted.
- A **certificate warning** means: stop. The site may be fake, expired, or your PC clock may be wrong.

### Settings

| Setting | What it does |
|---|---|
| Pop-up blocker | Stops unwanted windows |
| Clearing browsing data | Removes history, cookies and saved form data |
| Clearing cache | Removes saved copies of web files (fixes stale or broken pages) |
| Private-browsing mode | Doesn't save history, cookies or form data on that device. Does NOT hide you from the network, employer or website |
| Sign-in / browser data synchronization | Copies bookmarks, passwords and settings between devices. Protect that account |
| Ad blockers | Remove ads, which can carry malware |
| Proxy | A middle server your traffic passes through |
| Secure DNS | Encrypts website name lookups so others can't watch them |

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Phone lost, holds company data | Remote wipe (via MDM), with a remote backup in place |
| Brand new router still on factory login | Change the default administrator password, then update firmware |
| Hidden SSID, owner thinks network is now secure | No. Use WPA3 or WPA2 AES |
| Visitors need Wi-Fi without seeing office PCs | Guest network |
| Public web server must be reachable | Screened subnet |
| Is this download genuine? | Compare its hash with the publisher's |
| Browser shows certificate warning | Don't proceed |
