def get_longest_substring(input):
    current = []
    all_substrings = []
    for c in input:
        if c in current:
            all_substrings.append(''.join(current))
            cut_off = current.index(c) + 1
            current = current[cut_off:]
        current += c
    all_substrings.append(''.join(current))

    longest = max(all_substrings, key=len)
    return longest

longest = get_longest_substring("football")
print(longest)
print(len(longest))