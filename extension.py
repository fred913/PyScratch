#coding: utf-8
#PyScrach
#Author: Sheng Fan
from flask import *

class ApplicationExtension():
    Flask_app = Flask(__name__)
    def __init__(
            self,
            project_name:str = "Debug_Server"
    ):
        self.Flask_app = Flask(f"PyScratch_{project_name}")
        self.var = {}
        self.func = {}
        self.ProjName = project_name
        self.on_reset = None
        self.Flask_app.add_url_rule("/reset_all", None, self.reset_all_request)
        self.Flask_app.add_url_rule("/poll", None, self.get_vars())
    def reset_all_request(self):
        if self.on_reset != None:
            self.on_reset()
    def get_vars(self):
        res = ""
        for key in self.var:
            value = self.var[key]
            res += f"{key} {value}\n"
        return res
    def create_func(self, name, func, args=[]):
        self.func[name] = func
        uri = ""
        if args != []:
            uri += "/"
            for i in args:
                uri += f"{i}/"
            uri = uri[:-1]
        return self.Flask_app.add_url_rule(rule = f"/{name}{uri}", view_func = func)
    def run(self, *args, **kwargs):
        return self.Flask_app.run(args, kwargs)
