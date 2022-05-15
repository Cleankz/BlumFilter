
class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = []
        for i in range(self.filter_len):
            self.filter.append(0)
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        # 17
        result = 0
        for c in str1:
            code = ord(c)
            result += (result * 17 + code) % self.filter_len
        # реализация ...
        return result

    def hash2(self, str1):
        result = 0
        for c in str1:
            code = ord(c)
            result += (result * 223 + code) % self.filter_len
        return result

    def add(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        self.filter[h1] = 1
        self.filter[h2] = 1
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        if self.filter[h1] == 1 and self.filter[h2] == 1:
            return True
        return False
        # проверка, имеется ли строка str1 в фильтре
с = BloomFilter(32)
