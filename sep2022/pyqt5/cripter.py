from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)



def encrypt(filename, key):
    f = Fernet(key) 
    myfile = open(filename, "rb")
    file_data = myfile.read()
    encrypted_data = f.encrypt(file_data)

    myfile_two = open(filename, "wb")
    myfile_two.write(encrypted_data)
    myfile_two.close()


encrypt("afiletobeencripted.txt", key)
