#batch_file_rename
#Created:2018-10-16

'''
this will batch rename a group of files in a given directory

'''

__author__='guannanwu'
__version__='1.0'

import os
import argparse

def batch_rename(work_dir,old_ext,new_ext):
    '''
    this will batch rename a group of files
    '''
    for filename in os.listdir(work_dir):
        #get the file extension

        #os.path.splittext()分割文件的扩展名与文件名
        split_file=os.path.splitext(filename)#os.path is a module
        file_ext=split_file[1]

        if old_ext==file_ext:
            newfile=split_file[0]+new_ext

            #os.rename(src,dst),将src的文件名替换为dst的

            os.rename(
                os.path.join(work_dir,filename),
                os.path.join(work_dir,newfile)
            )
            

def get_parser():
    #创建一个解析对象
    parser=argparse.ArgumentParser(description='change extension of files in a working directory')

    parser.add_argument('work_dir',metavar='WORK_DIR',type=str,nargs=1,help='the directory where to change extension')
    parser.add_argument('old_ext',metavar='OLD_EXT',type=str,nargs=1,help='the old extension')
    parser.add_argument('new_ext',metavar='NEW_EXT',type=str,nargs=1,help='the new extension')
    return parser


def main():
    '''
    this will be called if the script is directly invoked
    '''
    parser=get_parser()
    #parser.parse_args()对对象进行解析
    args=vars(parser.parse_args())

    work_dir=args['work_dir'][0]

    old_ext=args['old_ext'][0]

    if old_ext[0]!='.':
        old_ext='.'+old_ext
    
    new_ext=args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = '.' + new_ext

    batch_rename(work_dir,old_ext,new_ext)

#当作为模块被导入的时候，不会运行下面的，而作为.py直接运行的时候，会运行下面的
if __name__=='__main__':
    main()