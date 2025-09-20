file_name = "relat_2024_final_v2.csv"

starts_with_relat = file_name.startswith("relat_")
contains_final = file_name.find("final") != -1

def get_file_version(file_name):
    start = file_name.find("_v")
    if start == -1:
        return None
    start += 2 
    end = file_name.find(".", start)
    if end == -1:
        end = len(file_name)
    return file_name[start:end]

print(starts_with_relat)
print(contains_final)
print(get_file_version(file_name))
