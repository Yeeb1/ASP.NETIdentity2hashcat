import argparse
import base64
from binascii import unhexlify, hexlify

def decode_input(input_string):
    decoded_data = base64.b64decode(input_string)
    kind = hexlify(decoded_data[0:1]).decode()

    if kind == '01':
        iter_bytes = decoded_data[1:5]
        salt = base64.b64encode(decoded_data[9:25]).decode()
        subkey = base64.b64encode(decoded_data[25:57]).decode()
        iter_count = int.from_bytes(iter_bytes, 'big')
        hash_algo = 'sha256'
    elif kind == '00':
        salt = base64.b64encode(decoded_data[1:17]).decode()
        subkey = base64.b64encode(decoded_data[17:49]).decode()
        iter_count = 1000
        hash_algo = 'sha1'
    else:
        raise ValueError('Unsupported hash')

    return hash_algo, iter_count, salt, subkey

def main():
    parser = argparse.ArgumentParser(description='Converts ASP.NET Identity (PBKDF2+HMAC-SHA256 and PBKDF2+HMAC-SHA1) to Hashcat format')
    parser.add_argument('input', type=str, help='Base64-encoded ASP.NET Identity')
    args = parser.parse_args()

    try:
        hash_algo, iter_count, salt, subkey = decode_input(args.input)
        print(f"{hash_algo}:{iter_count}:{salt}:{subkey}")
    except ValueError as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
