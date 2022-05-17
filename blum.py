

class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = [0] * self.filter_len
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        # 17
        result = 0
        for c in str1:
            code = ord(c)
            result += result * 17 + code
        # реализация ...
        return result % self.filter_len

    def hash2(self, str1):
        # x = "d"
        # a = format(ord(x),"b")
        # ''.join(format(ord(x), '08b'))
        result = 0
        for c in str1:
            code = ord(c)
            result += result * 223 + code
        return result % self.filter_len

    def add(self, str1):
        # str_encode = bytes(str1,"utf-8")
        # for byte in str_encode:
        #     for bit in byte:
        #         self.filter.append(bit)
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        self.filter[h1] = 1
        self.filter[h2] = 1
        # str_one = bytes(my_str, ‘utf-8’)
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
        h1 = self.hash1(str1)
        h2 = self.hash2(str1)
        if self.filter[h1] == 1 and self.filter[h2] == 1:
            return True
        return False
# c = BloomFilter(32)
# c.add("0123456789")
# c.add("1234567890")
# c.add("8901234567")
# c.add("9012345678")
# c.add("123456")
# bytearray
# a = [None] * 32
# print(type(a))
# bitarray60000 = 1<<60000
# print( type(bitarray60000))
# print(bitarray60000 | 1<<2)
# x = 0 # empty
# x |= 1<<19
# print(x)
# res = []
# for byte in a:
#     for bit in byte:
#         res.append(bit)
# print(res)
# result = []
# s = "0123456789"
# for c in s:
#     bits = bin(ord(c))[2:]
#     bits = '00000000'[len(bits):] + bits
#     result.extend([int(b) for b in bits])
# print(result)
# c = BloomFilter(32)
# c.hash2("dfds")
# x = "5"
# t = 123456789
# a = bytes(x, 'utf-8')
# b = x.encode('utf-8')
# h = ''.join(format(ord(x), '08b'))
# z = bin(t)
# # a = "08b" + ''.join(format(ord(x), '08b'))
# print(c.to_bin())
# # print(int(bin(50),2))
# # print(type(a))
# # print(type(b))
# # print(type(z))