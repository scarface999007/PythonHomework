class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        res = ""
        for item_list in self.list_of_lists:
            res += str(item_list) + "\n"
        return res

    def __add__(self, other):
        new_matrix = []
        new_row = []
        for item_list, other_item_list in zip(self.list_of_lists, other.list_of_lists):
            for item, other_item in zip(item_list, other_item_list):
                new_row.append(item + other_item)
            new_matrix.append(new_row)
            new_row = []
        return Matrix(new_matrix)

