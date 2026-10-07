# Core 1, Part 5: Displays: Panels, Resolution and Refresh

**Objective 3.1** (220-1201): *Compare and contrast display components and attributes.*
Domain: Hardware (25% of the exam).

Objective bullets covered: types (LCD: IPS, TN, VA; OLED; Mini-LED), touch screen/digitizer, inverter, attributes (pixel density, refresh rates, screen resolution, color gamut).

## How an LCD works

- **LCD** = Liquid Crystal Display. The panel does not make light. A **backlight** sits behind a layer of liquid-crystal shutters and color filters.
- A **pixel** is one dot of the picture (red, green and blue sub-dots).
- Older LCDs used a fluorescent tube backlight (CCFL). Newer ones use **LED** backlights.

## LCD panel types

| Type | Strengths | Weaknesses |
|---|---|---|
| **IPS** (In-Plane Switching) | Best color accuracy, widest viewing angles. Contrast about 1000:1 | Costs more, historically slower than TN |
| **TN** (Twisted Nematic) | Fastest response, cheapest | Poor viewing angles, weaker color (fades from the side) |
| **VA** (Vertical Alignment) | Best contrast (about 3000:1 typical), deep blacks | Usually slower response, viewing angles between TN and IPS |

## OLED and Mini-LED

| Type | Facts |
|---|---|
| **OLED** (Organic Light-Emitting Diode) | Every pixel makes its own light. **No backlight.** True black (a pixel switches fully off). Risk of **burn-in** from long static images. Common in phones, TVs, some laptops |
| **Mini-LED** | Still an **LCD**, but the backlight is thousands of tiny LEDs in **local dimming zones**. Brighter and better contrast than a normal LCD. No burn-in |

## Resolution

Resolution = number of pixels, **width x height**.

| Name | Resolution |
|---|---|
| HD | 1280 x 720 |
| Full HD (1080p) | 1920 x 1080 |
| QHD (1440p) | 2560 x 1440 |
| 4K UHD | 3840 x 2160 |
| 8K | 7680 x 4320 |

Running a screen below its **native resolution** looks blurry.

## Pixel density

- **Pixel density** = pixels per inch (**PPI**) = diagonal pixels / diagonal inches.
- Same resolution on a smaller screen = sharper (higher PPI).
- Examples: 24-inch Full HD is about 92 PPI; 27-inch QHD is about 109 PPI; 27-inch 4K is about 163 PPI.

## Refresh rate

- How many times per second the screen redraws, in **hertz (Hz)**.
- 60 Hz = standard office; 120, 144, 165, 240 Hz = gaming.
- To use a higher rate, the graphics card, the cable and the display setting must all support it.
- Refresh rate = smoothness. Resolution = sharpness. They are different things.

## Color gamut

- The range of colors a screen can show. Wider gamut = richer colors (especially reds and greens).
- **sRGB**: the standard baseline. **DCI-P3**: about 25% more colors than sRGB (video and film work). **Adobe RGB**: wider than sRGB, used in photography and print.
- Screens are rated by the percentage of a gamut they cover (for example "99% sRGB").

## Touch screen and digitizer

- The **digitizer** is the see-through layer over the display that senses touch and turns it into digital data.
- **Capacitive** (most phones and tablets): senses electricity in a finger, supports multi-touch.
- **Resistive** (older, industrial): senses pressure, works with gloves or a stylus.
- Picture fine but touch ignored or ghost touches: suspect the digitizer, not the display.

## Inverter

- Converts the laptop's low-voltage DC into the high-voltage AC that powers a **CCFL (fluorescent) backlight tube** in older LCDs.
- Failing inverter: **very dim or flickering** screen, picture still faintly visible with a flashlight.
- **LED backlights and OLED do not use an inverter.**

## Common scenarios

| Symptom | Likely answer |
|---|---|
| Colors wash out from the side | Use an IPS panel (TN has narrow angles) |
| Fast action looks choppy | Higher refresh rate (144 Hz or more), supported by GPU, cable and settings |
| Very dim screen, picture faintly visible with a flashlight | Failed inverter (or backlight) |
| Want deep blacks and no backlight | OLED |
| Want a very bright LCD with better contrast | Mini-LED |
| Text looks blurry at a non-native resolution | Set the display to its native resolution |
| Touch not responding, picture fine | Digitizer |
