#def is_odd(n):
 #   return n % 2 == 1
from unittest import result


#print(is_odd(12))


#def is_leap_year(year):
 #   if year % 400 == 0:
  #      return True
   # elif year % 100 == 0:
    #    return False
    #elif year % 4 == 0:
     #   return True
   # else:
    #    return False
#print (is_leap_year(2100))


# def triangle_number(n):
#     total = 0
#     for i in range(1, n + 1):
#         total = total + i
#         print(i, total)
# print(triangle_number(5))


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print (is_prime(21))


# def reverse(s):
#     result = ''
#     for ch in s:
#         result = ch + result
#     return result
# print(reverse("hello"))


#print(reverse("hello world"))
#def reverse_slice(s):
 #   return s[::-1]
#print(reverse_slice("hello world"))


# def remove_all_occurrences(sub, s):
#     return s.replace(sub, '')
# print(remove_all_occurrences("l", "hello"))


# def substitude(message, key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = ch + result
#
#         elif ch.isupper():
#             result + result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
# key = "qtgjdeotlprpşaxbvnlgznklurkfp"
# print(substitude("canberk", key))


# def remove_dups(s):
#     result = ""
#     for ch in s:
#         if ch.lower() not in result.lower():
#             result = result + ch
#     return result
# print(remove_dups("hello world"))