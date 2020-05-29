# Open3D
## Description
This is a solution repo for the assignment.pdf. It presents C++ and python solution to create a list of list of Identically colored connected components.  
Given a mesh that contains vertices and triangles, which have a color and are all connected together, the vertices that correspond together and are connected to each other are grouped together. This solution creates a list of all such groups and presents then in a sorted order.  
Solution to this assignment contains a `C++` `solution.cpp` file and a `python` `solution.py` file.  The `C++` solution calls the `IdenticallColoredConnectedComponents` api of `TriangleMesh` which uses depth first search to traverse through the vertices of a mesh.  
The `python` solution uses python binding for `C++` solution.  

## Instructions
### Download Merge and Build
To add this repo you can either git clone or download the zip file of this repo and unzip the file. Merge the `Open3D` directory with the `Open3D` directory of the source code of open3D. To build the repo you can follow the official instructions for compiling from source given here:  
http://www.open3d.org/docs/release/compilation.html  
You can also follow the commands below for Ubuntu and system's default python with python3). For other configurations follow the instructions on the link above.
```
# Install dependencies
util/scripts/install-deps-ubuntu.sh

# make build directory inside Open3D if it is not already present
mkdir build
cd build
sudo cmake -DPTHON_EXECUTABLE=/path/to/my/python3 ..
sudo make -j$(nproc)
sudo make install-pip-package
sudo make install
```
### Solution to the assignment
The C++ solution requires 2 arguments, an input file which contains the mesh data and an output file path where results can be stored.
`cd` to `<open3d directory>/build/bin/examples/`  
`./solution [path/to/input_mesh_file] [path/to/output_file]`  
For python solution-  
`cd` to `<open3d directory>/examples/Python/`  
`python3 solution.py`

## Algorithm
In order to find the identically colored connected components, the `depth first search` algorithm is used to traverse through all the components and find the similarly colored connected components. The steps are as follows:
1. Iterate through all the unvisited vertices
2. For every vertex, check if it has the same color to parent vertex.
3. For every vertex that has same color, if it is not visited then mark it as visited and append it to a list.
4. Sort the list as it should be presented in ascending order.
5. Append the list to the main list.
