


class Encrypt :
    
    
    def __init__(self,text,key):
        self.text = text
        self.key = key
        
    def Cipher(shift=0):
        return [chr((c + shift) % 26 + ord('a')) for c in range(26)]
    alphabets = Cipher()

    def cipher_dict (self):
        return {key: value for (key, value) in zip(Encrypt.alphabets,Encrypt.Cipher(self.key)) }

    def __repr__(self): 
        plain = self.alphabets
        ciphers = Encrypt.Cipher(self.key)
        
        cipher_text = ''
        for c in self.text:
            if 'a' <= c <= 'z':
                cipher_text += ciphers[plain.index(c)]
            else:
                cipher_text += c
        return cipher_text
    
        



class Break :
    
    
    def __init__(self,text):
        self.text = text
    def shifts(self):
        from collections import Counter
        e = (Counter(self.text.replace(' ','')).most_common()[0][0])
        return ord(e) - ord('e')

    def cipher_dict (self):
        return {key: value for (key, value) in zip(Encrypt.alphabets,Encrypt.Cipher(self.shifts())) }

    def __repr__ (self):
        
        plain = Encrypt.alphabets
        cipher = Encrypt.Cipher(self.shifts())
        plain_text = ''
        for c in self.text:
            if 'a' <= c <= 'z':
                plain_text += plain[cipher.index(c)]
            else:
                plain_text += c
        return plain_text
    def brut_force(self) :
        return [Encrypt(self.text,i) for i in range(27)]


class decrypt: 
    def __init__(self,text,key):
        self.text = text
        self.key = key
    def cipher_dict (self):
        return {key: value for (key, value) in zip(Encrypt.alphabets,Encrypt.Cipher(self.key)) }

    def __repr__ (self):
        plain = Encrypt.alphabets
        cipher = Encrypt.Cipher(self.key)
        plain_text = ''
        

        for c in self.text:
            if 'a' <= c <= 'z':
                plain_text += plain[cipher.index(c)]
            else:
                plain_text += c
        return plain_text
       



encrypted_text = Encrypt("seed to others baby new born eseet",55)


print("encrypted text:",encrypted_text)

decrypted_text = decrypt("vhhg wr rwkhuv edeb qhz eruq hvhhw",3)
print(decrypted_text)


breaked_text = Break("d b n")
print("break:",breaked_text)
print("break:",breaked_text.shifts())


print(breaked_text.brut_force())