/* vim: set ts=2 et sw=2 tw=80: */
/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this file,
 * You can obtain one at http://mozilla.org/MPL/2.0/. */

#ifndef x25519_vectors_h__
#define x25519_vectors_h__

#include <string>
#include <vector>

typedef struct x25519_testvector_str {
  uint32_t id;
  std::vector<uint8_t> Private;
  std::vector<uint8_t> Public;
  std::vector<uint8_t> Secret;
} x25519_testvector;

// ChaCha20/Poly1305 Test Vector 1, RFC 7539
// <http://tools.ietf.org/html/rfc7539#section-2.8.2>
// ChaCha20/Poly1305 Test Vector 2, RFC 7539
// <http://tools.ietf.org/html/rfc7539#appendix-A.5>
const chacha_testvector kx25519Vectors[] = {
  
   };

#endif  // chachapoly_vectors_h__
