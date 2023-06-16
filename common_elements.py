def main():
    # Same tests as the doctests above, but can be run from the terminal:
    # python common_elements.py

    print(common(['a'], ['a']))  # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))  # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))  # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))  # should print ['a']


def common(list1, list2):
    # takes 2 lists and return a new list with the elements which appear in both list1

    result_list = []

    for elem in list1:
        if elem in list2:
            if elem not in result_list:
                # print (elem)
                result_list.append(elem)

    return result_list


if __name__ == "__main__":
    main()