import os
# 定義相對路徑
relative_path = 'static/temp'

# 獲取相對路徑
relative_path = os.path.relpath(relative_path)

print(relative_path)