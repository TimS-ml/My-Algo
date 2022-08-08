'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


# same question...
def search_next_letter(letters, key):
    start, end = 0, len(letters)
    while start < end:
        mid = start + (end - start) // 2
        if key < letters[mid]:
            end = mid
        else:  # key >= letters[mid]:
            start = mid + 1

    # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
    return letters[start % len(letters)]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
