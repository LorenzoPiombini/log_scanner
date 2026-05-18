
START_ASAN_STRING = "================================================================="
END_ASAN = "==ABORTING"


def get_file_contet(file_name) -> str:
    with open(file_name,"r") as f:
        content = f.read()
        f.close()
        return content

def get_file_line_nr(file_name):
    return len(get_file_contet(file_name).split("\n"))

def write_file(file_name,content,op):
    with open(file_name,op) as f:
        f.write(content)
        f.close()


def filter_file_content(file_name,look_for,end_criteria):
    l = []
    data = get_file_contet(file_name)
    data_list = data.split("\n")
    save = False
    for line in data_list:
        if end_criteria in line:
            save = False
            l.append(line)
            l.append("\n")
            continue

        if save:
              l.append(line)
              continue

        if look_for in line:
            save = True
            l.append(line)

    if len(l) == 0:
        return "nothing found\n"

    return "\n".join(l)

