"""
The program entry file.
"""
import CART
import file_processing
from re import match
from sys import exit

def new_input(text):
    """New input function."""
    value = input(text)
    if match(r"#", value):
        exit()
    return value

def menu():
    print("----------------------------")
    print("Create model              -1")
    print("Load model                -2")
    print("----------------------------")
    return new_input("In [num]: ")




def main():
    """Main function."""
    print("----------------------------")
    print("CART wine quality prediction")
    print("----------------------------")
    print("Please enter the path of train.csv (./src/train.csv by default).")
    data_set_path = new_input("In [path]: ").strip()
    if data_set_path:
        featrue_set, data_set = file_processing.load_data_set(data_set_path)
    else:
        featrue_set, data_set = file_processing.load_data_set()
    number = menu()
    if number == "1":

        CART.create_tree()

    # set_above, set_below = CART.split_data_set(featrue_set, data_set, "quality", 6)
    


if __name__ == "__main__":
    main()