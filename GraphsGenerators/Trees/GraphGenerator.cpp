#include </home/federico/msc-graphstudy-master/dependencies/ogdf/include/ogdf/basic/graph_generators.h>
#include </home/federico/msc-graphstudy-master/dependencies/ogdf/include/ogdf/fileformats/GraphIO.h>
using namespace ogdf;

Graph createSingleTree(int n)
{
    Graph G;	
    randomTree(G, n);
    return G;
}

Graph createSingleConnectedGraph(int n)
{
    Graph G;	
    randomSimpleConnectedGraph(G, n, n+2);
    return G;
}

int main()
{
    int nt;
    cout << "Please enter an integer value to set the number of Tree: ";
    cin >> nt;
    for (int i=5; i<=5*nt; i+=5){
	GraphIO::writeGML(createSingleTree(i), "/home/federico/Scrivania/Tesi/Graphs/Trees/GeneratedTrees/output-tree"+std::to_string(i)+".gml");
    }
    
    int n;
    cout << "Please enter an integer value to set the number of PlanarConnectedGraph: ";
    cin >> npc;
    for (int i=10; i<=10*npc; i=i+10){
	GraphIO::writeGML(createSingleConnectedGraph(i), "/home/federico/Scrivania/Tesi/Graphs/PlanarConnectedGraphs/GeneratedPlanarConnectedGraphs/output-connected-graph"+std::to_string(i)+".gml");
    }

    return 0;
}



