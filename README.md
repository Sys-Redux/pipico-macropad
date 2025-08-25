<div id="header" align="center">
    <img src="https://github.com/user-attachments/assets/2b8f7f24-850b-4e5e-a963-936bc0882b5c" alt="Macropad" align="center" width="300" height="300"/>
</div>

<h1 align="center">🍓🍓PiPico-Macropad🍓🍓</h1>

Original 3D printed file by György Balássy:
https://www.printables.com/model/45559-star-wars-macro-keyboard
</br></br>
**🛠️Bill of Materials:**</br>
Raspberry Pi Pico / Pico W</br>
6 × momentary tactile push buttons (12 mm or similar)</br>
3 × LEDs (single-color) + 220 Ω resistors</br>
Breadboard or custom PCB</br>
Wires / jumper cables</br>
USB-C/Micro-USB cable (depending on Pico model)</br>

**💻Step-1: Download Dependencies**</br>
<a href="https://circuitpython.org/board/raspberry_pi_pico/">Circuit Python</a></br>
<a href="https://www.autohotkey.com/">AutoHotkey</a> (Windows)</br>
<a href="https://www.hammerspoon.org/">Hammerspoon</a> (Mac)</br></br>

**🛜Step-2: Wiring**</br>
| Button | Pico Pin | Pull Resistor    |
| ------ | -------- | ---------------- |
| B1     | GP0      | Internal Pull-Up |
| B2     | GP1      | Internal Pull-Up |
| B3     | GP2      | Internal Pull-Up |
| B4     | GP3      | Internal Pull-Up |
| B5     | GP4      | Internal Pull-Up |
| B6     | GP5      | Internal Pull-Up |
</br>

| LED | Pico Pin | Resistor |
| --- | -------- | -------- |
| L1  | GP6      | 220 Ω    |
| L2  | GP7      | 220 Ω    |
| L3  | GP8      | 220 Ω    |

</br></br>

**🐍Step-3: Install CircuitPython**</br>
1. Download the .UF2 from the CircuitPython link above for Raspberry Pi Pico.</br>
2. Hold the Pico’s BOOTSEL button while plugging it into your PC.</br>
3. Drag the .uf2 file onto the new USB drive called RPI-RP2.</br>
4. It will reboot as CIRCUITPY — this is your code drive.</br>
5. Add "code.py" from this repo to CIRCUITPY.</br></br>

**📁Step-4: Preparing Files**</br>
1. Download the Adafruit CircuitPython Bundle matching your version from:
https://circuitpython.org/libraries</br>
2. From the downloaded bundle, copy these folders into the lib folder on CIRCUITPY (you’ll need to make a lib folder first):</br>
    -adafruit_hid (for keyboard/macro functions)</br>
    -adafruit_debouncer.mpy</br</br>

**🚦Step-5: Enable on Startup**</br>
1. Download "macropad.ahk" from this repo to anywhere on your PC.</br>
2. Press ***Win + R***, type:</br>
        shell:startup</br>
3. Copy your .ahk script (or a shortcut to it) into this folder.</br></br>

<h3 align="center">Happy Making!</h3>
<p align="center">I hope everyone enjoys this project! Feel free to contact me with any questions.</p>


