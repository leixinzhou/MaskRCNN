# mask-rcnn


This is a Pytorch 1.0 implementation of [Mask R-CNN](https://arxiv.org/abs/1703.06870) that is based on https://github.com/darolt/mask_rcnn.

The difference:
* Add support to Python3

to train the network use:
python3 samples/nuclei.py train --dataset=path_to_dataset --model=coco

to detect use:
python3 samples/nuclei.py submit --dataset=path_to_dataset --model=path_to_trained_model

to check Kaggle's 2018 Databowl metric on a dataset use:
python3 samples/nuclei.py metric --dataset=path_to_dataset --model=path_to_trained_model

for installation instructions, just export mrcnn directory to PYTHONPATH and run:
python3 setup.py install or python3 setup.py install --prefix=your_dir

