"""
The program entry file.
"""
import CART
import file_processing as fp
from re import match
from sys import exit

def new_input(text):
    """New input function."""
    value = input(text).strip()
    if match(r"#", value):
        exit()
    return value


def menu_model():
    print("----------------------------")
    print("Create model              -1")
    print("Load model                -2")
    print("----------------------------")
    return new_input("In [num]: ")


def menu_prediction():
    print("----------------------------")
    print("Classification            -1")
    print("Regression                -2")
    print("----------------------------")


def mapping(target):
    if target > 6:
        return True
    return False


def main():
    """Main function."""
    print("----------------------------")
    print("CART wine quality prediction")
    print("----------------------------")
    print("Please enter the path of train.csv (./src/train.csv by default).")
    data_set_path = new_input("In [path]: ")
    if data_set_path:
        featrue_set, data_set = fp.load_data_set(data_set_path)
    else:
        featrue_set, data_set = fp.load_data_set()
    data_set, verify_set = CART.split_train_verify(data_set)
    number = menu_model()
    if number == "1":
        cart_tree = CART.create_tree(featrue_set, data_set)
        cart_tree = CART.prune(cart_tree, verify_set)
        fp.dump_model(cart_tree)
    elif number == "2":
        print("Please enter the path of model.json (./src/model.json by default).")
        data_set_path = new_input("In [path]: ").strip()
        if data_set_path:
            cart_tree = fp.load_model(data_set_path)
        else:
            cart_tree = fp.load_model()
    else:
        exit()
    print("Please enter the path of test.csv (./src/test.csv by default).")
    data_set_path = new_input("In [path]: ")
    if data_set_path:
        featrue_set, data_set = fp.load_data_set(data_set_path)
    else:
        featrue_set, data_set = fp.load_data_set()
    results = CART.predict(cart_tree, featrue_set, data_set)
    number = menu_prediction()
    if number == "1":
        correct = 0
        print("Prediction Fact")
        for result in results:
            result = map(mapping, result)
            print(result[0], result[1])
            if result[0] == result[1]:
                correct = correct + 1
        print(correct / len(results))
    elif number == "2":
        mse = 0
        print("Prediction Fact")
        for result in results:
            print(result[0], result[1])
            mse = mse + (result[0] - result[1]) ** 2
        print(mse / len(results))
    else:
        exit()
    

if __name__ == "__main__":
    main()