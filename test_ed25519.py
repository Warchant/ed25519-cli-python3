from __future__ import print_function
import binascii
import ed25519
from builtins import object


class Test_Ed25519(object):

    def test_keygen(self):
        priv = b'\x00' * 32
        assert len(priv) == 32

        pub = ed25519.derive_pubkey_from_priv(priv)

        if isinstance(pub, str) or isinstance(pub, unicode):
            pub = bytearray([ord(x) for x in pub])

        hpriv = binascii.hexlify(priv)
        hpub = binascii.hexlify(pub)

        print((hpriv, hpub))

        expectedPub = b"43eeb17f0bab10dd51ab70983c25200a1742d31b3b7b54c38c34d7b827b26eed"
        assert hpub == expectedPub
