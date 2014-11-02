

class KnuthMorrisPratt(object):
    def search(self, string, substring):
        """Yields all starting positions of copies of the substring in the string.
  Calling conventions are similar to string.find, but its arguments can be
  lists or iterators, not just strings, it returns all matches, not just
  the first one, and it does not need the whole string in memory at once.
  Whenever it yields, it will have read the string exactly up to and including
  the match that caused the yield."""

        # allow indexing into substring and protect against change during yield
        substring = list(substring)

        # build table of shift amounts
        shifts = [1] * (len(substring) + 1)
        shift = 1
        for pos in range(len(substring)):
            while shift <= pos and substring[pos] != substring[pos - shift]:
                shift += shifts[pos - shift]
            shifts[pos + 1] = shift

        # do the actual search
        start_pos = 0
        match_len = 0
        for c in string:
            while match_len == len(substring) or match_len >= 0 and substring[match_len] != c:
                start_pos += shifts[match_len]
                match_len -= shifts[match_len]
            match_len += 1
            if match_len == len(substring):
                yield start_pos

    def __str__(self):
        return 'Knuth Morris Pratt'
