# Core 2, Part 9: PBQ answers

Task file: [part-09-pbq.md](part-09-pbq.md). Try the tasks first.

---

## C2P09-PBQ1: Put the malware removal steps in order

**Correct order: H, C, G, D, J, I, F, A, B, E**

| Position | Step | Why |
|---|---|---|
| 1 | H, Investigate and verify malware symptoms | Be sure it is malware before acting |
| 2 | C, Quarantine the infected system | Disconnect it from the network so it cannot spread |
| 3 | G, Disable System Restore in Windows Home | Infected files can hide in old restore points |
| 4 | D, Remediate infected systems | Remove or fix the infection |
| 5 | J, Update anti-malware software | Get the newest definitions |
| 6 | I, Scan and removal techniques | Clean what the normal OS cannot (safe mode, preinstallation environment) |
| 7 | F, Reimage or reinstall | If it cannot be cleaned |
| 8 | A, Schedule scans and run updates | Catch it coming back |
| 9 | B, Enable System Restore and create a restore point in Windows Home | A clean saved point, after the infection is gone |
| 10 | E, Educate the end user | Prevent a repeat |

Memory aid: I Q D R U S R S E E (Investigate, Quarantine, Disable, Remediate, Update, Scan, Reimage, Schedule, Enable, Educate).

**Partial credit (10 points):** 1 per step in the right position. 9 to 10 = strong. 7 to 8 = pass-level (the usual slips are swapping steps 3 and 4 or steps 5 and 6). 6 or fewer = learn the memory aid and retry.

---

## C2P09-PBQ2: Name that threat

| # | Answer | Why |
|---|---|---|
| 1 | A, Cryptominer | Secretly uses your CPU or GPU to mine cryptocurrency: slow, hot, loud fans |
| 2 | H, Smishing | Phishing by SMS text message |
| 3 | K, Whaling | Phishing aimed at senior executives |
| 4 | E, Ransomware | Locks or encrypts files and demands payment |
| 5 | C, Evil twin | A fake Wi-Fi network copying a real one |
| 6 | F, Rootkit | Hides deep in the OS, even from antivirus; often needs the recovery environment or a reinstall |
| 7 | G, Shoulder surfing | Watching someone enter a password or PIN |
| 8 | D, Keylogger | Records every key you press to steal passwords |
| 9 | B, Dumpster diving | Searching the trash for useful information |
| 10 | L, Zero-day attack | Uses a flaw nobody has patched yet |

Not used: I (a virus attaches to files and spreads when they are run) and J (a trojan is disguised as useful software).

**Partial credit (10 points):** 1 per match. 9 to 10 = strong. 7 to 8 = pass-level. 6 or fewer = reread the malware and social engineering tables.
