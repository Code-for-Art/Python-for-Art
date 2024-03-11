#===============================================================================
# @艺用常见Python代码-批量修改图片大小
# @本代码由AI 文心大模型4.0 生成  JL进行人工挑选、整理和注释
# @本代码适用于为图片批量缩放大小，使用本代码前请先安装Pillow库
# @如未安装Pillow库，请以管理员身份打开终端并执行"pip install pillow"
# @如无法运行pip，请删除该版本Python，重新安装并勾选"Add python.exe to PATH"
# @无需理解整个代码的意思和原理，仅替换要修改的部分就可以实现功能
# @请忽略前面的部分向下拉直到看见--------要修改的部分开始--------
#===============================================================================

import os  
from PIL import Image  
  
def resize_images(input_folder, output_folder, new_size, is_width=True):  
    """  
    调整文件夹中所有图片的尺寸到指定的宽度或高度。  
  
    :param input_folder: 包含图片的输入文件夹路径。  
    :param output_folder: 输出调整尺寸后的图片的文件夹路径。  
    :param new_size: 新的宽度或高度（取决于is_width参数）。  
    :param is_width: 如果为True，则new_size为新宽度；如果为False，则new_size为新高度。  
    """  
  
    # 确保输出文件夹存在  
    if not os.path.exists(output_folder):  
        os.makedirs(output_folder)  
  
    # 遍历输入文件夹中的所有文件  
    for filename in os.listdir(input_folder):  
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):  
            input_path = os.path.join(input_folder, filename)  
            output_path = os.path.join(output_folder, filename)  
  
            try:  
                with Image.open(input_path) as img:  
                    if is_width:  
                        # 设置新的宽度并保持高度比例  
                        width, height = new_size, int(img.height * new_size / img.width)  
                    else:  
                        # 设置新的高度并保持宽度比例  
                        height, width = new_size, int(img.width * new_size / img.height)  
                      
                    resized_img = img.resize((width, height), Image.LANCZOS)  # Pillow10之后ANTIALIAS替换为LANCZOS
                    resized_img.save(output_path)  
  
                print(f"Resized {filename} to {width}x{height} and saved to {output_path}")  
  
            except Exception as e:  
                print(f"Error resizing {filename}: {e}")  
  
if __name__ == "__main__":  




#===============================================================================
#--------------------------------要修改的部分开始--------------------------------
    # 设置输入和输出文件夹路径  
    input_folder = "path/to/input/folder"  # 请替换为实际输入文件夹路径  
    output_folder = "path/to/output/folder"  # 请替换为实际输出文件夹路径  
    
    #如文件存储在工作目录aaa文件夹的aaa1子文件夹中，请将路径写为"aaa/aaa1"
    #如果要使用相对路径，请使用工作目录并信任。除此之外也可使用绝对路径
    #如文件储存在D盘的aaa文件夹中，要将改名的文件放在D盘的bbb文件夹中，请将上面的代码修改为：
    #src_directory = "D:/aaa"  # 请替换为源目录路径  
    #dst_directory = "D:/bbb"  # 请替换为目标目录路径  
    #如果这个路径是从文件管理器复制过来的，请将路径中的\手动修改为/
    #请不要将修改过的文件和原来的文件放在同一个文件夹中
    #如果之前没有bbb文件夹，程序会自动创建
  
    # 设置新的宽度或高度（以像素为单位）  
    # 例如，要设置新宽度为1920像素，调用函数如下：  
    resize_images(input_folder, output_folder, 1920, is_width=True)  
  
    # 或者，要设置新高度为1080像素，调用函数如下：  
    # resize_images(input_folder, output_folder, 1080, is_width=False)
#--------------------------------要修改的部分结束--------------------------------
#===============================================================================
