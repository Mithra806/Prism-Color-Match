
# Prism Color Match
A hardware version of the classic "Simon Says" memory game, built with a Raspberry Pi, an RGB LED, and three push buttons. The Pi flashes a sequence of colors that grows each round, and you have to repeat it back correctly using the buttons.
 
## How It Works
1. The game flashes a sequence of colors (starting at 3).
2. You repeat the sequence by pressing the matching color buttons.
3. **Correct guess** → a quick sequence of green, blue, red, red, blue, green flash plays, and the sequence grows by one color for the next round.
4. **Wrong guess** → the LED flashes red 3 times, and the game resets back to a 3-color sequence.
   
## Hardware
- Raspberry Pi (any model with GPIO)
- 3x push buttons (red, green, blue)
- 1x 220Ω resistor per LED color channel (3 total)
- 1x 10kΩ resistor per button (3 total)
- Breadboard + a bunch of male to male jumper wires

## Wiring / GPIO Pinout
 
| Component       | GPIO Pin | Resistor |
|-----------------|----------|----------|
| Red LED         | GPIO5    | 220Ω     |
| Green LED       | GPIO17   | 220Ω     |
| Blue LED        | GPIO27   | 220Ω     |
| Green Button    | GPIO18   | 10kΩ     |
| Blue Button     | GPIO23   | 10kΩ     |
| Red Button      | GPIO16   | 10kΩ     |
 
<img width="3024" height="4032" alt="WhatsApp Image 2026-08-07 at 10 34 53 PM" src="https://github.com/user-attachments/assets/d16b0381-7c5a-4e96-9657-dc7fc572c4d5" />

 
