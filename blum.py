

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 2147483647
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        # 17
        result = 0
        for c in str1:
            code = ord(c)
            result += result * 17 + code
        # реализация ...
        return result % self.filter_len
    def set_bit(self,v, index, set_b):
        mask = 1 << index # маска с единственным битом 1
        v &= ~mask # очищаем в значении v этот бит - ставим 0
        if set_b:
            v |= mask # если этот бит надо в 1 установить
        return v

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result += result * 223 + code
        return result % self.filter_len

    def add(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        self.filter = set_bit(self.filter,h1,True)
        self.filter = set_bit(self.filter,h2,True)
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        if self.filter << h1 & 1 and self.filter << h2 & 1:
            return True
        return False
s = BloomFilter(32)
s.add("1561651561561")
print(s.is_value("1561651561561"))