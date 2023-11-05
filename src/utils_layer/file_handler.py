import yaml


def read_yaml(file_path):
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError as e:
        raise YAMLNotFoundError(f"The file {file_path} does not exist.") from e
    except yaml.YAMLError as e:
        raise YAMLError(f"Error in configuration {file_path} file: {e}") from e


class YAMLNotFoundError(Exception):
    pass


class YAMLError(Exception):
    pass

