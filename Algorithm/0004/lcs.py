def lcs_recursive(str1, str2, str1_idx, str2_idx):
    """Computes longest common subsequence of str1 and str2 using recursive.
    """
    if str1_idx == -1 or str2_idx == -1:
        return ''
    if str1[str1_idx] == str2[str2_idx]:
        return lcs_recursive(str1, str2, str1_idx-1, str2_idx-1) + str1[str1_idx]
    return max(lcs_recursive(str1, str2, str1_idx-1, str2_idx),
            lcs_recursive(str1, str2, str1_idx, str2_idx-1), key=len)


def lcs_dynamic_programming(str1, str2):
    """Computes longest common subsequence of str1 and str2 using dynamic programming.
    """
    matrix = [[0 for i in range(len(str1)+1)] for i in range(len(str2)+1)]
    for i, s1 in enumerate(str1):
        for j, s2 in enumerate(str2):
            if s1 == s2:
                matrix[j+1][i+1] = matrix[j][i] + 1
            else:
                matrix[j+1][i+1] = max(matrix[j+1][i], matrix[j][i+1])
    result = ''
    row, col = len(str2), len(str1)
    while row != 0 and col != 0:
        if matrix[row][col] == matrix[row-1][col]:
            row -= 1
        elif matrix[row][col] == matrix[row][col-1]:
            col -= 1
        else:
            assert str2[row-1] == str1[col-1]
            result = str1[col-1] + result
            row -= 1
            col -= 1
    return result

if __name__ == '__main__':
    str1 = 'didactical'
    str2 = 'advantage'
    str3 = 'educational'
    print lcs_recursive(str1, str2, len(str1)-1, len(str2)-1)
    print lcs_dynamic_programming(str1, str2)
