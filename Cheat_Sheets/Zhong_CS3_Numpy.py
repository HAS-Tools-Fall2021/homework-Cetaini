# This is a cheet sheet on Numpy basics
# -------------------------------------
# PART I: Summarize Numpy Arrays

# %%
# What are they and how are they different than lists?
# - Numpy array is another data structure that store data as a grid, or a
#   matrix.
#   Numpy array could have multiple dimensions.
# - Difference between numpy arrays and Python lists:
#   1. All elements in a numpy array must be the same data type.
#   2. Numpy arrays support arithmetic and other mathematical operations that
#      run on each element of the array.
#   3. A numpy array is not edited by adding/removing/replacing elements in the
#      array. Instead, each time it is manipulated in some way, and it is
#      actually deleted and recreated each time.
#   4. Numpy arrays can store along multiple dimensions that are relative to
#      each other. This makes numpy arrays a very efficient data structure for
#      large datasets.
#   5. Numpy array needs to be created by a specific Python package, which
#      needs to be imported first.
import numpy as np

# %%
# How to make numpy arrays?
# - Converting Python sequences to Numpy Arrays (np.array)
a1D = np.array([1, 2, 3, 4])
a2D = np.array([[1, 2], [3, 4]])
a3D = np.array([[[1, 2], [3, 4]],
                [[5, 6], [7, 8]]])
# - Intrinsic Numpy array creation functions
#   - 1D array creation functions e.g. np.linspace, and np.arange
np.arange(2, 3, 0.1)  # np.range(start.0, stop.end, step.1)
np.linspace(1., 4., 6)  # np.linspace(start, stop, number of elements)
#   - 2D array creation functions e.g. np.eye, np.diag, and np.vander
np.eye(3, 5)
np.diag([1, 2, 3], 1)
np.vander((1, 2, 3, 4), 4)
#   - General ndarray creation functions
np.zeros((2, 3, 2))
np.ones((2, 3, 2))
np.random.rand(2, 3, 2)
np.indices((3, 3))
# - Replicating, joining, or mutating existing arrays
# - Reading arrays from disk, or files
# - Use special library functions, e.g., SciPy, Pandas, and OpenCV

# %%
# How to index and slice numpy arrays?
# - Indexing in numpy arrays are similar with Python's standard list
#   indexing.
#   From beginning: 0, 1, 2, ...
#   From the end: -1, -2, -3, ...
#   For multi-dimention array, use a comma-separated tuple of
#   indices.
# - Slicing a numpy array needs to combine index numbers with colons.
#   x[start.0:stop.end:step.1]

# %%
# Key methods associated with numpy arrays.
# - .copy(): This creates a copy of an array.
# - .reshape: This could reshape an array.
# - .sort: To sort an array in-place.
# - .min, .max, .sum ...

# %%
# Key attributes associated with numpy arrays
# - .ndim: Check dimension
# - .shape: Check shape
# - .size: Check size
# - .dtype: Check data type
# - .itemsize: Check size of each array element
# - .nbytes: Check the total size of the array

# %%
# PART II: Summarize important numpy functions
# - np.array: To create a numpy array
# - np.min, .max, .sum ...
x = np.arange(1, 6)
np.nansum(x)  # NaN-safe
# - .round, .floor, ... : Rounding functions
# - .reduce: Aggregate operation, e.g. .add.reduce, .multiply.reduce
np.add.reduce(x)
np.multiply.reduce(x)
# - .accumulate: This can store all accumulate results, combine with
#   operators also.
np.add.accumulate(x)
np.multiply.accumulate(x)
# - .outer: Compute the output of all pairs of two different inputs
np.multiply.outer(x, x)
# - np.concatenate, vstack, .hstack, .dstack: Joining two or more arrays
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])
np.vstack([x, grid])

y = np.array([[99],
              [99]])
np.hstack([grid, y])
# - np.split, .hsplit, .vsplit, .dsplit: Split an array
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])

grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [2])
left, right = np.hsplit(grid, [2])
# - np.abs: Absolute value
# - np.sin, .cos, ...: Trogonometric functions
# - np.exp, .log ...
