# Memorise list: Troubleshooting Windows (Core 2, Part 12)

Understand the video first, then learn these cold. They're the facts a scenario question assumes you already know.
Flashcards: [`flashcards/core2_part12.csv`](../../flashcards/core2_part12.csv) (import into Anki or any flashcard app).

| Question | Answer |
|---|---|
| BSOD stands for | Blue Screen of Death |
| First thing to note on a BSOD | The stop code |
| BSOD right after a driver update | Safe mode, roll back the driver |
| Where are crash dump files saved? | C:\Windows\Minidump |
| Safe mode loads | Only the basic drivers |
| Windows opens its recovery environment | Automatically after failed starts |
| Three bootrec switches | /fixmbr, /fixboot, /rebuildbcd |
| Command that repairs system files | `sfc /scannow` |
| "Operating system not found" first checks | USB/disc removed, boot order, drive detected |
| Causes of frequent shutdowns | Overheating, failing power supply, bad RAM |
| Tool to see what's using CPU, memory, disk | Task Manager |
| Tool to read the errors log | Event Viewer (`eventvwr.msc`) |
| Tool to manage services | `services.msc` |
| Why a service fails to start | A dependency isn't running, wrong startup type or account |
| Low memory fix | Close programs, restart, add RAM |
| USB controller resource warning fix | Fewer devices, powered hub, update drivers |
| Slow profile load causes | Large or corrupt profile, slow network profile server |
| Time resets every time PC is unplugged | Dead CMOS battery |
| Domain sign-in clock tolerance (Kerberos) | Within 5 minutes by default |
| Command to resync the clock | `w32tm /resync` |
