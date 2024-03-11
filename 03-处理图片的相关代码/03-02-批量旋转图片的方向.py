#===============================================================================
# @艺用常见Python代码-批量修改图片方向
# @本代码由AI 文心大模型4.0 生成  JL进行人工挑选、整理和注释
# @本代码适用于为图片批量旋转方向，使用本代码前请先安装Pillow库
# @如未安装Pillow库，请以管理员身份打开终端并执行"pip install pillow"
# @如无法运行pip，请删除该版本Python，重新安装并勾选"Add python.exe to PATH"
# @无需理解整个代码的意思和原理，仅替换要修改的部分就可以实现功能
# @请忽略前面的部分向下拉直到看见--------要修改的部分开始--------
#===============================================================================


import os  
from PIL import Image  
  
def rotate_images(src_folder, dst_folder, rotation_angle):  
    """  
    批量旋转图片并保存到新文件夹。  
  
    :param src_folder: 原始图片所在的文件夹。  
    :param dst_folder: 旋转后的图片保存的目标文件夹。  
    :param rotation_angle: 旋转角度，向左旋转为90，向右旋转为-90。  
    """  
    # 确保目标文件夹存在  
    os.makedirs(dst_folder, exist_ok=True)  
  
    # 遍历源文件夹中的所有文件  
    for filename in os.listdir(src_folder):  
        # 构造完整的文件路径  
        src_path = os.path.join(src_folder, filename)  
        dst_path = os.path.join(dst_folder, filename)  
  
        # 确保处理的是图片文件  
        if os.path.isfile(src_path) and any(src_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif']):  
            try:  
                # 打开图片  
                with Image.open(src_path) as img:  
                    # 旋转图片  
                    rotated_img = img.rotate(rotation_angle, expand=True)  
                    # 保存旋转后的图片  
                    rotated_img.save(dst_path)  
                print(f"图片 {filename} 已旋转并保存到 {dst_path}")  
            except Exception as e:  
                print(f"处理图片 {filename} 时出错：{e}")  
  
if __name__ == "__main__":  





#===============================================================================
#--------------------------------要修改的部分开始--------------------------------
    # 设置源文件夹和目标文件夹  
    SOURCE_FOLDER = "path/to/source/folder"  # 替换为源文件夹路径  
    DESTINATION_FOLDER = "path/to/destination/folder"  # 替换为目标文件夹路径  
    
    #如文件存储在工作目录aaa文件夹的aaa1子文件夹中，请将路径写为"aaa/aaa1"
    #如果要使用相对路径，请使用工作目录并信任。除此之外也可使用绝对路径
    #如文件储存在D盘的aaa文件夹中，要将改名的文件放在D盘的bbb文件夹中，请将上面的代码修改为：
    #src_directory = "D:/aaa"  # 请替换为源目录路径  
    #dst_directory = "D:/bbb"  # 请替换为目标目录路径  
    #如果这个路径是从文件管理器复制过来的，请将路径中的\手动修改为/
    #请不要将修改过的文件和原来的文件放在同一个文件夹中
    #如果之前没有bbb文件夹，程序会自动创建
  
    # 设置旋转角度，向左旋转90度或向右旋转-90度  
    ROTATION_ANGLE = 90  # 向左旋转，如果你想向右旋转，则使用 -90  
    
#--------------------------------要修改的部分结束--------------------------------
#===============================================================================
  
    # 调用函数批量旋转图片  
    rotate_images(SOURCE_FOLDER, DESTINATION_FOLDER, ROTATION_ANGLE)
