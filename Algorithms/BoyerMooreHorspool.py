# Returns positions where pattern is found in text
#     See http://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm for an explanation on how 
#     this algorithm works.
#     O(n)

class BoyerMooreHorspool(object):
    def search(self, string, substring):
        m = len(substring)
        n = len(string)
        if m > n:
            return
        
        skip = []
        for k in range(256):
            skip.append(m)
        for k in range(m - 1):
            skip[ord(substring[k])] = m - k - 1
        skip = tuple(skip)
        k = m - 1
        while k < n:
            j = m - 1
            i = k
            while j >= 0 and string[i] == substring[j]:
                j -= 1
                i -= 1
            if j == -1:
                yield i + 1
            k += skip[ord(string[k])]

    def __str__(self):
        return 'Boyer Moore Horspool'
