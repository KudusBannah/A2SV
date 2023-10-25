class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def solve():
            available = maxWidth - curr_count + len(line)
            if len(line) == 1:
                padding = "".join([" " for i in range(available)])
                left = 0
            else:
                space = available // (len(line)-1)
                padding = "".join([" " for i in range(space)])
                left = available - space * (len(line) - 1)

            s = ""
            for i in range(len(line)):
                s += line[i]
                if i != len(line) - 1 or len(line) == 1:
                    if left:
                        s += (padding + " ")
                        left -= 1
                    else:
                        s += padding
            return s


        lines = []
        line = []
        curr_count = 0
        for word in words:
            if curr_count + len(word) <= maxWidth:
                line.append(word)
                curr_count += (len(word) + 1)
            else:
                lines.append(solve())
                line = [word]
                curr_count = len(word) + 1
        
        s = ""
        for i in range(len(line)):
            s += line[i]
            if i != len(line) - 1:
                s += " "

        s += "".join([" " for i in range(maxWidth-len(s))])
        lines.append(s)
        return lines
