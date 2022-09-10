'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 1095, 852

why find middle first? why not one pass bindary search directly?
case:
1, 2, 3, 4, 9, 8, 7
      |        |
     mid     target

thus
- find mid point
- two binary search
'''


def search_bitonic_array(arr, key):


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
