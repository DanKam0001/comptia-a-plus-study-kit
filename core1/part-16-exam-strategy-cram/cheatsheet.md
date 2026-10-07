# Core 1, Part 16: Core 1 Exam Strategy, PBQs and a Cram Review

**Objectives:** this part adds no new objective. It covers **exam technique** for 220-1201 and a **cram review of every Core 1 objective** (1.1 to 5.6), pointing to the memorise sheets in this kit.

## The exam at a glance

| Fact | Value |
|---|---|
| Exam code | 220-1201 (Core 1). The retired exam is 220-1101 |
| Questions | At most 90 |
| Time | 90 minutes |
| Question types | Multiple choice and performance-based questions (PBQs) |
| Passing score | 675 on a scale of 100 to 900 |
| Domains | Mobile Devices 13%, Networking 23%, Hardware 25%, Virtualization and Cloud Computing 11%, Hardware and Network Troubleshooting 28% |

CompTIA recommends about 12 months of help desk or support experience for Core 1. CompTIA's official objectives are the authoritative list of what can be asked. Always check the current version.

## Strategy 1: performance-based questions (PBQs)

A PBQ is a small simulation. Typical jobs: drag labels onto a diagram, match items, put steps in order, or change settings on a pretend screen.

1. PBQs take longer than multiple choice, and they often appear first.
2. **Flag it and skip it.** Finish the multiple choice questions first, so you bank those points.
3. Come back with the time that is left.
4. Read the **whole task** before you click anything. Do the parts you know.
5. **Never leave a PBQ blank.** Place or fill in every part, even if you are unsure.
6. A PBQ is built from the same facts as the rest of the exam: ports, connectors, cable types, device names, settings. The labs in this kit are the best practice.

## Strategy 2: time

- 90 minutes for at most 90 questions is about **one minute per question**.
- First pass: answer what you know quickly.
- Stuck for about 30 seconds? **Pick your best answer, flag it, and move on.**
- CompTIA does not publish a penalty for wrong answers, but a blank can never score, so **never leave a question blank**. With about 10 minutes left, fill in anything still empty.
- Use any spare time to review flagged questions, not to second-guess answers you were sure of.

## Strategy 3: reading questions

- Read the **last sentence first** (what is actually being asked), then the scenario.
- Watch for the key words: **FIRST**, **BEST**, **MOST LIKELY**, **NOT**, **LEAST**.
- When two answers both look right:
  - Re-read the question for the exact situation.
  - For "first" questions, the **simple, cheap, low-risk step** usually beats a big repair (check the cable before replacing the motherboard).
  - Cross out answers that are plainly wrong, then choose among the rest.
  - The answer must fit the situation as written, not a situation you imagine.
- Read **every** option. A good-looking first option can still lose to a better fourth one.

## Strategy 4: think like the exam

- A symptom is a clue to a part (a line on every laser page is the drum or cartridge, a 169.254 address is DHCP, shutdowns after minutes are cooling or power).
- **Safety first:** a swollen battery means stop using it. ESD, lifting and power-off steps are the safe answer.
- The six-step troubleshooting method is **not tested in 220-1201** (the objectives say it was left out of the exam), but the habit still helps: find out what changed, try the simple fix first, test one thing at a time.

## Exam day

- Bring **two valid IDs**. Your primary ID is government-issued with your name, a recent photo and your signature. The first and last name must match your booking exactly.
- Arrive early, or log in early for an online exam.
- Retake rules (CompTIA): if you fail the first time, you can retake without a waiting period. From the second failure on, you must wait **14 calendar days** before the next attempt.
- The day before: review the memorise sheets, do not learn new topics, sleep.

## Cram review: every Core 1 part

Learn the **memorise sheet** for each part (`memorize.md` in its folder) and run its flashcards (`flashcards/core1_partNN.csv`).

| Part | Topic | Objectives | Folder |
|---|---|---|---|
| 1 | Motherboards, CPUs and Firmware | 3.5 | [core1/part-01-motherboards-cpus-firmware](../part-01-motherboards-cpus-firmware/memorize.md) |
| 2 | RAM: form factors, DDR, ECC, channels | 3.3 | [core1/part-02-ram](../part-02-ram/memorize.md) |
| 3 | Storage: HDD, SSD, NVMe, M.2, RAID | 3.4 | [core1/part-03-storage](../part-03-storage/memorize.md) |
| 4 | Power supplies, cables and connectors | 3.6, 3.2 | [core1/part-04-power-cables](../part-04-power-cables/memorize.md) |
| 5 | Displays | 3.1 | [core1/part-05-displays](../part-05-displays/memorize.md) |
| 6 | Printers and multifunction devices | 3.7, 3.8 | [core1/part-06-printers](../part-06-printers/memorize.md) |
| 7 | Ports and protocols | 2.1 | [core1/part-07-ports-protocols](../part-07-ports-protocols/memorize.md) |
| 8 | Network configuration and services | 2.4, 2.3 | [core1/part-08-network-config-services](../part-08-network-config-services/memorize.md) |
| 9 | Network hardware, connection types and tools | 2.5, 2.7, 2.8 | `core1/part-09-*` |
| 10 | Wireless and SOHO networks | 2.2, 2.6 | [core1/part-10-wireless-soho](../part-10-wireless-soho/memorize.md) |
| 11 | Laptops and mobile devices | 1.1, 1.2, 1.3 | [core1/part-11-laptops-mobile](../part-11-laptops-mobile/memorize.md) |
| 12 | Virtualization and cloud | 4.1, 4.2 | `core1/part-12-*` |
| 13 | Troubleshooting motherboards, RAM, CPU, power, drives, RAID | 5.1, 5.2 | `core1/part-13-*` |
| 14 | Troubleshooting displays, mobile devices, printers | 5.3, 5.4, 5.6 | [core1/part-14](../part-14-troubleshooting-displays-mobile-printers/memorize.md) |
| 15 | Troubleshooting networks | 5.5 | [core1/part-15](../part-15-troubleshooting-networks/memorize.md) |

## The numbers to have cold (full tables are in the memorise sheets)

- **Memory:** DIMM pins DDR3 240, DDR4 288, DDR5 288. SODIMM pins DDR3 204, DDR4 260, DDR5 262.
- **RAID:** 0 striping, no protection. 1 mirroring, 2 drives. 5 minimum 3 drives. 6 minimum 4. 10 minimum 4. RAID is not a backup.
- **Power and drives:** main connector 24-pin (20+4). SATA III 6 Gbps. M.2 2280 = 22 mm x 80 mm.
- **Cables:** Cat 6a 10 Gbps. Twisted pair maximum 100 m. USB 2.0 480 Mbps, USB 3.0 5 Gbps. VGA 15-pin analog.
- **Ports:** FTP 20-21, SSH 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, HTTP 80, POP3 110, IMAP 143, NetBIOS 137-139, LDAP 389, HTTPS 443, SMB 445, RDP 3389. See [ports-and-protocols](../../memorize/ports-and-protocols.md).
- **Wireless:** 2.4 GHz reaches further, 5 GHz is faster. Non-overlapping 2.4 GHz channels: 1, 6, 11.
- **Cloud:** IaaS, PaaS, SaaS. Type 1 hypervisor runs on the hardware, type 2 runs on an operating system.
- **Troubleshooting pairs:** see the memorise sheets for Parts 13, 14 and 15.

## Your last-week plan

1. Take a full timed [practice exam](../../exams/README.md). Mark every wrong answer with its objective number.
2. Re-watch only the parts for your weakest objectives.
3. Go through those parts' flashcards daily.
4. Take a second practice exam under the same conditions, flag-and-skip PBQs included.
