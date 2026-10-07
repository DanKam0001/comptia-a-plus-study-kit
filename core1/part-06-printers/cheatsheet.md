# Core 1, Part 6: Printers and Multifunction Devices

**Objectives 3.7** (deploy and configure multifunction devices/printers and settings) and **3.8** (perform appropriate printer maintenance) (220-1201).
Domain: Hardware (25% of the exam). Printer *troubleshooting* (lines, jams, garbled print) is objective 5.6, covered in a later part.

## The four printer types

| Type | How it marks the page | Typical use |
|---|---|---|
| Laser | Toner (fine powder) is melted onto the page by a hot **fuser** | Fast, offices |
| Inkjet | Printhead sprays tiny drops of liquid ink | Cheap to buy, home and photos |
| Thermal | Heat on special **thermal paper** (no ink or toner) | Receipts, shipping labels |
| Impact | Pins strike an inked **ribbon** (dot matrix) | **Multipart (carbon copy) forms**, invoices |

Only an impact printer can print through several layers of paper at once.

## Deploy a printer or multifunction device (3.7)

A **multifunction device (MFD)** prints, scans and copies.

| Topic | What to know |
|---|---|
| Unbox and location | Remove all tape and packing material, fit ink or toner. Put it on a flat, sturdy surface near power and network, with room for ventilation and for opening trays. Laser printers are heavy, so lift with care |
| Drivers | A **driver** lets the OS talk to the printer. Use the driver for your OS and printer model |
| PCL vs PostScript | **PCL** (Printer Control Language, CompTIA's wording) is the common everyday language. **PostScript** (from Adobe) is for graphics and professional publishing. The wrong choice can cause garbled print |
| Firmware | The printer's built-in software. Update it for bug fixes and security patches |
| Connectivity | **USB** (one computer), **Ethernet** (RJ45, shared on the network, most reliable for busy offices), **Wireless** (Wi-Fi, same network as the users) |
| Printer share | A printer attached to one PC is shared through that PC. The PC must be on |
| Print server | A computer, or a box built into the printer, on the network that manages the **print queue**. Always available |

## Configuration settings

| Setting | Meaning |
|---|---|
| Duplex | Print on both sides of the paper (saves paper) |
| Orientation | Portrait (tall) or landscape (wide) |
| Tray settings | Which tray to use, and the paper size and type loaded in it |
| Quality | Draft (fast, less ink) up to best (slower, more ink) |

## Security

| Feature | Meaning |
|---|---|
| User authentication | Sign in before printing or scanning |
| Badging | Tap an ID badge on the printer |
| Audit logs | Record of who printed or scanned what, and when |
| Secured prints | Job is held until the owner signs in at the printer (PIN or badge) |

## Network scan services and scanner types

- Scan to **email**, to a shared folder over **SMB** (port 445), or to a **cloud service**.
- **ADF** (automatic document feeder): pulls a stack of pages through one by one.
- **Flatbed scanner**: glass bed for single sheets, books and delicate paper.

## Maintenance (3.8)

| Printer | Parts | Maintenance |
|---|---|---|
| Laser | Toner, drum, fuser, rollers | Replace toner; apply a **maintenance kit** (replacement parts such as rollers and the fuser, used after a high page count); **calibrate**; **clean**. Switch off and let the fuser cool first |
| Inkjet | Ink cartridge, printhead, roller, feeder | Replace cartridges; **clean printheads**; **calibrate** (align); **clear jams** |
| Thermal | **Feed assembly**, special thermal paper, heating element | Replace paper; **clean the heating element** (cool, soft cloth, isopropyl alcohol); remove debris |
| Impact | Ribbon, printhead, **multipart paper** | Replace ribbon, printhead and paper |

## Common scenarios

| Scenario | Answer |
|---|---|
| Many users, printer plugged into one PC that is often off | Connect to the network and use a print server |
| Three-layer carbon copy invoices | Impact printer with multipart paper |
| Confidential pages left in the output tray | Secured print, with user authentication or badging |
| Scan paperwork to a shared Windows folder | Network scan to SMB |
| Scan a 50-page stack quickly | ADF |
| Scan a bound book or fragile page | Flatbed |
| Streaky inkjet output | Clean the printheads, then calibrate |
| Shop receipt printer, faint print | Clean the heating element, check the thermal paper |
