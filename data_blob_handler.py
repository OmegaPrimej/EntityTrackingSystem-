import os
import cryptography
from cryptography.fernet import Fernet
import hashlib
import hmac
import base64
Settings
DATA_BLOB_DIR = './data_blobs/'
DATA_BLOB_PREFIX = 'ENX_data_blob_'
DATA_BLOB_EXT = '.bin'
START_ID = 1
END_ID = 217
for id in range(START_ID, END_ID+1):
    file_name = f"{DATA_BLOB_PREFIX}{str(id).zfill(3)}{DATA_BLOB_EXT}"
    file_path = os.path.join(DATA_BLOB_DIR, file_name)
    print(f"Processing {file_path}...")
    # Add processing logic here, e.g., decryption or analysis
Settings
DATA_BLOB_DIR = './data_blobs/'
DATA_BLOB_PREFIX = 'ENX_data_blob_'
DATA_BLOB_EXT = '.bin'
START_ID = 1
END_ID = 217
Erebus Initiative decryption key (replace with actual key)
DECRYPTION_KEY_HASH = hashlib.sha256(b"er3bUs1n1ti@t1v3_k3y").digest()
DECRYPTION_KEY = base64.urlsafe_b64encode(DECRYPTION_KEY_HASH)
def authenticate_data_blob(file_path, expected_hmac):
    # Calculate HMAC for data blob
    calculated_hmac = hmac.new(DECRYPTION_KEY_HASH, open(file_path, 'rb').read(), hashlib.sha256).digest()
    return hmac.compare_digest(calculated_hmac, expected_hmac)
def decrypt_data_blob(file_path):
    cipher_suite = Fernet(DECRYPTION_KEY)
    decrypted_data = cipher_suite.decrypt(open(file_path, 'rb').read())
    return decrypted_data
for id in range(START_ID, END_ID+1):
    file_name = f"{DATA_BLOB_PREFIX}{str(id).zfill(3)}{DATA_BLOB_EXT}"
    file_path = os.path.join(DATA_BLOB_DIR, file_name)
    
    # Assume HMAC values are stored separately (replace with actual HMAC values)
    expected_hmac = hashlib.sha256(f"ENX_HMAC_{str(id).zfill(3)}".encode()).digest()
    
    print(f"Processing {file_path}...")
    
    if authenticate_data_blob(file_path, expected_hmac):
        print(f"Data blob {id} authentication successful.")
        decrypted_data = decrypt_data_blob(file_path)
        print(f"Decrypted data blob {id}: {decrypted_data}")
    else:
        print(f"Data blob {id} authentication failed. Potential tampering detected.")
