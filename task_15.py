import re

class BlockTranspositionCipher:
    @staticmethod
    def check_key(key):
        key = key.lower()
        if len(key) == 0 or len(key) > 26 or len(key) != len(set(key)): return False
        elif re.search(r'[^a-z]', key): return False
        return True

    def __init__(self, text, key, decrypt = False):
        if text is None or key is None or type(text) is not str or type(key) is not str: raise ValueError("Invalid data type")
        if self.check_key(key) is False: raise ValueError("Invalid key: {}".format(key))
        key = key.lower()
        if len(text) < len(key): text += ' ' * (len(key) - len(text))
        elif len(text) % len(key) != 0: text += ' ' * (len(key) - len(text) % len(key))
        self.__decrypt = decrypt
        self.__blocks = [text[i:i + len(key)] for i in range(0, len(text), len(key))]
        key_numbers = [ord(char) - 97 for char in key]
        key_numbers_sorted = sorted(key_numbers)
        if self.__decrypt:
            key_numbers_sorted, key_numbers = key_numbers, key_numbers_sorted
        for idx, chunk in enumerate(self.__blocks):
            chunk_dict = dict(zip(key_numbers_sorted, chunk))
            self.__blocks[idx] = ''.join(chunk_dict[num] for num in key_numbers)

    def get_result(self):
        result = ''.join(self.__blocks)
        if self.__decrypt: result = result.strip()
        return result

    def __iter__(self):
        self.__current_pointer = 0
        return self

    def __next__(self):
        if self.__current_pointer == len(self.__blocks): raise StopIteration
        self.__current_pointer += 1
        return self.__blocks[self.__current_pointer - 1]

main_key = "cab"
text_to_encrypt = "PYTHON"
cipher = BlockTranspositionCipher(text_to_encrypt, main_key)
print("Ключ: '{}', Исходная строка: '{}'".format(main_key, text_to_encrypt))
print("\nПроцесс шифрования по блокам:")
for ix, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {ix}: '{encrypted_block}'")
encrypted = cipher.get_result()
print("Зашифрованная строка: '{}'".format(encrypted))

cipher = BlockTranspositionCipher(encrypted, main_key, decrypt = True)
print("\nПроцесс дешифрования по блокам:")
for ix, decrypted_block in enumerate(cipher, 1):
    print(f"Блок {ix}: '{decrypted_block}'")
print("Расшифрованная строка: '{}'".format(cipher.get_result()))