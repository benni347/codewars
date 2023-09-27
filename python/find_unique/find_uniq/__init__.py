"""
:URL:   https://www.codewars.com/kata/585d7d5adb20cf33cb000235/
"""


def find_uniq(arr):
    for i in range(len(arr)):
        if i == 0:
            if arr[i] != arr[i + 1] and arr[1] == arr[i + 2]:
                return arr[i]
        if i == len(arr) - 1:
            return arr[i]
        if i != 0:
            if arr[i] != arr[-1] and arr[i] != arr[0]:
                return arr[i]


if __name__ == "__main__":
    # find_uniq([3, 10, 3, 3, 3])
    # find_uniq([3, 10, 3, 3, 3])
    # unittest.main()
    # mtc = MyTestCase()
    # mtc.test_something()
    r = find_uniq([0.8, 0.8, 0.8, 0.8, 0.11])
    print(r)
