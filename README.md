# 项目名称:Merge_data_to_Dorobot
 
## 📌 项目简介
（简要描述项目功能，例如：）  
> 这是一个基于 Python 3.10+ 的数据处理工具，
> Dorobot数据基于lerobotv2.1,增加了传感器数据和参数文件。提供将多个单条的Dorobot数据合并成整体。
 
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
（补充你的入口脚本，例如：）
```bash
python main.py
```

## 文件结构
### 单条数据结构示例：
> └── 水果收纳_测试采集任务11CopyCopy_276
    ├── 水果收纳_测试采集任务11CopyCopy_276_6151
    │   ├── data
    │   │   └── chunk-000
    │   │       └── episode_000000.parquet
    │   ├── depth
    │   │   └── chunk-000
    │   │       ├── observation.images.image_depth_left
    │   │       │   └── episode_000000.avi
    │   │       ├── observation.images.image_depth_right
    │   │       │   └── episode_000000.avi
    │   │       ├── observation.images.image_depth_top
    │   │       │   └── episode_000000.avi
    │   │       ├── observation.images.image_left
    │   │       ├── observation.images.image_right
    │   │       └── observation.images.image_top
    │   ├── meta
    │   │   ├── common_record.json
    │   │   ├── episodes.jsonl
    │   │   ├── episodes_stats.jsonl
    │   │   ├── info.json
    │   │   ├── op_dataid.jsonl
    │   │   ├── robot_Ervs4vKu9bG_realman.json
    │   │   └── tasks.jsonl
    │   └── videos
    │       └── chunk-000
    │           ├── observation.images.image_depth_left
    │           ├── observation.images.image_depth_right
    │           ├── observation.images.image_depth_top
    │           ├── observation.images.image_left
    │           │   └── episode_000000.mp4
    │           ├── observation.images.image_right
    │           │   └── episode_000000.mp4
    │           └── observation.images.image_top
    │               └── episode_000000.mp4
    ├── 水果收纳_测试采集任务11CopyCopy_276_6152
    │   ├── data
    │   │   └── chunk-000
    │   │       └── episode_000000.parquet
    │   ├── depth
    │   │   └── chunk-000
    │   │       ├── observation.images.image_depth_left
    │   │       │   └── episode_000000.avi
    │   │       ├── observation.images.image_depth_right
    │   │       │   └── episode_000000.avi
    │   │       ├── observation.images.image_depth_top
    │   │       │   └── episode_000000.avi
    │   │       ├── observation.images.image_left
    │   │       ├── observation.images.image_right
    │   │       └── observation.images.image_top
    │   ├── meta
    │   │   ├── common_record.json
    │   │   ├── episodes.jsonl
    │   │   ├── episodes_stats.jsonl
    │   │   ├── info.json
    │   │   ├── op_dataid.jsonl
    │   │   ├── robot_Ervs4vKu9bG_realman.json
    │   │   └── tasks.jsonl
    │   └── videos
    │       └── chunk-000
    │           ├── observation.images.image_depth_left
    │           ├── observation.images.image_depth_right
    │           ├── observation.images.image_depth_top
    │           ├── observation.images.image_left
    │           │   └── episode_000000.mp4
    │           ├── observation.images.image_right
    │           │   └── episode_000000.mp4
    │           └── observation.images.image_top
    │               └── episode_000000.mp4
    ├── 水果收纳_测试采集任务11CopyCopy_276_6153
    │   ├── data
    │   │   └── chunk-000
    │   │       └── episode_000000.parquet
    │   ├── depth
    │   │   └── chunk-000
    │   │       ├── observation.images.image_depth_left
    │   │       │   └── episode_000000.avi
    │   │       ├── observation.images.image_depth_right
    │   │       │   └── episode_000000.avi
    │   │       ├── observation.images.image_depth_top
    │   │       │   └── episode_000000.avi
    │   │       ├── observation.images.image_left
    │   │       ├── observation.images.image_right
    │   │       └── observation.images.image_top
    │   ├── meta
    │   │   ├── common_record.json
    │   │   ├── episodes.jsonl
    │   │   ├── episodes_stats.jsonl
    │   │   ├── info.json
    │   │   ├── robot_Ervs4vKu9bG_realman.json
    │   │   ├── op_dataid.jsonl
    │   │   └── tasks.jsonl
    │   └── videos
    │       └── chunk-000
    │           ├── observation.images.image_depth_left
    │           ├── observation.images.image_depth_right
    │           ├── observation.images.image_depth_top
    │           ├── observation.images.image_left
    │           │   └── episode_000000.mp4
    │           ├── observation.images.image_right
    │           │   └── episode_000000.mp4
    │           └── observation.images.image_top
    │               └── episode_000000.mp4
    └── merge_tag.txt
### 整体文件结构
> ├── data
│   └── chunk-000
│       ├── episode_000000.parquet
│       ├── episode_000001.parquet
│       └── episode_000002.parquet
├── depth
│   └── chunk-000
│       ├── observation.images.image_depth_left
│       │   ├── episode_000000.avi
│       │   ├── episode_000001.avi
│       │   └── episode_000002.avi
│       ├── observation.images.image_depth_right
│       │   ├── episode_000000.avi
│       │   ├── episode_000001.avi
│       │   └── episode_000002.avi
│       └── observation.images.image_depth_top
│           ├── episode_000000.avi
│           ├── episode_000001.avi
│           └── episode_000002.avi
├── meta
│   ├── common_record.json
│   ├── episodes.jsonl
│   ├── episodes_stats.jsonl
│   ├── info.json
│   ├── op_dataid.jsonl
│   ├── robot_Ervs4vKu9bG_realman.json
│   └── tasks.jsonl
└── videos
    └── chunk-000
        ├── observation.images.image_left
        │   ├── episode_000000.mp4
        │   ├── episode_000001.mp4
        │   └── episode_000002.mp4
        ├── observation.images.image_right
        │   ├── episode_000000.mp4
        │   ├── episode_000001.mp4
        │   └── episode_000002.mp4
        └── observation.images.image_top
            ├── episode_000000.mp4
            ├── episode_000001.mp4
            └── episode_000002.mp4

---
