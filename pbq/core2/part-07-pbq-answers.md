# Core 2, Part 7: PBQ answers

Task file: [part-07-pbq.md](part-07-pbq.md). Try the tasks first.

---

## C2P07-PBQ1: Sort the proofs of identity

**Part A**

| Column | Items | Why |
|---|---|---|
| Something you KNOW | A (Password), D (PIN) | Both are remembered secrets |
| Something you HAVE | B (Smart card), E (Hardware token), G (Key fob), H (Authenticator app on your phone) | Each is an object you hold; the app lives on your phone |
| Something you ARE | C (Fingerprint), F (Retina scan), I (Facial recognition), J (Voice recognition) | All are biometrics, which use your body |

**Part B**

| Pair | Answer | Why |
|---|---|---|
| 1 | No | Both are something you know; two passwords-type proofs are not multifactor |
| 2 | Yes | Know plus have |
| 3 | Yes | Have plus are |
| 4 | No | Both are something you are |

**Partial credit (14 points):** 1 per item in Part A and 1 per pair in Part B. 13 to 14 = strong. 10 to 12 = pass-level. 9 or fewer = reread the MFA section: factors are different kinds of proof, not just two proofs.

---

## C2P07-PBQ2: Choose the security setting

| Row | Answer | Why |
|---|---|---|
| 1 | WPA3 | Newest and strongest; choose it when the router and devices support it |
| 2 | AES | WPA2 uses AES. TKIP is older, weak encryption to avoid |
| 3 | RADIUS | Central server for network access such as Wi-Fi and VPN |
| 4 | TACACS+ | Mainly controls administrator sign-in to network devices such as routers and switches |
| 5 | Kerberos | Ticket-based sign-in used in Windows domains |
| 6 | Access control vestibule | Two doors, one person at a time; stops tailgating. A badge reader alone does not stop someone following you in |
| 7 | Bollards | Short strong posts that stop vehicles reaching a building |
| 8 | Video surveillance | Cameras record who was where |
| 9 | Just-in-time access | Powerful rights given only when needed, then removed |

**Partial credit (9 points):** 1 per row. 8 to 9 = strong. 6 to 7 = pass-level. 5 or fewer = reread the authentication methods table and the physical security table.
