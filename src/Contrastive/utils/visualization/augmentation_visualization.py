#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import torch
import torch.backends.cudnn as cudnn
from data.config import data_config, augmentation_config
from data.dataloader import data_loader_init
from model.config import model_config
from augment.gen_positive import GenPositive
from bk.option_old import args
import numpy as np

lowest_val_loss = float('inf')
best_prec1 = 0
torch.manual_seed(1)


def test(train_loader, model, suffix='each_rotation_10'):
    model.eval()
    for i, (inputs, _, index) in enumerate(train_loader):
        dir_path = "../experiments/visualization/augmentation/{}_{}".format(suffix, index[0])
        # if not os.path.exists(dir_path):
        #     os.makedirs(dir_path)
        augmentation_video = inputs[0].permute(1, 2, 3, 0).cpu().numpy()
        np.save("{}.npy".format(dir_path), augmentation_video)
        # print(augmentation_video.shape)
        # path = "{}/{}.avi".format(dir_path, str(index[0].cpu().numpy()))
        # print(path)
        # save_video(augmentation_video, path)
        print("{}/{} finished".format(i, len(train_loader)))
        # output = model(anchor)
    return True


def main():
    # =
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # close the warning
    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpus
    torch.manual_seed(1)
    cudnn.benchmark = True
    # == dataset config==
    num_class, data_length, image_tmpl = data_config(args)
    train_transforms, test_transforms, eval_transforms = augmentation_config(args)
    train_data_loader, val_data_loader, _, _, _, _ = data_loader_init(args, data_length, image_tmpl, train_transforms, test_transforms, eval_transforms)
    # == model config==
    model = model_config(args, num_class)
    pos_aug = GenPositive()
    # == train and eval==
    test(val_data_loader, model)
    return 1


if __name__ == '__main__':
    main()