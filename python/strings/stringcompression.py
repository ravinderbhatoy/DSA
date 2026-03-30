def compress(chars: list[str]) -> int:
    idx = 0
    read = 0
    while read < len(chars):
        ch = chars[read]
        count = 0
        while read < len(chars) and chars[read] == ch:
            count += 1
            read += 1
        chars[idx] = ch
        idx += 1
        if count > 1:
            for c in str(count):
                chars[idx] = c
                idx += 1
    return idx


chars = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars))
print(chars)
