# Python 项目模板

这是一个标准化的Python项目模板，提供了清晰的文件结构和配置。

## 项目结构

```
py_template/
├── run.py              # 启动文件
├── main.py             # 主程序
├── config.py           # 程序配置
├── start.py            # 启动脚本（自动进入虚拟环境）
├── requirements.txt    # 依赖包列表
├── README.md           # 项目说明
├── script/             # 次要程序文件夹
├── output/             # 生成文件
│   ├── images/         # 图片输出
│   └── data/           # 数据输出
├── data/               # 原始数据
├── utils/              # 工具文件夹
├── cache/              # 缓存内容
├── src/                # 主程序的内容分支
├── temp/               # 临时文件
└── tests/              # 测试文件
```

## 使用说明

1. 运行 `python start.py` 启动项目
2. 程序会自动检查虚拟环境并安装依赖
3. 主要功能在 `main.py` 中实现
4. 配置文件在 `config.py` 中管理

## 配置说明

`config.py` 是程序的核心配置文件，采用扁平化配置格式，更易读易用：

### 路径配置
- **数据相关路径**
  - `DATA_DIR`: 原始数据目录 (data/)
  - `CACHE_DIR`: 缓存文件目录 (cache/)
  - `TEMP_DIR`: 临时文件目录 (temp/)

- **输出相关路径**
  - `OUTPUT_DIR`: 输出根目录 (output/)
  - `IMAGES_DIR`: 图片输出目录 (output/images/)
  - `OUTPUT_DATA_DIR`: 数据输出目录 (output/data/)

- **程序相关路径**
  - `UTILS_DIR`: 工具模块目录 (utils/)
  - `SRC_DIR`: 源代码目录 (src/)
  - `SCRIPT_DIR`: 脚本目录 (script/)
  - `TESTS_DIR`: 测试目录 (tests/)

### 其他配置
- **文件格式配置**: 支持的图片和数据格式
- **运行时配置**: 缓存、日志等参数

### 配置使用示例
```python
from config import DATA_DIR, IMAGES_DIR, OUTPUT_DATA_DIR

# 读取原始数据
data_file = DATA_DIR / "input.csv"

# 保存图片
image_path = IMAGES_DIR / "result.png"

# 保存数据
data_path = OUTPUT_DATA_DIR / "output.json"
```

### 配置验证
```python
from config import validate_config

# 验证配置有效性
if validate_config():
    print("配置验证通过")
else:
    print("配置验证失败")
```

## 文件夹说明

- **output/images/**: 存放程序生成的图片文件
- **output/data/**: 存放程序生成的数据文件
- **data/**: 存放原始输入数据
- **utils/**: 存放工具函数和辅助模块
- **cache/**: 存放缓存文件，提高程序运行效率
- **src/**: 存放主要业务逻辑代码
- **tests/**: 存放测试代码 