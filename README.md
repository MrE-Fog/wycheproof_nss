scripts/ contains the python scripts to convert wycheproof test vectors to 
NSS C header files. 

Example:
python scripts/generate_chacha_poly_header.py

Source, base and target files need to be specified in the script, if they differ
from the current default.

target/ contains successfully converted test vectors.
Note that they are not formatted nicely. Use clang-format to change that. 

doc.txt contains a documentation of the available wycheproof test vectors, 
which of them are relevant for NSS and a rough description of what needs
to be done to implement each type of test vector for the NSS CI.
