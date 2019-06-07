# coding: utf-8

import binascii
import nfc

from card_hash import sha512
from authenticated_cards import authenticated_cards


def startup(targets):
    print("waiting for new NFC tags...")
    return targets

def connected(tag):
    print("connected:")
    print(tag)

    # 製造ID (IDm)
    idm = binascii.hexlify(tag.identifier).upper()
    print(idm)

    # 製造パラメータ (PMm)
    pmm = binascii.hexlify(tag.pmm).upper()
    print(pmm)

    # システムコード (sys)
    syscode = "%04X" % tag.sys
    print(syscode)

    card_hash = sha512(idm, pmm, syscode)

    if card_hash in authenticated_cards:
        print('OK')
    else:
        print('NG')

    return True

clf = nfc.ContactlessFrontend('usb')
print(clf)
if clf:
    while clf.connect(rdwr={
            'on-startup': startup,
            'on-connect': connected, }):
        pass
