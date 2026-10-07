# Core 2, Part 10: PBQ answers and marking

Questions are in `part-10-pbq.md`. Mark yourself honestly: one point per correct item, nothing for a wrong item (no negative marks). This kit marks each item separately. CompTIA does not publish its PBQ scoring rules, so treat this as practice marking, not the real formula.

---

## C2P10-PBQ1: Lock down the new router (8 points)

| # | Correct choice | Why |
|---|---|---|
| 1 | Change to a strong, unique password | Factory logins are often published online. |
| 2 | Update to the latest version | Old firmware has known security holes. |
| 3 | Off | UPnP lets devices open ports on their own, and malware can abuse that. |
| 4 | WPA3 | WPA3 is the newest and strongest of the four options, and the scenario says every device supports it. |
| 5 | HTTPS | Manage over HTTPS, never plain HTTP. |
| 6 | Off | The owner never manages it from the internet, so remove that door. |
| 7 | Create a separate guest network | Guest access gives internet only, with no route to inside devices. |
| 8 | In a screened subnet | A separate zone for public-facing servers (formerly called a DMZ). |

**Marking:** 8 = full marks. 6 to 7 = good, recheck the misses. Below 6 = reread the SOHO tables in the Part 10 cheat sheet. Rows 1 and 2 wrong would be the worst misses: they are the first two things to do on any new router.

---

## C2P10-PBQ2: Match the problem to the fix (9 points)

| # | Letter | Why |
|---|---|---|
| 1 | A | Remote wipe erases the phone from far away. |
| 2 | B | A locator application shows the phone on a map. |
| 3 | C | Swipe has no security, anyone can do it. |
| 4 | D | A matching hash means the file was not changed. |
| 5 | E | A certificate warning means stop. The site may be fake or expired. |
| 6 | F | A screened subnet holds public-facing servers away from the inside network. |
| 7 | G | A guest network keeps visitors away from office devices. |
| 8 | H | Secure DNS encrypts website name lookups. |
| 9 | J | A configuration profile pushes settings and rules to phones, usually through MDM. |

Not used: **I, Disable SSID broadcast.** It only hides the network name and is not real security.

**Marking:** 9 = full marks. 7 to 8 = good. Below 7 = redo the mobile and browser tables in the cheat sheet. If you picked I for anything, reread the wireless table: hiding a name is not encryption.
