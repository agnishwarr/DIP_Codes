def rle_encode(data):
    encoded_data = []
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1
        encoded_data.append((data[i], count))
        i += 1
    return encoded_data
def rle_decode(encoded_data):
    decoded_data = ""
    for symbol, count in encoded_data:
        decoded_data += symbol * count
    return decoded_data
image_data = "AAAABBBCCDAA"
encoded_data = rle_encode(image_data)
print("Encoded data:", encoded_data)
decoded_data = rle_decode(encoded_data)
print("Decoded data:", decoded_data)
