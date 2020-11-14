import json
import os
import random
import numpy as np
import shutil

if __name__ == '__main__':

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    filename= "/data/gt.json"
    train_path = os.path.join(ROOT_DIR + "/train")
    val_path = os.path.join(ROOT_DIR + "/val")
    images_path = os.path.join(ROOT_DIR + "/data/images")
    json_path = os.path.join(ROOT_DIR + filename)

    f = open(json_path)
    gt_json = json.load(f)
    f.close()

    imgs = list(gt_json.keys())
    random.shuffle(imgs)
    imgs_nr = len(imgs)
    train_imgs = imgs[0:int(0.8*imgs_nr)]
    val_imgs = imgs[int(0.8*imgs_nr):-1]

    train_json = dict()
    for i in train_imgs:
        shutil.copy2(src=os.path.join(images_path,i),dst=os.path.join(train_path,i))
        train_json[i] = gt_json[i]

    open(os.path.join(train_path, "via_region_data.json"),'w').close()
    with open(os.path.join(train_path, "via_region_data.json"),'w') as f:
        json.dump(train_json,f)

    val_json = dict()
    for i in val_imgs:
        shutil.copy2(src=os.path.join(images_path,i),dst=os.path.join(val_path,i))
        val_json[i] = gt_json[i]

    open(os.path.join(val_path, "via_region_data.json"), 'w').close()
    with open(os.path.join(val_path, "via_region_data.json"), 'w') as f:
        json.dump(val_json, f)

    r = 1


