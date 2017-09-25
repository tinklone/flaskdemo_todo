import os
def get_dir_files(root_dir):
    view_files = []
    for root,dirs,files in os.walk(root_dir):
        for filespath in files:
            if filespath.endswith('View.py'):
                view_files.append(filespath[:-3])
    return view_files

