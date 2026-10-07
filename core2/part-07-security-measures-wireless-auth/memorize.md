# Memorise list: Security Measures, Wireless Security and Authentication (Core 2, Part 7)

Understand the video first, then learn these cold.
Flashcards: [`flashcards/core2_part07.csv`](../../flashcards/core2_part07.csv) (import into Anki or any flashcard app).

## Physical security (10 controls)

Bollards, access control vestibule, badge reader, video surveillance, alarm systems, motion sensors, door locks, equipment locks, security guards, fences.

| Question | Answer |
|---|---|
| Which control stops tailgating? | Access control vestibule (mantrap) |
| Which control stops vehicles? | Bollards |
| Five biometrics | Retina, fingerprint, palm print, facial recognition (FRT), voice |
| Something you have / something you are | Key, fob, smart card, mobile key / biometrics |
| Magnetometer is | A metal detector |

## Logical security

| Question | Answer |
|---|---|
| Least privilege | Only the access the job needs |
| Zero Trust | Never trust automatically, verify every request |
| ACL | Access control list: who may do what with a resource |
| SSO | Sign in once, use many apps |
| SAML | Security Assertions Markup Language, used to pass identity for SSO |
| PAM | Privileged access management |
| Just-in-time access | Powerful rights only when needed, then removed |
| MDM / DLP / IAM | Mobile device management / data loss prevention / identity access management |

## MFA

| Question | Answer |
|---|---|
| MFA methods (7) | Email, hardware token, authenticator app, SMS, voice call, TOTP, OTP |
| TOTP | Time-based one-time password, usually changes every 30 seconds |
| Strongest vs weakest code delivery | Authenticator app or hardware token stronger; SMS and voice call weaker |
| Three factors | Know (password), have (token), are (biometric) |

## Wireless and authentication servers

| Question | Answer |
|---|---|
| Strongest Wi-Fi security | WPA3 |
| WPA2 uses which encryption | AES |
| TKIP | Old and weak. Avoid |
| RADIUS | Network access (Wi-Fi, VPN). UDP 1812 and 1813 |
| TACACS+ | Admin sign-in to network devices. TCP 49 |
| Kerberos | Tickets, Windows domains. Port 88 |
