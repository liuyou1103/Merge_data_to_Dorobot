# 项目名称: Merge_data_to_Dorobot

## 📌 项目简介
这是一个基于 Python 3.10+ 的数据处理工具，用于合并 **Dorobot** 数据（基于 lerobotv2.1），增加传感器数据和参数文件支持。  
**功能**：将多个单条 Dorobot 数据合并为整体结构。

---

## 🛠️ 环境要求
- **Python 版本**: 3.10 或更高  
- **依赖包**: 见 [`requirements.txt`](requirements.txt)

---

## 🚀 快速开始
### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行程序
```bash
python main.py  # 替换为你的入口脚本
```

---

## 📂 文件结构

### 单条数据示例
每个单条数据（如 `水果收纳_测试采集任务11CopyCopy_276`）包含以下目录：
```
水果收纳_测试采集任务11CopyCopy_276/
├── 水果收纳_测试采集任务11CopyCopy_276_6151/
│   ├── data/
│   │   └── chunk-000/
│   │       └── episode_000000.parquet
│   ├── depth/
│   │   └── chunk-000/
│   │       ├── observation.images.image_depth_left/
│   │       │   └── episode_000000.avi
│   │       ├── observation.images.image_depth_right/
│   │       │   └── episode_000000.avi
│   │       ├── observation.images.image_depth_top/
│   │       │   └── episode_000000.avi
│   ├── meta/
│   │   ├── common_record.json
│   │   ├── episodes.jsonl
│   │   ├── episodes_stats.jsonl
│   │   ├── info.json
│   │   ├── op_dataid.jsonl
│   │   ├── robot_Ervs4vKu9bG_realman.json
│   │   └── tasks.jsonl
│   └── videos/
│       └── chunk-000/
│           ├── observation.images.image_left/
│           │   └── episode_000000.mp4
│           ├── observation.images.image_right/
│           │   └── episode_000000.mp4
│           └── observation.images.image_top/
│               └── episode_000000.mp4
├── 水果收纳_测试采集任务11CopyCopy_276_6152/
│   └── (类似结构...)
└── merge_tag.txt
```

### 合并后的整体结构
合并后的数据目录如下：
```
水果收纳_测试采集任务11CopyCopy_276/
├── data/
│   └── chunk-000/
│       ├── episode_000000.parquet
│       ├── episode_000001.parquet
│       └── episode_000002.parquet
├── depth/
│   └── chunk-000/
│       ├── observation.images.image_depth_left/
│       │   ├── episode_000000.avi
│       │   ├── episode_000001.avi
│       │   └── episode_000002.avi
│       └── (其他深度图像...)
├── meta/
│   ├── common_record.json
│   ├── episodes.jsonl
│   ├── episodes_stats.jsonl
│   ├── info.json
│   ├── op_dataid.jsonl
│   ├── robot_Ervs4vKu9bG_realman.json
│   └── tasks.jsonl
└── videos/
    └── chunk-000/
        ├── observation.images.image_left/
        │   ├── episode_000000.mp4
        │   ├── episode_000001.mp4
        │   └── episode_000002.mp4
        └── (其他视频...)
```

---

## 📝 关键说明
1. **合并逻辑**  
   - 将所有单条数据的 `data/*.parquet`、`depth/*.avi`、`videos/*.mp4` 按文件名合并到统一目录。
   - `meta/` 下的 JSON 文件需处理冲突（如 `info.json` 合并字段）。

2. **依赖工具**  
   - 使用 `pandas` 处理结构化数据（如 `episodes.jsonl`）。
   - 使用 `shutil` 复制非结构化文件（如视频/图像）。
