# Memorise list: Troubleshooting Motherboards, RAM, CPU, Power, Drives and RAID (Core 1, Part 13)

Understand the video first, then learn these cold.
Flashcards: [`flashcards/core1_part13.csv`](../../flashcards/core1_part13.csv) (import into Anki or any flashcard app).

## Motherboard, RAM, CPU, power

| Question | Answer |
|---|---|
| POST stands for | Power-on self-test |
| Beep pattern at startup: what to do | Look up the maker's beep code in the motherboard manual |
| Windows crash screen | Blue screen of death (BSOD) |
| macOS freeze indicator | Spinning wheel (pinwheel) |
| Why is a crash screen called proprietary? | Each system has its own |
| Burning smell: first action | Power off and unplug at once |
| Swollen capacitor: fix | Replace the board or power supply |
| Date and time keep resetting | Flat CMOS battery |
| Motherboard battery type | Usually CR2032, 3 V coin cell |
| Overheating causes | Dust, failed fan, old thermal paste, poor airflow |
| Overheating fixes | Compressed air, replace fan, new thermal paste |
| Tools for testing a power supply | Power supply tester, multimeter |
| Blank screen, fans spinning: first checks | Monitor cable and input, reseat RAM and graphics card |
| No power at all: first checks | Outlet, cable, PSU switch, PSU test, front-panel header |
| Application crashes often point to | Bad RAM, overheating or a failing drive |

## Drives and RAID

| Question | Answer |
|---|---|
| Grinding or clicking from a hard drive | Failing: back up now, replace |
| S.M.A.R.T. stands for | Self-Monitoring, Analysis and Reporting Technology |
| S.M.A.R.T. failure warning means | Drive predicts it will fail. Back up and replace |
| IOPS stands for | Input/Output Operations Per Second |
| Bootable device not found: checks | Boot order, cables, drive detected in firmware |
| Drive missing in the OS but seen in firmware | Initialize it, assign a drive letter, check cables |
| Degraded array means | Working but a drive has failed, no protection left |
| Fix for a degraded RAID 5 | Replace the failed drive and let it rebuild |
| Array missing: first checks | Cables and RAID controller |
| RAID 0 survives how many failures? | None |
| RAID 1 / 5 / 6 survive | 1 / 1 / 2 drive failures |
| Minimum drives: RAID 0, 1, 5, 6, 10 | 2, 2, 3, 4, 4 |
| Is RAID a backup? | No |
| Amber or red drive LED usually means | Failed or failing drive |
