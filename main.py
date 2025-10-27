from merge_in_nas import DoRobotDataMerger
from pathlib import Path
import json
from typing import Optional, List
from datetime import datetime

def get_folders(data_path: Path) -> Optional[List[str]]:
    """获取路径下的所有文件夹"""
    if not data_path.exists():
        print(f"错误：路径 '{data_path}' 不存在！")
        return None
    folders = [item.name for item in data_path.iterdir() if item.is_dir()]
    return folders

def read_common_json(single_meta_task_common_path: Path) -> Optional[int]:
    """读取 common.json 并返回 task_id"""
    try:
        with open(single_meta_task_common_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            task_id = data.get("task_id")
            return int(task_id)
    except Exception as e:
        print(f"读取 common.json 失败: {str(e)}")
        return None
    
def handle_task(task_path: Path) -> bool:
    """处理单个任务，检查是否满足合并条件"""
    for single_task_path in task_path.iterdir():
        single_meta_task_common_path = single_task_path / "meta" / "common_record.json"
        if not single_meta_task_common_path.exists():
            return False
        return True


def take_merge_tag(task_path):
    """
    在指定路径下创建文件，记录当前时刻
    
    参数:
        task_path (pathlib.Path | str): 文件要保存的路径（支持 Path 对象或字符串）
        
    返回:
        str: 创建的文件路径（如果成功），否则返回 None
    """
    try:
        
        # 确保目录存在
        task_path.mkdir(parents=True, exist_ok=True)
        # 生成文件名
        filename = f"merge_tag.txt"
        filepath = task_path / filename  # 使用 / 运算符拼接路径
        # 写入当前时间到文件
        with open(filepath, 'w') as f:
            f.write(f"Merge tag created at: {datetime.now().isoformat()}\n")
        
    except Exception as e:
        print(f"Error creating merge tag file: {e}")
        return None
    
def handle_single_data(single_path: Path, merge_path: Path, log_path: Path):
    """处理单个数据目录"""
    merger = DoRobotDataMerger(
        output_dir=merge_path,
        log_dir=log_path,
        log_to_file=True  # 启用日志文件
    )
    # 获取 待合并任务数据路径
    folders = get_folders(single_path)
    if folders:
        for folder in folders:
            task_path = single_path / folder
            task_merge_tag_path = single_path / folder / "merge_tag.txt"
            # 检查该任务是否合并
            if task_merge_tag_path.exists():
                print(f"任务已合并: {folder}")
                continue
            if handle_task(task_path):
                try:
                    print(f"开始合并任务: {folder}")
                    # 1、合并数据
                    if merger.merge(str(task_path)):
                        # 2、设置已合并标记
                        take_merge_tag(task_path)

                except Exception as e:
                    print(f"合并失败: {str(e)}")

if __name__ == "__main__":
    # 功能： 1、合并数据成CoRobot 2、设置已合并标记, 该脚本仅合并，没有转换！！! 
    # 示例路径（根据实际需求修改）
    # 合并后数据路径
    merge_path = Path("/home/liuyou/Documents/merge_data")

    # 合并前数据父路径（会自动检测该目录下的数据目录，判断是否需要合并，合并后会打上合并标签，下次不会再合并）
    # 示例：single_path下，存在数据文件夹："水果收纳","餐具收纳","衣物收纳"
    single_path = Path("/home/liuyou/Documents/single_data/")

    # 日志路径
    log_path = Path("/home/liuyou/Documents/logs/")
    
    handle_single_data(single_path, merge_path,log_path)
