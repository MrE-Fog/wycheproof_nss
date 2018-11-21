#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:09:00 2018

@author: jonasda
"""

import json

source_file = '../source/chacha20_poly1305_test.json'
base_file = '../header_bases/chachapoly-vectors.h'
target_file = '../target/chachapoly-vectors.h'

# Imports a JSON testvector file.
def import_testvector(file):
    
    with open(file) as f:
        vectors = json.loads(f.read())

    return vectors


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


def format_testcase_to_nss(testcase):
    nss_vector = "\n// Comment: {}".format(testcase["comment"])
    nss_vector += "\n{{{},\n".format(testcase["tcId"]-1)
    nss_vector += "{},\n".format(string_to_hex_array(testcase["msg"]))
    nss_vector += "{},\n".format(string_to_hex_array(testcase["aad"]))
    nss_vector += "{},\n".format(string_to_hex_array(testcase["key"]))
    nss_vector += "{},\n".format(string_to_hex_array(testcase["iv"]))
    ct = testcase["ct"] + testcase["tag"]
    nss_vector += "{},\n".format(string_to_hex_array(ct))
    nss_vector += "{}}},\n".format(str(testcase["result"] == "valid").lower())

    return nss_vector


cases = import_testvector(source_file)

with open(base_file) as base:
    header = base.read()
    
header += "\n\n// Testvectors from project wycheproof\n"
header += "// <https://github.com/google/wycheproof>\n"
header += "const chacha_testvector kChaCha20WycheproofVectors[] = {\n"

invalidNonceGroup = "const chacha_testvector kChaCha20WycheproofInvalidNonceVectors[] = {\n"
    
for group in cases["testGroups"]:
    for case in group["tests"]:
        if case["comment"] == "invalid nonce size":
            invalidNonceGroup += format_testcase_to_nss(case)
        else:
            header += format_testcase_to_nss(case)
            
header = header[:-2] + "};\n\n"
header += invalidNonceGroup
header = header[:-2] + "};\n\n"

header += "#endif  // chachapoly_vectors_h__"

with open(target_file, 'w') as target:
    target.write(header)
