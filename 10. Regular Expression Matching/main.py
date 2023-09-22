class Solution(object):
    def isMatch(self, s, p):
        p = str(p)[::-1]
        s = str(s)[::-1]
        n = 0
        bufor = ""
        bufor2 = ""
        for i, patern in enumerate(str(p)):
            print(i, patern)
            if n == len(str(s)) and patern != '*':
                print('bufor: ', bufor, ',bufor2: ', bufor2,
                      ',patern: ', patern, ',poprzedni', s[n-1])
                if bufor2 == "" and bufor == "" and (s[n-1] != patern or s[n-1] != bufor2):
                    return False
                bufor = ""
            else:
                if patern == "*":
                    bufor = p[i+1]
                elif s[n] == bufor or bufor == '.':
                    while n < len(str(s)) and (s[n] == bufor or bufor == '.'):
                        n += 1
                        print('n', n)
                    else:
                        bufor2 = bufor
                        bufor = ""
                elif s[n] != bufor:
                    if s[n] == patern or patern == '.':
                        n += 1
                    elif bufor == "":
                        break
        print(n)
        if n < len(str(s)):
            return False
        else:
            return True


solution = Solution()
print(solution.isMatch("a", ".*..a*"))

# try:
#             buf = ""
#             n = 0
#             for i, patern in enumerate(str(p)):
#                 print(i, patern)
#                 if patern == "*":
#                     buf = p[i-1]
#                     print("buf", buf)
#                 if s[n] == patern or patern == "." or s[n] == buf or buf == ".":
#                     print('punkcik')
#                     n += 1
#                 elif buf == "" and p[i+1] == '*':
#                     print("siema")
#         except:
#             return False
#         if n == len(s):
#             return True
#         else:
#             return False


# try:
#             for i, litera in enumerate(str(s)):
#                 print(litera, p[i])
#                 if(p[i] == "*"):
#                     buf = p[i-1]
#                     if litera != buf and buf != ".":
#                         print('1', litera, buf)
#                 elif litera != p[i] and p[i] != "." and litera != buf:
#                     if buf == None:
#                         continue
#                     print('2')
#                     return False
#             return True
#         except:
#             print("except")
#             return False


#                     print(litera, p[i-1])
#                     if litera != p[i-1] and p[i-1] != ".":
#                         return False
#                 elif litera != p[i] and p[i] != ".":
#                     print("1")
#                     return False
#             return True
#         except:
#             return False

# s =
# "aab"
# p =
# "c*a*b"
