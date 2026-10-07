# Lab: See ports and protocols on your own PC (Windows)

**Time:** 15 minutes. **Needs:** a Windows PC with internet. Everything here is read-only.

Goal: watch real connections and see which ports they use.

## 1. List your live connections

Open PowerShell and run:

```powershell
Get-NetTCPConnection -State Established | Select-Object LocalPort, RemoteAddress, RemotePort | Sort-Object RemotePort | Format-Table
```

Look at the **RemotePort** column. Which numbers do you recognise from the list? Open a browser first if you see nothing: **443** (HTTPS) should appear.

## 2. Link a port to a program

```powershell
Get-NetTCPConnection -State Established | Where-Object RemotePort -eq 443 | Select-Object -First 5 OwningProcess | ForEach-Object { Get-Process -Id $_.OwningProcess | Select-Object Name }
```

You'll see the programs using port 443.

## 3. See UDP ports that are listening

```powershell
Get-NetUDPEndpoint | Select-Object LocalPort, OwningProcess | Sort-Object LocalPort | Select-Object -First 20
```

Look for **53** (DNS), **67** or **68** (DHCP), and **137** or **138** (NetBIOS). Not all will appear on every PC.

## 4. Test whether a port is open

```powershell
Test-NetConnection -ComputerName example.com -Port 443
Test-NetConnection -ComputerName example.com -Port 23
```

`TcpTestSucceeded : True` for 443 and `False` for 23 shows the idea of a firewall allowing one port and not another.

## 5. Check the Windows Firewall rule for Remote Desktop (read only)

```powershell
Get-NetFirewallRule -DisplayName "Remote Desktop*" | Select-Object DisplayName, Enabled, Direction
```

Remote Desktop uses port 3389. Is the rule enabled on your PC? (Don't enable it just for this lab.)

## 6. Write it up

Make a table of every port you saw, its protocol name, and whether it's TCP or UDP.

## Check yourself

- Which port and protocol replace Telnet when you want encryption?
- Which email protocol would you choose for a phone and a laptop to stay in sync?
- Why does live video usually use UDP?

## Going further (optional)

Install Wireshark (free), capture for ten seconds while loading a web page, and filter by `dns`, `tcp.port == 443` and `udp`. Only capture on your own network.
