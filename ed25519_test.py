import binascii

import unittest

import ed25519


class Ed25519Test(unittest.TestCase):

    def test_keygen(self):
        priv = binascii.unhexlify('0' * 64)
        self.assertEqual(len(priv), 32)

        pub = ed25519.derive_pubkey_from_priv(priv)

        hpriv = binascii.hexlify(priv)
        hpub = binascii.hexlify(pub)

        print(hpriv, hpub)

        expectedPub = "43eeb17f0bab10dd51ab70983c25200a1742d31b3b7b54c38c34d7b827b26eed"
        self.assertSequenceEqual(hpub, expectedPub)


if __name__ == '__main__':
    unittest.main()
