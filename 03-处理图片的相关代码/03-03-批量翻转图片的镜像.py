#===============================================================================
# @艺用常见Python代码-批量修改图片方向
# @本代码由AI 文心大模型4.0 生成  JL进行人工挑选、整理和注释
# @本代码适用于为图片批量翻转镜像，使用本代码前请先安装Pillow库和TQDM库
# @如未安装Pillow库，请以管理员身份打开终端并执行"pip install pillow"
# @如未安装TQDM库，请以管理员身份打开终端并执行"pip install tqdm"
# @如无法运行pip，请删除该版本Python，重新安装并勾选"Add python.exe to PATH"
# @无需理解整个代码的意思和原理，仅替换要修改的部分就可以实现功能
# @请忽略前面的部分向下拉直到看见--------要修改的部分开始--------
#===============================================================================

import os  
from PIL import Image  
from tqdm import tqdm  
  
# 设置输入和输出文件夹路径  
input_folder = 'path/to/input/folder'  # 输入文件夹，包含原始图片  
output_folder = 'path/to/output/folder'  # 输出文件夹，用于保存镜像后的图片  
  
# 确保输出文件夹存在  
if not os.path.exists(output_folder):  
    os.makedirs(output_folder)  
  
# 获取输入文件夹中所有图片文件的列表  
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png', '.bmp', '.gif', '.tif', '.tiff', '.pdf'))]  
  
# 使用tqdm显示进度条  
with tqdm(total=len(image_files), desc="镜像处理进度", unit="图片") as pbar:  
    for filename in image_files:  
        # 构建完整的文件路径  
        input_path = os.path.join(input_folder, filename)  
        output_path = os.path.join(output_folder, filename)  
          
        # 打开图片  
        with Image.open(input_path) as img:  
            # 水平镜像图片  
            mirrored_img = img.transpose(Image.FLIP_LEFT_RIGHT)  
              
            # 保存镜像后的图片  
            mirrored_img.save(output_path)  
          
        # 更新进度条  
        pbar.update()  
  
print("镜像处理完成。")
