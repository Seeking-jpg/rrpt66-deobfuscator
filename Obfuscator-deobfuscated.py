import os
from cryptography.fernet import Fernet
import base64
import random
import marshal
import zlib
from colorama import Fore, init
import string

init()
os.system('clear||cls')
cmd = 'mode 115,25'
os.system(cmd)

file = input(f"                                           {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.WHITE} Enter Your File Name : {Fore.RESET}")
os.system('clear||cls')
junksor = input(f"                           {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.WHITE} Do you want junk code injected into your code? [yes/no] : {Fore.RESET}").lower()

with open(file, encoding="utf-8") as file:
    data = file.read()

original_code = data

# Obfuscate code using multiple encoding layers with added random strings
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def moonwalk_style_code():
    # This function simulates a "moon walk" style with reversed and complex operations
    return f"""
def {generate_random_string()}():
    # Simulate moon walk style
    reversed_data = ''.join(reversed("{generate_random_string(50)}"))
    processed_data = base64.b64decode(reversed_data)
    print(processed_data)
    result = sum(ord(c) for c in processed_data)
    return result
"""

obfuscated = base64.b64encode(base64.b32encode(zlib.compress(marshal.dumps(original_code.encode()))))[::-1]
gotobase64 = base64.b64encode(obfuscated)
gotobase64x2 = base64.b64encode(gotobase64)
gotobase32 = base64.b32encode(gotobase64x2)
gotobase64x3 = base64.b64encode(gotobase32)

randomnum = random.randint(10, 500)
randomnum2 = random.randint(10, 500)
randomnum3 = random.randint(10, 500)
randomnum4 = random.randint(10, 500)
randomnum5 = random.randint(10, 500)

def genjunk():
    rand_str = generate_random_string()
    return f"""
def {random.choice(['process', 'handle', 'manage', 'operate'])}{random.randint(10000, 99999)}_{rand_str}():
    # Randomly generated function to obfuscate code
    {random.choice(['value', 'result', 'data', 'info'])}_{rand_str} = {random.randint(10000, 99999)}
    if {random.randint(10000, 99999)} % 2 == 0:
        print({random.randint(10000, 99999)})
        var1 = {random.randint(10000, 99999)}
        var2 = {random.randint(10000, 99999)}
        result = var1 + var2
        return result
    else:
        print("Alternate path executed")
        value = {random.randint(10000, 99999)}
        dummy_var = {random.randint(10000, 99999)}
        return value
"""

def junkgenerator(junkrange):
    junks = ''
    for a in range(junkrange):
        junks += genjunk()
    return junks

stubkey = Fernet.generate_key()
cipher = Fernet(stubkey)
encrypted_data = cipher.encrypt(gotobase64x3)
newdata = encrypted_data.decode()
hex_str = newdata.encode().hex()

stub = f"""__CRACK_ME__ = ''
{junkgenerator(2567)}
import base64 as ______; import marshal as ____; import zlib as __________; from cryptography.fernet import Fernet
import base64; import os; import random; import string
__mikey__="{base64.b64encode(stubkey).decode()}"; mydata="{hex_str}";
__CMC__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))))
__mycip__= Fernet(base64.b64decode(__mikey__))
__step1__=bytes.fromhex(mydata); __step2__=__mycip__.decrypt(__step1__)
__decr__=base64.b64decode(__step2__); __decrdata__=__decr__; __gotnew__=base64.b32decode(__decr__)
__newdecr__={random.randint(999999,999999999999)}; __getnew__=__newdecr__
__myb64code__=base64.b64decode(__gotnew__); __myb64codee__=base64.b64decode(__myb64code__)
___ = __myb64codee__; exec(__CMC__(___))
{junkgenerator(2567)}
{moonwalk_style_code()}
"""

stub2 = f"""__CRACK_ME__ = ''
import base64 as ______; import marshal as ____; import zlib as __________; from cryptography.fernet import Fernet
import base64; import os; import random; import string
__mikey__="{base64.b64encode(stubkey).decode()}"; mydata="{hex_str}";
__CMC__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))))
__mycip__= Fernet(base64.b64decode(__mikey__))
__step1__=bytes.fromhex(mydata); __step2__=__mycip__.decrypt(__step1__)
__decr__=base64.b64decode(__step2__); __decrdata__=__decr__; __gotnew__=base64.b32decode(__decr__)
__newdecr__={random.randint(999999,999999999999)}; __getnew__=__newdecr__
__myb64code__=base64.b64decode(__gotnew__); __myb64codee__=base64.b64decode(__myb64code__)
___ = __myb64codee__; exec(__CMC__(___))
"""

if junksor == 'yes':
    filename = 'Obfuscated(Junk).py'
    with open(filename, "w") as file:
        file.write(stub)
elif junksor == 'no':
    filename = 'Obfuscated(Classic).py'
    with open(filename, "w") as file:
        file.write(stub2)

os.system('clear||cls')
print(f'                                              {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.GREEN} Code obfuscated!{Fore.RESET}\n                                            {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET}{Fore.GREEN} {filename}{Fore.RESET}\n\n')
input(f'                            {Fore.LIGHTCYAN_EX}[{Fore.RESET}{Fore.CYAN}+{Fore.RESET}{Fore.LIGHTCYAN_EX}]{Fore.RESET} If you want to convert your obfuscated code to exe, \n        first copy the modules in your original code and paste them in the top line of your obfuscated code.\n')
