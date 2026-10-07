# Lab: Inspect your own network hardware (Windows)

**Time:** 15 minutes. **Needs:** a Windows PC on a home network. Everything is read-only.

Goal: find the devices and addresses from Part 9 on your own network.

## 1. Find your NIC and MAC address

Open PowerShell and run:

```powershell
Get-NetAdapter | Select-Object Name, InterfaceDescription, MacAddress, LinkSpeed, Status
```

- Which adapters are wired (Ethernet) and which are Wi-Fi?
- Write down the **MacAddress**. The first six characters identify the maker. Search them online ("MAC address lookup") to see which company it is.

## 2. Find your router (default gateway)

```powershell
ipconfig | findstr /i "Gateway"
```

That address is your router. Type it into a browser to see its admin page (don't change anything). Does it also act as a switch and an access point?

## 3. See other devices on your network

```powershell
arp -a
```

This table pairs IP addresses with **MAC addresses**, which is how a switch forwards data on a LAN.

## 4. Work out your connection type

Look at the box your internet comes from (or your provider's website):

- Coaxial cable and a cable modem?
- A telephone socket and a DSL modem?
- A small box where a fiber line enters (an ONT)?
- A mobile or satellite service?

## 5. Check your Wi-Fi channel (optional)

```powershell
netsh wlan show interfaces
```

Find **Channel**, **Radio type** and **Signal**. A Wi-Fi analyzer app would show all nearby networks. Many free ones exist.

## 6. Write it up

```
NIC (wired / Wi-Fi) and MAC:
Router (default gateway):
Is the router also a switch and AP?
Connection type:
Wi-Fi channel and signal:
Network type (PAN / LAN / WLAN / MAN / WAN) of each thing I saw:
```

## Check yourself

- What would you use to power an access point that has no nearby power socket?
- Which tool finds one cable in a bundle?
- What does an ONT do?

## Going further (optional)

If you have a spare cable and a crimper, practise making a patch cable (see Part 4 for T568A and T568B colors), then check it with a cable tester.
