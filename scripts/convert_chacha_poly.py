#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:09:00 2018

@author: jonasda
"""

import json

# Imports a JSON testvector file.
def import_testvector(file):
    
    with open(file) as f:
        vectors = json.loads(f.read())

    return vectors


def string_to_hex_array(string):
    result = ""
    result += "{\n\t"
    for i in range(0, len(string)/2):
        result += "0x"
        result += string[i*2]
        result += string[i*2+1]
        if i != len(string)/2-1:
            result += ", "
        if (i+1)%12 == 0:
            result += "\n\t"

    result += "};"
    return result


def format_testcase_to_nss(testcase, name):
    nss_vector = "const uint8_t "
    nss_vector += name
    nss_vector += "Data[] = "
    nss_vector += string_to_hex_array(testcase["msg"])
    nss_vector += "\nconst uint8_t "
    nss_vector += name
    nss_vector += "AAD[] = "
    nss_vector += string_to_hex_array(testcase["aad"])
    nss_vector += "\nconst uint8_t "
    nss_vector += name
    nss_vector += "Key[] = "
    nss_vector += string_to_hex_array(testcase["key"])
    nss_vector += "\nconst uint8_t "
    nss_vector += name
    nss_vector += "IV[] = "
    nss_vector += string_to_hex_array(testcase["iv"])
    ct = testcase["ct"] + testcase["tag"]
    nss_vector += "\nconst uint8_t "
    nss_vector += name
    nss_vector += "CT[] = "
    nss_vector += string_to_hex_array(ct)
    nss_vector += "\nconst bool "
    nss_vector += name
    nss_vector += "Valid = "
    if (testcase["result"] == "valid"):
        nss_vector += "true;\n"
    else:
        nss_vector += "false;\n"

    return nss_vector

def generate_gtests_function(name):
    func = "\nTEST_F(Pkcs11ChaCha20Poly1305Test, Chec"
    func += name
    func += ") {\n\tENCRYPT_DECRYPT("
    func += name 
    func += "); \n}"
    return func

cases = import_testvector("../source/chacha20_poly1305_test.json")

index = 3

test_vectors = ""
gtests_functions = ""

for group in cases["testGroups"]:
    for case in group["tests"]:
        name = "kTestVector{}".format(index)
        test_vectors += format_testcase_to_nss(case, name)
        gtests_functions += generate_gtests_function(name)
        index += 1

print test_vectors
print gtests_functions

    
