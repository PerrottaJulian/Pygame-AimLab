import ast
filename = "test.txt"

def save_file (value, filename):
     with open(filename, "w") as f:
        f.write(value)
         
def load_file (filename):
    with open(filename, "r") as f:
        read = f.read()
    return read


#values["Record"] = val

save_file(str(987), filename)

