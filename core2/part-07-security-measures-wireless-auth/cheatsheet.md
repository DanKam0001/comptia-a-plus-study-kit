# Core 2, Part 7: Security Measures, Wireless Security and Authentication

**Objectives 2.1 and 2.3** (220-1202):
- 2.1: *Summarize various security measures and their purposes.*
- 2.3: *Compare and contrast wireless security protocols and authentication methods.*

Domain: Security (28% of the exam).

## 2.1 Physical security

| Control | What it does |
|---|---|
| Bollards | Short, strong posts that stop vehicles reaching a building |
| Access control vestibule | A small room with two doors; only one person gets through at a time. Also called a mantrap. Stops **tailgating** |
| Badge reader | Opens a door only for a valid card or badge |
| Video surveillance | Cameras that record who was where. Also a deterrent |
| Alarm systems | Sound or send an alert when a sensor trips |
| Motion sensors | Notice movement (lights, alarms, cameras) |
| Door locks | Keep rooms closed |
| Equipment locks | Secure servers, racks and laptops (cable locks, locked cabinets) |
| Security guards | People who check who enters and respond to problems |
| Fences | Keep people out of an area |

## 2.1 Physical access security

| Item | Notes |
|---|---|
| Key fobs | Small tag that unlocks a door |
| Smart cards | Card with a chip that proves who you are |
| Mobile digital key | A phone works as the door key |
| Keys | Ordinary physical keys |
| Biometrics | Use your body. Retina scanner, fingerprint scanner, palm print scanner, facial recognition technology (FRT), voice recognition technology |
| Lighting | Makes intruders easier to see |
| Magnetometers | Metal detectors (like airport arches) |

Keys, fobs, smart cards and mobile keys are **something you have**. Biometrics are **something you are**.

## 2.1 Logical security

| Term | Meaning |
|---|---|
| Principle of least privilege | Give people only the access their job needs |
| Zero Trust model | Nobody is trusted automatically, even inside the network. Verify every request |
| Access control lists (ACLs) | A list saying who may do what with a file, folder or device |
| MFA (multifactor authentication) | Two or more different kinds of proof |
| SAML | Security Assertions Markup Language. Lets one service tell another who you are (used for SSO) |
| SSO | Single sign-on. Sign in once, use many apps |
| Just-in-time access | Powerful rights given only when needed, then removed |
| PAM | Privileged access management. Controls and records powerful (admin) accounts |
| MDM | Mobile device management. Controls and secures phones and tablets |
| DLP | Data loss prevention. Stops sensitive data leaving the company |
| IAM | Identity access management. Manages who users are and what they can reach |
| Directory services | A central list of users and resources (for example Active Directory) |

**MFA methods listed in the objectives**

| Method | Notes |
|---|---|
| Email | A code sent to an email address |
| Hardware token | A small device that shows a code |
| Authenticator application | An app on your phone that shows a code. Stronger than SMS |
| SMS | Code by text message. Weaker, because messages can be intercepted |
| Voice call | Code read out by an automated call |
| TOTP | Time-based one-time password. A code that changes (usually every 30 seconds) |
| OTP | One-time password or passcode. Works once only |

Different **factors** are different kinds of proof: something you know (password, PIN), have (token, phone), are (biometric). Two passwords are **not** multifactor.

## 2.3 Wireless security protocols and encryption

| Protocol / method | Notes |
|---|---|
| WPA2 | Long-standing standard. Uses **AES** |
| WPA3 | Newest and strongest. Choose it if the router and devices support it |
| TKIP | Temporal Key Integrity Protocol. Older encryption, now weak. Avoid |
| AES | Advanced Encryption Standard. Strong encryption used by WPA2 and WPA3 |

Core 1 Part 10 covers setting up a SOHO wireless network. Part 10 of this series covers hardening a SOHO router.

## 2.3 Authentication methods

| Method | What it is | Remember |
|---|---|---|
| RADIUS | Remote Authentication Dial-In User Service | Central server for **network access** (Wi-Fi, VPN). Common ports: UDP 1812 (authentication) and 1813 (accounting) |
| TACACS+ | Terminal Access Controller Access-Control System Plus | Mainly used to control **administrator sign-in to network devices** (routers, switches). TCP port 49 |
| Kerberos | Ticket-based sign-in | Used in **Windows domains**. A ticket is issued so your password is not sent repeatedly. Port 88 |
| Multifactor | Two or more kinds of proof | See the MFA table above |

(The ports in this table are not listed in the objectives but are standard and good to know.)

## Common scenarios

| Symptom | Likely answer |
|---|---|
| People follow staff through the door without a badge | Access control vestibule |
| Stop vehicles ramming the entrance | Bollards |
| Check what happened at a door last night | Video surveillance |
| Stolen password gave access to an account | Add multifactor authentication |
| Strongest Wi-Fi security on a new router | WPA3 |
| Users should sign in once for many apps | SSO (often with SAML) |
| Contractor needs admin rights for one hour | Just-in-time access, managed with PAM |
| Staff must only open the files their job needs | Least privilege, enforced with ACLs |
| Wi-Fi and VPN logins checked by one central server | RADIUS |
| Admin sign-ins to switches and routers controlled and logged | TACACS+ |
