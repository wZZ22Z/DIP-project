# DIP-project
# DIP-project

文件 BEST_checkpoint_coco_5_cap_per_img_5_min_word_freq.pth为训练好的模型。由于时间问题和运行速度，该模型并未训练完全。完整的训练模型预计在7.5号训练完成。

本项目使用pytorch完成图像配字幕（Image Captioning）

环境为：

python3.8 

PyTorch1.9.1

文件包括：

| 项目文件              | 功能                                   |
| --------------------- | -------------------------------------- |
| utils.py              | 支撑各种功能的辅助文件                 |
| create_input_files.py | 生成输入的训练数据、测试数据、验证数据 |
| datasets.py           | 继承PyTorch的DataSet类                 |
| models.py             | 定义模型结构                           |
| train.py              | 训练模型                               |
| caption.py            | 使用beam search生成字幕并进行可视化    |

其中，关键文件为models.py、train.py以及caption.py

[模型链接](https://pan.baidu.com/s/1gpJTgFSWJNEpyIqMSbBUxg)

提取码1234

