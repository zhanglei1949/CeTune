import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from conf import common
import web
from web import form
import json
import requests

render = web.template.render('templates/')
urls = (
  '/', 'index',
  '/configuration/(.+)', 'configuration',
  '/monitor', 'monitor',
  '/results', 'results'
)
class index:
    def GET(self):
        web.seeother('/static/index.html')
class cases:
   def __init__(self, conf_path):
       pass
   def case_dump(self):
       pass
   def case_check(self):
       pass
   def case_set(self):
       pass 
   
class configuration:
    all_conf = common.Config("../conf/all.conf") #all_conf is a class named Config
    tune_conf = common.load_yaml_conf("../conf/tuner.yaml") #tune_conf is a OrderDict
    def GET(self, function_name = ""):
        return common.eval_args( self, function_name, web.input() )

    def get_group(self,request_type):
        request_type_list = ["workflow","cluster","system","ceph","benchmark","analyzer"]
        if request_type in request_type_list:
            return self.all_conf.get_group(request_type)

    def get_group_list(self):
        return self.all_conf.get_group_list()
    def benchmark_table(self,path):
	case_conf = cases.("../conf/cases.conf")
        cases_conf.case_dump()
        cases_conf.case_set()
    def run_status(self):
	pass
    def check_set(self,key,value):
        #table_key_list = ["benchmark_engine","worker","container_size","io_pattern","block_size","work_depth","ramup_time","run_time","device"]
	check_list = []
        if key in string_list
        if key in num_list
        pass
    def set(self):
        conf_json = requests.get("http://192.168.5.22:8080/configuration/set_check").content
        conf_dict = simplejson.loads(conf_json)
        res = []
        for k,v in conf_dict.iterms
             tmp_list = check_set(k,v)
             disc = tmp_list[0]
             flag = tmp_list[1]
             tmp_dict = {'key':k,'value':v,'Disc': disc,'check': flag}
             res.append(tmp_dict)
        res_json = simplejson.dumps(res)
        return res_json
        

class monitor:
    def GET(self):
        return render.monitor()

class results:
    def GET(self):
        return render.results()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
