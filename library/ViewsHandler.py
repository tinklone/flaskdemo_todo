from settings import APP_VIEWS
from  utils.FileTools import get_dir_files
print APP_VIEWS
def get_views():
    view_files = get_dir_files(APP_VIEWS)
    return ["views.%s"%vf for vf in view_files]

def get_class():
    view_files = get_dir_files(APP_VIEWS)
    return view_files
if __name__=='__main__':
    print get_views()

