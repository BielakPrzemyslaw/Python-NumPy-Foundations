import os
import distutils.dir_util

folder_on_disc_C = "C:/Users/bielakp/Desktop/Target/"

old_name = r"C:/Users/bielakp/Desktop/Target/NX11"
new_name = r"C:/Users/bielakp/Desktop/Target/NX 11"

src = r"C:/Users/bielakp/Desktop/Oryginal/NX 11"
dst = r"C:/Users/bielakp/Desktop/Target/NX 11"

for f in os.listdir(folder_on_disc_C):
    if f.endswith(" 11"):
        folder_on_disc_C = os.path.join(src, dst)
        distutils.dir_util.copy_tree(src, dst)
        print("Copy")
    else:
        if f.endswith("11"):
            os.rename(old_name, new_name)
            folder_on_disc_C = os.path.join(src, dst)
            distutils.dir_util.copy_tree(src, dst)
            os.rename(new_name, old_name)
            print("Copy2")


