# Greedy Algorithms

# Greedy algorithms are all about choosing the best solution available locally at that time, combining them until the solution is achieved.

# Insertion sort, selection sort, topological sort, prims algo, kruskals and djikastras algo are all greedy algorithms.

# In insertion sort, we're going to be diving the array into two parts: sorted and unsorted part. Then accordingly we're going to be inserting each element into its perfect position in the sorted array. All these local solutions lead to global solution which is fully sorted array therefore its greedy.

# In selection sort, we again have two parts: sorted and unsorted. Each time in the unsorted array we'll find the minimum element and put it in its perfect position in the sorted array. Local optimum solution leads to global solution therefore it is greedy.

# In topological sort, we use stack and locally take solution that meets the criteria and then push it onto a stack.Therefore it is greedy.

# In prims and kruskals we choose the least cost edge locally until entire minimum spanning tree is formed