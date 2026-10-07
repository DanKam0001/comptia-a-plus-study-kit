# Core 1, Part 10: Wireless and Setting Up a SOHO Network

**Objectives 2.2 and 2.6** (220-1201): *Explain wireless networking technologies* and *Given a scenario, configure basic wired/wireless small office/home office (SOHO) networks.*
Domain: Networking (23% of the exam).

## Frequencies (2.2)

| Band | Range | Speed | Notes |
|---|---|---|---|
| 2.4 GHz | Longest, passes walls best | Slowest | Most crowded. Shared with Bluetooth, microwaves, cordless phones |
| 5 GHz | Shorter | Faster | More channels, less crowded |
| 6 GHz | Shortest | Fastest | Needs Wi-Fi 6E or Wi-Fi 7 devices. Very little interference |

## Channels (2.2)

- A band is split into **channels**. Two networks on the same or overlapping channels cause **interference** and slow each other down.
- **2.4 GHz in the US:** channels 1 to 11. Only **1, 6 and 11** do not overlap each other. Much of Europe allows 1 to 13.
- **Regulations:** each country sets which channels and power levels are legal, so a router must be set to the correct region.
- **Channel selection:** use a Wi-Fi analyzer to see which channels are busy, then pick a quiet one (or move to 5 or 6 GHz).
- **Channel width:** 20, 40, 80 and 160 MHz (Wi-Fi 7 adds 320 MHz on 6 GHz). Wider = faster, but uses more spectrum and clashes more.

## 802.11 standards (2.2)

Speeds are theoretical maximums. Real speeds are lower.

| Standard | Friendly name | Bands | Max speed |
|---|---|---|---|
| 802.11b | | 2.4 GHz | 11 Mbps |
| 802.11a | | 5 GHz | 54 Mbps |
| 802.11g | | 2.4 GHz | 54 Mbps |
| 802.11n | Wi-Fi 4 | 2.4 and 5 GHz | 600 Mbps |
| 802.11ac | Wi-Fi 5 | 5 GHz only | about 6.9 Gbps |
| 802.11ax | Wi-Fi 6 (6E adds 6 GHz) | 2.4 and 5 GHz (6E: and 6 GHz) | 9.6 Gbps |
| 802.11be | Wi-Fi 7 | 2.4, 5 and 6 GHz | 46 Gbps |

Newer devices work with older routers at the older speed (backward compatible).

## Short-range wireless (2.2)

| Technology | Range | Notes |
|---|---|---|
| Bluetooth | About 10 m (33 ft) for most devices | 2.4 GHz. Headsets, mice, keyboards. Devices must be **paired** |
| NFC (near-field communication) | About 4 cm | 13.56 MHz. Tap to pay, tap to pair. Needs touching distance |
| RFID (radio-frequency identification) | Varies | Tag plus reader. **Passive** tags have no battery (powered by the reader). **Active** tags have a battery and longer range. Door passes, stock tags, pet chips |

## IP addressing (2.6)

- **IPv4:** 32 bits, written as four numbers from 0 to 255, for example `192.168.1.25`. About 4.3 billion addresses in total, which ran short.
- **Private addresses** (never routed on the internet, used inside a SOHO network):
  - `10.0.0.0` to `10.255.255.255`
  - `172.16.0.0` to `172.31.255.255`
  - `192.168.0.0` to `192.168.255.255`
- **Public addresses:** everything else. Your internet provider gives one to your router.
- **IPv6:** 128 bits, eight groups of hex digits split by colons. Leading zeros can be dropped and one run of zero groups shortened to `::`, so `2001:0db8:0000:0000:0000:0000:0000:0001` becomes `2001:db8::1`.
- **Static:** typed in by hand, never changes. Good for printers, servers, the router itself.
- **Dynamic:** handed out by a DHCP server (usually the router). The normal choice. Core 1 Part 8, *How a Network Configures Itself*, covers DHCP in full.
- **APIPA** (Automatic Private IP Addressing): when a device asks for an address and gets no DHCP answer, it gives itself `169.254.x.x` (mask 255.255.0.0). It works on the local network only, so **no internet**. A 169.254 address means "check the DHCP server, the cable, or the Wi-Fi connection".
- **Subnet mask:** says which part of an address is the local network. Home default `255.255.255.0` means the first three numbers must match.
- **Default gateway:** the router's address on your network. Everything that is not local goes through it. Often `192.168.1.1` or `192.168.0.1`.

## Setting up a SOHO router (2.6, practical steps)

1. Plug the internet line (from the modem or ONT) into the router's **WAN** port.
2. Connect computers to the **LAN** ports, or to the Wi-Fi.
3. Log in to the router's settings page (address and default login are on the label).
4. **Change the default admin password.**
5. Set the **SSID** (network name) and a strong Wi-Fi password.
6. Keep **DHCP** on so devices get addresses automatically.
7. **Update the firmware.**
8. Test: can a device reach the internet?

Wi-Fi security settings and extra hardening are covered in Core 2 Part 7, *Security Measures, Wireless Security and Authentication*, and Core 2 Part 10, *Securing Mobile Devices, SOHO Networks and Browsers*.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Wi-Fi slow in the evening, 2.4 GHz, many neighbors | Move to 5 GHz or a clear channel (1, 6 or 11) |
| Address starts with 169.254, no internet | APIPA: no DHCP answer |
| Phone taps a reader to pay | NFC |
| Far corner of the house has weak signal | 2.4 GHz reaches further than 5 GHz, or add an access point |
| Newest devices, least interference | 6 GHz (Wi-Fi 6E or Wi-Fi 7) |
