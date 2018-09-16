# solve-caesar
decrypting a caesar encrypted text with unknown shift
'''python
import caesar_kit


# message : CAESAR SHIFTED CIPHER TEXT
encrypted_text = '''
gb zl ynjlre :
V’z qvibeprq. Fubhyq V fryy zl rk-jvsr’f $10X qvnzbaq evat gb ohl n qbt ?
V unir pbzr bhg ng na naahny ybff bs $5,000.00 gb $10,000.00 orpnhfr V unccra gb fcraq zber zbarl ba zl qbtf naq arire urfvgngr gb ohl gurz gur irel orfg..

'''

# Use .Break method to Decrypt CAESAR SHIFTED CIPHER TEXT
decrypt = caesar_kit.Break( encrypted_text )

# print decrypted plain text 
print ( decrypt )


# use .cipher_dict() to get Cipher dictionary
print ( decrypt.cipher_dict() )
'''
