/* vim: set ts=2 et sw=2 tw=80: */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this file,
 * You can obtain one at http://mozilla.org/MPL/2.0/. */

#ifndef chachapoly_vectors_h__
#define chachapoly_vectors_h__

#include <string>
#include <vector>

typedef struct ECDH_secp224r1_testvector_str {
  uint32_t id;
  std::vector<uint8_t> Public;
  std::vector<uint8_t> Private;
  std::vector<uint8_t> Secret;
  bool invalid_tag;
  bool invalid_iv;
} ECDH_secp224r1_testvector;

// Testvectors from Project wycheproof
// <https://github.com/google/wycheproof>
const chacha_testvector kECDHsecp224r1Vectors[] = {
    
}
#endif  // chachapoly_vectors_h__
