def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  
  letters = [chr(ord('a') + i) for i in range(26)]
  #numbers = [str(i) for i in range(0,10)]
  #print(numbers)
  x = rotation_factor%26
  y = rotation_factor%10
  #print(x,'x')
  c = 0
  temp = ""
  #print(temp)
  
  for i in input_str:
      if i.lower() in letters:
          index = letters.index(i.lower())
          #print(index,'index',i,'i')
          if index+x>=25:
              index = (index+x)%25-1
              #print(index,'index',letters[index])
          else:
            index = index+x
            #print(index,'index',letters[index])
          #print(letters[index+x-1],'letters[index+x-1]')
          if i.isupper():
              temp += letters[index].upper()
              #print(temp,'temp')
          else:
              temp += letters[index]
              #print(temp,'temp')
      elif i.isdigit():
        if y==0:
          temp+=i
          continue
        m = int(i)
        if m>=9:
            m = m%9 +y-1
        else:
            m=m+y
        temp +=str(m)
      else:
        temp+=i
            
  return temp





###
# Rotational Cipher
# One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
# For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
# Given a string and a rotation factor, return an encrypted string.
# Signature
# string rotationalCipher(string input, int rotationFactor)
# Input
# 1 <= |input| <= 1,000,000
# 0 <= rotationFactor <= 1,000,000
# Output
# Return the result of rotating input a number of times equal to rotationFactor.
# Example 1
# input = Zebra-493?
# rotationFactor = 3
# output = Cheud-726?
# Example 2
# input = abcdefghijklmNOPQRSTUVWXYZ0123456789
# rotationFactor = 39
# output = nopqrstuvwxyzABCDEFGHIJKLM9012345678