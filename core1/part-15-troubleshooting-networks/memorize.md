# Memorise list: Troubleshooting Networks (Core 1, Part 15)

Understand the video first, then learn these cold. They're the symptom-to-answer pairs a scenario question assumes you know.
Flashcards: [`flashcards/core1_part15.csv`](../../flashcards/core1_part15.csv) (import into Anki or any flashcard app).

## Symptom to cause

| Question | Answer |
|---|---|
| Limited connectivity, address starts 169.254 | No reply from DHCP. Windows used an APIPA address |
| Wi-Fi drops only when the microwave runs | Interference on the 2.4 GHz band |
| Calls choppy and robotic, web pages fine | Jitter (and the fix is QoS or a wired connection) |
| Switch port light blinks on and off repeatedly | Port flapping: bad cable, connector, NIC or port |
| Video call lags, long delay before replies | High latency |
| Wi-Fi fine near the router, drops far away | Distance and walls. Move closer or add an access point |
| One device cannot get online, everyone else can | The device, its cable or its settings |
| Everyone is offline | Router, modem or internet provider |
| Wi-Fi refuses a known device | Authentication failure: password, security type, account |

## Numbers and facts

| Question | Answer |
|---|---|
| APIPA address range starts | 169.254 |
| Maximum twisted pair Ethernet run | 100 m (328 ft) |
| Non-overlapping 2.4 GHz channels | 1, 6 and 11 |
| 2.4 GHz vs 5 GHz | 2.4 reaches further, slower, crowded. 5 is faster, shorter range |
| Latency vs jitter | Latency is the delay. Jitter is the variation in the delay |
| QoS does | Gives chosen traffic (such as voice) priority |

## Tools

| Question | Answer |
|---|---|
| Shows signal strength and which channels neighbors use | Wi-Fi analyzer |
| Tests a cable for wiring faults | Cable tester |
| Finds one cable among many | Toner probe |
| Tests that a network port can send and receive | Loopback plug |
