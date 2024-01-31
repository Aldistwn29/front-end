# cara melalukan import liberary terdapat 2 cara yaitu dengan 1 . import library sebagai alias 
                                                             # 2 . langsung merujuk pada objek
# cara 1 . import library sebagai alias        
# import library array
# import array as arr

# array_integer = arr.array('i',[1,2,3,4])
# array_char1 = arr.array('u',['N','u','S','A'])
# array_char2 = arr.array('u',['P','u','T','R','a'])
# array_double = arr.array('d',[10.5,20.3,6.5])
# print(array_char1[0])
# print(array_integer[2])
# print(array_char2[4])
# print(array_double[1])

# cara kedua langsung merujuk pada objek
# import library array
# from array import array

# array_integer = array('i',[1,2,3,4])
# array_char1 = array('u',['N','u','S','A'])
# array_char2 = array('u',['P','u','T','R','a'])
# array_double = array('d',[10.5,20.3,6.5])
# print(array_char1[0])
# print(array_integer[2])
# print(array_char2[4])
# print(array_double[1])

# menambahkan array 

# # dengan menggunakan insert dan append
# from array import array

# array_integer = array('i',[1,2,3,4])
# array_char1 = array('u',['N','u','S','A'])
# array_char2 = array('u',['P','u','T','R','a'])
# array_double = array('d',[10.5,20.3,6.5])

# array_integer.insert(1,6)
# array_integer.append(10)
# print(array_integer)

# mengghappus dengan remove dan pop 
# pop
# from array import array

# array_integer = array('i',[1,2,3,4])
# array_char1 = array('u',['N','u','S','A'])
# array_char2 = array('u',['P','u','T','R','a'])
# array_double = array('d',[10.5,20.3,6.5])

# array_integer.pop(0)
# print(array_integer)
# remove

# from array import array

# array_integer = array('i',[1,2,3,4])
# array_char1 = array('u',['N','u','S','A'])
# array_char2 = array('u',['P','u','T','R','a'])
# array_double = array('d',[10.5,20.3,6.5])

# array_integer.remove(4)
# print(array_integer)
# kombinasi remove dgn insert dan append

# from array import array

# array_integer = array('i',[1,2,3,4])
# array_char1 = array('u',['N','u','S','A'])
# array_char2 = array('u',['P','u','T','R','a'])
# array_double = array('d',[10.5,20.3,6.5])

# array_integer.insert(1,6)
# array_integer.append(10)
# array_integer.remove(4)
# print(array_integer)

# kombinas pop dgn insert dan append 

from array import array

array_integer = array('i',[1,2,3,4])
array_char1 = array('u',['N','u','S','A'])
array_char2 = array('u',['P','u','T','R','a'])
array_double = array('d',[10.5,20.3,6.5])

array_integer.insert(1,6)
array_integer.append(10)
array_integer.pop(0)
print(array_integer)

#   searching  array dgn menggunakan index 
# contoh harus mengguanakan kombinasi insert , append 
# from array import array

# array_integer = array('i',[1,2,3,4])
# array_char1 = array('u',['N','u','S','A'])
# array_char2 = array('u',['P','u','T','R','a'])
# array_double = array('d',[10.5,20.3,6.5])

# array_integer.insert(1,6)
# array_integer.append(10)
# print(array_integer)
# print(array_integer.index(10))


# contoh indeex kombinasi dgn inser , append , dan pop
# from array import array

# array_integer = array('i',[1,2,3,4])
# array_char1 = array('u',['N','u','S','A'])
# array_char2 = array('u',['P','u','T','R','a'])
# array_double = array('d',[10.5,20.3,6.5])

# array_integer.insert(1,6)
# array_integer.append(10)
# array_integer.pop(2)
# print(array_integer)
# print(array_integer.index(10))

# # contoh indeex kombinasi dgn inser , append , dan remove

# from array import array

# array_integer = array('i',[1,2,3,4])
# array_char1 = array('u',['N','u','S','A'])
# array_char2 = array('u',['P','u','T','R','a'])
# array_double = array('d',[10.5,20.3,6.5])

# array_integer.insert(1,6)
# array_integer.append(10)
# array_integer.remove(6)
# print(array_integer)
# print(array_integer.index(10))


