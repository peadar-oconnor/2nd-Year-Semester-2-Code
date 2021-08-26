from CS2516Assignment import *

'''
# Heap part 1
heap = BinaryHeapNoIndex()
heap.add(40, "40")
heap.add(27, "27")
heap.add(29, "29")
heap.add(30, "30")
heap.add(35, "35")
heap.add(49, "49")
heap.add(43, "43")
print(heap.remove_root())
print(heap.get_root())
print(heap)
print(heap.length())

print()
print("------------------------------")
print()
'''

'''
# Final heap test
heap = BinaryHeap()
heap.add(40, "40")
heap.add(27, "27")
heap.add(29, "29")
heap.add(30, "30")
heap.add(35, "35")
heap.add(49, "49")
heap.add(43, "43")
print(heap.remove_root())
print(heap.get_root())
print(heap)
print(heap.length())

print()
print("------------------------------")
print()

apq = AdaptablePriorityQueue()
a = apq.add(40, "a")
b = apq.add(27, "b")
c = apq.add(29, "c")
d = apq.add(30, "d")
e = apq.add(35, "e")
f = apq.add(49, "f")
g = apq.add(43, "g")
print(apq.remove_min())
print(apq)
print(apq.min())
apq.update_key(f, 55)
print(apq)
apq.update_key(f, 31)
print(apq)
apq.update_key(d, 50)
print(apq)
print(apq.get_key(e))
print(apq.remove(d))
print(apq)
'''

'''
g1 = graphreader("simplegraph1.txt")
g2 = graphreader("simplegraph2.txt")

g_vs = g2.vertices()
v1 = g_vs[13]
print("---")
print(g2.dijkstra(v1))
'''

'''
srm = routemapreader("simpleroute.txt")
rm_v = srm.vertices()
v1 = rm_v[0]
v4 = rm_v[3]
print(srm.get_coordinates(v1))
print("------")
print(srm.dijkstra(v1))
print(srm.sp(v1, v4))
srm.print_path(v1, v4)
'''

routemap = routemapreader('corkCityData.txt')
ids = {}
ids['wgb'] = 1669466540
ids['turnerscross'] = 348809726
ids['neptune'] = 1147697924
ids['cuh'] = 860206013
ids['oldoak'] = 358357
ids['gaol'] = 3777201945
ids['mahonpoint'] = 330068634
sourcestr = 'wgb'
deststr='neptune'
source = routemap.get_vertex_by_label(ids[sourcestr])
dest = routemap.get_vertex_by_label(ids[deststr])
tree = routemap.sp(source,dest)
routemap.printvlist(tree)
