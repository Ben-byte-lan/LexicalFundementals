from DataClean import clean_gutenberg_file
import os
print("Started")
main_folder = "Test"
for root, dirs, files in os.walk(main_folder):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            clean_gutenberg_file(os.path.join(root, file), os.path.join(root, f'C{file}'))
            print("DONE")



