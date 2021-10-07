import json
import os
import pickle
import properties
import normalize

def prepare_vector(path):
    prepared_propertie = []
    with open(path) as f:
        data = json.load(f)
        if path.find('rdf-local')!=-1:
            log_diameter = len(data['data'])
            for i in range(log_diameter):
                prepared_propertie.append(data['data'][i]['mean'])
                prepared_propertie.append(data['data'][i]['rms'])
                #prepared_propertie.append(data['data'][i]['data'][0]['entropy'])
                prepared_propertie.append(data['data'][i]['entropy-intercept'])
                prepared_propertie.append(data['data'][i]['entropy-slope'])
            for i in range(log_diameter, 10):
                prepared_propertie.append(data['data'][log_diameter-1]['mean'])
                prepared_propertie.append(data['data'][log_diameter-1]['rms'])
                #prepared_propertie.append(data['data'][log_diameter-1]['data'][0]['entropy'])
                prepared_propertie.append(data['data'][log_diameter-1]['entropy-intercept'])
                prepared_propertie.append(data['data'][log_diameter-1]['entropy-slope'])
        else:
             if path.find('edge-length')==-1:
                 prepared_propertie.append(data['mean'])
             prepared_propertie.append(data['rms'])
             prepared_propertie.append(data['entropy-intercept'])
             prepared_propertie.append(data["entropy-slope"])
             if path.find('princomp')!=-1:
                prepared_propertie = data['component']+prepared_propertie
    return prepared_propertie       

def prepare_layout_vector(path):
    for g in os.listdir(path):
        inside_graph_path = path+'/'+g
        onlydir = [f for f in os.listdir(inside_graph_path) if os.path.isdir(os.path.join(inside_graph_path, f))]
        for l in onlydir:
            input_vector = []
            inside_layout_path = inside_graph_path+'/'+l
            for p in properties.PROPERTIES:
                input_vector.extend(prepare_vector(inside_layout_path+'/'+p+'.json'))    
            with open(inside_layout_path+'/input_vector', 'wb') as fp:
                pickle.dump(normalize.normalize_input_vector(input_vector, normalize.new_mean_std_list), fp)
                                    
#prepare_vector('/home/federico/Project/Properties/rdfGlobal/rdf-local.json') 