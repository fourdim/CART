

def split_train_verify(data_set):
    verify_set = data_set[900:]
    data_set = data_set[:900]
    return data_set, verify_set


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


def gini(sub_set):
    sub_set_len = len(sub_set)
    good = 0
    for set_row in sub_set:
        if set_row[-1] > 6:
            good = good + 1
    gini_index = 1 - (good / sub_set_len) ** 2 - ((sub_set_len - good) / sub_set_len) ** 2
    return gini_index


def best_split_strategy(feature_set, data_set, branch_max_error, branch_min_size):
    target_value_list = get_target_value_list(data_set)
    # Find if the target value are the same.
    if target_value_list[1:] == target_value_list[:-1]:
        return None, mean(target_value_list)
    best_feature = 0
    best_value = 0
    best_gini = float("inf")
    for outer_index, feature in enumerate(feature_set):
        for value in set([element[outer_index] for element in data_set]):
            set_above, set_below = split_data_set(feature_set, data_set, feature, value)
            if len(set_above) < branch_min_size or len(set_below) < branch_min_size:
                continue
            new_gini = (len(set_above) * gini(set_above)
                      + len(set_below) * gini(set_below)) / len(data_set)
            if new_gini < best_gini:
                best_feature = feature
                best_value = value
                best_gini = new_gini
    if (gini(data_set) - best_gini) < branch_max_error:
        return None, mean(target_value_list)
    return best_feature, best_value


def create_tree(feature_set, data_set, branch_max_error=0, branch_min_size=1):
    feature, value = best_split_strategy(feature_set, data_set, branch_max_error, branch_min_size)
    if feature is None:
        return value
    cart_tree = {}
    cart_tree["feature"] = feature
    cart_tree["value"] = value
    set_above, set_below = split_data_set(feature_set, data_set, feature, value)
    cart_tree["left"] = create_tree(feature_set, set_above, branch_max_error, branch_min_size)
    cart_tree["right"] = create_tree(feature_set, set_below, branch_max_error, branch_min_size)
    return cart_tree


def get_tree_mean(cart_tree):
    if isinstance(cart_tree["left"], dict):
        cart_tree["left"] = get_tree_mean(cart_tree["left"])
    if isinstance(cart_tree["right"], dict):
        cart_tree["right"] = get_tree_mean(cart_tree["right"]) 
    return (cart_tree["left"] + cart_tree["right"]) / 2


def prune(cart_tree, feature_set, verify_set):
    if len(verify_set) == 0:
        return get_tree_mean(cart_tree)
    set_above, set_below = split_data_set(feature_set, verify_set, cart_tree["feature"], cart_tree["value"])
    if isinstance(cart_tree["left"], dict) or isinstance(cart_tree["right"], dict):
        if isinstance(cart_tree["left"], dict):
            cart_tree["left"] = prune(cart_tree["left"], feature_set, set_above)
        if isinstance(cart_tree["right"], dict):    
            cart_tree["right"] = prune(cart_tree["right"], feature_set, set_below)
        return cart_tree
    error_no_merge = sum([(element - cart_tree["left"]) ** 2 for element in get_target_value_list(set_above)]) + \
                     sum([(element - cart_tree["right"]) ** 2 for element in get_target_value_list(set_below)])
    avg = (cart_tree["left"] + cart_tree["right"]) / 2
    error_merge = sum([(element - avg) ** 2 for element in get_target_value_list(verify_set)])
    if error_merge < error_no_merge:
        return avg
    return cart_tree

def trace(cart_tree, feature_dict, element):
    if element[feature_dict[cart_tree["feature"]]] > cart_tree["value"]:
        if isinstance(cart_tree["left"], dict):
            return trace(cart_tree["left"], feature_dict, element)
        else:
            return cart_tree["left"]
    else:
        if isinstance(cart_tree["right"], dict):
            return trace(cart_tree["right"], feature_dict, element)
        else:
            return cart_tree["right"]


def predict(cart_tree, feature_set, data_set):
    feature_dict = {}
    for index, feature in enumerate(feature_set):
        feature_dict[feature] = index
    results = []
    for element in data_set:
        results.append((trace(cart_tree, feature_dict, element), element[-1]))
    return results


if __name__ == "__main__":
    print("Please run main.py")
