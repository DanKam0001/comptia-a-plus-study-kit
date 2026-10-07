# Core 2, Part 4: Windows Networking on the Client

**Objective 1.7** (220-1202): *Given a scenario, configure Microsoft Windows networking features on a client/desktop.*
Domain: Operating Systems (28% of the exam).

Core 1 covers the network hardware and protocols (Core 1 Part 8, *How a Network Configures Itself*, explains DHCP, DNS and VPNs in depth). This part is only about settings on the Windows computer.

## Domain joined vs workgroup

| | Workgroup | Domain |
|---|---|---|
| Who keeps the accounts | Each computer, on its own | A central server (domain controller running **Active Directory**) |
| Sign in | A separate account on every PC | One account works on every PC in the domain |
| Settings | Set on each PC | Pushed from the server by **Group Policy** |
| Size | A few home or small office PCs | Companies, schools, any large office |
| Editions | All | **Not Windows Home** (Pro and above can join) |

Join a domain: Settings, Accounts, Access work or school, Connect; or System Properties, Computer Name, Change. Default workgroup name is `WORKGROUP`.

## Shared resources

| Resource | What to know |
|---|---|
| File server | A computer holding shared folders many people use |
| Shared printer | One printer many computers use. Add it from Devices and Printers or Settings, Devices, Printers |
| Network path (UNC) | `\\server\share`, for example `\\FILESERVER\Accounts`. Type it in the File Explorer address bar |
| Mapped drive | A share given a drive letter. File Explorer, This PC, Map network drive. Pick a letter (such as Z:), type the path, tick **Reconnect at sign-in** |
| Command line | `net use Z: \\server\share` (`/delete` to remove) |

## Local OS firewall (Windows Defender Firewall)

- Watches traffic in and out. **Default: inbound blocked unless allowed, outbound allowed.**
- **Application restrictions and exceptions:** Control Panel, Windows Defender Firewall, *Allow an app or feature through Windows Defender Firewall*, then tick the app for Private and/or Public networks.
- **Configuration:** *Advanced settings* (`wf.msc`) holds **inbound rules** and **outbound rules**. A rule can allow or block by program, by **port number**, or by protocol.
- Three profiles: **Domain, Private, Public**. Each can have different settings.
- Don't turn the firewall off just to make something work. Add an exception.

## Client network configuration

| Setting | Meaning (everyday version) |
|---|---|
| IP address | The computer's own address (house number) |
| Subnet mask | Which addresses are on the same local network (the street) |
| Default gateway | The router, the exit from the local network |
| DNS server | Turns names into IP addresses (the phone book) |

- **Dynamic** = a DHCP server hands out the settings automatically (Obtain an IP address automatically). The normal choice.
- **Static** = typed in by hand. Used for printers, servers and anything that must keep one address.
- Example only: IP 192.168.1.50, mask 255.255.255.0, gateway 192.168.1.1, DNS 8.8.8.8.
- Where: Settings, Network and Internet, Wi-Fi or Ethernet, **IP assignment**, Edit (Automatic (DHCP) or Manual); or Network and Sharing Center, Change adapter settings, right click the adapter, Properties, Internet Protocol Version 4 (TCP/IPv4).

## Establish network connections

| Connection | Notes |
|---|---|
| Wired | Ethernet cable (RJ45) to a router or wall port |
| Wireless | Wi-Fi. Pick the network, enter the password |
| WWAN / cellular | Wireless wide area network. A cellular connection using a SIM or eSIM, in a laptop with a cellular modem |
| VPN | Secure encrypted tunnel to another network. Settings, Network and Internet, VPN, Add VPN (provider, connection name, server address, sign-in info) |

## Proxy settings

A **proxy** is a middleman server that web traffic passes through, often to filter or log it. Settings, Network and Internet, **Proxy**: *Automatically detect settings*, *Use setup script*, or *Manual proxy* (address and port). Also in Internet Options, Connections, LAN settings. A site that fails only on a work network may be a proxy problem.

## Public network vs private network

| | Private | Public |
|---|---|---|
| Use at | Home, trusted workplace | Coffee shop, airport, hotel |
| Other PCs can see yours | Yes (network discovery on) | No (hidden) |
| File and printer sharing | Allowed | Blocked |

Change it: Settings, Network and Internet, Wi-Fi (or Ethernet), the network's properties, **Network profile type**. When unsure, choose Public.

## Metered connections

Tells Windows the connection has limited data (a phone hotspot, cellular). Windows holds back large background downloads such as some updates. Settings, Network and Internet, Wi-Fi, the network's properties, **Metered connection**, On. Limitation: updates and some apps wait until you switch to an unmetered network.

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Home user must reach company files securely | VPN |
| Laptop at coffee shop is sharing files | Set the network profile to Public |
| 50 PCs, one sign in, central settings | Join a domain |
| Daily share should appear as a drive letter | Map a network drive |
| A program can't be reached from outside | Add a Windows Defender Firewall exception |
| Printer must keep the same address | Static IP |
| Website fails only at work | Check proxy settings |
| Phone hotspot is eating data on updates | Turn on metered connection |
