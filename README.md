# PiHole-MiniTFT-Display
A text based stats display code for the Adafruit Mini PiTFT with 2 buttons display.

This was built for a Pi Zero W

Your Pi needs to have the dsiplay set up to use the Mini PiTFT as a console display and **NOT** for Circut Python

However, you need to make sure you have the modules:
```
time
json
subprocess
os
sys
requests
digitalio
board
```

You also need a Pi-Hole API key

Display: https://www.adafruit.com/product/4393

How to set up the display for console output: https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi/kernel-module-install

For use with Pi Hole

In `/etc/rc.local`, before the `exit 0`, you need to add

```
sleep 10
sudo python3 path/to/PiHoleConsoleStuff.py &
```

The path could be something like: `/home/pi/PiHoleConsoleStuff.py`

This needs to be ran on the Pi that the Pi-Hole is on

Button A is the top button, press this to turn on the stats on the display, it'll look like:
```
IP: <whatever your ip for the pi is>

<HostName>
Ads Blocked: <ammount of ads blocked>
Clients: <ammount of clients recived>
CPU: <CPU Usage>
Mem: <Memory Usage>
Disk: <Disk Usage>
DNS Queries: <Ammount of DNS Queries>
```

If no button is pressed, the screen will be blank (not even a cursor, just backlight) This prevents screen burn-in
