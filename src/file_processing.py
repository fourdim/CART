from json import loads, dumps

def load_data_set(file_path = "./src/train.csv"):
    """Load the data set."""
    feature_set = []
    data_set = []
    try:
        with open(file_path, "r") as train_file:
            for index, line in enumerate(train_file.readlines()):
                line_processed = line.strip().split(", ")
                if index:
                    numeric_line = list(map(float, line_processed))
                    data_set.append(numeric_line)
                else:
                    feature_set = line_processed
    except (FileNotFoundError, PermissionError) as exception:
        print(exception)
        exit()
    return tuple(feature_set), tuple(data_set)


def load_model(file_path="./src/model.json"):
    try:
        with open(file_path, "r") as model_file:
            model = loads(model_file.read())
    except (FileNotFoundError, PermissionError) as exception:
        print(exception)
        exit()
    return model


def dump_model(model, file_path="./src/model.json"):
    try:
        with open(file_path, "w") as model_file:
            model_file.write(dumps(model, sort_keys=True, indent=4))
        print("Model construction complete.")
    except PermissionError as exception:
        print(exception)
        exit()