import time
from datetime import datetime

# 暂停1秒
time.sleep(1)

# 获取当前时间并格式化
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 输出当前时间
print(f"当前时间：{current_time}")