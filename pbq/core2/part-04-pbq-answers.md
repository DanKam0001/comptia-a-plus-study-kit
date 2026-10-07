# Core 2, Part 4: PBQ answers

Task file: [part-04-pbq.md](part-04-pbq.md). Try the tasks first.

---

## C2P04-PBQ1: Fix the network settings screen

| Field | Answer | Why |
|---|---|---|
| IP address | **192.168.1.20** | The sheet gives .20 as this PC's own address. .1 was the router's address typed into the wrong field |
| Subnet mask | **No change** (255.255.255.0) | Already matches the sheet |
| Default gateway | **192.168.1.1** | The gateway is the router, the exit from the network |
| Preferred DNS server | **8.8.8.8** | The DNS server turns names into addresses; a subnet mask does not belong in this field |

The "Use the following IP address" choice was already right: a PC that must keep one address needs a static (manual) setting.

**Partial credit (4 points):** 1 per field. A field you changed that was already right (the mask) earns 0. 4 = full marks. 3 = pass-level. 2 or fewer = reread the "Client network configuration" table.

---

## C2P04-PBQ2: Which setting solves it?

| # | Answer | Why |
|---|---|---|
| 1 | B, Public profile | Public hides your PC and blocks file and printer sharing; use it at coffee shops |
| 2 | H, Metered connection | Tells Windows the data is limited, so it holds back large background downloads such as some updates |
| 3 | A, VPN | A secure encrypted tunnel to another network |
| 4 | D, Map a network drive | Gives a share a drive letter; tick Reconnect at sign-in |
| 5 | G, Proxy settings | A site that fails only on a work network may be a proxy problem |
| 6 | C, Join a domain | One account on every PC in the domain, with settings pushed by Group Policy |
| 7 | F, Static IP address | Typed in by hand, so it never changes |
| 8 | E, Firewall exception | Allow the app through Windows Defender Firewall instead of turning the firewall off |

**Partial credit (8 points):** 1 per match. 7 to 8 = strong. 5 to 6 = review the "Common scenarios" table. 4 or fewer = reread Part 4's cheatsheet.
