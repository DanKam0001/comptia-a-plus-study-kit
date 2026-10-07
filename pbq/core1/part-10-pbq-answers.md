# Core 1, Part 10: PBQ answers

Do the tasks in [`part-10-pbq.md`](part-10-pbq.md) first.

**Marking note:** real PBQs can earn partial credit, so each item here is marked on its own. CompTIA does not publish its PBQ scoring rules, so treat this as practice marking, not the real formula. Rough guide: all correct is a pass for this drill, 75 percent or more means you are close, below 50 percent means go back to the [cheatsheet](../../core1/part-10-wireless-soho/cheatsheet.md).

---

## C1P10-PBQ1: Set Up the New Router (6 points)

| Order | Step | Why |
|---|---|---|
| 1 | E Plug the internet line into the WAN port | The router needs its internet connection first |
| 2 | C Connect a laptop to a LAN port | You need a connected device to reach the settings page |
| 3 | F Open the settings page and log in | You cannot change settings until you are logged in |
| 4 | A Change the default admin password | The first security step on a new router, since everyone knows the default login |
| 5 | D Set the SSID and Wi-Fi password | Wi-Fi settings come after the admin login is secured |
| 6 | B Test internet on the new Wi-Fi | You can only test the new Wi-Fi once it exists |

**Answer string:** E, C, F, A, D, B

**Marking:** 1 point for each step you placed in its correct position. A step in the wrong place scores 0, but the steps around it can still score.

---

## C1P10-PBQ2: Address and Standard Sorting (12 points)

| # | Answer | Why |
|---|---|---|
| 1 | Private | Inside 192.168.0.0 to 192.168.255.255 |
| 2 | APIPA | Starts 169.254, the self-given address when DHCP does not answer |
| 3 | Private | 172.20 is inside 172.16.0.0 to 172.31.255.255 |
| 4 | Public | 172.32 is just outside the 172.16 to 172.31 private range |
| 5 | Private | Inside 10.0.0.0 to 10.255.255.255 |
| 6 | Public | 192.169 is outside 192.168.x.x, so not private |
| 7 | Public | Not in any private or APIPA range |
| 8 | Private | 172.31.255.254 is the top of the 172.16 to 172.31 range |
| 9 | 802.11ac | Wi-Fi 5: 5 GHz only, about 6.9 Gbps |
| 10 | 802.11b | 2.4 GHz only, 11 Mbps |
| 11 | 802.11be | Wi-Fi 7 |
| 12 | 802.11n | Wi-Fi 4: 2.4 and 5 GHz, 600 Mbps |

**Marking:** 1 point per blank. For 9 to 12 accept the answer with or without "802.11" only if the letters are exact (ac, b, be, n).
