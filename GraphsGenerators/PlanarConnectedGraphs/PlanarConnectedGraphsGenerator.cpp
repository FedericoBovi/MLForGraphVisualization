#include </home/federico/OGDF-snapshot/include/ogdf/basic/graph_generators.h>
#include </home/federico/OGDF-snapshot/include/ogdf/fileformats/GraphIO.h>
using namespace ogdf;

Graph createSingleConnectedGraph(int n)
{
    Graph G;	
    planarConnectedGraph(G, n, n+2);
    return G;
}

int main()
{
    int n;
    cout << "Please enter an integer value to set the number of PlanarConnectedGraph: ";
    cin >> n;
    for (int i=10; i<=10*n; i=i+10){
	GraphIO::writeGML(createSingleConnectedGraph(i), "/home/federico/Scrivania/Tesi/Graphs/PlanarConnectedGraphs/GeneratedPlanarConnectedGraphs/output-connected-graph"+std::to_string(i)+".gml");
    }
    return 0;
}
