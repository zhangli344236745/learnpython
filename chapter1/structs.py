import struct
import json

info = b"test.txt"
print(info)
print(type(info))
print(len(info))
res = struct.pack("i",len(info))
print(len(res))

real_len = struct.unpack("i",res)
print(real_len)

data_dict = {
    "file_name": "path",
    "file_size": 33
}

data_json = json.dumps(data_dict)
print(len(data_json.encode("utf-8")))
res = struct.pack("i",len(data_json.encode("utf-8")))
print(len(res))