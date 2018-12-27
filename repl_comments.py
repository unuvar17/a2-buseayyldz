from hashlib import sha256


def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
 

password = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"

password_input = input ("Enter Password: ")

password_input_hash = create_hash(password_input)
       
while password == password_input_hash:
           print ("Enter your comment")
           comment = input()
if password != password_input_hash:
           print ("I'm sorry I can’t let you do that.")

