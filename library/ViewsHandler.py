
from  utils.FileTools import get_dir_files
view_file_path = r"E:\maxlong\python\projects\FlaskDemo\views"
def get_views():
    view_files = get_dir_files(view_file_path)
    return ["views.%s"%vf for vf in view_files]

def get_class():
    view_files = get_dir_files(view_file_path)
    return view_files

