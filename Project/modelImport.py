import keras as ks 

path = '/home/federico/msc-graphstudy-master/data/model/'

# load YAML and create model
yaml_file = open(path+'model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = ks.models.model_from_yaml(loaded_model_yaml)

# load weights into new model
loaded_model.load_weights(path+"weights.hdf5")
print("Loaded model from disk")