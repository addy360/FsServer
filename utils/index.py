import pathlib

class MyFs():
    def __init__(self):
        self.path = pathlib.Path.home()

    def set_path(self,path):
        self.path = pathlib.Path(path)

    def get_home_dir(self):
        return pathlib.Path(pathlib.Path.home())

    def list_files (self):
        files = []
        try:
            for i in self.path.iterdir():
                if(i.is_file()):
                    files.append(i.as_uri())
        except :
            return False
       
        return files 

    def list_dirs (self):
        dirs = []
        try:
            for i in self.path.iterdir():
                if(i.is_dir()):
                    dirs.append(i.as_uri())
        except PermissionError:
            return False
        except FileNotFoundError:
            return False
        return dirs

    def list_all_dirs(self):
        dirs = self.list_dirs()   
        for dir_path in dirs:
            print(dir_path)
            self.set_path(dir_path)
            self.list_all_dirs()

    def find_file(self, query):
        dirs = self.list_dirs()
        for dir_path in dirs:
            for f in self.path.glob(query):
                print(f)
            self.set_path(dir_path)
            self.find_file(query)
            

    def run(self):
        return self.list_dirs()




