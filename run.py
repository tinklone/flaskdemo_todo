#coding:utf-8
from app import app
import importlib
from library.ViewsHandler import  get_views,get_class

from views.QuotesView import QuotesView
from views.TestView import TestView



modules = get_views()
view_classes = get_class()
print modules
for index in range(len(modules)):
    import_module = importlib.import_module(modules[index])
    print(dir(import_module))
    view_class = getattr(import_module,view_classes[index])
    cls_obj = view_class()
    cls_obj.register(app)
print "vscode test"

if __name__ == '__main__':
    app.run(debug=True)
