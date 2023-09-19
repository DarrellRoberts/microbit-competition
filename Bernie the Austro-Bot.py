# 'import speech' & 'import microbit' taken from https://microbit-micropython.readthedocs.io/en/latest/tutorials/buttons.html#
import speech
import microbit

# 'from microbit import *' taken from https://microbit-micropython.readthedocs.io/en/latest/tutorials/buttons.html# 
from microbit import *
while True:
    if button_a.is_pressed():
        speech.pronounce("/HAWLOW. MAYN NAEMER IXTZ BERNIY.", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("HI, I'M BERNIE!")
        display.show(Image.HAPPY)
        microbit.sleep(2000)
        display.clear()
    elif button_b.is_pressed():
# the function below (although does nothing) was needed as a glitch occured where the sequence wouldn't break
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.pronounce("YEHTZ, ZEYUL BIHS ZVAEN-ZIHG.", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("COUNT TO 20")
        speech.say("EYEN. SVIE. DRIE. FEAR. FONF. ZEX. ZEEBEN. ACHT. NOIN. ZAYN.",speed=150, pitch=60, throat=200, mouth=180)
        speech.say("ELF. SVOLF. DRIE-ZAYN. FEAR-ZAYN. FONF-ZAYN.", speed=150, pitch=60, throat=200, mouth=180)
        speech.say("ZEX-ZAYN. ZEEBEN-ZAYN. ACHT-ZAYN. NOIN-ZAYN. SVAAN-ZIG.", speed=150, pitch=60, throat=200, mouth=180)
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.pronounce("YEHTZ, MAENCHER DOYCHEHN AWSDRUHKER.", speed=700, pitch=60, throat=200, mouth=180) 
        microbit.display.scroll("NOW GERMAN PHRASES")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.pronounce("GUHTIHN TAEG.", speed=700, pitch=60, throat=200, mouth=180) 
        microbit.display.scroll("HELLO")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.pronounce("AWF VIYDERZHEYN", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("GOODBYE")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.say("Dang-ker.", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("THANK YOU")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.say("Bit-ter.", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("YOU'RE WELCOME")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.pronounce("VIY GEYTS?", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("HOW ARE YOU?")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.say("MEER-ER GAYTS GOOT.", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("I'M GOOD")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.pronounce("EHNTSHUXDIYGAEN SIY.", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("EXCUSE ME")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.say("KANST DO ENG-LISH?", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("SPEAK ENGLISH?")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.pronounce("IXCH KAEN NIXCH DOYCH.", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("I CAN'T SPEAK GERMAN")
    elif button_b.is_pressed():
        microbit.display.scroll("")
        break
while True:
    if button_a.is_pressed():
        speech.say("VIY FIL?", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("HOW MUCH?")
    elif button_b.is_pressed():
        speech.pronounce("DIY- EHNDER. SHERNER TAEG.", speed=700, pitch=60, throat=200, mouth=180)
        microbit.display.scroll("THE END. HAVE A NICE DAY")
        display.show(Image.HAPPY)
        microbit.sleep(6000)
        display.clear()
        break


    