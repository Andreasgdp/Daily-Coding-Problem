path = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'


def longest_dir_path(path):
    longest_so_far = -1
    height_at_level = {-1: 0}
    level = 0

    for line in path.split('\n'):
        for char in line:
            if char == '\t':
                level += 1
            else:
                break

        string = line.strip()
        if '.' in string:
            longest_so_far = max(longest_so_far, len(
                string) + height_at_level[level-1])
        else:
            height_at_level[level] = (
                height_at_level[level-1] + len(string) + 1)
        level = 0
    return longest_so_far


test = longest_dir_path(path)

print(test)

# Note 1