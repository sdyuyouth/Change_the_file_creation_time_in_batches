import os
import random
from datetime import datetime, timedelta
import win32file


def set_random_timestamps(folder_path, start_date, end_date):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue  # 跳过子文件夹

        # 生成随机时间
        random_date = start_date + timedelta(
            seconds=random.randint(0, int((end_date - start_date).total_seconds()))
        )

        # 修改文件的访问时间和修改时间
        os.utime(file_path, (random_date.timestamp(), random_date.timestamp()))

        # 获取文件句柄
        handle = win32file.CreateFile(
            file_path,
            win32file.GENERIC_WRITE,
            0,  # 不共享
            None,  # 安全属性
            win32file.OPEN_EXISTING,  # 打开现有文件
            win32file.FILE_ATTRIBUTE_NORMAL,  # 普通文件属性
            None  # 模板（无）
        )

        # 直接使用 datetime 对象作为 SetFileTime 的参数
        win32file.SetFileTime(handle, random_date, random_date, random_date)
        print(f"文件 '{file_path}' 的时间已更新。")

        # 关闭文件句柄
        win32file.CloseHandle(handle)


def main():
    # 用户输入
    folder_path = input("请输入文件夹路径：")
    start_str = input("请输入最早的时间（格式如YYYY-MM-DD HH:MM:SS）：")
    end_str = input("请输入最晚的时间（格式如YYYY-MM-DD HH:MM:SS）：")

    try:
        start_date = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
        end_date = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
        if end_date <= start_date:
            raise ValueError("结束日期必须晚于开始日期")
    except ValueError as e:
        print(e)
        return

    # 更新文件时间戳
    set_random_timestamps(folder_path, start_date, end_date)

    # 等待用户输入以查看结果
    input("所有文件的时间戳已更新。按 Enter 键退出。")


if __name__ == "__main__":
    main()
