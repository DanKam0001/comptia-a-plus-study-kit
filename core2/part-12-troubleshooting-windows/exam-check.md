# Exam check: Troubleshooting Windows

Cover the answers and try each one out loud first.

**1.** A PC shows a blue screen with a stop code every time it starts, right after a new driver was installed. What is the best first step?
<details><summary>Answer</summary>Boot into safe mode and roll back the driver. Why: a blue screen right after a change points at that change, and safe mode loads only basic drivers.</details>

**2.** A laptop powers on but says operating system not found. What should you check first?
<details><summary>Answer</summary>The boot order, and that the drive is detected in firmware. Remove any USB stick first.</details>

**3.** A PC's clock resets to the wrong date every time it's unplugged. What is the most likely fix?
<details><summary>Answer</summary>Replace the CMOS battery. It keeps the clock running when there's no power.</details>

## More practice (written for this kit)

**4.** A PC turns itself off under load, and the vents are full of dust. What is the most likely cause?
<details><summary>Answer</summary>Overheating. Clean the fans and vents, and check the cooler and thermal paste.</details>

**5.** A service won't start and the error says a dependency failed. What do you do?
<details><summary>Answer</summary>Open services.msc, check the Dependencies tab and start the dependency service first.</details>

**6.** Which command checks and repairs Windows system files?
<details><summary>Answer</summary>`sfc /scannow`.</details>

**7.** A domain user can't sign in and the PC's clock is 10 minutes wrong. What do you fix?
<details><summary>Answer</summary>Sync the clock with a time server. Kerberos allows about 5 minutes of difference.</details>

**8.** A PC has many USB devices plugged in and shows a USB controller resource warning. What do you try?
<details><summary>Answer</summary>Unplug devices, use a powered hub, and update the USB drivers in Device Manager.</details>
