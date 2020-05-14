"""
The program entry file.
"""
import CART
import file_processing as fp

def new_input(text):
    """New input function."""
    value = input(text).strip()
    if value.startswith("#"):
        exit()
    return value


def menu_model():
    """Menu for the models."""
    print("----------------------------")
    print("Create model              -1")
    print("Load model                -2")
    print("----------------------------")
    return new_input("In [num]: ")


def menu_prediction():
    """Menu for prediction."""
    print("----------------------------")
    print("Classification            -1")
    print("Regression                -2")
    print("----------------------------")
    return new_input("In [num]: ")


def mapping(target):
    """Map the value to true and false."""
    if target > 6:
        return True
    return False


def print_result(number, results):
    """Print the result."""
    if number == "1":
        correct = 0
        print("Prediction Fact")
        for result in results:
            result = tuple(map(mapping, result))
            print(result[0], end=" ")
            if result[0]:
                print(end=" ")
            print(result[1])
            if result[0] == result[1]:
                correct = correct + 1
        print("The accuracy is", round(correct * 100 / len(results), 5), "%")
    elif number == "2":
        mse = 0
        print("Prediction Fact")
        # fp.dump_model(results, "./src/result.json")
        # You can uncomment it if you want to see the results in the file.
        for result in results:
            print(round(result[0], 1), result[1])
            mse = mse + (result[0] - result[1]) ** 2
        print("The MSE is", round(mse / len(results), 5))
    else:
        exit() # I should have use sys.exit(). However, sys is not built-in.


def main():
    """Main function."""
    print("----------------------------")
    print("CART wine quality prediction")
    print("----------------------------")
    number = menu_model()
    if number == "1":
        print("Please enter the path of train.csv (./src/train.csv by default).")
        data_set_path = new_input("In [path]: ")
        if data_set_path:
            feature_set, data_set = fp.load_data_set(data_set_path)
        else:
            feature_set, data_set = fp.load_data_set()
        data_set, verify_set = CART.split_train_verify(data_set)
        print("Loading...")
        cart_tree = CART.create_tree(feature_set[:-1], data_set, 0, 2)
        cart_tree = CART.prune(cart_tree, feature_set[:-1], verify_set)
        fp.dump_model(cart_tree)
    elif number == "2":
        print("Please enter the path of model.json (./src/model.json by default).")
        data_set_path = new_input("In [path]: ")
        if data_set_path:
            cart_tree = fp.load_model(data_set_path)
        else:
            cart_tree = fp.load_model()
    else:
        exit() # I should have use sys.exit(). However, sys is not built-in.
    print("Please enter the path of test.csv (./src/test.csv by default).")
    data_set_path = new_input("In [path]: ")
    if data_set_path:
        feature_set, data_set = fp.load_data_set(data_set_path)
    else:
        feature_set, data_set = fp.load_data_set("./src/test.csv")
    results = CART.predict(cart_tree, feature_set, data_set)
    number = menu_prediction()
    print_result(number, results)




if __name__ == "__main__":
    main()
