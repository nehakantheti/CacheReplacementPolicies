# Python code for LFU cache implementation
cache_max_size = 4
cache_size = 0
cache = [None] * cache_max_size
indices = {}

# Generic function to swap two pairs
def swap(a, b):
	temp = a
	a = b
	b = temp

# Returns the index of the parent node
def parent(i):
	return (i - 1) // 2

# Returns the index of the left child node
def left(i):
	return 2 * i + 1

# Returns the index of the right child node
def right(i):
	return 2 * i + 2

# Self made heap to Rearranges
# the nodes in order to maintain the heap property
def heapify(v, m, i, n):
	l = left(i)
	r = right(i)
	minim = i
	if l < n:
		minim = (i if v[i][1] < v[l][1] else l)
	if r < n:
		minim = (minim if v[minim][1] < v[r][1] else r)
	if minim != i:
		m[v[minim][0]] = i
		m[v[i][0]] = minim
		swap(v[minim], v[i])
		heapify(v, m, minim, n)

# Function to Increment the frequency
# of a node and rearranges the heap
def increment(v, m, i, n):
	v[i][1] += 1
	heapify(v, m, i, n)

# Function to Insert a new node in the heap
def insert(v, m, value, n):
	if n == len(v):
		del m[v[0][0]]
		print("Cache block " + str(v[0][0]) + " removed.")
		v[0] = v[n-1]
		heapify(v, m, 0, n-1)
	v[n] = [value, 1]
	m[value] = n
	i = n
	# Insert a node in the heap by swapping elements
	while i and v[parent(i)][1] > v[i][1]:
		m[v[i][0]] = parent(i)
		m[v[parent(i)][0]] = i
		swap(v[i], v[parent(i)])
		i = parent(i)
	print("Cache block " + str(value) + " inserted.")

# Function to refer to the block value in the cache
def refer(cache, indices, value, cache_size):
	if not value in indices:
		insert(cache, indices, value, cache_size)
	else:
		increment(cache, indices, indices[value], cache_size)

# Driver Code
def main():
	refer(cache, indices, 1, cache_size)
	refer(cache, indices, 2, cache_size)
	refer(cache, indices, 1, cache_size)
	refer(cache, indices, 3, cache_size)
	refer(cache, indices, 2, cache_size)
	refer(cache, indices, 4, cache_size)
	refer(cache, indices, 5, cache_size)
	return 0

main()

# This code is contributed by ishankhandelwals.
