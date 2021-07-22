totalAlphabets = "abcdefghijklmnopqrstuvwxyz"
string = input("Enter the string to be encrypted and then decrypted:")
string = string.lower()
encryption, decryption = "", ""
key = int(input("Enter the key:"))

for alphabet in string:
    new_placeValue = (totalAlphabets.find(alphabet)+key) % len(totalAlphabets)
    encryption += totalAlphabets[new_placeValue]

for alphabet in encryption:
    new_placeValue = (totalAlphabets.find(alphabet)+key) % len(totalAlphabets)
    decryption += totalAlphabets[new_placeValue]

print("Encrypted text:", encryption)
print("Decrypted text:", decryption)
