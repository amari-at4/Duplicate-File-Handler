# write your code here
import os
import sys
import hashlib


def file_md5(file_name):
    hash_md5 = hashlib.md5()
    with open(file_name, "rb") as file_descriptor:
        hash_md5.update(file_descriptor.read())
    return hash_md5.hexdigest()


if len(sys.argv) != 2:
    print("Directory is not specified")
else:
    print("Enter file format:")
    extension = input()
    print("""Size sorting options:
1. Descending
2. Ascending""")
    while True:
        print()
        print("Enter a sorting option:")
        order = int(input())
        print()
        if order < 1 or order > 2:
            print("Wrong option")
        else:
            break
    files_set_size = {}
    for root, dirs, files in os.walk(sys.argv[1], topdown=True):
        for name in files:
            filename = os.path.join(root, name)
            if extension != "":
                _, filename_extension = os.path.splitext(filename)
                if filename_extension != f".{extension}":
                    continue
            file_size = os.path.getsize(filename)
            file_size_key = str(file_size)
            file_hash = file_md5(filename)
            try:
                first_level_dict = files_set_size[file_size_key]
            except KeyError:
                files_set_size[file_size_key] = {}
            try:
                files_set_size[file_size_key][file_hash]
            except KeyError:
                files_set_size[file_size_key][file_hash] = []
            files_set_size[file_size_key][file_hash].append(filename)
    if order == 1:
        sort_reverse = True
    else:
        sort_reverse = False
    sorted_sizes = sorted(files_set_size.keys(), key=lambda x: float(x), reverse=sort_reverse)
    for size in sorted_sizes:
        print(f"{size} bytes")
        for file_hash in files_set_size[size].keys():
            for file in files_set_size[size][file_hash]:
                print(file)
        print()
    while True:
        print()
        print("Check for duplicates?")
        duplicates = input()
        print()
        if duplicates != "yes" and duplicates != "no":
            print("Wrong option")
        else:
            break
    if duplicates == "yes":
        file_number = 1
        file_list = dict()
        for size in sorted_sizes:
            first_size = True
            for file_hash in files_set_size[size].keys():
                first_file = True
                if len(files_set_size[size][file_hash]) > 1:
                    for file in files_set_size[size][file_hash]:
                        if first_size:
                            print(f"{size} bytes")
                            first_size = False
                        if first_file:
                            print(f"Hash: {file_hash}")
                            first_file = False
                        print(f"{file_number}. {file}")
                        file_list[file_number] = (size, file)
                        file_number += 1
                    print()
        while True:
            print()
            print("Delete files?")
            delete_files = input()
            print()
            if delete_files != "yes" and delete_files != "no":
                print("Wrong option")
            else:
                break
        if delete_files:
            while True:
                print()
                print("Enter file numbers to delete?")
                try:
                    files_to_delete = list(map(int, input().split()))
                except ValueError:
                    print()
                    print("Wrong option")
                    continue
                print()
                if len(files_to_delete) == 0:
                    print("Wrong option")
                else:
                    found_all = True
                    for file_index in files_to_delete:
                        if file_index not in file_list:
                            found_all = False
                            break
                    if found_all:
                        break
                    print("Wrong option")
            saved_bytes = 0
            for file_index in files_to_delete:
                os.remove(file_list[file_index][1])
                saved_bytes += int(file_list[file_index][0])
            print(f"Total freed up space: {saved_bytes} bytes")
