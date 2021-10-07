import subprocess
import os 

PROPERTIES=['rdf-global', 'rdf-local', 'angular', 'edge-length', 'princomp-1', 'princomp-2', 'tension']
FIXED_COUNT_BINS_LOG_2 = list(range(3, 10))
FIXED_COUNT_BINS = [ 2**i for i in FIXED_COUNT_BINS_LOG_2 ]

path_properties = '/home/federico/msc-graphstudy-master/src/properties/'
kernel = ['BOXED', 'GAUSSIAN']

def call_propertie(propertie ,input_path, final_position):
    cmd = []
    if propertie.find('princomp')==-1:
        princomp_flag=''
    else:
        princomp_flag = propertie.replace("princomp","")
        propertie = 'princomp'
#    if propertie.find('rdf-local')==-1:    
#        proc = subprocess.run([path_properties+"./"+propertie+" --kernel="+kernel[0]+'--bins={:d}'.format(b) for b in FIXED_COUNT_BINS+' --meta='+final_position+'/'+propertie+princomp_flag+'.json'+' '+princomp_flag+' '+input_path], shell=True)
#    else:
#        proc = subprocess.run([path_properties+"./"+propertie+" --kernel="+kernel[0]+'--bins={:d}'.format(b) for b in FIXED_COUNT_BINS+' --meta='+final_position+'/'+propertie+princomp_flag+'.json'+' '+princomp_flag+' '+input_path], shell=True)
    cmd.append(path_properties+"./"+propertie) 
    cmd.append(" --kernel="+kernel[0])
    cmd.extend('--bins={:d}'.format(b) for b in FIXED_COUNT_BINS)
    cmd.append('--meta='+final_position+'/'+propertie+princomp_flag+'.json')
    cmd.append(princomp_flag)
    cmd.append(input_path)
    proc = subprocess.run([' '.join(cmd)], shell=True)    
    print (proc)

def call_properties_layout(path):
    onlyfile = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if onlyfile and onlyfile[0].find('layout')!=-1:
        call_path=os.path.join(path, onlyfile[0])
        for p in PROPERTIES:
            call_propertie(p, call_path, path)
    else:
        onlydirectories =  [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        for d in onlydirectories:
            call_properties_layout(os.path.join(path, d))
           
        
#call_propertie('rdf-local','/home/federico/Project/GeneratedTreesDrawings/output-tree50.gml', '/home/federico/Project/Properties/rdfGlobal')        
        
        