class FileReader(object):
    def __init__(self, file_name, mode='r'):
        print('__init__ called')
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('__enter__ called')
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ called')
        self.file.close()


with FileReader('sample.txt', 'w') as f:
    f.write('hello')