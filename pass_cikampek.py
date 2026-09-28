import random, string
karakter = string.ascii_letters + string.digits + "!@#$%"
password = "".join(random.choice(karakter) for i in range(12))
print(f"Password Baru: {password}")
