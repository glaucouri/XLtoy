import os
import subprocess



for fname in os.listdir():
    if fname.endswith('xlsx'):

        # Without parser enabled
        destname = "{}.yaml".format(os.path.splitext(fname)[0])
        if os.path.exists(destname):
            print("{} nothing to do".format(destname))
        else:
            print('Doing {}'.format(destname))
            with open(destname, 'wt') as outfile:
                subprocess.run(['xltoy','collect',fname,'--yaml'], stdout=outfile)


        # Parser enabled
        destname = "{}.parsed.yaml".format(os.path.splitext(fname)[0])
        if os.path.exists(destname):
            print("{} nothing to do".format(destname))
        else:
            print('Doing {}'.format(destname))
            with open(destname, 'wt') as outfile:
                subprocess.run(['xltoy','collect',fname,'--parsed','--yaml'], stdout=outfile)

