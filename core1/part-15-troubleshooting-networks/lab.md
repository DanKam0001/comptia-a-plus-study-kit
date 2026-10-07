# Lab: Look at your own network like a technician (Windows, free)

**Time:** 15 minutes. **Needs:** a Windows PC on your home network. Every step only reads information. Nothing here changes a setting.

Goal: find the pieces Part 15 talks about, on a real network.

## 1. Is it one device or everyone?

Pick up a phone on the same Wi-Fi and open any website. Then do the same on the PC. This is the first question for any problem: does the fault follow one device, or all of them?

## 2. Check the address (look for APIPA)

Open PowerShell (Start menu, type `powershell`) and run:

```powershell
ipconfig
```

Find your **IPv4 Address**. Write it down.

- A normal home address starts with 192.168 or 10.
- An address starting with **169.254** is the APIPA fallback. You will only see it if DHCP is not answering.

## 3. Check you can reach the router, then the internet

```powershell
ping 192.168.1.1
ping 8.8.8.8
```

Replace the first address with your **Default Gateway** from `ipconfig`. The first test reaches the router, the second reaches the internet. If the first works and the second does not, the problem is past your router (modem or provider).

Look at the `time=` numbers. That is **latency**, in milliseconds. Run the test a few times. If the numbers jump around a lot, that is **jitter**.

## 4. Look at your Wi-Fi signal

```powershell
netsh wlan show interfaces
```

Find **Signal** (a percentage), **Radio type**, **Channel** and **Band**. Move to another room and run it again. Does the signal drop? Which band are you on, 2.4 GHz or 5 GHz?

To see nearby networks and their channels:

```powershell
netsh wlan show networks mode=bssid
```

Count how many networks use the same channel as yours. Crowded channels cause interference.

## 5. Look at the link light (wired only)

If your PC has an Ethernet cable, find the small light beside the port. Note its color and whether it blinks. A light that blinks on and off repeatedly with no activity is the sign of a bad cable or port.

## 6. Write it up

```
IPv4 address (APIPA or normal):
Default gateway:
Ping to router (ms):  Ping to internet (ms):
Wi-Fi signal / band / channel:
Networks on the same channel:
```

## Check yourself

- If `ipconfig` showed 169.254.x.x, what would you check first?
- Your calls break up but web pages are fine. Which word describes the problem?
- Everyone in the house is offline. Where do you look first?

## Going further (optional)

Install a free Wi-Fi analyzer app on your phone and walk around the house. Note where the signal is weakest. Move your router, and compare.
