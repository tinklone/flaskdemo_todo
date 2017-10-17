# coding:utf-8
from app import app
import importlib
from library.ViewsHandler import get_views, get_class

from views.QuotesView import QuotesView
from views.TestView import TestView
import os

modules = get_views()
view_classes = get_class()
print modules
for index in range(len(modules)):
    import_module = importlib.import_module(modules[index])
    print(dir(import_module))
    view_class = getattr(import_module, view_classes[index])
    cls_obj = view_class()
    if view_classes[index] == 'IndexView':
        cls_obj.register(app, route_base='/')
    else:
        cls_obj.register(app)
print "vscode test"

if __name__ == '__main__':
    port = 5000
    if os.name == 'nt':
        port = 80
    app.run(debug=True, port=port)
