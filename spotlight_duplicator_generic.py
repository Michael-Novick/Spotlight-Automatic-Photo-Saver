import os
import shutil


def main():
    # Header
    print_header()
    # print(save_location)
    # print(copy_location)

    save_location = get_directory_from_user()
    username = os.getlogin()
    copy_location = "\\Users\\" + username + "\\AppData\\Local\\Packages\\Microsoft.Windows.Content" \
                    "DeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"  # Windows directory with spotlight files

    print('Updating Photos Folder...')

    # Collect file names
    names = collect_file_names(save_location)

    # Duplicate files
    files, number = duplicate(copy_location, save_location, names)
    print('{} files duplicated. '.format(number))


def print_header():
    print('SPOTLIGHT PHOTOS UPDATER')
    print()


def get_directory_from_user():
    save_location = input('Please enter the directory of the folder you wish to save Spotlight images into: ')
    return save_location


def collect_file_names(save_location):
    names = os.listdir(save_location)
    clear_names = []
    for m in names:
        m = m.rstrip('.jpg')
        clear_names.append(m)
    return clear_names


def duplicate(copy_location, save_location, names):
    all_file_names = os.listdir(copy_location)
    count = 0
    new_files = []
    for m in all_file_names:
        if m not in names:
            current_location = copy_location + "\\" + '{}'.format(m)
            if os.stat(current_location).st_size >= 200000:
                new_files.append(m)
                shutil.copy(current_location, save_location)
                new_copied_file = save_location + "\\" + '{}'.format(m)
                os.rename(new_copied_file, new_copied_file + '.jpg')
                count += 1
    return new_files, count


def print_closer(number):
    print('{} Spotlight photos have been added to your folder.'.format(number))


if __name__ == '__main__':
    main()
