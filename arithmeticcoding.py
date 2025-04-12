class ArithmeticEncoder:
    def __init__(self, precision=32):
        self.precision = precision

    def encode(self, message, probabilities):
        # Calculate cumulative probabilities
        cumulative_probabilities = [0] * (len(probabilities) + 1)
        cumulative_probabilities[0] = 0
        for i in range(len(probabilities)):
            cumulative_probabilities[i + 1] = cumulative_probabilities[i] + probabilities[i]

        # Initialize interval to cover entire range [0, 1)
        low = 0
        high = 1
        range_size = 1

        # Encode each symbol in the message
        for symbol in message:
            symbol_index = symbol
            symbol_low = cumulative_probabilities[symbol_index]
            symbol_high = cumulative_probabilities[symbol_index + 1]
            symbol_range = symbol_high - symbol_low

            # Update interval based on symbol probabilities
            low += range_size * symbol_low
            high = low + range_size * symbol_range
            range_size = high - low

        # Output a binary representation of the interval
        output = format(int(low * (1 << self.precision)), '0{}b'.format(self.precision))

        return output

class ArithmeticDecoder:
    def __init__(self, precision=32):
        self.precision = precision

    def decode(self, encoded_message, probabilities, message_length):
        # Calculate cumulative probabilities
        cumulative_probabilities = [0] * (len(probabilities) + 1)
        cumulative_probabilities[0] = 0
        for i in range(len(probabilities)):
            cumulative_probabilities[i + 1] = cumulative_probabilities[i] + probabilities[i]

        # Convert encoded message to integer
        encoded_integer = int(encoded_message, 2) / (1 << self.precision)

        # Initialize interval to cover entire range [0, 1)
        low = 0
        high = 1
        range_size = 1

        # Decode each symbol in the message
        decoded_message = []
        for _ in range(message_length):
            # Find symbol index based on interval
            symbol_index = -1
            for i in range(len(cumulative_probabilities) - 1):
                if cumulative_probabilities[i] <= (encoded_integer - low) / range_size < cumulative_probabilities[i + 1]:
                    symbol_index = i
                    break

            # Output decoded symbol and update interval
            decoded_message.append(symbol_index)
            symbol_low = cumulative_probabilities[symbol_index]
            symbol_high = cumulative_probabilities[symbol_index + 1]
            symbol_range = symbol_high - symbol_low
            low += range_size * symbol_low
            high = low + range_size * symbol_range
            range_size = high - low

        return decoded_message

# Example usage:
message = [0, 1, 2, 3, 0, 1, 2, 3]
probabilities = [0.2, 0.3, 0.25, 0.25]
encoder = ArithmeticEncoder()
encoded_message = encoder.encode(message, probabilities)
print("Encoded message:", encoded_message)
decoder = ArithmeticDecoder()
decoded_message = decoder.decode(encoded_message, probabilities, len(message))
print("Decoded message:", decoded_message)
