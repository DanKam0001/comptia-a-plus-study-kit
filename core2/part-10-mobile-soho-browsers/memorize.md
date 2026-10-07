# Memorise list: Securing Mobile Devices, SOHO Networks and Browsers (Core 2, Part 10)

Understand the video first, then learn these cold. They're the facts a scenario question assumes you already know.
Flashcards: [`flashcards/core2_part10.csv`](../../flashcards/core2_part10.csv) (import into Anki or any flashcard app).

## Mobile

| Question | Answer |
|---|---|
| Five screen lock types | PIN code, pattern, fingerprint, facial recognition, swipe |
| Which screen lock gives no security? | Swipe |
| What protects the encryption key on a phone? | The screen lock |
| Lost phone, data must be protected | Remote wipe |
| Keeps data safe when you wipe | Remote backup |
| Finds a lost phone on a map | Locator application |
| MDM stands for | Mobile Device Management |
| BYOD stands for | Bring Your Own Device |
| What pushes settings and rules to a phone? | Configuration profile (usually via MDM) |
| Endpoint security software for phones | Antivirus, anti-malware, content filtering |

## SOHO router

| Question | Answer |
|---|---|
| First thing to do on a new router | Change the default administrator password |
| Why update router firmware | Fix known security holes |
| Secure management access means | Use HTTPS, not HTTP. Disable unused remote management |
| UPnP | Universal Plug and Play. Turn it off |
| Screened subnet | Zone for public-facing servers. Old name: DMZ |
| IP filtering | Allow or block by IP address |
| Content filtering | Block categories of websites |
| Port forwarding | Sends traffic on one port to one inside device |
| Firewall port hygiene | Disable unused ports |

## Wireless

| Question | Answer |
|---|---|
| SSID stands for | Service Set Identifier (the network name) |
| Does disabling SSID broadcast secure the network? | No. It only hides the name |
| Encryption ranking best to worst | WPA3, WPA2 (AES), WPA, WEP |
| Never use | WEP |
| Visitors on Wi-Fi without office access | Guest access (separate network) |

## Browser

| Question | Answer |
|---|---|
| Check a downloaded file is genuine | Compare its hash with the publisher's (for example SHA-256) |
| PowerShell command for a file hash | `Get-FileHash file -Algorithm SHA256` |
| What does a valid certificate prove? | The site is who it says, and the connection is encrypted |
| Certificate warning: what to do | Stop. Don't proceed |
| Does private browsing hide you from your employer? | No. It only skips saving history, cookies and form data on that device |
| Secure DNS does | Encrypts website name lookups |
| Clearing cache does | Removes saved copies of web files |
| Ad blocker also helps with | Malicious ads |
