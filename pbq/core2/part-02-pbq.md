# Core 2, Part 2: Performance-Based Questions

**Part:** Windows Tools: Task Manager, MMC Snap-ins, Settings (objectives 1.4, 1.6)
**Answers:** [part-02-pbq-answers.md](part-02-pbq-answers.md). Do not open it until you have finished both tasks.

The real 220-1202 exam has performance-based questions (PBQs). This kit cannot run a simulator, so each task is done on paper or in a text file. Try it before you look at the cheatsheet. You earn credit for each correct part, so never leave a row blank.

---

## C2P02-PBQ1: Which tool do I open?

| | |
|---|---|
| **Objectives** | 1.4 |
| **Type** | Matching |
| **Time guide** | 5 minutes |

**Scenario.** You are on the help desk. Eight users call with eight different problems. For each one you will press **Windows key + R** (the Run box) and type the file name of the right Windows tool.

**Task.** Match each problem (1 to 8) to **one** file name (A to I). Each file name is used **at most once**, and one is not needed.

**Materials: file names**

| Letter | Type this in the Run box |
|---|---|
| A | `eventvwr.msc` |
| B | `diskmgmt.msc` |
| C | `taskschd.msc` |
| D | `devmgmt.msc` |
| E | `msinfo32.exe` |
| F | `resmon.exe` |
| G | `perfmon.msc` |
| H | `msconfig.exe` |
| I | `regedit.exe` |

**Problems**

1. You want a detailed live view of which process is using the disk right now.
2. A script must run automatically every night.
3. You need to control how Windows starts, including the safe boot option.
4. A program keeps crashing and you want to read the error that Windows recorded about it.
5. A device shows a yellow warning triangle and you want to update or roll back its driver.
6. You want to record detailed CPU, memory and disk counters over a period of time.
7. A brand-new drive does not show up in File Explorer. You need to initialize it and create a volume.
8. You need a full report that shows whether Secure Boot is on and which BIOS mode the PC uses.

**Marking.** 8 points: 1 point per correct match.

---

## C2P02-PBQ2: Set up a laptop's power options

| | |
|---|---|
| **Objectives** | 1.6 |
| **Type** | Configure this form |
| **Time guide** | 6 minutes |

**Scenario.** A teacher's laptop is set up in Control Panel under **Power Options**. Below is a text version of the settings screen. Each row describes what the teacher wants. Choose **one option** for each row.

**Materials**

Lid and power-state choices (rows 1 to 3): **Do nothing**, **Sleep**, **Hibernate**, **Shut down**.

| Row | What the teacher wants | Setting | Your choice |
|---|---|---|---|
| 1 | With the laptop plugged in at the desk and an external monitor attached, closing the lid must keep it running. | When I close the lid (plugged in) | |
| 2 | With the laptop on battery and put in a bag, closing the lid must save the work to the drive and then use no power at all. | When I close the lid (on battery) | |
| 3 | When stepping away for ten minutes, the laptop must wake in seconds, with the work kept in RAM and only a little power used. | Power state to use | |
| 4 | A wireless USB mouse keeps "disappearing" after it has been idle. Windows is switching off idle USB ports to save energy. | USB selective suspend: **Enabled** or **Disabled** | |
| 5 | The owner wants a normal shutdown to save the Windows kernel to disk so the next start is quicker. | Fast startup: **On** or **Off** | |
| 6 | Nobody has changed the power plan. Which plan is selected by default? | Power plan: **Balanced**, **Power saver** or **High performance** | |

**Marking.** 6 points: 1 point per row.
