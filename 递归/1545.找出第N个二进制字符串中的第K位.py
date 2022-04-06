def findKthBit(n: int, k: int):

    if n == 1:
        return '0'
    if k == 2 ** (n - 1)  :

        return '1'
    if k < 2 ** (n - 1):
        return findKthBit(n - 1, k)
    elif findKthBit(n - 1, 2 ** (n) - k) == '1':

        return '0'
    else:

        return '1'

print(findKthBit(4, 12))
