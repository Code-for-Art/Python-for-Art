#===============================================================================
# @艺用常见Python代码-批量修改图片大小
# @本代码由AI 文心大模型4.0 生成  JL进行人工挑选、整理和注释
# @本代码适用于为图片批量更改格式，使用本代码前请先安装Pillow库
# @如未安装Pillow库，请以管理员身份打开终端并执行"pip install pillow"
# @如无法运行pip，请删除该版本Python，重新安装并勾选"Add python.exe to PATH"
# @无需理解整个代码的意思和原理，仅替换要修改的部分就可以实现功能
# @请忽略前面的部分向下拉直到看见--------要修改的部分开始--------
# @本代码有2个部分需要修改，第1个部分是图片格式，第2个部分是图片路径
#===============================================================================

import os  
from PIL import Image  




#===============================================================================
#-------------------------------要修改的部分1开始--------------------------------

def batch_convert_images(input_folder, output_folder, input_extension='.jpg', output_extension='.bmp'): 

# 请在前面单引号里填上原始的文件格式如：'.jpg'，请在后面的单引号里填上要生成的文件格式如：'.bmp'
# 常见的文件格式均可互相转换，如：'.bmp'、'.jpg'、'.png'、'.gif'、'.pdf'等

#-------------------------------要修改的部分1结束--------------------------------
#===============================================================================



    """  
    批量转换图片格式。  
      
    :param input_folder: 包含原图片的文件夹路径。  
    :param output_folder: 输出文件夹路径。  
    :param input_extension: 原图片的文件扩展名（默认是.jpg）。  
    :param output_extension: 输出图片的文件扩展名（默认是.bmp）。  
    """  
    # 确保输出文件夹存在  
    if not os.path.exists(output_folder):  
        os.makedirs(output_folder)  
      
    # 遍历输入文件夹中的所有图片文件  
    for filename in os.listdir(input_folder):  
        if filename.lower().endswith(input_extension):  
            # 构建完整的输入和输出文件路径  
            input_path = os.path.join(input_folder, filename)  
            filename_without_ext = os.path.splitext(filename)[0]  
            output_path = os.path.join(output_folder, f"{filename_without_ext}{output_extension}")  
              
            # 打开图片并保存为新的格式  
            with Image.open(input_path) as img:  
                img.save(output_path)  
              
            print(f"Converted {input_path} to {output_path}")  
  

#===============================================================================
#-------------------------------要修改的部分2开始--------------------------------
# 设置输入和输出文件夹路径  
input_folder = "path/to/input/jpg_folder"  # 请替换为实际的.jpg图片文件夹路径  
output_folder = "path/to/output/bmp_folder"  # 请替换为期望的输出文件夹路径 

    #如文件存储在工作目录aaa文件夹的aaa1子文件夹中，请将路径写为"aaa/aaa1"
    #如果要使用相对路径，请使用工作目录并信任。除此之外也可使用绝对路径
    #如文件储存在D盘的aaa文件夹中，要将改名的文件放在D盘的bbb文件夹中，请将上面的代码修改为：
    #src_directory = "D:/aaa"  # 请替换为源目录路径  
    #dst_directory = "D:/bbb"  # 请替换为目标目录路径  
    #如果这个路径是从文件管理器复制过来的，请将路径中的\手动修改为/
    #请不要将修改过的文件和原来的文件放在同一个文件夹中
    #如果之前没有bbb文件夹，程序会自动创建
    
#-------------------------------要修改的部分2结束--------------------------------
#=============================================================================== 
  
# 调用函数进行批量转换  
batch_convert_images(input_folder, output_folder)
