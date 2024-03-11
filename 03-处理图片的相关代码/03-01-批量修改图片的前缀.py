#===============================================================================
# @艺用常见Python代码-批量修改文件名字
# @本代码由AI 文心大模型4.0 生成  JL进行人工挑选、整理和注释
# @本代码适用于为帧序列批量增加、删除、修改动画或视频帧序列的前缀
# @无需理解整个代码的意思和原理，仅替换要修改的部分就可以实现功能
# @请忽略前面的部分向下拉直到看见--------要修改的部分开始--------
#===============================================================================

import os  
import shutil  
  
def batch_rename_copy_to_folder(src_directory, dst_directory, add_prefix='', remove_prefix='', replace_prefix=''):  
    """  
    批量复制并重命名文件到新的文件夹中，同时保留原始文件。  
  
    :param src_directory: 源目录，包含要修改的文件。  
    :param dst_directory: 目标目录，用于存储修改后的文件副本。  
    :param add_prefix: 要添加到文件名前的前缀。  
    :param remove_prefix: 要从文件名中删除的前缀。  
    :param replace_prefix: 要替换的前缀，格式为'旧前缀:新前缀'，如果不需要替换则留空。  
    """  
    # 确保源目录存在  
    if not os.path.isdir(src_directory):  
        print(f"错误：'{src_directory}' 不是一个有效的源目录。")  
        return  
  
    # 创建目标目录，如果不存在的话  
    os.makedirs(dst_directory, exist_ok=True)  
  
    # 检查是否有替换前缀的需求，并处理  
    replace_from = ''  
    replace_to = ''  
    if replace_prefix:  
        parts = replace_prefix.split(':')  
        if len(parts) == 2:  
            replace_from = parts[0]  
            replace_to = parts[1]  
        else:  
            print("错误：'replace_prefix' 参数格式不正确，应为 '旧前缀:新前缀'。")  
            return  
  
    # 遍历源目录中的所有文件  
    for filename in os.listdir(src_directory):  
        # 构造完整的源文件路径  
        src_path = os.path.join(src_directory, filename)  
  
        # 确保处理的是文件而不是目录  
        if os.path.isfile(src_path):  
            # 根据参数修改文件名  
            if filename.startswith(remove_prefix):  
                new_filename = filename[len(remove_prefix):]  
            else:  
                new_filename = filename  
            new_filename = new_filename.replace(replace_from, replace_to)  
            if add_prefix:  
                new_filename = add_prefix + new_filename  
  
            # 构造完整的目标文件路径  
            dst_path = os.path.join(dst_directory, new_filename)  
  
            # 复制并重命名文件到目标目录  
            shutil.copy2(src_path, dst_path)  
            print(f"已复制并重命名：'{src_path}' -> '{dst_path}'")  
  
if __name__ == "__main__":  






#===============================================================================
#--------------------------------要修改的部分开始--------------------------------

    # 设置源目录和目标目录  
    src_directory = "path/to/source"  # 请替换为源目录路径  
    dst_directory = "path/to/destination"  # 请替换为目标目录路径  
    
    #如文件存储在工作目录aaa文件夹的aaa1子文件夹中，请将路径写为"aaa/aaa1"
    #如果要使用相对路径，请使用工作目录并信任。除此之外也可使用绝对路径
    #如文件储存在D盘的aaa文件夹中，要将改名的文件放在D盘的bbb文件夹中，请将上面的代码修改为：
    #src_directory = "D:/aaa"  # 请替换为源目录路径  
    #dst_directory = "D:/bbb"  # 请替换为目标目录路径  
    #如果这个路径是从文件管理器复制过来的，请将路径中的\手动修改为/
    #请不要将修改过的文件和原来的文件放在同一个文件夹中
    #如果之前没有bbb文件夹，程序会自动创建
  
    # 设置前缀操作参数（根据需要选择使用）  
    add_prefix = "new_prefix_"  # 要增加的前缀，留空则不增加  
    remove_prefix = "old_prefix_"  # 要删除的前缀，留空则不删除  
    replace_prefix = "old_part:new_part"  # 要替换的前缀，格式为'旧前缀:新前缀'，留空则不替换
    
    #如要将文件的前缀C-01-修改为C-02-，请将上面的代码修改为：
    #add_prefix = ""  # 要增加的前缀，留空则不增加  
    #remove_prefix = ""  # 要删除的前缀，留空则不删除  
    #replace_prefix = "C-01-:C-02-"  # 要替换的前缀，格式为'旧前缀:新前缀'，留空则不替换  

#--------------------------------要修改的部分结束--------------------------------
#===============================================================================





    # 调用函数批量复制并重命名文件到目标目录  
    batch_rename_copy_to_folder(src_directory, dst_directory, add_prefix, remove_prefix, replace_prefix)
    
