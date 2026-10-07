# Exam check: Troubleshooting Networks

Cover the answers and try each one out loud first.

**1.** A laptop shows limited connectivity, and has given itself an address that starts with 169.254. What is the most likely cause?
<details><summary>Answer</summary>The laptop could not get an address from the DHCP server.<br><br><em>Why:</em> 169.254 is the APIPA fallback address. Windows uses it when DHCP does not answer.</details>

**2.** A Wi-Fi connection keeps dropping, but only when someone uses the microwave. What should you do?
<details><summary>Answer</summary>Change the Wi-Fi channel, or move to the 5 GHz band.<br><br><em>Why:</em> a microwave oven interferes with the crowded 2.4 GHz band.</details>

**3.** Phone calls over the internet sound choppy and robotic, but web pages load fine. What is the most likely cause?
<details><summary>Answer</summary>Jitter on the connection.<br><br><em>Why:</em> live calls suffer when the delay between data pieces keeps changing. QoS or a wired connection helps.</details>

## More practice (written for this kit)

**4.** A switch port's link light blinks on and off over and over. What is this called, and what do you try first?
<details><summary>Answer</summary>Port flapping. Replace the cable, then try a different port.</details>

**5.** A user's laptop is the only device that cannot reach the internet. Where do you look first?
<details><summary>Answer</summary>At that laptop: its cable or Wi-Fi, its address and its settings.</details>

**6.** Wi-Fi works well beside the router but drops at the far end of the house. What do you do?
<details><summary>Answer</summary>Move closer, move the router central, or add an access point.</details>

**7.** A phone joins the office Wi-Fi but is refused when it asks to sign in. Name the symptom and one likely cause.
<details><summary>Answer</summary>An authentication failure. Likely a wrong or expired password or account, or a security type the device cannot use.</details>

**8.** Which tool shows signal strength and the channels nearby networks use?
<details><summary>Answer</summary>A Wi-Fi analyzer.</details>

**9.** A network cable run is 130 m long and the connection is slow and drops often. Why?
<details><summary>Answer</summary>Twisted pair Ethernet has a maximum run of 100 m. The cable is too long.</details>

**10.** What does QoS do for a VoIP phone?
<details><summary>Answer</summary>It gives voice traffic priority over other traffic, which reduces choppy calls.</details>
