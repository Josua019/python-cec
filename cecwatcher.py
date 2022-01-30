import time
import cec
import os

# Replace as necessary with your own HA entity and services for volume
entity_id='media_player.soundbar'
def volume_up():
    os.system("irsend SEND_ONCE sony_stereo KEY_VOLUMEUP")
    print("volume up")
def volume_down():
    os.system("irsend SEND_ONCE sony_stereo KEY_VOLUMEDOWN")
    print("volume down")
def volume_mute():
    os.system("irsend SEND_ONCE sony_stereo KEY_MUTE")
    print("mute")
def power_toggle():
    os.system("irsend SEND_ONCE sony_stereo KEY_POWER")
    print("power")

def callback(event, *argv):
    if event == cec.EVENT_COMMAND:
        command = argv[0]
        #print("command", command)
        if command['opcode'] == cec.CEC_OPCODE_REQUEST_ARC_START:
            print("Reporting ARC started")
            cec.transmit(cec.CECDEVICE_TV, cec.CEC_OPCODE_REPORT_ARC_STARTED, '', cec.CECDEVICE_AUDIOSYSTEM)
    elif event == cec.EVENT_KEYPRESS:
        code, duration = argv
        print("keypress", code, duration)
        if code == 65 and duration == 0:
            volume_up()
        elif code == 66 and duration == 0:
            volume_down()
        elif code == 67 and duration == 0:
            volume_mute()
    else:
        print("event", event, argv)

cec.add_callback(callback, cec.EVENT_ALL & ~cec.EVENT_LOG)
cec.init()

devices = cec.list_devices()
print(devices)

# Sleep forever (CEC stuff will run in the background)
while True:
    time.sleep(100)
