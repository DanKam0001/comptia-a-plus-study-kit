# Core 1, Part 9: Network Hardware, Connection Types and Tools

**Objectives 2.5** (compare and contrast common networking hardware devices), **2.7** (compare and contrast internet connection types, network types, and their characteristics) and **2.8** (explain networking tools and their purposes) (220-1201).
Domain: Networking (23% of the exam). The cables and connectors themselves are in Part 4 (objective 3.2).

## Networking hardware (2.5)

| Device | What it does |
|---|---|
| Router | Joins different networks and directs traffic. Home router joins the home network to the internet. Often also includes a switch and access point |
| Switch | Connects devices inside one network and forwards data by **MAC address** |
| Unmanaged switch | Plug and play, no settings |
| Managed switch | Log in and configure: VLANs, port settings, monitoring |
| Access point (AP) | Lets wireless devices join the wired network |
| Patch panel | Board of ports in a rack. Wall cables end at the back (punched down), short patch cables link the front to the switch |
| Firewall | Allows or blocks traffic by rules. A dedicated box or software in a router |
| Cable modem | Internet over the **coaxial** cable TV network |
| DSL | Digital Subscriber Line: internet over a telephone line (RJ11) |
| ONT (Optical Network Terminal) | Where **fiber** enters the building: converts light to Ethernet |
| NIC (Network Interface Card) | Wired port or Wi-Fi chip that connects a computer to the network |
| MAC address | Media Access Control address, the physical address burned into a NIC. 48 bits, written as 12 hex characters (example 00:1A:2B:3C:4D:5E). First half = maker, second half = unique number |

## Power over Ethernet (PoE)

Power and data on one network cable. Good for access points, cameras and VoIP phones.

| Way to supply | Meaning |
|---|---|
| PoE switch | Power sourcing built into the switch |
| PoE injector | Small box added between a normal switch and the device |

| Standard | Name | Power (from the switch port) |
|---|---|---|
| 802.3af | PoE (Type 1) | up to 15.4 W |
| 802.3at | PoE+ (Type 2) | up to 30 W |
| 802.3bt | Type 3 | up to 60 W |
| 802.3bt | Type 4 | up to 90 W (a little more at the source) |

The device receives slightly less than the switch sends, because some power is lost in the cable.

## Internet connection types (2.7)

| Type | Notes |
|---|---|
| Fiber | Glass cable and light, usually the fastest. Ends at an ONT |
| Cable | Coax and a cable modem. Common and fast, bandwidth shared with neighbors |
| DSL | Telephone line. Speed drops the farther you are from the provider's equipment |
| Satellite | Reaches remote areas. High latency (delay) because of distance |
| Cellular | Mobile network (4G, 5G). Handy, may have data caps |
| WISP | Wireless Internet Service Provider: radio link from a local tower to a rooftop antenna. Needs a clear line of sight |

## Network types (2.7)

| Type | Meaning |
|---|---|
| PAN | Personal Area Network: your own devices within a few meters (Bluetooth) |
| LAN | Local Area Network: one home or building |
| WLAN | Wireless LAN |
| MAN | Metropolitan Area Network: a city |
| WAN | Wide Area Network: large areas, the internet is the biggest |
| SAN | Storage Area Network: a fast network linking servers to shared storage |

## Networking tools (2.8)

| Tool | What it does |
|---|---|
| Crimper | Attaches an RJ45 (or RJ11) connector to a cable end |
| Cable stripper | Removes the outer jacket without cutting the wires |
| Punchdown tool | Seats wires into a punchdown block or the back of a patch panel and trims the excess |
| Toner probe | A tone generator at one end, a probe traces the cable and beeps. Finds an unlabelled cable |
| Cable tester | Checks every wire is connected correctly (continuity, miswires) |
| Loopback plug | Sends the signal back into a port to test the port itself |
| Network tap | Copies traffic so it can be inspected without interrupting |
| Wi-Fi analyzer | Shows nearby networks, channels and signal strength |

## Common scenarios

| Scenario | Answer |
|---|---|
| Access point on a ceiling with no power socket | PoE (PoE switch or injector) |
| Find which cable in a bundle goes to a room | Toner probe |
| Check a freshly made cable | Cable tester |
| Test whether a NIC or port is faulty | Loopback plug |
| Attach an RJ45 plug | Crimper |
| Terminate wires on a patch panel | Punchdown tool |
| Box on the wall where fiber ends | ONT |
| Internet in a remote area with no cable | Satellite, cellular or WISP |
| Choose the best channel for Wi-Fi | Wi-Fi analyzer |
| Inspect traffic without breaking the link | Network tap |
