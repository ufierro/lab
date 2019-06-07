def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1:
        return 1
    prev_len = 0
    char_buf = []
    curr_count = 0
    for char in s:
        if char in char_buf:
            if len(char_buf) > curr_count:
                curr_count = len(char_buf)
            pos = char_buf.index(char)
            if pos == len(char_buf)-1:
                char_buf.clear()
            elif pos == 0:
                del char_buf[pos]
            else:
                char_buf = char_buf[pos+1:]
        char_buf.append(char)
    if len(char_buf) > curr_count:
        return len(char_buf)
    return curr_count


print(lengthOfLongestSubstring("ohvhjdml"))
