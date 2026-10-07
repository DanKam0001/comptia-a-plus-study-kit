# Core 1, Part 14: Troubleshooting Displays, Mobile Devices and Printers

**Objectives 5.3, 5.4 and 5.6** (220-1201): *Given a scenario, troubleshoot video, projector, and display issues. Troubleshoot common mobile device issues. Troubleshoot printer issues.*
Domain: Hardware and Network Troubleshooting (28% of the exam, the biggest domain).

The exam gives you a symptom and asks for the **most likely cause** or the **best fix**. Learn each symptom with its cause and its fix. Always try the cheap, simple, low-risk step first.

## 5.3 Video, projector and display issues

| Symptom | Likely cause | Fix |
|---|---|---|
| Incorrect input source ("No signal", black screen) | Monitor or projector set to a different input | Choose the right input in the screen's menu or with the source button |
| Physical cabling issues | Loose, bent or damaged cable, wrong cable or adapter | Reseat both ends, try a known-good cable, check the right port is used |
| Burnt-out bulb | Projector lamp reached the end of its hours | Let the projector cool, replace the lamp, reset the lamp-hours counter |
| Fuzzy image | Wrong resolution (not native), loose cable, projector out of focus | Set the **native resolution**, reseat the cable, adjust the focus ring |
| Display burn-in | A static image left on screen too long (mainly OLED, also old plasma) | Screensaver, moving content, lower brightness. Often permanent |
| Dead pixels | Faulty pixels (stay black, or stuck on one color) | Usually not repairable. Replace the panel or screen if there are too many |
| Flashing screen | Loose or damaged cable, wrong refresh rate, failing backlight or inverter, bad graphics driver | Reseat or replace the cable, set a supported refresh rate, update the driver, repair the backlight |
| Incorrect color display | Loose cable pins (a bent VGA pin loses a color), wrong color profile, bad driver | Reseat or replace the cable, reset or recalibrate color settings, update the driver |
| Audio issues | Cable or connection does not carry audio (VGA and DVI do not), wrong output device, muted | Use HDMI or DisplayPort, pick the right output device, unmute |
| Dim image | Brightness too low, failing LCD backlight or inverter, old projector lamp, dirty projector filter | Raise brightness, replace the backlight or inverter, replace the lamp, clean the filter |
| Intermittent projector shutdown | **Overheating**: clogged filters or vents, failed fan, old lamp | Clean filters and vents, leave airflow space, replace the fan or lamp |
| Sizing issues | Wrong resolution, aspect ratio or scaling | Set the native resolution, adjust scaling or the aspect ratio setting |
| Distorted image | Wrong resolution, bad cable, driver problem, projector angle (keystone) | Set the native resolution, replace the cable, update the driver, use keystone correction or reposition the projector |

Useful background: an LCD's backlight is powered by an **inverter** on older screens. Projector lamps are rated in hours, and most projectors show the lamp hours in their menu.

## 5.4 Mobile device issues

| Symptom | Likely cause | Fix |
|---|---|---|
| Poor battery health | Battery worn out, heavy use, high brightness | Check battery health in settings, lower brightness, **replace the battery** |
| **Swollen battery** | Gas building up inside a lithium-ion battery. A **fire risk** | **Stop using it, do not charge it, do not press or puncture it.** Replace it safely and recycle the old one |
| Broken screen | Cracked glass or damaged display | Replace the screen (assembly) |
| Improper charging | Bad cable, weak charger, dirty or damaged charging port | Try another cable and charger, clean the port, repair or replace the port |
| Poor or no connectivity | Airplane mode on, radios off, bad settings, no signal | Check airplane mode, toggle Wi-Fi or Bluetooth, reset network settings, check the SIM |
| Liquid damage | Water or other liquid inside | Power off at once, do not charge, remove case and SIM, take it for repair |
| Overheating | Heavy app, hot environment, thick case, charging while in use, rogue app or malware | Close apps, take the case off, let it cool, update, scan for malware |
| Digitizer issues | The touch-sensing layer is faulty (touch is dead or "ghost touches", picture fine) | Restart, clean the screen, replace the screen/digitizer assembly |
| Physically damaged ports | Bent or broken charging or data port | Repair or replace the port |
| Malware | Pop-ups, fast battery drain, heat, unknown apps | Remove suspicious apps, run a security scan, factory reset as a last resort |
| Cursor drift or touch calibration | Touch input not lined up | Restart, remove the screen protector, recalibrate the touch settings, update |
| Unable to install new applications | No free storage, outdated OS, app not compatible | Free up storage, update the operating system, check compatibility |
| Stylus does not work | Dead battery or no charge, not paired, worn tip, not a compatible stylus | Charge or replace the battery, re-pair over Bluetooth, replace the tip, use a compatible stylus |
| Degraded performance | Too many apps, low storage, old OS, malware | Restart, close apps, free storage, update, scan for malware |

## 5.6 Printer issues

| Symptom | Likely cause | Fix |
|---|---|---|
| Lines down the printed pages | Laser: dirty or damaged **drum** or toner cartridge. Inkjet: clogged print head | Clean or replace the drum or cartridge. Run the inkjet head-cleaning cycle |
| Garbled print | Wrong or corrupt driver, wrong printer language, bad cable | Reinstall the correct driver, replace the cable |
| Paper jams | Wrong or damp paper, overfilled tray, worn rollers, debris | Remove the jam gently, use the right dry paper, do not overfill, replace worn rollers |
| Faded prints | Low toner or ink, toner-saving mode, worn drum | Replace or shake the cartridge, turn off toner saver, replace the drum |
| Paper not feeding | Worn or dirty **pickup roller**, tray loaded wrong, wrong paper | Clean or replace the pickup roller, reload the paper correctly |
| Multipage misfeed | Damp paper sticking together, worn separation pad or rollers | Fan the paper, use dry paper, replace the pad or rollers |
| Multiple prints pending in queue | A stuck job is blocking the others | Delete the stuck job, restart the **print spooler** |
| Speckling on printed pages | Stray toner: leaking cartridge, dirty printer, waste toner | Replace the cartridge, clean the inside |
| Double or echo images on the print | Worn **drum** (ghosting) or a problem with the **fuser** | Replace the imaging drum or the fuser |
| Grinding noise | Broken gear, or an object stuck in the rollers | Stop, power off, look inside, remove the object or replace the gears |
| Finishing issues: staple jams | Jammed staples, empty staple cartridge | Clear the jam, load staples |
| Finishing issues: hole punch | Full punch bin, jam | Empty the punch bin, clear the jam |
| Incorrect page orientation | Wrong portrait or landscape setting in the print dialog or driver | Change the orientation setting |
| Tray not recognized | Tray not seated, sensor or driver configuration | Push the tray in fully, check the driver's installed-options settings |
| Connectivity issues | Bad cable, wrong network, changed IP address, Wi-Fi drop | Check cables, re-join the network, check the printer's address, reinstall the port |
| Frozen print queue | Print spooler service stuck | Restart the **Print Spooler** service, clear the queue |

## Safety reminders

- Let projector lamps and printer fusers **cool** before touching them. They get very hot.
- Never charge or puncture a swollen battery. Take used batteries to proper recycling, never the household bin.
- Power printers off and unplug before reaching inside.
