# Core 1, Part 9: PBQ practice (Network Hardware, Connection Types and Tools)

Two performance-based question (PBQ) drills for **objectives 2.5, 2.7 and 2.8** (220-1201). Print this page or copy the answer blanks into a text file. Do the tasks **before** you open [`part-09-pbq-answers.md`](part-09-pbq-answers.md). Facts come from the Part 9 [cheatsheet](../../core1/part-09-network-hardware-tools/cheatsheet.md) and [memorise sheet](../../core1/part-09-network-hardware-tools/memorize.md).

---

## C1P09-PBQ1: Toolbox Match-up

| | |
|---|---|
| **ID** | C1P09-PBQ1 |
| **Objectives** | 2.8 |
| **Type** | Matching (drag and drop style) |
| **Time guide** | 5 minutes |
| **Points** | 8 (1 per correct match) |

### Scenario

You are wiring a small office. A bag of network tools sits on the bench and you have eight jobs to do. Each job needs exactly one tool, and each tool is used once.

### Task

Write the tool letter next to each job number.

### Materials

**Tools**

| Letter | Tool |
|---|---|
| A | Cable tester |
| B | Punchdown tool |
| C | Wi-Fi analyzer |
| D | Crimper |
| E | Network tap |
| F | Toner probe |
| G | Loopback plug |
| H | Cable stripper |

**Jobs**

| # | Job | Your tool letter |
|---|---|---|
| 1 | Attach an RJ45 plug to the end of a new cable | |
| 2 | Remove the outer jacket from a cable without nicking the wires inside | |
| 3 | Push the wires into the back of a patch panel and trim the extra | |
| 4 | Find which cable in a bundle runs to the reception desk by following a tone | |
| 5 | Check that a freshly made patch cable has every wire connected in the right place | |
| 6 | Plug into a switch port to test whether the port itself works | |
| 7 | Copy the traffic on a link so it can be inspected without interrupting the connection | |
| 8 | See nearby Wi-Fi networks, their channels and their signal strength | |

---

## C1P09-PBQ2: New Branch Connection Form

| | |
|---|---|
| **ID** | C1P09-PBQ2 |
| **Objectives** | 2.5, 2.7 |
| **Type** | Configure this (pick the right option for each field) |
| **Time guide** | 7 minutes |
| **Points** | 10 (1 per field) |

### Scenario

A company is opening three small sites and adding network gear. You fill in a setup form: first the internet connection for each site, then the power for network devices, then how to supply that power.

### Task

For every field, write the one option that fits best. Part A and Part C: pick from the option list shown. Part B: use this rule: **choose the lowest standard whose power limit is enough for the device.**

### Materials

**Part A: internet connection.** Options: Fiber, Cable, DSL, Satellite, Cellular, WISP.

| Field | Site description | Your answer |
|---|---|---|
| A1 | A farm with no phone line or cable TV line. The internet comes from a dish pointing at the sky. The owner accepts a noticeable delay | |
| A2 | A rural clinic. A radio link runs from a local tower to an antenna on the roof, and it needs a clear line of sight to the tower | |
| A3 | A city office. A glass cable carrying pulses of light enters the building | |
| A4 | The wall box where the glass cable in A3 ends and the light is turned into Ethernet. Options: ONT, Cable modem, Patch panel, Access point | |

**Part B: Power over Ethernet (PoE) standard.** Options: 802.3af, 802.3at, 802.3bt Type 3, 802.3bt Type 4.

First attempt: you may look at the limits below. Second attempt: cover them.

| Standard | Power limit at the switch port |
|---|---|
| 802.3af | 15.4 W |
| 802.3at | 30 W |
| 802.3bt Type 3 | 60 W |
| 802.3bt Type 4 | 90 W |

| Field | Device and the power it needs | Your answer |
|---|---|---|
| B1 | VoIP phone, needs 8 W | |
| B2 | Ceiling access point, needs 20 W | |
| B3 | Pan and tilt camera, needs 45 W | |
| B4 | Large outdoor camera with heater, needs 65 W | |

**Part C: how to supply the power.** Options: PoE switch, PoE injector.

| Field | Situation | Your answer |
|---|---|---|
| C1 | The office keeps its current ordinary switch and needs to power just one new camera | |
| C2 | The office is buying a new switch and wants the switch itself to power twelve cameras and phones | |
