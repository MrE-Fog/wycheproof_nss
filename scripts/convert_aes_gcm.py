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
    


# typedef struct gcm_kat_str {
#   std::string key;    -> key
#   std::string plaintext;      -> msg
#   std::string additional_data;        -> aad
#   std::string iv;     -> iv
#   std::string hash_key;       -> 
#   std::string ghash;      -> tag?
#   std::string result;     -> ct
# } gcm_kat_value;

{"00000000000000000000000000000000", "", "", "000000000000000000000000",
     "66e94bd4ef8a2c3b884cfa59ca342b2e", "00000000000000000000000000000000",
     "58e2fccefa7e3061367f1d57a4e7455a"},
     
{
"tcId" : 1,
"comment" : "",
"key" : "5b9604fe14eadba931b0ccf34843dab9",
"iv" : "028318abc1824029138141a2",
"aad" : "",
"msg" : "001d0c231287c1182784554ca3a21908",
"ct" : "26073cc1d851beff176384dc9896d5ff",
"tag" : "0a3ea7a5487cb5f7d70fb6c58d038554",
"result" : "valid",
"flags" : []
},
