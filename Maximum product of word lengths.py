class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_bits = []
        for word in words:
            word_bit, length = 0, 0

            for letter in word:
                idx = ord(letter) - 97
                word_bit = word_bit | (1 << idx)
                length += 1
            words_bits.append([word_bit, length])

        max_ = 0
        for i in range(len(words_bits)):
            for j in range(i + 1, len(words_bits)):
                word1, word2 = words_bits[i], words_bits[j]

                if (word1[0] ^ word2[0]) == (word1[0] + word2[0]):
                    max_ = max(max_, words_bits[i][1] * words_bits[j][1])
        return max_