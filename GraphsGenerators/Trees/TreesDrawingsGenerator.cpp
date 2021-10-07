#include </home/federico/msc-graphstudy-master/dependencies/ogdf/include/ogdf/fileformats/GraphIO.h>
#include </home/federico/msc-graphstudy-master/dependencies/ogdf/include/ogdf/basic/GraphAttributes.h>
#include </home/federico/msc-graphstudy-master/dependencies/ogdf/include/ogdf/energybased/FMMMLayout.h>
#include <stdio.h>
#include <iostream>
#include <string>
#include <dirent.h>
#include <vector>
#include <sys/stat.h>
#include </home/federico/Tesi/Graphs/Trees/normalizer.hxx>
using namespace ogdf;

std::vector<std::string> open(std::string path) {

    DIR*    dir;
    dirent* pdir;
    std::vector<std::string> files;

    dir = opendir(path.c_str());

    while (pdir = readdir(dir)) {
        files.push_back(pdir->d_name);
    }
    
    return files;
}

void make_directory(std::string path){
    int n= path.length();
    char char_array[n+1];
    std::strcpy(char_array, path.c_str());
    const int dir_err = mkdir(char_array, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
    if (-1 == dir_err){
        printf("Error creating directory!n");
        exit(1);
    }
}

int main()
{
    int spring_strength [3] = {1, 20, 50};
    int rep_forces_strength[3] = {1, 20, 50};
    std::string path = "/home/federico/Tesi/Graphs/Trees/GeneratedTrees/";
    std::vector<std::string> f;
    f = open(path);
    auto itr = std::find(f.begin(), f.end(), "..");
    if (itr != f.end()) f.erase(itr);
    auto itr2 = std::find(f.begin(), f.end(), ".");
    if (itr2 != f.end()) f.erase(itr2);
    for (auto it : f){	
        Graph G;	
        GraphIO::readGML(G,"/home/federico/Tesi/Graphs/Trees/GeneratedTrees/"+it);
        GraphAttributes GA(G);
        GA.directed()=false;
	char* dataset_path = "/home/federico/Tesi/Dataset/";
	make_directory(dataset_path+it);
	int layout_counter = 0;
	for(int i=0; i<sizeof(spring_strength)/sizeof(*spring_strength); i++){
		for(int j=0; j<sizeof(rep_forces_strength)/sizeof(*rep_forces_strength); j++){
			make_directory(dataset_path+it+"/"+std::to_string(layout_counter));
			FMMMLayout fmmm;
			fmmm.springStrength(spring_strength[i]);
			fmmm.repForcesStrength(rep_forces_strength[j]);
			fmmm.call(GA);
			normalize_layout(GA);			
			GraphIO::writeGML(GA, dataset_path+it+"/"+std::to_string(layout_counter)+"/"+"layout.gml");
			layout_counter+=1;
		}
        }
    }
    return 0;
}
