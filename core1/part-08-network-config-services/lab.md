# Lab: Look at DHCP and DNS on your own PC (Windows)

**Time:** 15 minutes. **Needs:** a Windows PC on a home network. Everything is read-only.

Goal: see a lease, a DNS lookup and a DNS record for yourself.

## 1. Read your DHCP lease

Open PowerShell and run:

```powershell
ipconfig /all
```

Under your active adapter find:

- **DHCP Enabled** (Yes means your address is dynamic)
- **IPv4 Address**
- **Physical Address** (that's your MAC address, the thing a reservation is tied to)
- **DHCP Server** (usually your router)
- **Lease Obtained** and **Lease Expires**
- **DNS Servers**

## 2. Look up DNS records

```powershell
nslookup example.com
nslookup -type=AAAA example.com
nslookup -type=MX gmail.com
nslookup -type=TXT gmail.com
```

Which record type gave an IPv4 address, which gave an IPv6 address, and which named mail servers? In the TXT results, look for a line starting `v=spf1`. That's an **SPF** record.

## 3. See a CNAME

```powershell
nslookup -type=CNAME www.github.com
```

If it returns an alias, that's a CNAME. (Some names have none.)

## 4. Your router's DHCP settings (optional)

Open your router's admin page (the **Default Gateway** from step 1, in a browser). Look for **DHCP**: the scope or address range, the lease time, and any reservation list. Don't change anything.

## 5. Write it up

```
My IPv4 address and MAC:
DHCP server:
Lease expires:
DNS server:
Domain I checked: A / AAAA / MX / TXT results
```

## Check yourself

- Which DHCP feature would you use to make a printer keep one address?
- Which record type holds an SPF policy?
- What does a VPN protect you from on a cafe's Wi-Fi?

## Going further (optional)

Run `ipconfig /release` then `ipconfig /renew` on a spare PC and watch the lease times change. Don't do this on a PC you are connected to remotely, because you'll lose the connection.
