#===============================================================================
# @艺用常见Python代码-批量修改图片大小
# @本代码由AI 文心大模型4.0 生成  JL进行人工挑选、整理和注释
# @本代码适用于为图片批量添加水印，使用本代码前请先安装Pillow库
# @如未安装Pillow库，请以管理员身份打开终端并执行"pip install pillow"
# @如无法运行pip，请删除该版本Python，重新安装并勾选"Add python.exe to PATH"
# @无需理解整个代码的意思和原理，仅替换要修改的部分就可以实现功能
# @请忽略前面的部分向下拉直到看见--------要修改的部分开始--------
#===============================================================================

import os  
from PIL import Image  
  
def add_watermark(image_path, watermark_path, output_path, watermark_width_percent=1.0):  
    """  
    给图片添加水印。  
  
    :param image_path: 原图片路径。  
    :param watermark_path: 水印图片路径（PNG格式）。  
    :param output_path: 输出图片路径。  
    :param watermark_width_percent: 水印宽度占图片宽度的百分比。  
    """  
    # 打开原图片和水印图片  
    base_image = Image.open(image_path).convert("RGBA")  
    watermark = Image.open(watermark_path).convert("RGBA")  
  
    # 计算水印的新宽度  
    watermark_width = int(base_image.width * watermark_width_percent)  
    # 保持水印的宽高比  
    watermark_height = int(watermark.height * (watermark_width / watermark.width))  
    watermark = watermark.resize((watermark_width, watermark_height), Image.LANCZOS)  # Pillow10之后ANTIALIAS替换为LANCZOS  
  
    # 计算水印的位置（右下角）  
    position = (base_image.width - watermark.width, base_image.height - watermark.height)  
  
    # 如果水印图片有透明通道，则需要使用alpha_composite来合并图片  
    if watermark.mode == "RGBA":  
        base_image_with_alpha = Image.new("RGBA", base_image.size)  
        base_image_with_alpha.paste(base_image, mask=base_image.split()[-1])  
        base_image_with_alpha.alpha_composite(watermark, position)  
        base_image = base_image_with_alpha  
    else:  
        # 如果水印图片没有透明通道，则可以直接粘贴（但这里我们假设水印是PNG格式，所以应该有透明通道）  
        base_image.paste(watermark, position, watermark)  
  
    # 保存添加水印后的图片  
    base_image.save(output_path, "PNG")  
  
def batch_watermark(input_folder, watermark_path, output_folder, watermark_width_percent=1.0):  
    """  
    批量给文件夹里的图片添加水印。  
  
    :param input_folder: 包含原图片的文件夹路径。  
    :param watermark_path: 水印图片路径（PNG格式）。  
    :param output_folder: 输出文件夹路径。  
    :param watermark_width_percent: 水印宽度占图片宽度的百分比。  
    """  
    # 确保输出文件夹存在  
    if not os.path.exists(output_folder):  
        os.makedirs(output_folder)  
  
    # 遍历输入文件夹中的所有图片文件  
    for filename in os.listdir(input_folder):  
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  
            input_path = os.path.join(input_folder, filename)  
            output_path = os.path.join(output_folder, filename)  
  
            # 添加水印并保存图片  
            add_watermark(input_path, watermark_path, output_path, watermark_width_percent)  
            print(f"Added watermark to {filename} and saved as {output_path}")  
  
if __name__ == "__main__":  



#===============================================================================
#--------------------------------要修改的部分开始--------------------------------

    # 设置输入和输出文件夹路径以及水印图片路径  
    input_folder = "path/to/input/folder"  # 请替换为实际输入文件夹路径  
    watermark_path = "path/to/watermark.png"  # 请替换为实际水印图片路径（PNG格式）  
    output_folder = "path/to/output/folder"  # 请替换为实际输出文件夹路径  

#--------------------------------要修改的部分结束--------------------------------
#===============================================================================



  
    # 批量添加水印  
    batch_watermark(input_folder, watermark_path, output_folder)
