import os


def find_largest_files():
    directory = "dir"
    files = []
    for path, subdir, file in os.walk(directory):
        for name in file:
            file_path = os.path.join(path, name)
            file_size = os.path.getsize(file_path)
            files.append({'path': file_path, 'size': file_size})
    sorted_files = sorted(files, key=lambda user: (user['size']), reverse=True)

    # display top 5 files based on size
    for file in sorted_files[:5]:
        print('path: {} || size: {}'.format(file['path'], file['size']))


find_largest_files()
