"""
CheckBadChars.py 
Author: snowcra5h@icloud.com

For OSED students, this script will find the hex values that do not contain any bad characters.
These may be PPR values that can be used to jump to the shellcode.

    - The bad characters are defined in the bad_chars list.
    - The hex values are defined in the hex_values list.
    - The script will print out the hex values that do not contain any bad characters.

"""

from typing import List


def check_bad_chars(byte_str: bytes, bad_chars: List[int]) -> bool:
    for bc in bad_chars:
        if bc in byte_str:
            return True
    return False


def main():
    bad_chars = [0x00, 0x02, 0x09, 0x0a, 0x0d, 0x20]
    hex_values = [0x1000878d, 0x100087b8, 0x100020ca, 0x100087d9, 0x1001bb0a, 0x1001bb9f, 0x10049044, 0x1006eb74, 0x1006eb7b, 0x1008868a, 0x100886e0, 0x10088b5d, 0x10088b88, 0x10088b9a, 0x10088ba9, 0x1008921b, 0x10089241, 0x10089b57, 0x10089be3, 0x1008a4a3, 0x1008a4c2, 0x1008a525, 0x1008a538, 0x1008ae39, 0x1008aebf,
                  0x1008afcc, 0x1008afd5, 0x100999f2, 0x1009a328, 0x100a3f1b, 0x100b7019, 0x100b7043, 0x101073c9, 0x101220f9, 0x1012cfa0, 0x1012d082, 0x1012fb3e, 0x10130103, 0x1013017f, 0x101301c0, 0x101301f5, 0x10133edf, 0x10133fdb, 0x1013417f, 0x10134198, 0x1013ae22, 0x1013ae2d, 0x1013ae38, 0x1013f6c4, 0x101541dd, 0x10154204, 0x101591c4]

    hex_values = [bytes.fromhex(hex(x)[2:]) for x in hex_values]

    good_values = []
    for hex_value in hex_values:
        if not check_bad_chars(byte_str=hex_value, bad_chars=bad_chars):
            good_values.append(hex_value.hex())
    print("[+] good values found:")
    for good_value in good_values:
        print(f"0x{good_value}")


if __name__ == '__main__':
    main()
