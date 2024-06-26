<h2>Tensorflow-Image-Segmentation-MoNuSeg (2024/06/27)</h2>

This is the first experiment of Image Segmentation for MoNuSeg (Multi Organ Nuclei Segmentation) based on
the <a href="https://github.com/sarah-antillia/Tensorflow-Image-Segmentation-API">Tensorflow-Image-Segmentation-API</a>, and
<a href="https://drive.google.com/file/d/1QY6VAFbZSwDmtGVGYYiU9xwWXpQ2yFbn/view?usp=sharing">
MoNuSeg-2018-ImageMask-Dataset-V1.zip</a>, which was derived by us from the original dataset <a href="https://monuseg.grand-challenge.org/Data/">Challenges/MoNuSeg/Data</a>.<br>
<br>
The dataset used here has been taken from the following web-site<br>
<b>Challenges/MoNuSeg/Data</b><br>
<pre>
https://monuseg.grand-challenge.org/Data/
</pre>
Please see also <a href="https://github.com/sarah-antillia/ImageMask-Dataset-MoNuSeg">ImageMask-Dataset-MoNuSeg</a>
<br>
<hr>
<b>Actual Image Segmentation for Images of 1000x1000 pixels</b><br>
<table>
<tr>
<th>Input: image</th>
<th>Mask (ground_truth)</th>
<th>Prediction: inferred_mask</th>
</tr>
<tr>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/images/TCGA-AC-A2FO-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/masks/TCGA-AC-A2FO-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test_output/TCGA-AC-A2FO-01A-01-TS1.jpg" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/images/TCGA-EJ-A46H-01A-03-TSC.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/masks/TCGA-EJ-A46H-01A-03-TSC.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test_output/TCGA-EJ-A46H-01A-03-TSC.jpg" width="320" height="auto"></td>
</tr>

</table>

<hr>
<br>
In this experiment, we have used the simple UNet Model 
<a href="./src/TensorflowUNet.py">TensorflowSlightlyFlexibleUNet</a> for this Oral Cancer Segmentation.<br>
As shown in <a href="https://github.com/sarah-antillia/Tensorflow-Image-Segmentation-API">Tensorflow-Image-Segmentation-API</a>.
you may try other Tensorflow UNet Models:<br>

<li><a href="./src/TensorflowSwinUNet.py">TensorflowSwinUNet.py</a></li>
<li><a href="./src/TensorflowMultiResUNet.py">TensorflowMultiResUNet.py</a></li>
<li><a href="./src/TensorflowAttentionUNet.py">TensorflowAttentionUNet.py</a></li>
<li><a href="./src/TensorflowEfficientUNet.py">TensorflowEfficientUNet.py</a></li>
<li><a href="./src/TensorflowUNet3Plus.py">TensorflowUNet3Plus.py</a></li>
<li><a href="./src/TensorflowDeepLabV3Plus.py">TensorflowDeepLabV3Plus.py</a></li>

<br>

<h3>1. Dataset Citation</h3>

The dataset used here has been taken from the following web-site<br>
<b>Challenges/MoNuSeg/Data</b><br>
<pre>
https://monuseg.grand-challenge.org/Data/
</pre>
Please cite the following papers if you use the training and testing datasets of this challenge:<br>

N. Kumar et al., "A Multi-organ Nucleus Segmentation Challenge," in IEEE Transactions on <br>
Medical Imaging (in press) [Supplementary Information] [Code]<br>
N. Kumar, R. Verma, S. Sharma, S. Bhargava, A. Vahadane and A. Sethi, <br>
"A Dataset and a Technique for Generalized Nuclear Segmentation for Computational Pathology,"<br>
in IEEE Transactions on Medical Imaging, vol. 36, no. 7, pp. 1550-1560, July 2017 [Code]<br>
<br>

<b>License</b>: CC BY-NC-SA 4.0<br><br>

<h3>
<a id="2">
2 MoNuSeg ImageMask Dataset
</a>
</h3>
 If you would like to train this MoNuSeg Segmentation model by yourself,
 please download the dataset from the google drive 
<a href="https://drive.google.com/file/d/1QY6VAFbZSwDmtGVGYYiU9xwWXpQ2yFbn/view?usp=sharing">
MoNuSeg-2018-ImageMask-Dataset-V1.zip</a>.
<br>
Please expand the downloaded ImageMaskDataset and place it under <b>./dataset</b> folder to be
<pre>
./dataset
└─MoNuSeg
    ├─test
    │   ├─images
    │   └─masks
    ├─train
    │   ├─images
    │   └─masks
    └─valid
        ├─images
        └─masks
</pre>

<b>MoNuSeg Dataset Statistics</b><br>
<img src ="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/MoNuSeg-ImageMask-Dataset-V1_Statistics.png" width="512" height="auto"><br>
<br>
As shown above, the number of images of train and valid dataset is not necessarily large. 
<br>

<br>
<b>Train_images_sample</b><br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/asset/train_images_sample.png" width="1024" height="auto">
<br>
<b>Train_masks_sample</b><br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/asset/train_masks_sample.png" width="1024" height="auto">
<br>

<h3>
4 Train TensorflowUNet Model
</h3>
 We have trained MoNuSeg TensorflowUNet Model by using the following
<a href="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/train_eval_infer.config"> <b>train_eval_infer.config</b></a> file. <br>
Please move to ./projects/MoNuSeg and run the following bat file.<br>
<pre>
>1.train.bat
</pre>
, which simply runs the following command.<br>
<pre>
>python ../../../src/TensorflowUNetTrainer.py ./train_eval_infer.config
</pre>
<pre>
; train_eval_infer.config
; 2024/06/27(C) antillia.com
[model]
model          = "TensorflowUNet"
generator      = False
image_width    = 512
image_height   = 512
image_channels = 3
input_normalize = False
num_classes    = 1
base_filters   = 16
base_kernels   = (5,5)
num_layers     = 8
dropout_rate   = 0.05
learning_rate  = 0.0001
clipvalue      = 0.5
dilation       = (2,2)
loss           = "bce_dice_loss"
metrics        = ["binary_accuracy"]
show_summary   = False

[train]
epochs        = 100
batch_size    = 2
patience      = 10
;metrics       = ["iou_coef", "val_iou_coef"]
metrics       = ["binary_accuracy", "val_binary_accuracy"]
model_dir     = "./models"
eval_dir      = "./eval"
image_datapath = "../../../dataset/MoNuSeg/train/images/"
mask_datapath  = "../../../dataset/MoNuSeg/train/masks/"
create_backup  = False
learning_rate_reducer = True
reducer_factor        = 0.2
reducer_patience      = 4

save_weights_only = True
;Inference execution flag on epoch_changed
epoch_change_infer     = True

; Output dir to save the inferred masks on epoch_changed
epoch_change_infer_dir =  "./epoch_change_infer"

;Tiled-inference execution flag on epoch_changed
epoch_change_tiledinfer     = False

; Output dir to save the tiled-inferred masks on epoch_changed
epoch_change_tiledinfer_dir =  "./epoch_change_tiledinfer"

; The number of the images to be inferred on epoch_changed.
num_infer_images       = 1


[eval]
image_datapath = "../../../dataset/MoNuSeg/valid/images/"
mask_datapath  = "../../../dataset/MoNuSeg/valid/masks/"

[test] 
image_datapath = "../../../dataset/MoNuSeg/test/images/"
mask_datapath  = "../../../dataset/MoNuSeg/test/masks/"

[infer] 
images_dir    = "./mini_test/images"
output_dir    = "./mini_test_output"
;merged_dir   = "./mini_test_output_merged"
;binarize      = True
sharpening   = True

[tiledinfer] 
overlapping   = 128
images_dir    = "./mini_oscc_test/images"
output_dir    = "./mini_oscc_test_output"
;merged_dir   = "./mini_test_output_merged"
;binarize      = True
sharpening   = True

[segmentation]
colorize      = False
black         = "black"
white         = "green"
blursize      = None

[mask]
blur      = False
blur_size = (3,3)
binarize  = False
threshold = 127
</pre>
In this configuration file above, we added the following parameters to enable <b>epoch_change_infer</b> callback in [train] section.<br>
<pre>
[train]
;Inference execution flag on epoch_changed
epoch_change_infer     = True
; Output dir to save the inferred masks on epoch_changed
epoch_change_infer_dir =  "./epoch_change_infer"

; The number of the images to be inferred on epoch_changed.
num_infer_images       = 1
</pre>

By using this callback, on every epoch_change, the inference procedures can be called
 for an image in <b>mini_test</b> folder.<br><br>
<b>Epoch_change_inference output</b><br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/asset/epoch_change_infer.png" width="1024" height="auto"><br>
<br>
<br>
The training process has just been stopped at epoch 57 by EarlyStopping Callback as shown below.<br><br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/asset/train_console_output_at_epoch_57.png" width="720" height="auto"><br>
<br>
<br>
<a href="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/eval/train_metrics.csv">train_metrics.csv</a><br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/eval/train_metrics.png" width="520" height="auto"><br>

<br>
<a href="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/eval/train_losses.csv">train_losses.csv</a><br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/eval/train_losses.png" width="520" height="auto"><br>

<br>

<h3>
5 Evaluation
</h3>
Please move to a <b>./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg</b> folder,<br>
and run the following bat file to evaluate TensorflowUNet model for MoNuSeg.<br>
<pre>
./2.evaluate.bat
</pre>
This bat file simply runs the following command.
<pre>
python ../../../src/TensorflowUNetEvaluator.py ./train_eval_infer_aug.config
</pre>
Evaluation console output:<br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/asset/evaluate_console_output_at_epoch_57.png" width="720" height="auto">
<br><br>
<a href="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/evaluation.csv">evaluation.csv</a><br>
The loss (bce_dice_loss) score for this test dataset is not so low, and accuracy not so heigh as shown below.<br>
<pre>
loss,0.3081
binary_accuracy,0.8354
</pre>

<h3>
6 Inference
</h3>
Please move to a <b>./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg</b> folder<br>
,and run the following bat file to infer segmentation regions for images by the Trained-TensorflowUNet model for MoNuSeg.<br>
<pre>
./3.infer.bat
</pre>
This simply runs the following command.
<pre>
python ../../../src/TensorflowUNetInferencer.py ./train_eval_infer_aug.config
</pre>
<hr>
<b>mini_test_images</b><br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/asset/mini_test_images.png" width="1024" height="auto"><br>
<b>mini_test_mask(ground_truth)</b><br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/asset/mini_test_masks.png" width="1024" height="auto"><br>

<hr>
<b>Inferred test masks</b><br>
<img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/asset/mini_test_output.png" width="1024" height="auto"><br>
<br>


<b>Enlarged images and masks </b><br>

<table>
<tr>
<th>Image</th>
<th>Mask (ground_truth)</th>
<th>Inferred-mask</th>
</tr>

<tr>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/images/TCGA-2Z-A9J9-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/masks/TCGA-2Z-A9J9-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test_output/TCGA-2Z-A9J9-01A-01-TS1.jpg" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/images/TCGA-69-7764-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/masks/TCGA-69-7764-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test_output/TCGA-69-7764-01A-01-TS1.jpg" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/images/TCGA-AC-A2FO-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/masks/TCGA-AC-A2FO-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test_output/TCGA-AC-A2FO-01A-01-TS1.jpg" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/images/TCGA-GL-6846-01A-01-BS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/masks/TCGA-GL-6846-01A-01-BS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test_output/TCGA-GL-6846-01A-01-BS1.jpg" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/images/TCGA-HC-7209-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test/masks/TCGA-HC-7209-01A-01-TS1.jpg" width="320" height="auto"></td>
<td><img src="./projects/TensorflowSlightlyFlexibleUNet/MoNuSeg/mini_test_output/TCGA-HC-7209-01A-01-TS1.jpg" width="320" height="auto"></td>
</tr>

</table>
<br>
<br>
<!--
  -->

<h3>
References
</h3>

<b>1. A Multi-Organ Nucleus Segmentation Challenge</b><br>
PMID: 31647422 PMCID: PMC10439521 DOI: 10.1109/TMI.2019.2947628<br>
Neeraj Kumar, Ruchika Verma, Deepak Anand, Yanning Zhou, Omer Fahri Onder, Efstratios Tsougenis, <br>
Hao Chen, Pheng-Ann Heng, Jiahui Li, Zhiqiang Hu, Yunzhi Wang, Navid Alemi Koohbanani, <br>
Mostafa Jahanifar, Neda Zamani Tajeddin, Ali Gooya, Nasir Rajpoot, Xuhua Ren, Sihang Zhou, Qian Wang,<br>
Dinggang Shen, Cheng-Kun Yang, Chi-Hung Weng, Wei-Hsiang Yu, Chao-Yuan Yeh, Shuang Yang, Shuoyu Xu, <br>
Pak Hei Yeung, Peng Sun, Amirreza Mahbod, Gerald Schaefer, Isabella Ellinger, Rupert Ecker, Orjan Smedby,<br>
Chunliang Wang, Benjamin Chidester, That-Vinh Ton, Minh-Triet Tran, Jian Ma, Minh N Do, Simon Graham, <br>
Quoc Dang Vu, Jin Tae Kwak, Akshaykumar Gunda, Raviteja Chunduri, Corey Hu, Xiaoyang Zhou, Dariush Lotfi,<br>
Reza Safdari, Antanas Kascenas, Alison O'Neil, Dennis Eschweiler, Johannes Stegmaier, Yanping Cui, Baocai Yin,<br>
Kailin Chen, Xinmei Tian, Philipp Gruening, Erhardt Barth, Elad Arbel, Itay Remer, Amir Ben-Dor, <br>
Ekaterina Sirazitdinova, Matthias Kohl, Stefan Braunewell, Yuexiang Li, Xinpeng Xie, Linlin Shen, Jun Ma, <br>
Krishanu Das Baksi, Mohammad Azam Khan, Jaegul Choo, Adrian Colomer, Valery Naranjo, Linmin Pei, <br>
Khan M Iftekharuddin, Kaushiki Roy, Debotosh Bhattacharjee, Anibal Pedraza, Maria Gloria Bueno, <br>
Sabarinathan Devanathan, Saravanan Radhakrishnan, Praveen Koduganty, Zihan Wu, Guanyu Cai, <br>
Xiaojie Liu, Yuqin Wang, Amit Sethi<br>
<pre>
https://pubmed.ncbi.nlm.nih.gov/31647422/
</pre>
<br>
<b>4. ImageMask-Dataset-MoNuSeg</b><br>
Toshiyuki Arai antillia.com<br>
<pre>
https://github.com/sarah-antillia/ImageMask-Dataset-MoNuSeg
</pre>


