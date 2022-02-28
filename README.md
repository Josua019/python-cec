# Cec to IR wit libcec

Based on a [project from the Homeassistant commuity](https://community.home-assistant.io/t/cec-volume-control-for-ir-devices-by-pretending-to-be-an-hdmi-arc-device/323047)

## Installing

### Install dependencies

```bash
sudo apt-get install libcec-dev build-essential python3-dev python3-pip git
```

### Clone repo

```bash
git clone https://github.com/Josua019/python-cec.git
```

### Build and install

```bash
sudo python3 setup.py install
```

## Run

```bash
python3 cecwatcher.py
```

A log file will be created and the console will output relevant information

## Create a service

Stop the script with Ctrl+C

### Create the file

```bash
sudo nano /etc/systemd/system/cecwatcher.service
```

### Paste this:

**update the path at 'ExecStart'**

```bash
# systemd unit file for cecwatcher.py

[Unit]
Description=CEC Watcher

[Service]
ExecStart=/usr/bin/python3 /home/pi/Documents/python-cec/cecwatcher.py
# Disable Python's buffering of STDOUT and STDERR, so that output from the
# service shows up immediately in systemd's logs
Environment=PYTHONUNBUFFERED=1
User=pi

[Install]
# Tell systemd to automatically start this service when the system boots
# (assuming the service is enabled)
WantedBy=default.target
```

### Start the service

```bash
sudo systemctl start cecwatcher
sudo systemctl status cecwatcher
```

### Set it up to start on boot

```bash
sudo systemctl enable cecwatcher
```

## Fixing issues

If status shows an error try fixing it, run

```bash
sudo systemctl reset-failed
```

and resart the service
