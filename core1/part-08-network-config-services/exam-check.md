# Exam check: How a Network Configures Itself

Cover the answers and try each one out loud first.

**1.** A network printer gets a different address every time it restarts, so staff computers keep losing it. What should you set up in DHCP?
<details><summary>Answer</summary>A DHCP reservation for the printer. It ties the printer's MAC address to one IP address.</details>

**2.** Email sent from a company's domain keeps landing in spam folders, and the company needs to prove who is allowed to send it. Which DNS records help?
<details><summary>Answer</summary>TXT records holding SPF, DKIM and DMARC.</details>

**3.** A staff member working from a cafe needs to reach the office file shares safely over the public Wi-Fi. What should they use?
<details><summary>Answer</summary>A VPN, an encrypted tunnel to the office.</details>

## More practice (written for this kit)

**4.** Which DNS record points a name to an IPv6 address?
<details><summary>Answer</summary>AAAA.</details>

**5.** Which DNS record says which server receives email for a domain?
<details><summary>Answer</summary>MX (Mail Exchanger).</details>

**6.** Guest devices must be kept away from company computers on the same switch. What do you configure?
<details><summary>Answer</summary>A separate VLAN for guests (on a managed switch).</details>

**7.** A website gets so many visitors that one server can't cope. Which appliance spreads the load?
<details><summary>Answer</summary>A load balancer.</details>

**8.** Which part of AAA records what a user did?
<details><summary>Answer</summary>Accounting. Authentication is who you are, authorization is what you may do.</details>

**9.** A factory's control system runs old software that can't be updated. Which term describes this kind of system?
<details><summary>Answer</summary>SCADA, a legacy/embedded system. Isolate it from the main network.</details>
