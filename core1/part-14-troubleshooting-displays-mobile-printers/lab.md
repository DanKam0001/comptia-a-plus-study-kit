# Lab: Diagnose display, phone and printer faults on your own devices (Windows and a phone)

**Time:** 15 to 20 minutes. **Needs:** a Windows PC with a monitor, and a smartphone or tablet. Everything here is read-only or a safe settings change you can undo. You do not break anything.

Goal: see the symptoms from Part 14 for yourself, and know where the fix lives.

## 1. Display: native resolution and refresh rate

1. Right-click the desktop, choose **Display settings**.
2. Find **Display resolution**. The one marked **(Recommended)** is the native resolution. Write it down.
3. Under **Advanced display**, find the **refresh rate**. Write it down.
4. Optional, and reversible: set the resolution one step lower, look at how fuzzy the text becomes, then set it back to the recommended one. That is exactly the "fuzzy, distorted image" symptom.

## 2. Display: dead pixels

Open a full-screen solid color (search the web for "dead pixel test" or use a plain colored image) and cycle through black, white, red, green and blue. Look for any dot that never changes. That is a dead or stuck pixel.

## 3. Display: input and cable

Look at the back or edge of your monitor and find its **input** button or menu. Write down which input names it offers (HDMI 1, DisplayPort, and so on) and which one your PC is using. If you have a spare cable, note which connector types it has.

## 4. Phone or tablet: battery health

- iPhone: **Settings > Battery > Battery Health**.
- Android: the path varies by maker. Look in **Settings > Battery** (or **Device care**), or dial the maker's diagnostics code.

Write down the battery health. Then look at the back of your device. A swollen battery would show as a bulge or a lifting back cover. Yours should be flat.

## 5. Phone or tablet: connectivity and storage

1. Find **Airplane mode** and note where it is, then find **Reset network settings** (do not run it). It is the fix for "poor or no connectivity".
2. Open **Storage** in settings. How full is it? A phone that is nearly full can't install new apps.

## 6. Printer: queue and spooler

On Windows, press **Windows key + R**, type `services.msc`, press Enter, and find **Print Spooler**. Note its status. Restarting this service is the fix for a frozen queue (do not restart it during a real print job).

Open **Settings > Bluetooth & devices > Printers & scanners** and click a printer, then **Open print queue**. If there is a stuck job you can cancel it from here.

## 7. Write it up

```
Native resolution / refresh rate:
Dead pixels found (yes/no):
Monitor inputs / input in use:
Phone battery health:
Phone storage used:
Print Spooler status:
```

## Check yourself

- A projector shuts down mid-talk and restarts after a rest. What is wrong and what is the fix?
- A screen is clear, but touches are ignored. Which layer is faulty?
- A laser printer shows a line down every page. Which two parts could be dirty or damaged?

## Going further (optional)

If you have an old laser or inkjet printer, run its built-in cleaning cycle, then print a test page. Look for lines, fading and speckles on the page, and match each one to the table in the cheat sheet.
