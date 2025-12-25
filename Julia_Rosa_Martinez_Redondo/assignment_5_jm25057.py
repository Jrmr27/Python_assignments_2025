# ~~~~~~~~A C T I V I T Y 5 PYTHON - NumPy Practice~~~~~~~~
# By Julia Rosa Martinez Redondo jm25057

import numpy as np   # numpy basics


# ~~~~~~~~TASK 1~~~~~~~~
nums1 = np.arange(1, 11)
print("nums 1 to 10:")
print(nums1)

arr2d = np.arange(1, 10).reshape(3, 3)
print("\n3x3 array:")
print(arr2d)
print("shape:", arr2d.shape)


# ~~~~~~~~TASK 2~~~~~~~~
nums12 = np.arange(1, 13)
print("\nnums before reshape:")
print(nums12)

resh1 = nums12.reshape(3, 4)
print("\nreshape 3x4:")
print(resh1)

resh2 = nums12.reshape(2, 6)
print("\nreshape 2x6:")
print(resh2)
# same values, just moved


# ~~~~~~~~TASK 3~~~~~~~~
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("\nmatrix:")
print(mat)

mean_cols = mat.mean(axis=0)
print("\nmean axis 0:")
print(mean_cols)

sum_rows = mat.sum(axis=1)
print("sum axis 1:")
print(sum_rows)
# axis 0 goes down
# axis 1 goes side


# ~~~~~~~~TASK 4~~~~~~~~
rand_nums = np.random.randint(0, 50, 10)
print("\nrandom nums:")
print(rand_nums)

avg = rand_nums.mean()
print("avg:")
print(avg)

above_avg = rand_nums[rand_nums > avg]
print("bigger than avg:")
print(above_avg)


# ~~~~~~~~TASK 5~~~~~~~~
nums20 = np.arange(0, 21)
print("\nnums 0 to 20:")
print(nums20)

even_nums = nums20[nums20 % 2 == 0]
print("even nums:")
print(even_nums)

div3_nums = nums20[nums20 % 3 == 0]
print("div by 3:")
print(div3_nums)


# ~~~~~~~~TASK 6~~~~~~~~
class MatrixTool:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)

    def row_mean(self):
        return self.matrix.mean(axis=1)

    def above_threshold(self, t):
        return self.matrix[self.matrix > t]


tool = MatrixTool(mat)
print("\nrow mean:")
print(tool.row_mean())

print("above 5:")
print(tool.above_threshold(5))


# ~~~~~~~~TASK 7~~~~~~~~
rand_mat = np.random.rand(5, 5)
print("\nrandom matrix:")
print(rand_mat)

bin_mat = rand_mat.copy()
bin_mat[bin_mat < 0.5] = 0
bin_mat[bin_mat >= 0.5] = 1

print("\nafter change:")
print(bin_mat)
