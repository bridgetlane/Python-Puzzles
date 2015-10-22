# implements a basic binary search, and a binary search that returns the first and last occurrence
class Binsearch(object):
    def __init__(self, A, n, x):
        self.all_nums = A
        self.total_nums = n
        self.search = x
        self.orig = self.bin_search()
        self.first = self.search_first_occurrence()
        self.last = self.search_last_occurrence()
    def __str__(self):
        string = "Search: " + str(self.all_nums) + " for " + str(self.search)
        return string
    def bin_search(self):
        low = 0
        high = self.total_nums - 1
        while (low <= high):
            middle = (low+high)/2
            if (self.search == self.all_nums[middle]):
                return middle
            elif (self.search < self.all_nums[middle]):
                high = middle - 1
            else:
                low = middle + 1
        return -1
    def search_first_occurrence(self):
        low = 0
        high = self.total_nums - 1
        index = -1
        while (low <= high):
            middle = (low+high)/2
            if (self.search == self.all_nums[middle]):
                index = middle
                high = middle - 1
            elif (self.search < self.all_nums[middle]):
                high = middle - 1
            else:
                low = middle + 1
        return index
    def search_last_occurrence(self):
        low = 0
        high = self.total_nums - 1
        index = -1
        while (low <= high):
            middle = (low+high)/2
            if (self.search == self.all_nums[middle]):
                index = middle
                low = middle + 1
            elif (self.search < self.all_nums[middle]):
                high = middle - 1
            else:
                low = middle + 1
        return index

# some examples
def main():
    my_search = Binsearch([1,2,3,3,3,4],6,3)
    print(str(my_search))
    print("found at index: " + str(my_search.orig))
    print("first occurrence at index: " + str(my_search.first))
    print("last occurrence at index: " + str(my_search.last))

main()