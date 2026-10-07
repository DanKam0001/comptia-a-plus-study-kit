# Lab: Inspect your own display (Windows)

**Time:** 10 to 15 minutes. **Needs:** any Windows PC, laptop or monitor. Everything here is read-only except where it says you may change a setting and change it back.

Goal: find the resolution, refresh rate and panel facts of a real screen.

## 1. Resolution and scale

Open **Settings > System > Display**. Note the **Display resolution** (Recommended = native) and **Scale**.

## 2. Refresh rate

In the same page open **Advanced display**. Note **Choose a refresh rate**. If a higher one is listed, you may switch to it, then switch back if you prefer.

## 3. Work out pixel density

Measure the screen diagonal in inches (or look up the model). Then calculate:

```
PPI = sqrt(width_pixels^2 + height_pixels^2) / diagonal_inches
```

Example: 1920 x 1080 on 24 inches = about 92 PPI. Compare with a phone: a 6-inch 2400 x 1080 phone is about 400 PPI.

## 4. Find the panel type

Search your monitor or laptop model with "panel type". Is it IPS, TN, VA or OLED? Check the viewing angle: look at the screen from the side. Do colors fade?

## 5. The motion test

Go to a free "UFO test" style motion website in your browser. Compare the smoothness at 60 Hz with a higher setting if you have one.

## 6. The flashlight test (safe, laptop only)

In a dim room, shine a torch at an off-angle on a laptop screen showing a picture. On a working screen nothing is surprising. A very dim screen with a faint picture visible means a backlight or inverter problem (on older laptops).

## 7. Write it up

```
Screen size (in) / resolution / PPI:
Refresh rate:
Panel type (IPS / TN / VA / OLED):
Backlight (LED or none/OLED):
Touch screen? (capacitive?):
```

## Check yourself

- A designer sees washed-out colors from the side. Which panel type fixes it?
- A gamer's fast action looks choppy at 60 Hz. What do they need?
- A very dim laptop screen shows a faint picture under a torch. Which part is suspect?
