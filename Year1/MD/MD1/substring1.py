def longest_duplicate_substr(str1):
    l = []

    for i in range(len(str1)):

        for j in range(i + 1, len(str1) + 1):
            l.append(str1[i:j])

    dict1 = {}

    longest_duplicated_substring = ""

    for i in l:

        if i not in dict1:

            dict1[i] = 1

        else:

            dict1[i] += 1

            if len(i) > len(longest_duplicated_substring):
                max_key = i

    return longest_duplicated_substring


longest = longest_duplicate_substr("abababcdefc")
print(longest)
print(len(longest))
