import os
import argparse

from PIL import Image
import PIL

def walk(path, r = False):
    if os.path.isfile(path):
        compress(path)
    else :
        for f in os.listdir(path):

            if os.path.isdir(os.path.join(path,f)) & r:
                print('Searching subfolder : ' + f)
                walk(os.path.join(path,f), r) 
            else:
                compress(os.path.join(path,f))
def compress(f):
    if f.endswith('.jpg') | f.endswith('.png') | f.endswith('.gif'):
        Image.open(f).save(f,optimize=True,quality=85)
        print(f'File : "{f}" compressed')

parser = argparse.ArgumentParser()
parser.add_argument('-r', action='store_true', default=False, help='use recursion')
parser.add_argument('--path', default=os.getcwd(), help='the path of the file or folder to compress, default to current work directory')
args = parser.parse_args()

walk(args.path,args.r)
