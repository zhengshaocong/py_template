# -*- coding: utf-8 -*-
"""
主程序文件
演示如何使用config.py中的配置
"""

from config import (
    DATA_DIR, CACHE_DIR, TEMP_DIR,
    OUTPUT_DIR, IMAGES_DIR, OUTPUT_DATA_DIR,
    UTILS_DIR, SRC_DIR, SCRIPT_DIR, TESTS_DIR,
    ensure_directories, validate_config
)
import json
from pathlib import Path

def main():
    """主函数"""
    print("程序启动...")
    
    # 确保所有必要的目录存在
    ensure_directories()
    
    # 验证配置
    if not validate_config():
        print("配置验证失败，程序退出")
        return
    
    # 演示配置使用
    demo_config_usage()
    
    print("程序运行完成！")

def demo_config_usage():
    """演示配置使用"""
    print("\n=== 配置使用演示 ===")
    
    # 1. 数据目录使用示例
    print("1. 数据目录配置:")
    print(f"   原始数据目录: {DATA_DIR}")
    print(f"   缓存目录: {CACHE_DIR}")
    print(f"   临时目录: {TEMP_DIR}")
    
    # 2. 输出目录使用示例
    print("\n2. 输出目录配置:")
    print(f"   图片输出目录: {IMAGES_DIR}")
    print(f"   数据输出目录: {OUTPUT_DATA_DIR}")
    
    # 3. 创建示例文件
    create_demo_files()

def create_demo_files():
    """创建演示文件"""
    print("\n3. 创建演示文件:")
    
    # 创建示例数据文件
    demo_data = {
        "项目名称": "Python项目模板",
        "版本": "1.0.0",
        "描述": "这是一个标准化的Python项目模板",
        "配置格式": "扁平化配置，更易读易用"
    }
    
    # 保存到数据输出目录
    output_file = OUTPUT_DATA_DIR / "demo_output.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(demo_data, f, ensure_ascii=False, indent=2)
    print(f"   创建数据文件: {output_file}")
    
    # 创建示例文本文件
    demo_text = "这是一个演示文件，展示如何使用新的扁平化配置格式。"
    text_file = OUTPUT_DATA_DIR / "demo_output.txt"
    with open(text_file, 'w', encoding='utf-8') as f:
        f.write(demo_text)
    print(f"   创建文本文件: {text_file}")
    
    # 创建缓存文件示例
    cache_data = {
        "缓存时间": "2024-01-01", 
        "状态": "正常",
        "配置类型": "扁平化配置"
    }
    cache_file = CACHE_DIR / "demo_cache.json"
    with open(cache_file, 'w', encoding='utf-8') as f:
        json.dump(cache_data, f, ensure_ascii=False, indent=2)
    print(f"   创建缓存文件: {cache_file}")

if __name__ == "__main__":
    main() 