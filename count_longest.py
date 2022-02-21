def count_longest(queue):
    result = [0]
    for index,data in enumerate(queue):
        count = 0
        for val in queue[index:]:
            if(val == data):
                count += 1
                result.append(count)
            else:
                result.append(count)
                break
    return max(result)

if __name__ == '__main__':
    print(count_longest(['h','e','l','l','o']))
    print(count_longest(['m','m','m','m','m']))
    print(count_longest(['h','e','e','e']))
    print(count_longest([]))
