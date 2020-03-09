import matplotlib.pyplot as plt
import numpy as np

def plot(x, y):
    if type(y[0]) is list:
        for y_i in range(len(y)):
            plt.plot(x, y[y_i])
        plt.show()
    else:
        plt.plot(x, y)
        plt.show()

def file_preparation(file_name):
    cls_labels_res = []
    num_gt_res = []
    count_res = []

    file_name = file_name.split(',')
    for file in file_name:
        print(file)
        cls_labels = []
        num_gt = []

        f = open(file, 'r')
        for line in f:
            cls_labels.append(int(line.split()[1]))
            num_gt.append(int(line.split()[3]))
        cls_labels_res.append(cls_labels)
        num_gt_res.append(num_gt)
    for i in range(len(cls_labels_res[0])):
        count_res.append(i+1)

    return cls_labels_res, num_gt_res, count_res


def main():
    # y = [[3, 4, 6, 7, 3, 5], [6, 8, 5, 8, 9, 10], [2, 1, 4, 3, 2, 2]]
    # # y = [3, 4, 6, 7, 3, 5]
    # x = [1, 2, 3, 4, 5, 6]
    # # print(y[0])
    # res = []
    # for i in range(len(y)):
    #     res.append(np.divide(y[i], x).tolist())
    # print(res)



    cls_labels, num_gt, count = file_preparation('retinanet_giou_record_proposal_gtbbox.txt,fcos_giou_record_proposal_gtbbox.txt,atss_iou_giou_record_proposal_gtbbox.txt')
    num_cls_labels_per_gt = []
    for i in range(len(cls_labels)):
        num_cls_labels_per_gt.append(np.divide(cls_labels[i], num_gt[i]).tolist())
    # print(num_cls_labels_per_gt[1])
    plot(count, num_cls_labels_per_gt[2])

    # plot(x, y[1])

if __name__ == '__main__':
    main()