# Core 1, Part 15: Troubleshooting Networks

**Objective 5.5** (220-1201): *Given a scenario, troubleshoot network issues.*
Domain: Hardware and Network Troubleshooting (28% of the exam).

The exam gives you a symptom and asks for the **most likely cause** or the **best fix**. The objective names ten symptoms. Learn each with its cause and fix.

## A simple order of attack

1. **One device or everyone?** One device: check that device, its cable, its settings. Everyone: check the router, modem and internet provider.
2. **Work from the bottom up.** Cable plugged in and **link lights** on? Does the device have a proper IP address? Can it reach the router? Can it reach the internet?
3. Change **one thing at a time** and test again.

Commands such as `ping` and `ipconfig` help here. They are taught in Core 2 Part 3, The Windows Command Line, and Core 2 Part 4, Windows Networking on the Client. They are not listed in the 220-1201 objectives.

## The symptoms

| Symptom | Likely cause | Fix |
|---|---|---|
| **Intermittent wireless connectivity** | Distance, thick walls, too many devices, interference, weak or poorly placed access point | Move closer, add an access point, move the router central and high, use a Wi-Fi analyzer to find a better channel |
| **Slow network speeds** | Too many devices or heavy downloads, bad or damaged cable, old router, provider fault, wireless interference | Find and stop heavy use, replace the cable, update or replace the router, test wired against wireless |
| **Limited connectivity** | The device joined the network but got no address from DHCP, so it used an **APIPA** address (169.254.x.x) | Check the cable or Wi-Fi, renew the address, check the DHCP server or router, restart the router |
| **Jitter** | The delay between packets keeps changing, often from congestion or a poor connection | Reduce other traffic, use a wired connection, give real-time traffic priority (QoS) |
| **Poor VoIP quality** | Jitter, high latency or lost packets, often when other traffic competes with the call | Give voice traffic priority (**QoS**), use a wired connection, reduce other traffic |
| **Port flapping** | A switch port repeatedly goes up and down: bad or loose cable, failing network card or switch port, cable too long, speed or duplex mismatch | Replace the cable, try another port, test with a **cable tester**, check the run is no more than 100 m, check speed and duplex settings |
| **High latency** | A long delay before replies arrive: congestion, a distant server, a weak wireless link, a provider issue | Reduce traffic, use a wired connection, restart the modem and router, contact the provider |
| **External interference** | Microwave ovens, cordless phones, Bluetooth, neighboring Wi-Fi, metal and water weakening the signal | Change the Wi-Fi channel (on 2.4 GHz, channels 1, 6 and 11 do not overlap), use the 5 GHz band, move the router away |
| **Authentication failures** | Wrong password, security type mismatch (for example an old device and WPA3), expired or wrong account on a central server, wrong date and time | Re-enter the password, forget the network and rejoin, check the account, check the date and time. Never switch security off to get around it |
| **Intermittent internet connectivity** | Modem or router fault, loose cable, provider outage, overloaded network | Restart the modem and router, check cables, test wired, check provider status, contact the provider |

## Background you need

- **APIPA** (Automatic Private IP Addressing): the fallback address a Windows device gives itself when DHCP does not answer. It starts with **169.254**. It only works for talking to other APIPA devices on the same network, so there is no internet.
- **Latency** is the delay for a reply. **Jitter** is how much that delay varies. **Bandwidth** is how much data the link can carry.
- **Wi-Fi bands:** 2.4 GHz reaches further but is slower and crowded. 5 GHz is faster but passes through walls less well. 6 GHz is also listed in the objectives.
- **Twisted pair Ethernet** maximum run: **100 m** (328 ft).
- **Tools named in objective 2.8 that help here:** Wi-Fi analyzer (signal and channels), cable tester (wiring faults), loopback plug (tests a network port), toner probe (find a cable).

## Notes on what the objectives do not name

The objectives list the symptoms but not the fixes. The fixes above are the standard technician answers. **QoS** is not named in the 220-1201 objectives but is the usual cure for poor VoIP quality.
