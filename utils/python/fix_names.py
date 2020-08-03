#!/usr/bin/python3
import os
import re

def main():

    path = '../../public/img/team'
    photo_names = os.listdir(path)

    for photo_name in photo_names:
        renamed = re.sub('_',  '-', photo_name)
        os.rename(os.path.join(path,photo_name),
                os.path.join(path, renamed))


if __name__ == '__main__':
    main()
