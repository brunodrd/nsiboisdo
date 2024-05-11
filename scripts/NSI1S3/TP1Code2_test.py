assert convertir_sur_16_bits(0) == '0000000000000000'
assert convertir_sur_16_bits(2**16 - 1) == '1111111111111111'
assert convertir_sur_16_bits(256) == '0000000100000000'