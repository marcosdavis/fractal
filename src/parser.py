from pathlib import Path

def parser(filename):
    """
    Open the file passed, check if there are enough tokens
    to have a key connected to 1 value. If there is enough,
    set the key as the value. Return the dictionary created.
    """
    f = open(filename)
    frac_dict = dict()
    frac_dict['name'] = Path(filename).stem
    ln_num = 0
    for line in f:
        ln_num += 1
        ln_frmted = line.rstrip().lower()
        # Skip any line that starts with '#' or if the line is empty.
        if ln_frmted.startswith('#') or ln_frmted == "":
            continue
        # Create the dictionary pair into 2 elements in an array.
        dict_pair = ln_frmted.replace(' ', '').split(':')
        if len(dict_pair) != 2 or dict_pair[0] == '' or dict_pair[1] == '':
            f.close()
            raise RuntimeError(f'Parse error at line #{ln_num} of {filename}: wrong number of tokens\n {line}')
        else:
            frac_dict[dict_pair[0]] = dict_pair[1]
    f.close()
    return frac_dict