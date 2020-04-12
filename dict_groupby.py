def group_by_owners_set(files):
    v = {}

    for key, value in files.items():
        v.setdefault(value, set()).add(key)
    return v

def group_by_owners_list(files):
    v = {}

    for key, value in files.items():
        v.setdefault(value, list()).append(key)
    return v

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners_set(files))
    print("********************")
    print(group_by_owners_list(files))