#!/usr/bin/env bash
python main.py --gpus 3 --method pt_and_ft --pt_method be \
--pt_batch_size 4 --pt_workers 4  --arch i3d --pt_spatial_size 224 --pt_stride 4 --pt_data_length 16 \
--pt_nce_k 3569 --pt_softmax \
--pt_moco --pt_epochs 10 --pt_save_freq 4 --pt_print_freq 100 --pt_dataset hmdb51 \
--pt_train_list ../datasets/lists/hmdb51/hmdb51_rgb_train_split_1.txt \
--pt_val_list ../datasets/lists/hmdb51/hmdb51_rgb_val_split_1.txt \
--ft_train_list ../datasets/lists/hmdb51/hmdb51_rgb_train_split_1.txt \
--ft_val_list ../datasets/lists/hmdb51/hmdb51_rgb_val_split_1.txt \
--ft_dataset hmdb51 --ft_mode rgb \
--ft_lr 0.001 --ft_lr_steps 10 20 25 30 35 40 --ft_epochs 45 --ft_batch_size 4 \
--ft_data_length 64 --ft_spatial_size 224 --ft_workers 4 --ft_stride 1 --ft_dropout 0.5 \
--ft_print-freq 100 --ft_fixed 0