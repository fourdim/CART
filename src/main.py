"""
The program entry file.
"""

def load_data_set():
    """Load the data set."""
    # TODO: 转换成元组节省内存空间，增加速度 全编完以后再换 防止出现要list性质的地方
    # 已测试，本处代码可正常运行
    feature_set = []
    data_set = []
    with open("./src/train.csv", "r") as train_file:
        for index, line in enumerate(train_file.readlines()):
            line_processed = line.strip().split(",")
            if index:
                numeric_line = list(map(float, line_processed))
                data_set.append(numeric_line)
            else:
                feature_set.append(line_processed)
    return feature_set, data_set


def main():
    """Main function."""
    featrue_set, data_set = load_data_set()


if __name__ == "__main__":
    main()