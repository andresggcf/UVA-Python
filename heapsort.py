from minheap import minheap

def heapsort(a):
  """heapsort algorithm using minheap as an auxiliary data structure
  """
  h = minheap(len(a))
  for x in a: h.insert(x)
  for i in range(len(a)):
    a[i] = h.get_min()
    h.remove_min()