from node import Node



def split_main_prune():
    pass


def split_data_set(feature_set, data_set, feature, value):
    """Split the data set in terms of a specific value."""
    # 已测试本处代码正常运行
    for index, element in enumerate(feature_set):
        if element == feature:
            feature_no = index
    set_above = [element for element in data_set if element[feature_no] > value]
    set_below = [element for element in data_set if element[feature_no] <= value]
    return set_above, set_below


def get_target_value_list(data_set):
    target_value_list = []
    for line in data_set:
        target_value_list.append(line[-1])
    return target_value_list


def mean(target_value_list):
    average = sum(target_value_list) / len(target_value_list)
    return average


def var(target_value_list):
    average = mean(target_value_list)
    varience = 0
    for element in target_value_list:
        varience = varience + (element - average) ** 2
    return varience


def get_shape(data_set):
    row = len(data_set)
    col = len(data_set[0])
    return row, col


def best_split_strategy(data_set, branch_max_error, branch_min_size):
    target_value_list = get_target_value_list(data_set)
    # Find if the target value are the same.
    if target_value_list[1:] == target_value_list[:-1]:
        return None, mean(target_value_list)


def create_tree(data_set, branch_max_error, branch_min_size):
    pass


def prune(tree, prune_data_set):
    pass
