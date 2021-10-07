import keras as ks 
import os
import pickle
import numpy
import csv
import normalize


path_model = '/home/federico/msc-graphstudy-master/data/model/'
path_dataset = '/home/federico/Tesi/Dataset/'
os.remove('/home/federico/Tesi/results.csv')

# load YAML and create model
yaml_file = open(path_model+'model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = ks.models.model_from_yaml(loaded_model_yaml)

# load weights into new model
loaded_model.load_weights(path_model+"weights.hdf5")
print("Loaded model from disk")

def resolve_match(g, layout_one, layout_two):
    one = open(g+layout_one+'/input_vector','rb')
    vector_one = numpy.asarray(pickle.load(one)).reshape(1, 67)
    two = open(g+layout_two+'/input_vector','rb')
    vector_two = numpy.asarray(pickle.load(two)).reshape(1, 67)
    graph= open(g+'graph.txt', 'r')
    graph_vector = list(csv.reader(graph))
    graph_vector = [float(i) for i in graph_vector[0]]
    graph_vector = normalize.normalize_input_vector(graph_vector, normalize.new_graph_mean_std_list)#not the best to do it here
    graph_vector = numpy.asarray(graph_vector).reshape(1, 2)
    result = loaded_model.predict([vector_one, vector_two, graph_vector])
    if result>0.0:
        return layout_two
    elif result<0.0:
        return layout_one
    
def do_tournament():   
    for g in os.listdir(path_dataset):
        inside_graph_path = path_dataset+g+'/'
        #first turn
        ft_winner_list = []
        ft_winner_list.append(resolve_match(inside_graph_path, '0', '1'))
        for i in range(2, 14, 2):
            ft_winner_list.append(resolve_match(inside_graph_path, str(i), str(i+1)))
        ft_winner_list.append(resolve_match(inside_graph_path, '14', '15'))
        #second turn
        st_winner_list = []
        st_winner_list.append(resolve_match(inside_graph_path, ft_winner_list[0], ft_winner_list[1]))
        for i in range(2, 6, 2):
            st_winner_list.append(resolve_match(inside_graph_path, ft_winner_list[i], ft_winner_list[i+1]))
        st_winner_list.append(resolve_match(inside_graph_path, ft_winner_list[6], ft_winner_list[7]))    
        #third turn
        tt_winner_list=[] 
        tt_winner_list.append(resolve_match(inside_graph_path, st_winner_list[0], st_winner_list[1]))
        tt_winner_list.append(resolve_match(inside_graph_path, st_winner_list[2], st_winner_list[3]))
        #final turn
        winner = resolve_match(inside_graph_path, tt_winner_list[0], tt_winner_list[1])
        with open('/home/federico/Tesi/results.csv', 'a+') as f:
            f.write(g+', '+str(winner))
            f.write('\n')
        