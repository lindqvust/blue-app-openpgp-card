# Copyright 2017 Cedric Mesnil <cslashm@gmail.com>, Ledger SAS
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import binascii
from gpgcard import GPGCard

gpgcard = GPGCard()
gpgcard.connect("pcsc:Ledger")
gpgcard.get_all()


gpgcard.verify_pin(0x81, "123456")
gpgcard.verify_pin(0x83, "12345678")

gpgcard.verify_pin(0x81, "123456")
gpgcard.verify_pin(0x83, "12345678")

gpgcard.generate_asym_key_pair(0x80, 0xb600)
gpgcard.generate_asym_key_pair(0x80, 0xb800)
gpgcard.generate_asym_key_pair(0x80, 0xa400)

# Use 'gpg -k --with-subkey-fingerprint' to find fingerprints

sig_fingerprint = b'FB327D541D9FC796B0419C64828CAB9CA0EBA7EC'
aut_fingerprint = b'34E66F064987FE012C1F09D60D872860BD92ECC3'
dec_fingerprint = b'2B61FF5583894906DB5625703AAF31D1A7FC7B4F'

sig_fingerprint_bin = binascii.unhexlify(sig_fingerprint)
aut_fingerprint_bin = binascii.unhexlify(aut_fingerprint)
dec_fingerprint_bin = binascii.unhexlify(dec_fingerprint)

gpgcard.sig_fingerprints = sig_fingerprint_bin
gpgcard.aut_fingerprints = aut_fingerprint_bin
gpgcard.dec_fingerprints = dec_fingerprint_bin

# gpgcard.restore("backup_card.pickle", True)
