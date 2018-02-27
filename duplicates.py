import sys
import os
import collections


def search_files_in_dir(working_dir):
    files_dictionary = dict()
    for current_dir, subdirs, files in os.walk(working_dir):
        for name in files:
            path = os.path.join(current_dir, name)
            size = os.stat(path).st_size
            files_dictionary[path] = (name, size)
    return files_dictionary


def search_duplicates(file_dictionary):
    value_occurrences = collections.Counter(file_dictionary.values())
    duplicate_files_dict = {key: value for key, value in file_dictionary.items()
                     if value_occurrences[value] > 1}
    return duplicate_files_dict.keys()


if __name__ == '__main__':
    working_dir = sys.argv[1]
    files_dict = search_files_in_dir(working_dir)
    duplicate_files = search_duplicates(files_dict)

    print("Duplicate files:")
    for duplicate in duplicate_files:
        print(duplicate)
