#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, x25519
from cryptography.hazmat.primitives import serialization, asymmetric
import cryptography
import binascii

def string_to_hex_array(string):
    result = "{"
    for i in range(0, len(string)/2):
        result += "0x"
        result += string[i*2]
        result += string[i*2+1]
        if i != len(string)/2-1:
            result += ", "
        if (i+1)%12 == 0:
            result += "\n\t"

    result += "}"
    return result
    
# 
# example = {
#           "tcId" : 1,
#           "comment" : "normal case",
#           "curve" : "curve25519",
#           "public" : "9c647d9ae589b9f58fdc3ca4947efbc915c4b2e08e744a0edf469dac59c8f85a",
#           "private" : "4852834d9d6b77dadeabaaf2e11dca66d19fe74993a7bec36c6e16a0983feaba",
#           "shared" : "87b7f212b627f7a54ca5e0bcdaddd5389d9de6156cdbcf8ebe14ffbcfb436551",
#           "result" : "valid",
#           "flags" : []
# };

example224 = {
    "tcId" : 1,
    "comment" : "normal case",
    "public" : "304e301006072a8648ce3d020106052b81040021033a00047d8ac211e1228eb094e285a957d9912e93deee433ed777440ae9fc719b01d050dfbe653e72f39491be87fb1a2742daa6e0a2aada98bb1aca",
    "private" : "565577a49415ca761a0322ad54e4ad0ae7625174baf372c2816f5328",
    "shared" : "b8ecdb552d39228ee332bafe4886dbff272f7109edf933bc7542bd4f",
    "result" : "valid",
    "flags" : []
};

example224_2 = {
    "tcId" : 2,
    "comment" : "compressed public key",
    "public" : "3032301006072a8648ce3d020106052b81040021031e00027d8ac211e1228eb094e285a957d9912e93deee433ed777440ae9fc71",
    "private" : "565577a49415ca761a0322ad54e4ad0ae7625174baf372c2816f5328",
    "shared" : "b8ecdb552d39228ee332bafe4886dbff272f7109edf933bc7542bd4f",
    "result" : "acceptable",
    "flags" : [
        "CompressedPoint"
        ]
};

example224_3 = {
"tcId" : 3,
"comment" : "edge case for shared secret",
"public" : "304e301006072a8648ce3d020106052b81040021033a0004e73a6ca72f3a2fae6e0a01a0ed03bfa3058b04576942eaf063095e62ca16fd31fa0f38eeb592cbeea1147751fdd2a5b6cc0ead404467a5b6",
"private" : "0a2b6442a37f9201b56758034d2009be64b0ab7c02d7e398cac9665d6",
"shared" : "00000000000000000000000000000000000000000000000000000003",
"result" : "valid",
"flags" : []
};

ex = example224_3


public_key = serialization.load_der_public_key(
    binascii.unhexlify(ex["public"]),
    default_backend()
)

der_public = public_key.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

private_key = ec.derive_private_key(
    int(ex["private"], 16),
    ec.SECP224R1(), 
    default_backend()
)

der_private = private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

hex_public = binascii.hexlify(der_public)
hex_private = binascii.hexlify(der_private)

print(der_private)


print(hex_public)
print(hex_private)

print(string_to_hex_array(hex_private))
print(string_to_hex_array(hex_public))
print(string_to_hex_array(ex["shared"]))

# steps: 
# Derive Public key of private?
# Wrap both in ASN1 structure
# Print ASN1 as Hex. 
# Format Hex to NSS test format. 
# 
