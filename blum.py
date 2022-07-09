

class BloomFilter:

    def __init__(self, input_filter_len): # было f_len, начальная длина фильтра
        self.filter_len = input_filter_len
        self.filter_of_bytes = 1 << input_filter_len # было self.filter
        # создаём битовый массив длиной f_len ...


    def hash_function_1(self, input_str):# было str_1 - входная строка, было hash1 - фнукция рассчитывающая hash функцию
        # 17
        result_of_hash_function = 0 # было result - результат вычислений
        for letter in input_str:# было str1, было c
            letter_to_num = ord(let)# было code - преобразует символ строки в числовое представление
            result_of_hash_function +=  result_of_hash_function * 17 + letter_to_num
        # реализация ...
        return result_of_hash_function % self.filter_len

    def hash_function_2(self, input_str):#было hash2
        result_of_hash_function = 0
        for letter in input_str:
            letter_to_num = ord(letter)
            result_of_hash_function += result_of_hash_function * 223 + letter_to_num
        return result_of_hash_function % self.filter_len

    def add_str_to_filter(self, str1):# было add - добавляет строку в  битовый массив
        result_of_hash_function_1 = self.hash1(str1) # было h1, результат вычислений первой хэш функции
        result_of_hash_function_2 = self.hash2(str1) # было h2, результат вычислений второй хэш функции
        self.filter_of_bytes = self.set_bit(self.filter_of_bytes,result_of_hash_function_1,True)
        self.filter_of_bytes = self.set_bit(self.filter_of_bytes,result_of_hash_function_2,True)
        # добавляем строку str1 в фильтр
        
    def set_bit(self,v, index, set_bytes): # было set_b логическая переменная 
        mask = 1 << index # маска с единственным битом 1
        if set_bytes:
            v |= mask # если этот бит надо в 1 установить
            return v
        v &= ~mask # очищаем в значении v этот бит - ставим 0
        return v

    def is_value_in_filter(self, input_str):# было is_value функция проверяющая есть ли строка в массиве
        result_of_hash_function_1 = self.hash_function_1(input_str) # hash1
        result_of_hash_function_2 = self.hash_function_2(input_str) # hash2
        if (self.filter_of_bytes & (1 << result_of_hash_function_1))!=0 and self.filter_of_bytes & (1 << result_of_hash_function_2))!=0:
            return True
        return False
# s = BloomFilter(32)
# s.add("1561651561561")
# print(s.is_value_in_filter("1561651561501"))
