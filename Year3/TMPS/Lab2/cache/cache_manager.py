from datetime import datetime, timedelta
from threading import Lock
from typing import Dict, Optional, Any


class WeatherDataCache:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Double-checked locking pattern
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize_cache()
        return cls._instance

    def _initialize_cache(self):
        """Initialize cache storage and settings"""
        self._cache: Dict[str, Dict[str, Any]] = {}
        self._access_count: Dict[str, int] = {}
        self._last_accessed: Dict[str, datetime] = {}
        self._cache_ttl = timedelta(minutes=30)
        self._max_cache_size = 1000

    def set_ttl(self, minutes: int) -> None:
        """Set the Time-To-Live for cache entries"""
        self._cache_ttl = timedelta(minutes=minutes)

    def set_max_size(self, size: int) -> None:
        """Set maximum cache size"""
        self._max_cache_size = size

    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve data from cache
        Returns None if key not found or data expired
        """
        with self._lock:
            if key not in self._cache:
                return None

            if self._is_expired(key):
                self._remove(key)
                return None

            self._access_count[key] += 1
            self._last_accessed[key] = datetime.now()
            return self._cache[key]

    def set(self, key: str, data: Dict[str, Any]) -> None:
        """Store data in cache with automatic cleanup if needed"""
        with self._lock:
            # Check if cache cleanup is needed
            if len(self._cache) >= self._max_cache_size:
                self._cleanup()

            self._cache[key] = data
            self._access_count[key] = 1
            self._last_accessed[key] = datetime.now()

    def _is_expired(self, key: str) -> bool:
        """Check if cache entry has expired"""
        last_accessed = self._last_accessed.get(key)
        if not last_accessed:
            return True
        return datetime.now() - last_accessed > self._cache_ttl

    def _remove(self, key: str) -> None:
        """Remove an item from cache and all tracking dictionaries"""
        self._cache.pop(key, None)
        self._access_count.pop(key, None)
        self._last_accessed.pop(key, None)

    def _cleanup(self) -> None:
        """
        Clean up cache when it reaches max size
        Removes expired entries and least frequently accessed items
        """
        # First, remove all expired items
        expired_keys = [k for k in self._cache.keys() if self._is_expired(k)]
        for key in expired_keys:
            self._remove(key)

        # If still over size limit, remove least frequently accessed items
        if len(self._cache) >= self._max_cache_size:
            # Sort by access count and last accessed time
            items = list(self._cache.keys())
            items.sort(key=lambda k: (self._access_count[k], self._last_accessed[k]))

            # Remove oldest, least accessed items until under size limit
            items_to_remove = items[:len(items) - self._max_cache_size + 1]
            for key in items_to_remove:
                self._remove(key)

    def clear(self) -> None:
        """Clear all cache data"""
        with self._lock:
            self._initialize_cache()

    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        with self._lock:
            return {
                'size': len(self._cache),
                'max_size': self._max_cache_size,
                'ttl_minutes': self._cache_ttl.total_seconds() / 60,
                'items': {
                    key: {
                        'access_count': self._access_count[key],
                        'last_accessed': self._last_accessed[key].isoformat(),
                        'is_expired': self._is_expired(key)
                    }
                    for key in self._cache
                }
            }


def generate_weather_cache_key(location: str, date: str) -> str:
    """Generate a standardized cache key for weather data"""
    return f"weather:{location}:{date}"


def generate_astronomy_cache_key(location: str, date: str) -> str:
    """Generate a standardized cache key for astronomy data"""
    return f"astronomy:{location}:{date}"
