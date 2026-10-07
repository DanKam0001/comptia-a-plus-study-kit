# Core 2, Part 10: PBQ practice (Mobile, SOHO networks, browsers)

Objectives 2.8, 2.10, 2.11 (220-1202). Print this page or copy it into a text file and fill it in. Do not open `part-10-pbq-answers.md` until you have finished both tasks. Use only the Part 10 cheat sheet if you get stuck, and note what you had to look up.

---

## C2P10-PBQ1: Lock down the new router

| | |
|---|---|
| **ID** | C2P10-PBQ1 |
| **Objectives** | 2.10 |
| **Type** | Configure this (choose one option per setting, like a settings screen) |
| **Time guide** | 5 minutes |

**Scenario.** A small office has just unpacked a new router. The owner will manage it only from a PC inside the office, never from the internet. Every device in the office supports the newest Wi-Fi security. The office also runs one small public website on a server in the building, and visitors often ask for Wi-Fi.

**Task.** For each setting below, tick the ONE option you would choose.

**Materials: the settings screen**

| # | Setting | Option 1 | Option 2 | Option 3 | Option 4 |
|---|---|---|---|---|---|
| 1 | Administrator password | [ ] Leave the factory default | [ ] Change to a strong, unique password | | |
| 2 | Router firmware | [ ] Leave as shipped | [ ] Update to the latest version | | |
| 3 | UPnP | [ ] On | [ ] Off | | |
| 4 | Wi-Fi encryption | [ ] WEP | [ ] WPA | [ ] WPA2 (AES) | [ ] WPA3 |
| 5 | Management page protocol | [ ] HTTP | [ ] HTTPS | | |
| 6 | Remote (from the internet) management | [ ] On | [ ] Off | | |
| 7 | Visitor Wi-Fi | [ ] Give visitors the main office network password | [ ] Create a separate guest network | | |
| 8 | Where the public website server lives | [ ] On the same inside network as the office PCs | [ ] In a screened subnet | [ ] Directly on the modem with no firewall | |

---

## C2P10-PBQ2: Match the problem to the fix

| | |
|---|---|
| **ID** | C2P10-PBQ2 |
| **Objectives** | 2.8, 2.10, 2.11 |
| **Type** | Matching (drag and drop on paper: write one letter beside each problem) |
| **Time guide** | 6 minutes |

**Scenario.** You work the help desk for a company with phones, a small office network and web browsers to look after. Nine different calls come in during one morning.

**Task.** Write the letter of the best answer beside each problem. Each letter is used at most once. One answer is not used.

**Materials**

Problems:

| # | Problem | Your letter |
|---|---|---|
| 1 | A phone holding company email is gone for good. It must be erased from far away. | |
| 2 | An employee left a phone in a taxi and wants to see where it is on a map. | |
| 3 | Which screen lock gives no protection at all? | |
| 4 | You downloaded an installer and want to check nobody tampered with it. | |
| 5 | Your bank's website shows a certificate warning. | |
| 6 | A public web server must be reachable without exposing the inside PCs. | |
| 7 | Visitors need internet but must not reach the office PCs. | |
| 8 | You want to stop others watching which website names your PC looks up. | |
| 9 | IT wants to push the same Wi-Fi settings and passcode rules to every company phone. | |

Answers:

| Letter | Answer |
|---|---|
| A | Remote wipe |
| B | Locator application |
| C | Swipe |
| D | Compare the file's hash with the one the publisher posted |
| E | Stop and do not proceed |
| F | Screened subnet |
| G | Guest network |
| H | Secure DNS |
| I | Disable SSID broadcast |
| J | Configuration profile |
