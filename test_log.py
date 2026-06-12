import logging
import os

# 使用绝对路径
log_file = os.path.join(os.path.dirname(__file__), 'test.log')
print(f"日志文件路径: {log_file}")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_file,
    filemode='w',
    force=True   # ← 加上 force=True，强制重新配置
)

def test_demo():
    logging.info("这条日志应该写入文件")
    print("测试执行完毕")