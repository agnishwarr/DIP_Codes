def lzw_compress(data):
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}
    result = []
    current_sequence = ""
    for symbol in data:
        new_sequence = current_sequence + symbol
        if new_sequence in dictionary:
            current_sequence = new_sequence
        else:
            result.append(dictionary[current_sequence])
            dictionary[new_sequence] = dictionary_size
            dictionary_size += 1
            current_sequence = symbol
    if current_sequence:
        result.append(dictionary[current_sequence])
    return result
def lzw_decompress(compressed_data):
    dictionary_size = 256
    dictionary = {i: chr(i) for i in range(dictionary_size)}
    result = ""
    previous_sequence = chr(compressed_data.pop(0))
    result += previous_sequence
    for code in compressed_data:
        current_sequence = ""
        if code in dictionary:
            current_sequence = dictionary[code]
        elif code == dictionary_size:
            current_sequence = previous_sequence + previous_sequence[0]
        result += current_sequence
        dictionary[dictionary_size] = previous_sequence + current_sequence[0]
        dictionary_size += 1
        previous_sequence = current_sequence
    return result
image_data = "wabbawabba"
compressed_data = lzw_compress(image_data)
print("Compressed data:", compressed_data)
decompressed_data = lzw_decompress(compressed_data)
print("Decompressed data:", decompressed_data)
