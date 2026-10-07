# Core 1, Part 8 PBQs: How a Network Configures Itself

Performance-based question (PBQ) practice for **Objectives 2.4 and 2.3** (220-1201). Do each task on paper or in a text file. Answers are in a separate file ([part-08-pbq-answers.md](part-08-pbq-answers.md)), so don't open it until you have finished.

If you are stuck, check the [Part 8 cheat sheet](../../core1/part-08-network-config-services/cheatsheet.md), mark that item, and lose the point.

---

## C1P08-PBQ1: Fill in the DHCP server form

- **Objective:** 2.4
- **Type:** Configure this (DHCP server form)
- **Time guide:** 6 minutes

### Scenario

You are setting up DHCP (Dynamic Host Configuration Protocol, which hands out IP addresses) for a small office. DHCP must hand out addresses from 192.168.1.100 to 192.168.1.200. The router uses 192.168.1.1. An old door controller cannot use DHCP, so someone typed 192.168.1.150 into it by hand. The office printer has the MAC address AA-BB-CC-DD-EE-01. It must always get 192.168.1.120, and you want that managed from the DHCP server.

### Materials

```
+-------------------------------------------------------------+
|  DHCP SERVER SETUP                                          |
|-------------------------------------------------------------|
|  Scope start address:   [ __________________ ]              |
|  Scope end address:     [ __________________ ]              |
|  Exclusion address(es): [ __________________ ]              |
|  Reservation MAC:       [ __________________ ]              |
|  Reservation IP:        [ __________________ ]              |
+-------------------------------------------------------------+
```

### Task

**Part A.** Fill in the five boxes. Write "none" for a box that does not need an entry. The exclusion must cover **only** addresses that are inside the scope and in use by hand.

**Part B.** For each device, write how it gets its address: `Dynamic`, `Static` or `Reservation`.

| Device | How it gets its address |
|---|---|
| Staff laptops that come and go | |
| Router at 192.168.1.1 (typed in by hand) | |
| Door controller at 192.168.1.150 (typed in by hand) | |
| Office printer at 192.168.1.120 (chosen by MAC address on the server) | |

**Part C.** DHCP also gives each device a time limit on its address. What is that called, in one word?

### Marking

12 points: Part A 5 (one per box), Part B 4 (one per device), Part C 1, plus 2 for one sentence explaining why the exclusion is needed (it stops DHCP handing .150 to a laptop and causing an address clash).

---

## C1P08-PBQ2: Match the need to the service

- **Objective:** 2.4 and 2.3
- **Type:** Matching
- **Time guide:** 7 minutes

### Scenario

You are the IT contact for a small company with a website, email, a managed switch and remote workers. Ten needs came in this week. Match each need to the one best answer. The answer list has twelve entries, so two are not needed.

### Materials

**Needs**

1. A remote worker needs safe access to the office network across the internet.
2. Guest Wi-Fi must be kept apart from company PCs on the same managed switch.
3. The company's website name must reach a server's IPv6 address.
4. `shop.example.com` should always follow wherever `www.example.com` points (an alias).
5. Tell the world which server receives email for the company's domain.
6. List which servers are allowed to send mail for the domain, to fight spam, using a DNS text record.
7. Add a digital signature to every message so the receiver can check it was not altered.
8. Tell receiving servers what to do when those checks fail (for example reject the mail) and to send reports.
9. Spread website visitors across three web servers.
10. The clocks on the servers disagree, and logs do not line up.

**Answers**

- **A.** VPN
- **B.** VLAN
- **C.** A record
- **D.** AAAA record
- **E.** CNAME record
- **F.** MX record
- **G.** SPF
- **H.** DKIM
- **I.** DMARC
- **J.** Load balancer
- **K.** NTP
- **L.** Proxy server

### Task

Write the letter for each need. Each letter is used at most once.

### Marking

10 points: 1 per need.
