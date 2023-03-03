
from __future__ import annotations

class XORCipher:
    def __init__(self,key:int = 0):
        self.__key = key

    def encrypt(self,content:str,key:int) -> list[str]:
        assert isinstance(key,int) and isinstance(content,str)
        key = key or self.__key or 1
        key %= 255
        return [chr(ord(ch) ^ key) for ch in content]

    def decrypt(self,content:str,key:int) -> list[str]:
        assert isinstance(key, int) and isinstance(content, list)

        key = key or self.__key or 1

        # make sure key is an appropriate size
        key %= 255

        return [chr(ord(ch) ^ key) for ch in content]

    def encrypt_string(self,content: str, key :int = 0) -> str:
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1
        while key > 255:
            key -= 255

        ans = ""
        for ch in content:
            ans += chr(ord(ch) ^ key)
        return ans

    def decrypt_string(self, content: str, key: int = 0) -> str:
        """
        input: 'content' of type string and 'key' of type int
        output: decrypted string 'content'
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(key, int) and isinstance(content, str)

        key = key or self.__key or 1

        # make sure key can be any size
        while key > 255:
            key -= 255

        # This will be returned
        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)
        return ans

    def encrypt_file(self,file: str,key:int = 0) -> bool:
        assert isinstance(file, str) and isinstance(key, int)
        try:
            with open(file) as fin:
                with open("encrypt.out","w+") as fout:
                    for line in fin:
                        fout.write(self.encrypt_string(line,key))
        except OSError:
            return False
        return True

    def decrypt_file(self, file: str, key: int) -> bool:
        """
        input: filename (str) and a key (int)
        output: returns true if decrypt process was
        successful otherwise false
        if key not passed the method uses the key by the constructor.
        otherwise key = 1
        """

        # precondition
        assert isinstance(file, str) and isinstance(key, int)

        try:
            with open(file) as fin:
                with open("decrypt.out", "w+") as fout:
                    # actual encrypt-process
                    for line in fin:
                        fout.write(self.decrypt_string(line, key))

        except OSError:
            return False

        return True

crypt = XORCipher()
key = 67
# test encrypt
print(crypt.encrypt("hallo welt",key))
# test decrypt
print(crypt.decrypt(crypt.encrypt("hallo welt",key), key))

# test encrypt_string
print(crypt.encrypt_string("hallo welt",key))

# test decrypt_string
print(crypt.decrypt_string(crypt.encrypt_string("hallo welt",key),key))


if (crypt.encrypt_file("test.txt",key)):
      print("encrypt successful")
else:
      print("encrypt unsuccessful")

if (crypt.decrypt_file("encrypt.out",key)):
      print("decrypt successful")
else:
      print("decrypt unsuccessful")
