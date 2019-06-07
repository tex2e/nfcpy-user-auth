
# User Auth with nfcpy

### Setup in MacOS

```
$ brew install libusb
$ pip2 install nfcpy
```

### Setup in RaspberryPi

```
$ sudo apt install libusb-dev
$ pip2 install nfcpy
```

Assign the device to the 'plugdev' group.

```
$ sudo sh -c 'echo SUBSYSTEM==\"usb\", ACTION==\"add\", ATTRS{idVendor}==\"054c\", ATTRS{idProduct}==\"06c3\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'
$ sudo udevadm control -R
```

### Prepare a Card's Hash Value

First, read an IC card. Then put a hash into authenticated_cards.py

```
$ python2 card_hash.py
SONY RC-S380/P on usb:020:004
waiting for new NFC tags...
connected:
Type3Tag 'FeliCa Lite-S (RC-S966)' ID=XXXXXXXXXXXXXXXX PMM=00F1000000014300 SYS=88B4
IDm: XXXXXXXXXXXXXXXX
PMm: 00F1000000014300
sys: 88B4
sha512(IDm, PMm, sys): 94dc624736db7a533983d26af9b015a08a2b54db8a8382536ae7d6aa9617b5bdda35ff8353a6df173a0f16a2333c391a27177a1a29d0c7e7212e20c6894acc37
```

```
$ vim authenticated_cards.py

authenticated_cards = [
  '94dc624736db7a533983d26af9b015a08a2b54db8a8382536ae7d6aa9617b5bdda35ff8353a6df173a0f16a2333c391a27177a1a29d0c7e7212e20c6894acc37',
]
```

### User Auth With a IC Card

```
$ python2 card_auth.py
SONY RC-S380/P on usb:020:004
waiting for new NFC tags...
```
