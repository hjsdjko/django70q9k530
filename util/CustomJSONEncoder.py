from datetime import datetime, date
import json
from decimal import Decimal

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        if isinstance(obj, Decimal):
            # 如果是整数，返回整数
            if obj % 1 == 0:
                return int(obj)
            # 否则返回浮点数
            return float(obj)
        return super().default(obj)