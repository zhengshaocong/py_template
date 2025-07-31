# -*- coding: utf-8 -*-
"""
缓存管理工具模块
提供缓存管理、清理、验证等功能
"""

import json
import time
import hashlib
from pathlib import Path
from typing import Any, Dict, Optional, Union
from config import CACHE_DIR, CACHE_EXPIRE_TIME

class CacheManager:
    """缓存管理器"""
    
    def __init__(self, cache_dir: Optional[Path] = None, expire_time: int = None):
        """初始化缓存管理器"""
        self.cache_dir = cache_dir or CACHE_DIR
        self.expire_time = expire_time or CACHE_EXPIRE_TIME
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def _get_cache_key(self, key: str) -> str:
        """生成缓存键"""
        # 使用MD5哈希确保文件名安全
        return hashlib.md5(key.encode('utf-8')).hexdigest()
    
    def _get_cache_path(self, key: str) -> Path:
        """获取缓存文件路径"""
        cache_key = self._get_cache_key(key)
        return self.cache_dir / f"{cache_key}.json"
    
    def set_cache(self, key: str, data: Any) -> bool:
        """设置缓存"""
        try:
            cache_path = self._get_cache_path(key)
            cache_data = {
                "data": data,
                "timestamp": time.time(),
                "key": key
            }
            
            with open(cache_path, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)
            
            return True
        except Exception as e:
            print(f"设置缓存失败: {e}")
            return False
    
    def get_cache(self, key: str) -> Optional[Any]:
        """获取缓存"""
        try:
            cache_path = self._get_cache_path(key)
            
            if not cache_path.exists():
                return None
            
            with open(cache_path, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
            
            # 检查是否过期
            if time.time() - cache_data["timestamp"] > self.expire_time:
                self.delete_cache(key)
                return None
            
            return cache_data["data"]
        except Exception as e:
            print(f"获取缓存失败: {e}")
            return None
    
    def delete_cache(self, key: str) -> bool:
        """删除缓存"""
        try:
            cache_path = self._get_cache_path(key)
            if cache_path.exists():
                cache_path.unlink()
            return True
        except Exception as e:
            print(f"删除缓存失败: {e}")
            return False
    
    def clear_cache(self) -> bool:
        """清空所有缓存"""
        try:
            for cache_file in self.cache_dir.glob("*.json"):
                cache_file.unlink()
            return True
        except Exception as e:
            print(f"清空缓存失败: {e}")
            return False
    
    def get_cache_info(self) -> Dict[str, Any]:
        """获取缓存信息"""
        cache_files = list(self.cache_dir.glob("*.json"))
        total_size = sum(f.stat().st_size for f in cache_files)
        
        # 统计过期缓存
        expired_count = 0
        valid_count = 0
        
        for cache_file in cache_files:
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)
                
                if time.time() - cache_data["timestamp"] > self.expire_time:
                    expired_count += 1
                else:
                    valid_count += 1
            except:
                expired_count += 1
        
        return {
            "总文件数": len(cache_files),
            "有效缓存": valid_count,
            "过期缓存": expired_count,
            "总大小": total_size,
            "缓存目录": str(self.cache_dir)
        }
    
    def cleanup_expired(self) -> int:
        """清理过期缓存，返回清理的文件数"""
        cleaned_count = 0
        
        for cache_file in self.cache_dir.glob("*.json"):
            try:
                with open(cache_file, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)
                
                if time.time() - cache_data["timestamp"] > self.expire_time:
                    cache_file.unlink()
                    cleaned_count += 1
            except:
                # 如果文件损坏，也删除
                cache_file.unlink()
                cleaned_count += 1
        
        return cleaned_count

# 全局缓存管理器实例
cache_manager = CacheManager()

def get_cache(key: str) -> Optional[Any]:
    """获取缓存的便捷函数"""
    return cache_manager.get_cache(key)

def set_cache(key: str, data: Any) -> bool:
    """设置缓存的便捷函数"""
    return cache_manager.set_cache(key, data)

def delete_cache(key: str) -> bool:
    """删除缓存的便捷函数"""
    return cache_manager.delete_cache(key)

def clear_cache() -> bool:
    """清空缓存的便捷函数"""
    return cache_manager.clear_cache()

def get_cache_info() -> Dict[str, Any]:
    """获取缓存信息的便捷函数"""
    return cache_manager.get_cache_info()

def cleanup_expired_cache() -> int:
    """清理过期缓存的便捷函数"""
    return cache_manager.cleanup_expired() 