# Memorise list: Wireless and Setting Up a SOHO Network (Core 1, Part 10)

Understand the video first, then learn these cold.
Flashcards: [`flashcards/core1_part10.csv`](../../flashcards/core1_part10.csv) (import into Anki or any flashcard app).

## Bands and channels

| Question | Answer |
|---|---|
| Which band has the longest range and the most crowding? | 2.4 GHz |
| Which band is newest, and which devices can use it? | 6 GHz. Wi-Fi 6E and Wi-Fi 7 |
| Non-overlapping 2.4 GHz channels (US) | 1, 6 and 11 |
| Channel widths | 20, 40, 80, 160 MHz (Wi-Fi 7 adds 320 MHz) |
| Who decides which channels are legal? | The country's regulations |

## 802.11 standards

| Standard | Bands | Max speed |
|---|---|---|
| 802.11b | 2.4 GHz | 11 Mbps |
| 802.11a | 5 GHz | 54 Mbps |
| 802.11g | 2.4 GHz | 54 Mbps |
| 802.11n (Wi-Fi 4) | 2.4 and 5 GHz | 600 Mbps |
| 802.11ac (Wi-Fi 5) | 5 GHz only | about 6.9 Gbps |
| 802.11ax (Wi-Fi 6, 6E) | 2.4 and 5 GHz (6E: and 6 GHz) | 9.6 Gbps |
| 802.11be (Wi-Fi 7) | 2.4, 5 and 6 GHz | 46 Gbps |

## Short range

| Question | Answer |
|---|---|
| Bluetooth range and band | About 10 m, 2.4 GHz |
| NFC range | About 4 cm (touching distance), 13.56 MHz |
| Passive RFID tag | No battery, powered by the reader |

## IP addressing

| Question | Answer |
|---|---|
| IPv4 size and format | 32 bits, four numbers 0 to 255 |
| IPv6 size and format | 128 bits, hex groups split by colons |
| Private range 1 | 10.0.0.0 to 10.255.255.255 |
| Private range 2 | 172.16.0.0 to 172.31.255.255 |
| Private range 3 | 192.168.0.0 to 192.168.255.255 |
| APIPA range | 169.254.0.0 to 169.254.255.255 (mask 255.255.0.0) |
| What does an APIPA address mean? | The device got no answer from DHCP. Local only, no internet |
| Common home subnet mask | 255.255.255.0 |
| Default gateway is | The router's address on your network |
| Static vs dynamic | Static = typed by hand. Dynamic = from DHCP |

## SOHO router

| Question | Answer |
|---|---|
| Which router port takes the internet line? | WAN |
| First security step on a new router | Change the default admin password |
| SSID is | The Wi-Fi network name |
| Why update router firmware? | Fixes bugs and security holes |
