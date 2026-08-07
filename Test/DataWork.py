"""Not a perfect solution as I had to back in a delete some prefaces, but accomplished alot of the other issues 
that truly would have beyond tiresome.
"""


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



