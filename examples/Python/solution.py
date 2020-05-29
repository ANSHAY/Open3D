import open3d as o3d
import os
# ------------------------------------------------------------------------------
def _relative_path(path):
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    return os.path.join(script_dir, path)

FILENAME = _relative_path("../TestData/test_mesh.ply")
OUTPUT_FILE = _relative_path("../Results/results.txt")

# \brief helper function that performs depth first search
# to trace the components of a mesh
# \param adj adjacency matrix of vertices
# \param vertices a vector of all vertices in the mesh
# \param visited a vector that keeps track of the visited vertices
# \param color vector with values 0, 1, 2 corresponding to 3 colors
# for every vertex
# \param current_color color of calling vertex
# \param i index of the current vertex
###
#def dfs(adj, vertices, visited, color, current_color, i):
#    if visited[i]:
#        return
#    if color[i] != current_color:
#        return
#    visited[i] = True
#    vertices.append(i)
#    for child in adj[i]:
#        dfs(adj, vertices, visited, color, current_color, child)
###
# ----------------------------------------------------
# \brief Function that groups identically colored connected vertices together.
# \param mesh pointer to a TriangleMesh
# \return cc connected components grouped together.
###
#def Identically_colored_connected_components(mesh):
#    mesh.compute_adjacency_list()
#    adj = mesh.adjacency_list
#    cc = []
#    visited = [False]*len(adj)
#    color = [] # get color from mesh data
#    for m in mesh.vertex_colors:
#        if(m[0] == 1):
#            color.append(0)
#        elif(m[1] == 1):
#            color.append(1)
#        else:
#            color.append(2)
#    for i in range(0, len(adj)):
#        vertices = []
#        dfs(adj, vertices, visited, color, color[i], i)
#        if vertices:
#            vertices.sort()
#            cc.append(vertices);
#    return cc;
###
# ------------------------------------------------------
# ------------------------------------------------------------------------------
# Read triangle mesh "test_mesh.ply"
mesh = o3d.io.read_triangle_mesh(FILENAME);
# Then get connected components
connected_components = mesh.identically_colored_connected_components()
# Print connected_components in the specified format
with open(OUTPUT_FILE, 'w+') as fout:
    for v in connected_components:
        for i in v:
            fout.write(str(i))
            if(i != v[-1]):
                fout.write(' ')
        fout.write('\n')
