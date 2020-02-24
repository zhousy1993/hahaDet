from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

dataDir='/home/zhousy/coco/annotations/instances_train2017.json'

coco = COCO(dataDir)

# print(len(coco.getAnnIds()))
# print(coco.getAnnIds())
# print(coco.getAnnIds()[0])
# print(len(coco.getImgIds()))
# print(coco.getImgIds())
# print(coco.getImgIds()[0])
# print(len(coco.getCatIds()))
# print(coco.getCatIds())
# print(coco.getCatIds()[0])

img_id = coco.getImgIds()

ann_id = coco.getAnnIds()

cat_id = coco.getCatIds()

print(cat_id)

total_anns = [coco.loadAnns(id)[0] for id in ann_id]

# print(len(total_anns))
# print(total_anns[0])



# sample_ann = coco.loadAnns(ann_id)
# print('haha')
# print(sample_ann[0]['bbox'])

def statistics_sum_ins_per_cat(total_anns, cat_id):
    """
    Func: calculate the sum of the bbox for each catagories throughout the dataset
    Args:
        total_anns:

    Returns:

    """
    count_sum = [0 for i in range(len(cat_id))]
    print(len(count_sum))
    count = 0
    for i in range(len(total_anns)):
        print(total_anns[i]['category_id'])
        count += 1
        print(count)
        count_sum[cat_id.index(total_anns[i]['category_id'])-1] = count_sum[cat_id.index(total_anns[i]['category_id'])-1] + 1

    return count_sum

def main():
    a = statistics_sum_ins_per_cat(total_anns, cat_id)
    print(a)

if __name__ == '__main__':
    main()