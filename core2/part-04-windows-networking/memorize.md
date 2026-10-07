# Memorise list: Windows Networking on the Client (Core 2, Part 4)

Understand the video first, then learn these cold. They're the facts a scenario question assumes you already know.
Flashcards: [`flashcards/core2_part04.csv`](../../flashcards/core2_part04.csv) (import into Anki or any flashcard app).

## Domain and workgroup

| Question | Answer |
|---|---|
| Who keeps the accounts in a workgroup | Each computer, separately |
| Who keeps the accounts in a domain | A central server (domain controller, Active Directory) |
| Which edition cannot join a domain | Windows Home |
| How settings reach domain PCs | Group Policy |
| Default workgroup name | WORKGROUP |

## Shares

| Question | Answer |
|---|---|
| Network path format | `\\server\share` |
| Map a network drive: where | File Explorer, This PC, Map network drive |
| Keep the mapped drive after a restart | Tick "Reconnect at sign-in" |
| Map a drive from the command line | `net use Z: \\server\share` |

## Firewall

| Question | Answer |
|---|---|
| Default inbound / outbound behaviour | Inbound blocked unless allowed. Outbound allowed |
| Let one app through | Allow an app or feature through Windows Defender Firewall |
| Where to make rules for a program or port | Advanced settings (wf.msc): inbound and outbound rules |
| The three firewall profiles | Domain, Private, Public |

## IP settings

| Question | Answer |
|---|---|
| The four client settings | IP address, subnet mask, default gateway, DNS server |
| Dynamic means | A DHCP server assigns them automatically |
| Static means | Typed in by hand |
| What needs a static address | Printers, servers |
| Open adapter IPv4 settings | Network and Sharing Center, Change adapter settings, Properties, Internet Protocol Version 4 |

## Connections, proxy, profiles

| Question | Answer |
|---|---|
| WWAN stands for | Wireless Wide Area Network (cellular, SIM or eSIM) |
| The four connection types on the objectives | VPN, wireless, wired, WWAN/cellular |
| VPN is | An encrypted tunnel to another network |
| Proxy is | A middleman server that web traffic passes through |
| Proxy options in Windows | Automatically detect, setup script, manual (address and port) |
| Private vs public network | Private: trusted, sharing allowed, discoverable. Public: untrusted, hidden, sharing blocked |
| Which to choose at a coffee shop | Public |
| Metered connection does | Limits background data such as large updates |
