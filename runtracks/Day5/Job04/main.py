import string
# Cesar Upgraded
alphabet = string.ascii_lowercase + " " + string.ascii_uppercase + ".,;!?-_#&@%/\<>" + string.digits

def Rot_Cypher(value, source):
    return "".join([alphabet[ (alphabet.find(character) + value ) % len(alphabet) ] for character in source])

def Rot_Decypher(value, source):
    return "".join([alphabet[ (alphabet.find(character) + len(alphabet)-value ) % len(alphabet) ] for character in source])

# exec
key = 13
phrase = "Welcome / To \ My World - prog88 & Jeff @!"
encrypted = Rot_Cypher(key, phrase)
print(encrypted)
decrypted = Rot_Decypher(key, encrypted)
print(decrypted)