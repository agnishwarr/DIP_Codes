import numpy as np

def set_operations(a, b):
    print("Set 1:", a)
    print("Set 2:", b)

    # Union
    union_set = np.union1d(a, b)
    print("Union:", union_set)

    # Intersection
    intersection_set = np.intersect1d(a, b)
    print("Intersection:", intersection_set)

    # Difference
    difference_set1 = np.setdiff1d(a, b)
    print("Difference (Set 1 - Set 2):", difference_set1)

    difference_set2 = np.setdiff1d(b, a)
    print("Difference (Set 2 - Set 1):", difference_set2)

    # Symmetric Difference
    symmetric_difference_set = np.setxor1d(a, b)
    print("Symmetric Difference:", symmetric_difference_set)

    # Subset and Superset
    is_subset = np.in1d(a, b).all()
    is_superset = np.in1d(b, a).all()
    print("Is Set 1 a Subset of Set 2:", is_subset)
    print("Is Set 1 a Superset of Set 2:", is_superset)

if __name__ == "__main__":
    # Example sets represented as NumPy arrays
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([3, 4, 5, 6, 7])

    # Perform set operations
    set_operations(a, b)
