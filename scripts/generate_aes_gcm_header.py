#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:09:00 2018

@author: jallmann@mozilla.com
"""

import json

source_file = '../source/aes_gcm_test.json'
base_file = '../header_bases/gcm-vectors.h'
target_file = '../target/gcm-vectors.h'


# Imports a JSON testvector file.
def import_testvector(file):
    
    with open(file) as f:
        vectors = json.loads(f.read())
    return vectors

# Writes one testvector into C-header format. (Not clang-format conform)
def format_testcase(vector):
    result = "{{ {},\n".format(vector["tcId"])
    result += " \"{}\",\n".format(vector["key"])
    result += " \"{}\",\n".format(vector["msg"])
    result += " \"{}\",\n".format(vector["aad"])
    result += " \"{}\",\n".format(vector["iv"])
    result += " \"\",\n"
    result += " \"{}\",\n".format(vector["tag"])
    result += " \"{}\",\n".format(vector["ct"] + vector["tag"])
    result += " {}}},\n\n".format(str(vector["result"] == "valid" or vector["result"] == "acceptable").lower())

    return result


cases = import_testvector(source_file)

with open(base_file) as base:
    header = base.read()

header += "// Testvectors from project wycheproof\n"
header += "// <https://github.com/google/wycheproof>\n"
header += "const gcm_kat_value kGcmWycheproofVectors[] = {\n"

for group in cases["testGroups"]:
    for test in group["tests"]:
        if "ZeroLengthIv" not in test["flags"]:
            header += format_testcase(test)

header = header[:-3] + "};\n\n"

header += "const gcm_kat_value kGcmWycheproofEmptyIVVectors[] = {"

for group in cases["testGroups"]:
    for test in group["tests"]:
        if "ZeroLengthIv" in test["flags"]:
            header += format_testcase(test)

header = header[:-3] + "};\n\n"

header += "#endif  // gcm_vectors_h__"

with open(target_file, 'w') as target:
    target.write(header)
