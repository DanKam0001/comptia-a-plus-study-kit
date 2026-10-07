# Lab: Explore Windows networking on your own PC

**Time:** 20 to 25 minutes. **Needs:** a Windows 10 or 11 PC on a home network. Steps are look-only unless a step says "optional". Write down any setting before you change it, and change it back afterwards.

## 1. Read your four client settings

Open Command Prompt and run `ipconfig /all`. Write down:

```
IPv4 address:
Subnet mask:
Default gateway:
DNS server(s):
DHCP Enabled: (Yes = dynamic, No = static)
```

Then find the same numbers in **Settings, Network and Internet, Wi-Fi (or Ethernet), your network, Properties**. Does **IP assignment** say Automatic (DHCP) or Manual?

## 2. See the adapter dialog

Press **Windows key + R**, type `ncpa.cpl`, Enter. Right click your adapter, **Properties**, double click **Internet Protocol Version 4 (TCP/IPv4)**. Note whether "Obtain an IP address automatically" is selected. **Cancel** without changing anything.

## 3. Public or private?

In **Settings, Network and Internet, Wi-Fi (or Ethernet), your network**, find **Network profile type**. Which is selected? Why is that the right choice for your home? Which would you pick at a cafe?

## 4. Metered connection and proxy

On the same screen find the **Metered connection** switch (look only). Then open **Settings, Network and Internet, Proxy** and note whether "Automatically detect settings" is on.

## 5. Firewall

Open **Control Panel, Windows Defender Firewall, Allow an app or feature through Windows Defender Firewall**. Find three apps and see which networks (Private, Public) each is allowed on. Then click **Advanced settings** and look at **Inbound Rules** and **Outbound Rules**. Close without changing anything.

## 6. Shares and mapped drives

1. In File Explorer, click **This PC** and look at the drives and network locations.
2. Type `\\localhost\C$` in the address bar. You'll be asked for administrator credentials (it's the hidden administrative share). Cancel unless you want to see it.
3. If you have a NAS, a second PC with a shared folder, or a router with a USB drive, **Map network drive**, pick Z:, tick Reconnect at sign-in, and open it. Disconnect afterwards with `net use Z: /delete`.

## 7. Domain or workgroup?

Open **Settings, System, About**, then **Domain or workgroup** (or run `sysdm.cpl`, Computer Name). Is your PC in a workgroup (probably `WORKGROUP`) or a domain? If you are on Windows Home, note why joining a domain isn't offered.

## 8. VPN (optional)

If you have a free VPN account (or a work one), open **Settings, Network and Internet, VPN, Add VPN** and see the fields it asks for: provider, connection name, server address, sign in info. You don't need to connect.

## Write it up

```
IP / mask / gateway / DNS:
Dynamic or static:
Network profile:
Domain or workgroup:
Apps allowed through the firewall (three):
```

## Check yourself

- A laptop at a cafe is sharing files. Which setting should change? (Network profile to Public)
- What is the difference between a static and a dynamic address? (typed by hand vs given by DHCP)
- What does a domain give a company that a workgroup doesn't? (One central sign in and central settings)
- What does a VPN do? (Builds an encrypted tunnel to another network)

## Going further (optional)

In Windows Defender Firewall's Advanced settings, create an **outbound** rule that blocks a harmless test program, confirm it can't connect, then delete the rule.
