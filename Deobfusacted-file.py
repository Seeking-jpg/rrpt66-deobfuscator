import base64
from cryptography.fernet import Fernet
import pickle  # Assuming it's using pickle in `__CMC__` for deserialization.

# The key and data
__mikey__ = 'blahblahKEY'
mydata = 'blashblah code'

# Decryptor function
def decrypt():
    # Step 1: Convert `mydata` from hex to bytes
    __step1__ = bytes.fromhex(mydata)
    
    # Step 2: Use the Fernet cipher to decrypt
    __mycip__ = Fernet(base64.b64decode(__mikey__))
    __step2__ = __mycip__.decrypt(__step1__)
    
    # Step 3: Base64 decode the result of decryption
    __decr__ = base64.b64decode(__step2__)
    
    # Step 4: Base32 decode the result
    __gotnew__ = base64.b32decode(__decr__)
    
    # Step 5: Base64 decode the result again
    __myb64code__ = base64.b64decode(__gotnew__)
    __myb64codee__ = base64.b64decode(__myb64code__)
    
    # At this point, __myb64codee__ should be the final decrypted data
    print("Decrypted Data (after all decoding steps):")
    print(__myb64codee__)
    
    try:

        data = pickle.loads(__myb64codee__)
        print("Successfully loaded data using pickle:")
        print(data)
    except Exception as e:
        print("Could not load data using pickle. It's likely not a pickle object.")
        print(e)
    

    try:
        exec(__myb64codee__.decode('utf-8'))
        print("Successfully executed the code.")
    except Exception as e:
        print("Execution failed:")
        print(e)

decrypt()
