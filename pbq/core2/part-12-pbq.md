# Core 2, Part 12: PBQ practice (Troubleshooting Windows)

Objective 3.1 (220-1202). Print this page or copy it into a text file and fill it in. Do not open `part-12-pbq-answers.md` until you have finished both tasks.

---

## C2P12-PBQ1: Match the symptom to the first fix

| | |
|---|---|
| **ID** | C2P12-PBQ1 |
| **Objectives** | 3.1 |
| **Type** | Matching (drag and drop on paper: write one letter beside each symptom) |
| **Time guide** | 5 minutes |

**Scenario.** You are the only technician on shift. Eight calls come in about Windows PCs. For each one, pick the best first fix.

**Task.** Write the letter of the best answer beside each symptom. Each letter is used at most once. Two answers are not used.

**Materials**

| # | Symptom | Your letter |
|---|---|---|
| 1 | A blue screen appears right after a graphics driver was updated. | |
| 2 | A black screen says "Operating system not found". A USB stick was left plugged in. | |
| 3 | The clock resets to an old date every time the PC is unplugged. | |
| 4 | A service will not start. The error says a dependency failed. | |
| 5 | Windows warns about USB controller resources. Many devices are plugged in. | |
| 6 | A domain user cannot sign in. The PC clock is 10 minutes wrong. | |
| 7 | A PC shuts itself down under load. The vents are clogged with dust. | |
| 8 | You want to see which program is using the most memory right now. | |

| Letter | Answer |
|---|---|
| A | Boot to safe mode, then roll back the driver |
| B | Remove the USB stick, then check the boot order |
| C | Replace the CMOS battery |
| D | Start the service it depends on |
| E | Use a powered USB hub and fewer devices |
| F | Sync the clock with a time server (`w32tm /resync`) |
| G | Clean the dust from the vents and fans |
| H | Open Task Manager |
| I | Reinstall Windows straight away |
| J | Replace the keyboard |

---

## C2P12-PBQ2: Fix a blue screen after an update

| | |
|---|---|
| **ID** | C2P12-PBQ2 |
| **Objectives** | 3.1 |
| **Type** | Ordering (number the steps), plus fill in the blanks |
| **Time guide** | 6 minutes |

**Scenario.** A user's PC shows a blue screen every time it starts. It began right after a driver update yesterday. The user is waiting.

**Task.**

**Part A.** Number the steps 1 to 5 in the order you would do them. One step is a wrong move: leave it blank.

| Your number | Step |
|---|---|
| | Restart normally and check that Windows now stays up. |
| | Open Device Manager and roll back the driver that was just updated. |
| | Write down the stop code shown on the blue screen. |
| | Boot into safe mode. |
| | Reinstall Windows. |
| | Record the fix in the ticket (issue, progress, resolution). |

**Part B.** Fill in the blanks.

| # | Blank |
|---|---|
| 1 | Any three of the four `bootrec` switches that repair boot: `/_____`, `/_____`, `/_____` |
| 2 | The command to check and repair Windows system files: `sfc /_____` |
| 3 | The command to resync the clock: `w32tm /_____` |
| 4 | Crash dump files are saved in `C:\Windows\_____` |
| 5 | A domain sign-in (Kerberos) by default needs clocks within ___ minutes |
