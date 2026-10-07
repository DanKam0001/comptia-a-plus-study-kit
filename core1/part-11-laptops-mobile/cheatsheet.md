# Core 1, Part 11: Laptops and Mobile Devices: Hardware, Accessories, MDM

**Objectives 1.1, 1.2 and 1.3** (220-1201):
- 1.1 *Given a scenario, monitor mobile device hardware and use appropriate replacement techniques.*
- 1.2 *Compare and contrast accessories and connectivity options for mobile devices.*
- 1.3 *Given a scenario, configure basic mobile device network connectivity and provide application support.*

Domain: Mobile Devices (13% of the exam).

## 1.1 Hardware and replacement

| Part | What to know |
|---|---|
| Battery | Lithium-ion or lithium-polymer. Most common replacement. A swollen battery is dangerous: stop using it, unplug it, replace it and recycle the old one properly (Core 1 Part 14 covers the symptom) |
| Keyboard/keys | Usually clips in and connects by a thin ribbon cable. Some are riveted or built into the top case |
| RAM | **SODIMM** sticks. On many thin laptops the RAM is **soldered** and cannot be upgraded |
| HDD/SSD | 2.5-inch drive (7 mm or 9.5 mm thick) or an **M.2** stick |
| Wireless cards | Small card, usually M.2 (older: mini PCIe). Two antenna leads snap on |
| Wi-Fi antenna connector/placement | Usually two thin wires, often marked main and aux, routed through the hinge up into the screen bezel. **Forgetting to reconnect them gives a very weak signal** |
| Camera/webcam, microphone | Sit above the screen in the bezel. Cables run through the hinge |
| Physical privacy and security | **Biometrics** (fingerprint reader, facial recognition) and **near-field (NFC) scanner** for tapping a card or phone. Webcam shutter and mic switch are privacy features |

**Safe replacement habits:** shut down, unplug the charger, disconnect the battery, wear an ESD strap, photograph steps, keep screws in labelled piles (different screws are different lengths), use the maker's service manual, and recycle old batteries properly.

## 1.2 Accessories and connection methods

| Connection | Notes |
|---|---|
| USB | Standard A and B shapes. **miniUSB** and **microUSB** are older (5 pins, not reversible) |
| **USB-C** | Small, oval, reversible, 24 pins |
| **Lightning** | Apple's reversible connector, 8 pins. iPhone 15 and later use USB-C |
| **NFC** | Very short range (about 4 cm). Tap to pay or tap to pair |
| **Bluetooth** | About 10 m. Headsets, keyboards, speakers |
| **Tethering/hotspot** | One phone shares its internet with other devices over USB, Bluetooth or Wi-Fi |

| Accessory | What it does |
|---|---|
| Stylus | Pen for writing or drawing on a touch screen |
| Headsets, speakers, webcam | Audio and video in and out |
| Trackpad, drawing pad, track point | Pointing devices. A track point is the little stick between the G, H and B keys |
| **Docking station** | One connection to a laptop gives screen, keyboard, network and often charging. Can add extra ports and features. Often made for specific models |
| **Port replicator** | Simply duplicates the ports the laptop already has |

## 1.3 Network connectivity and app support

**Wireless/cellular data:** enable or disable cellular data, Wi-Fi, hotspot and airplane mode in settings. **3G, 4G and 5G** are generations of cellular data, each faster than the last. A **SIM** (Subscriber Identity Module) identifies the phone to the carrier. The common smallest size is nano-SIM (12.3 x 8.8 mm). An **eSIM** is built into the phone and set up by scanning a QR code or downloading a profile, so there is no card to swap.

**Bluetooth pairing, five steps:**
1. Enable Bluetooth.
2. Enable pairing (put the device in pairing or discoverable mode).
3. Find the device in the list.
4. Enter the PIN if asked.
5. Test connectivity.

If a device cannot be found, it is almost always not in pairing mode.

**Location services:** **GPS** uses satellites (most accurate, best outdoors). **Cellular location** uses nearby cell towers (less accurate, works indoors). Phones also use nearby Wi-Fi networks.

**Mobile device management (MDM):**
- Lets an organization manage many phones and tablets from one console (examples: Microsoft Intune, Jamf).
- **Device configurations:** *corporate* (company owns the device) or **BYOD** (bring your own device, often with a separate work profile so personal data stays private).
- **Policy enforcement:** require a passcode, require encryption, lock the screen after a time, remote lock, remote wipe.
- **Corporate applications:** install, update and remove company apps.

**Mobile device synchronization:** calendar, contacts, and business applications (mail, cloud storage). Syncing uses data, so **recognise data caps** on cellular plans and prefer Wi-Fi for large syncs. Backups and recovery on the Core 2 side are in Core 2 Part 14, *Documentation, Change Management, Backup and Recovery*; securing phones is in Core 2 Part 10, *Securing Mobile Devices, SOHO Networks and Browsers*.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Wi-Fi weak after the card was replaced | Antenna leads not reconnected |
| Company wants passcodes and remote wipe on all phones | MDM |
| Headset not in the Bluetooth list | Put it in pairing mode |
| One cable to give a laptop screen, keyboard, network and charging | Docking station |
| Phone has no data abroad but a spare data plan exists | Use a local SIM or add an eSIM plan |
| Staff use their own phones for work | BYOD |
