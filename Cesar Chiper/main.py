#SE 104 Assignment (Due April 17, 2020 13:00)
#Ayberk SAYGI
#Student No.:201928029

text = input("What is your text? ")
shift = int(input("What is your shift? "))

def caesarencryption(text, shift):
  EncryptedText = ""
  for ch in text:
    if ch.isalpha():                             #Checked whether a character is an alphabet or not.
      stayInAlphabet = ord(ch) + shift
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      elif stayInAlphabet > ord('Z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      EncryptedText += finalLetter
  print ("Your Encrypted Text Is: ", EncryptedText)
  return EncryptedText

caesarencryption(text, shift)