
class bruteForceSearch(object):
    def search(self, string, substring):
        if len(substring) == 0 or len(string) < len(substring):
            return
        
        j = 0

        while j + len(substring) <= len(string):
            i = 0
            while i < len(substring) and substring[i] == string[j + i]:
                i += 1
            if i == len(substring):  # Match found
                yield j
            j += 1

    def __str__(self):
        return 'brute-force'