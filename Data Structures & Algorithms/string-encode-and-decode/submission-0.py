class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_parts = []
        for s in strs:
            # Append length, delimiter '#', and the string it self
            # Hello -> 5#Hello, A#bc -> 4#A#bc
            encoded_parts.append(f"{len(s)}#{s}")

        # print(encoded_parts)
        # Join the list into a single string (more efficient than string concatenation)
        return "".join(encoded_parts)
    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded_strs = []
        i = 0

        while i < len(s):
            print(s)
            # Find the position of the next '#' starting from index i
            # '5#Hello' -> 1
            hash_pos = s.find('#', i)

            # Extract the length of the next string
            # '5#Hello' -> s[0:1] -> 5
            length = int(s[i:hash_pos])

            # The actual string starts immediately after the '#'
            # start = 2, end = 7
            start = hash_pos + 1
            end = start + length

            # Slice the string and add it to our result list
            decoded_strs.append(s[start:end])

            # Move the pointer 'i' to the start of the next encoded chunk
            i = end

        return decoded_strs
