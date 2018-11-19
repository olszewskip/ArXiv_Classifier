def save_dict(dict_, file_name):
    with open(file_name, "w") as file:
        for key, value in dict_.items():
            file.write("".join([str(key),"\t" , str(value), "\n"]))

            
def read_dict(dict_, file_name):
    with open(file_name, "r") as file:
        for line in file:
            key, value = line.rstrip('\n').split('\t')
            dict_[key] = value


