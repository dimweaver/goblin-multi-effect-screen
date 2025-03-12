# goblin-multi-effect-screen
 Test for opening graphic on waveshare g to be used on Goblin MFX DSP unit
 to display the UI to interact with the analog inpupts.

 ## How to run


Open the Raspberry Pi terminal and enter the following command in the config interface:

- Enable SPI Interface

```bash
    sudo raspi-config
```
Choose Interfacing Options -> SPI -> Yes Enable SPI interface

- Reboot Rasp        
```bash
    sudo sudo reboot
```
- Install the function library:
```bash
    sudo apt-get update
    sudo apt-get install python3-pip
    sudo apt-get install python3-pil
    sudo apt-get install python3-numpy
    sudo pip3 install spidev
```
- Install gpiozero library
```bash
    sudo apt-get update
    sudo apt install python3-gpiozero
```
- Clone repo
```bash
    git clone https://github.com/dimweaver/goblin-multi-effect-screen.git
    cd e-Paper/RaspberryPi_JetsonNano/
```
- Run
Screen testing script
```bash
    cd goblin-multi-effect-screen/examples/
    python3 epd_2in13g_test.py  
```
- UI Test
```bash
    cd goblin-multi-effect-screen/examples/
    python3 epd_2in13g_goblin.py  
```