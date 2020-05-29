#include<Open3D/Open3D.h>
#include<string>
#include<vector>
#include<set>
#include<algorithm>
#include<fstream>
using namespace open3d;
using namespace std;

void PrintUsage() {
    PrintOpen3DVersion();
    // clang-format off
    utility::LogInfo("Usage:");
    utility::LogInfo("    > solution [input_mesh_filename] [output_text_filename]");
    // clang-format on
}

int main(int argc, char *argv[]) {
    if(argc!=3){
        PrintUsage();
        return 1;
    }
    string filename = argv[1];
    string output_file = argv[2];
    // Read triangle mesh "test_mesh.ply"
    geometry::TriangleMesh mesh;
    io::ReadTriangleMesh(filename, mesh);
    // Then get connected components
    auto connected_components = mesh.IdenticallyColoredConnectedComponents();
    // Print connected_components in the specified format
    fstream fout;
    fout.open(output_file, fstream::out|fstream::trunc);
    for (vector<int> v:connected_components){
        for(size_t i=0; i<v.size(); ++i){
            fout<<v[i];
            if(i<v.size()-1){
                fout<<' ';
            }
        }
        fout<<"\n";
    }
    fout.close();
    return 0;
}
