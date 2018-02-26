import sys
import os


if __name__ == '__main__':
    working_dir = sys.argv[1]

    files_dict = dict()
    duplicate_files = []
    for current_dir, subdirs, files in os.walk(working_dir):
        for name in files:
            path = os.path.join(current_dir, name)
            size = os.stat(path).st_size

            for key, value in files_dict.items():
                if value == [name, size]:
                    duplicate_files.append(path)
                    duplicate_files.append(key)
            files_dict[path] = [name, size]

    print("Duplicate files:")
    for duplicate in duplicate_files:
        print(duplicate)
