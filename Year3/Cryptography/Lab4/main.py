import streamlit as st
import textwrap


def initial_permutation(block):
    # Initial Permutation (IP) table
    IP = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]

    return ''.join(block[i - 1] for i in IP)


def final_permutation(block):
    # Final Permutation (IP^-1) table
    FP = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25]

    return ''.join(block[i - 1] for i in FP)


def expansion(block):
    # Expansion table
    E = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]

    return ''.join(block[i - 1] for i in E)


def s_box_substitution(block):
    # S-boxes
    S_BOXES = [
        # S1
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
        # S2-S8 would go here...
    ]

    # For demonstration, we'll use just S1 box for all substitutions
    result = ""
    for i in range(0, 48, 6):
        chunk = block[i:i + 6]
        row = int(chunk[0] + chunk[5], 2)
        col = int(chunk[1:5], 2)
        val = S_BOXES[0][row][col]
        result += format(val, '04b')

    return result


def p_box_permutation(block):
    # P-box permutation table
    P = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]

    return ''.join(block[i - 1] for i in P)


def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_hex(binary):
    return hex(int(binary, 2))[2:].upper()


def des_single_round(message, block_index, key):
    # Convert message to binary
    binary_message = text_to_binary(message)

    # Split into 64-bit blocks
    blocks = textwrap.wrap(binary_message, 64)

    # Pad last block if necessary
    if len(blocks[-1]) < 64:
        blocks[-1] = blocks[-1].ljust(64, '0')

    if block_index >= len(blocks):
        return "Error: Block index out of range"

    # Get the specified block
    block = blocks[block_index]

    # Initial Permutation
    block = initial_permutation(block)

    # Split block into left and right halves
    left = block[:32]
    right = block[32:]

    # Expansion
    expanded_right = expansion(right)

    # XOR with key
    key_binary = format(int(key, 16), '048b')
    xored = ''.join('1' if a != b else '0' for a, b in zip(expanded_right, key_binary))

    # S-box substitution
    substituted = s_box_substitution(xored)

    # P-box permutation
    permuted = p_box_permutation(substituted)

    # XOR with left half
    new_right = ''.join('1' if a != b else '0' for a, b in zip(left, permuted))

    # Combine for final block
    final_block = right + new_right

    # Final Permutation
    result = final_permutation(final_block)

    # Convert to hexadecimal
    hex_result = binary_to_hex(result)

    return hex_result


def main():
    st.title("Single Round DES Encryption")

    # Input fields
    message = st.text_area("Enter message:", value="The Data Encryption Standard...")
    block_index = st.number_input("Enter block index:", min_value=0, value=0)
    key = st.text_input("Enter 48-bit key (in hex):", value="123456789ABC")

    if st.button("Encrypt"):
        if len(key) != 12:  # 48 bits = 12 hex characters
            st.error("Key must be exactly 48 bits (12 hex characters)")
        else:
            try:
                result = des_single_round(message, block_index, key)
                st.success(f"Encrypted block {block_index} (hex): {result}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()