from csv import reader

normalize_list= open('/home/federico/Project/normalizeFeatures.csv', 'r')
mean_std_list = list(reader(normalize_list, delimiter='\t'))
new_mean_std_list = []
for i in mean_std_list:
    tmp_list = []
    tmp_list.append(float(i[2]))
    tmp_list.append(float(i[3]))
    new_mean_std_list.append(tmp_list)

normalize_list= open('/home/federico/Project/normalizeGraph.csv', 'r')
mean_std_list = list(reader(normalize_list, delimiter='\t'))
new_graph_mean_std_list = []
for i in mean_std_list:
    tmp_list = []
    tmp_list.append(float(i[0]))
    tmp_list.append(float(i[1]))
    new_graph_mean_std_list.append(tmp_list)   


def normalize_input_vector(input_vector, new_mean_std_list):
    for i in range(len(input_vector)):
        input_vector[i] = (input_vector[i]-new_mean_std_list[i][0])/new_mean_std_list[i][1]
    return input_vector
       