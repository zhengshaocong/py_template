# -*- coding: utf-8 -*-
"""
程序配置文件
用于设定程序运行时的各种参数和路径
"""

import os
from pathlib import Path

# ==================== 基础路径配置 ====================
# 项目根目录
ROOT_DIR = Path(__file__).parent

# 数据相关路径
DATA_DIR = ROOT_DIR / "data"           # 原始数据目录
CACHE_DIR = ROOT_DIR / "cache"         # 缓存文件目录
TEMP_DIR = ROOT_DIR / "temp"           # 临时文件目录

# 输出相关路径
OUTPUT_DIR = ROOT_DIR / "output"       # 输出根目录
IMAGES_DIR = OUTPUT_DIR / "images"     # 图片输出目录
OUTPUT_DATA_DIR = OUTPUT_DIR / "data"  # 数据输出目录

# 程序相关路径
UTILS_DIR = ROOT_DIR / "utils"         # 工具模块目录
SRC_DIR = ROOT_DIR / "src"             # 源代码目录
SCRIPT_DIR = ROOT_DIR / "script"       # 脚本目录
TESTS_DIR = ROOT_DIR / "tests"         # 测试目录

# ==================== 文件格式配置 ====================
# 支持的图片格式
SUPPORTED_IMAGE_FORMATS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

# 支持的数据格式
SUPPORTED_DATA_FORMATS = ['.csv', '.json', '.xlsx', '.txt', '.pickle']

# 默认输出格式
DEFAULT_IMAGE_FORMAT = '.png'
DEFAULT_DATA_FORMAT = '.csv'



# ==================== 工具函数 ====================
def ensure_directories():
    """确保所有必要的目录都存在"""
    directories = [
        DATA_DIR, CACHE_DIR, TEMP_DIR,
        OUTPUT_DIR, IMAGES_DIR, OUTPUT_DATA_DIR,
        UTILS_DIR, SRC_DIR, SCRIPT_DIR, TESTS_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"确保目录存在: {directory}")

def get_config_info():
    """获取配置信息"""
    return {
        "数据目录": str(DATA_DIR),
        "缓存目录": str(CACHE_DIR),
        "临时目录": str(TEMP_DIR),
        "输出目录": str(OUTPUT_DIR),
        "图片输出目录": str(IMAGES_DIR),
        "数据输出目录": str(OUTPUT_DATA_DIR),
        "工具目录": str(UTILS_DIR),
        "源码目录": str(SRC_DIR),
        "脚本目录": str(SCRIPT_DIR),
        "测试目录": str(TESTS_DIR)
    }

# ==================== 配置验证 ====================
def validate_config():
    """验证配置的有效性"""
    errors = []
    
    # 检查必要的目录是否可写
    for dir_name, dir_path in [
        ("数据目录", DATA_DIR),
        ("缓存目录", CACHE_DIR),
        ("输出目录", OUTPUT_DIR)
    ]:
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            # 测试写入权限
            test_file = dir_path / ".test_write"
            test_file.write_text("test")
            test_file.unlink()
        except Exception as e:
            errors.append(f"{dir_name} ({dir_path}) 不可写: {e}")
    
    if errors:
        print("配置验证失败:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    print("配置验证通过")
    return True

if __name__ == "__main__":
    # 测试配置
    print("=== 配置测试 ===")
    ensure_directories()
    validate_config()
    
    print("\n配置信息:")
    for key, value in get_config_info().items():
        print(f"  {key}: {value}") 