# solve-caesar
# خوارزمية لكسر شيفرة قيصر
decrypting a caesar encrypted text with unknown shift
```python
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
```
## Encrypting :
```python
import caesar_kit


# message : your text
message = '''
It so good that you are trying to find such communities around.
 This can help you interact with the people of same interests and hence find more opportunities around.
  I am not aware of any Facebook groups, but rather I think there are sites where you can go and find such groups in sites like hacker rank, code chef, hacker earth, code school and so on.
 Maybe u can google about them and you might find some mailing list or IRC channels where you could find such group of people .
'''

# Use .Encrypt method to encrypt message text , 16 is the shift key
encrypt = caesar_kit.Encrypt( message , 16 )

# print encrypted plain text 
print ( encrypt )


# use .cipher_dict() to get Cipher dictionary
print ( encrypt.cipher_dict() )
```
