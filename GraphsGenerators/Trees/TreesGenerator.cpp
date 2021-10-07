#include </home/federico/OGDF-snapshot/include/ogdf/basic/graph_generators.h>
#include </home/federico/OGDF-snapshot/include/ogdf/fileformats/GraphIO.h>
using namespace ogdf;

Graph createSingleTree(int n)
{
    Graph G;	
    randomTree(G, n);
    return G;
}

int main()
{
    int n;
    cout << "Please enter an integer value to set the number of Tree: ";
    cin >> n;
    for (int i=10; i<=10*n; i=i+10){
	GraphIO::writeGML(createSingleTree(i), "/home/federico/Scrivania/Tesi/Graphs/Trees/GeneratedTrees/output-tree"+std::to_string(i)+".gml");
    }
    return 0;
}
