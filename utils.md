# Utils 工具模块说明

`utils/` 文件夹用于存放各种辅助函数和工具类，提供程序运行所需的通用功能。

## 文件结构

```
utils/
├── __init__.py              # 包初始化文件
├── file_utils.py            # 文件操作工具
├── data_utils.py            # 数据处理工具
├── cache_utils.py           # 缓存管理工具
└── interactive_utils.py     # 交互式界面工具
```

## 功能说明

### file_utils.py
- JSON/CSV/文本文件读写
- 文件格式检查和验证
- 文件名清理和路径处理
- 文件大小格式化

### data_utils.py
- 数据清洗和验证
- 数据过滤和排序
- 数据合并和采样
- DataFrame转换

### cache_utils.py
- 缓存设置和获取
- 缓存过期管理
- 缓存清理和信息统计
- 自动过期处理

### interactive_utils.py
- 交互式菜单系统
- 用户输入验证
- 进度条和加载动画
- 表格显示和格式化
- 确认对话框

## 使用示例

### 基础工具使用
```python
from utils.file_utils import read_json, write_csv
from utils.data_utils import clean_data, validate_data
from utils.cache_utils import get_cache, set_cache
```

### 交互式界面使用
```python
from utils.interactive_utils import (
    print_header, print_success, print_error,
    confirm, select_option, show_menu, show_table
)

# 显示标题
print_header("我的程序", "版本 1.0")

# 显示成功消息
print_success("操作完成")

# 确认操作
if confirm("确定要删除文件吗？", default=False):
    # 执行删除操作
    pass

# 显示菜单
menu_items = [
    {"name": "选项1", "action": func1},
    {"name": "选项2", "action": func2}
]
show_menu(menu_items, "主菜单")

# 显示表格
data = [{"姓名": "张三", "年龄": 25}, {"姓名": "李四", "年龄": 30}]
show_table(data, "用户列表")
```

## 交互式界面特性

### 1. 美观的输出格式
- 彩色状态图标 (✓ ✗ ⚠ ℹ)
- 格式化标题和分隔线
- 进度条和加载动画

### 2. 用户友好的输入
- 智能默认值处理
- 输入验证和错误提示
- 支持中文确认 (是/否)

### 3. 菜单系统
- 多级菜单支持
- 描述性选项说明
- 优雅的退出机制

### 4. 数据展示
- 自动格式化表格
- 列宽自适应
- 清晰的分隔线 