# Core 2, Part 16: Scripting, Remote Access and AI

**Objectives 4.8, 4.9 and 4.10** (220-1202):
- 4.8 *Explain the basics of scripting.*
- 4.9 *Given a scenario, use remote access technologies.*
- 4.10 *Explain basic concepts related to artificial intelligence (AI).*

Domain: Operational Procedures (21% of the exam).

## 4.8 Scripting basics

A **script** is a text file of commands that run in order, so repeat jobs happen automatically.

### Script file types

| Extension | What it is | Where |
|---|---|---|
| `.bat` | Batch file | Windows |
| `.ps1` | PowerShell script | Windows (also available elsewhere) |
| `.vbs` | VBScript | Windows (older) |
| `.sh` | Shell script | Linux and macOS |
| `.js` | JavaScript | Browsers, and on servers |
| `.py` | Python | Any system with Python installed |

### Use cases for scripting

- Basic automation
- Restarting machines
- Remapping network drives
- Installation of applications
- Automated backups
- Gathering of information and data
- Initiating updates

### Other considerations when using scripts

- **Unintentionally introducing malware** (a script from an untrusted source)
- **Inadvertently changing system settings**
- **Browser or system crashes due to mishandling of resources**
- Habit: read it before you run it, run it on one machine first, and only use trusted sources.

## 4.9 Remote access technologies

| Method | What it is | Notes |
|---|---|---|
| **RDP** (Remote Desktop Protocol) | Full Windows desktop over the network | Port 3389. Needs a Windows edition that can host it (see Core 2 Part 1). Do not expose it directly to the internet |
| **VPN** (virtual private network) | Encrypted tunnel into a network | Makes a remote device act as if it is on the local network |
| **VNC** (virtual network computing) | Graphical screen sharing across many system types | Port 5900. Not encrypted by default, so tunnel it |
| **SSH** (Secure Shell) | Encrypted command line | Port 22. Also used for secure file copying |
| **RMM** (remote monitoring and management) | Software to watch and fix many computers from one console | Used by IT support companies |
| **SPICE** (Simple Protocol for Independent Computing Environments) | Remote display protocol for virtual machines | |
| **WinRM** (Windows Remote Management) | Run commands and scripts on remote Windows computers | Ports 5985 (HTTP) and 5986 (HTTPS) |
| **Third-party tools** | Screen-sharing software, videoconferencing software, file transfer software, desktop management software | Use reputable vendors |

### Security considerations

- Get the user's permission, and end the session when finished.
- Strong passwords and multi-factor authentication.
- Keep remote software updated.
- Use encryption (VPN, SSH). Put RDP behind a VPN.
- Screen sharing shows everything on screen, including private messages.
- Third-party tools mean trusting another company with access.

## 4.10 Artificial intelligence (AI)

- **Application integration:** AI built into everyday apps.
- **Policy**
  - **Appropriate use:** use it only for approved work and purposes.
  - **Plagiarism:** passing off AI-written (or anyone's) work as your own.
- **Limitations**
  - **Bias:** unfair leanings from the training data.
  - **Hallucinations:** confident answers that are made up.
  - **Accuracy:** it can be plain wrong, so check it.
- **Private vs public**
  - **Data security:** who can get at the data.
  - **Data source:** where the AI's knowledge came from.
  - **Data privacy:** where your input goes and who can see it.
  - Public AI sits outside your control. Private AI runs inside the company.

## Common scenarios

| Scenario | Answer |
|---|---|
| Same change on 200 PCs | Script it (`.bat` or `.ps1`) |
| Secure command line on a remote Linux server | SSH |
| Remote Windows desktop | RDP (behind a VPN) |
| Support company manages hundreds of client PCs | RMM |
| Script from a forum changed settings unexpectedly | Risk of running untrusted scripts |
| Staff pasting customer data into a public chatbot | Data privacy and security risk. Use an approved private AI, or don't |
| AI cites a source that doesn't exist | Hallucination |
