# Core 1, Part 8 PBQ answers

Tasks: [part-08-pbq.md](part-08-pbq.md). Facts come from the [Part 8 cheat sheet](../../core1/part-08-network-config-services/cheatsheet.md).

---

## C1P08-PBQ1: Fill in the DHCP server form

**Part A**

| Box | Entry | Why |
|---|---|---|
| Scope start | **192.168.1.100** | The range DHCP may hand out |
| Scope end | **192.168.1.200** | |
| Exclusion address(es) | **192.168.1.150** | In the scope but typed by hand, so DHCP must never give it out. The router (.1) is outside the scope, so it needs no exclusion |
| Reservation MAC | **AA-BB-CC-DD-EE-01** | A reservation identifies the device by its MAC address |
| Reservation IP | **192.168.1.120** | It must always get this address |

**Part B**

| Device | Answer | Why |
|---|---|---|
| Staff laptops | **Dynamic** | Address handed out by DHCP |
| Router at .1 | **Static** | Typed in by hand |
| Door controller at .150 | **Static** | Typed in by hand (hence the exclusion) |
| Office printer at .120 | **Reservation** | DHCP always gives this MAC the same address |

**Part C:** **Lease** (how long a device may keep its address before it must renew).

**Own-words point:** DHCP would otherwise hand .150 to another device and cause two devices to fight over one address.

**Marking (12 points):** Part A 5, Part B 4, Part C 1, explanation 2 (1 for saying DHCP must not give .150 to others, 1 for saying this prevents a clash or duplicate address).
- 11 to 12: strong. 8 to 10: fine, review scope, exclusion and reservation. Under 8: redo the DHCP table.
- Common slip: excluding .1 as well. The router address is outside the scope, so nothing needs excluding.

---

## C1P08-PBQ2: Match the need to the service

| Need | Answer | Why |
|---|---|---|
| 1 | **A** VPN | An encrypted tunnel across an untrusted network |
| 2 | **B** VLAN | Splits one switch into separate virtual networks (managed switch) |
| 3 | **D** AAAA | AAAA points a name to an IPv6 address (an A record is IPv4) |
| 4 | **E** CNAME | An alias pointing one name at another name |
| 5 | **F** MX | Mail Exchanger, the server that receives the domain's email |
| 6 | **G** SPF | Lists the servers allowed to send mail for the domain |
| 7 | **H** DKIM | A digital signature on each message |
| 8 | **I** DMARC | Says what to do when SPF or DKIM fail, and sends reports |
| 9 | **J** Load balancer | Spreads traffic across servers |
| 10 | **K** NTP | Keeps all clocks in step |

Unused: **C** (A record, IPv4 only) and **L** (proxy server, makes requests for users).

**Marking (10 points):** 1 per need.
- 9 to 10: strong. 7 to 8: fine, recheck the DNS record and SPF/DKIM/DMARC tables. Under 7: relearn the TXT-based spam tools and VLAN vs VPN.
- Common slip: C for need 3. An A record is IPv4, so an IPv6 address needs AAAA.
