# Exam check: Virtualization and Cloud

Cover the answers and try each one out loud first.

**1.** A developer wants to test some risky software without putting their own PC at risk. What is the best choice?
<details><summary>Answer</summary>Run it inside a virtual machine as a sandbox. The VM is walled off from the host and can be deleted afterward.</details>

**2.** A shop's website needs many more servers during a sale, and far fewer afterward. Which cloud characteristic makes this possible?
<details><summary>Answer</summary>Elasticity. Resources grow when demand rises and shrink when it falls.</details>

**3.** A company wants its staff to use email and office tools without running any servers or installing software themselves. Which cloud service model is this?
<details><summary>Answer</summary>SaaS, software as a service. The provider runs everything and users just use the app.</details>

## More practice (written for this kit)

**4.** A hypervisor installs directly on server hardware with no operating system underneath. Which type is it?
<details><summary>Answer</summary>Type 1 (bare metal).</details>

**5.** A virtual machine will not start and reports that hardware virtualization is disabled. Where is it fixed?
<details><summary>Answer</summary>In the BIOS/UEFI firmware: enable Intel VT-x or AMD-V.</details>

**6.** Which cloud model is built for one organization only?
<details><summary>Answer</summary>Private cloud.</details>

**7.** Which costs money in many clouds, data coming in (ingress) or data going out (egress)?
<details><summary>Answer</summary>Egress, data going out, usually costs money. Ingress is usually free.</details>

**8.** How is a container different from a virtual machine?
<details><summary>Answer</summary>A container shares the host's operating system and packages just an app, so it is lighter and starts faster. A VM carries its own full guest operating system.</details>
