# Lab: Look at your own Wi-Fi and IP settings (Windows)

**Time:** 15 minutes. **Needs:** a Windows PC on Wi-Fi or Ethernet. Everything here is read-only. You won't change any setting.

## 1. Read your IP settings

Open PowerShell (Start menu, type `powershell`) and run:

```powershell
ipconfig /all
```

Find your active adapter and write down:
- **IPv4 Address.** Is it private? Which of the three private ranges?
- **Subnet Mask.** Probably 255.255.255.0.
- **Default Gateway.** That is your router.
- **DHCP Enabled.** Yes means dynamic. Note the **DHCP Server**, usually the same as the gateway.
- Do you also have an **IPv6 Address**? Does it start with `fe80`? That is a local-only address.

## 2. Find your public address

Open a browser and search "what is my IP". Compare it with the address from step 1. They should be different: one is private, one is public.

## 3. See your Wi-Fi band, channel and standard

```powershell
netsh wlan show interfaces
```

Look at **Radio type** (for example 802.11ac or 802.11ax), **Band**, **Channel** and **Receive/Transmit rate**.
- Which standard and friendly name (Wi-Fi 5, Wi-Fi 6) is your link using?
- Is it on 2.4 or 5 GHz?

## 4. See the neighbors

```powershell
netsh wlan show networks mode=bssid
```

Count how many networks share your channel. On 2.4 GHz, how many use channels 1, 6 and 11 compared with others?

## 5. Log in to your router (look only)

The gateway address from step 1 is the router's settings page. Type it into a browser. Do **not** change anything. Find: the SSID, the Wi-Fi channel setting, whether DHCP is on, and the firmware version.

## 6. Write it up

```
My IP / mask / gateway:
Private or public?
DHCP on?
Wi-Fi standard and band:
Channel and how crowded it is:
```

## Check yourself

- Your PC shows 169.254.x.x. What happened and where do you look first?
- Your Wi-Fi is slow in the evening on 2.4 GHz. What two changes might help?
- Which wireless technology only works at a few centimetres?

## Going further (optional)

Install a free Wi-Fi analyzer app on a phone and walk around the house. Compare signal strength on 2.4 GHz and 5 GHz in the same room.
