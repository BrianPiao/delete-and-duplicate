import os
import shutil
import time

def main():
    # initializing the count
	deleted_folders_count = 0
	deleted_files_count = 0

	# specify the path
	path = "/PATH_TO_DELETE"

	# specify the days
	days = 30

	# converting days to seconds


	# time.time() returns current time in seconds
	seconds = time.time() - (days * 24 * 60 * 60)
    if (os.path.exists(path)):
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder (root_folder)
                deleted_folders_count += 1
                break
            else:

				# checking folder from the root_folder
				for folder in folders:

					# folder path
					folder_path = os.path.join(root_folder, folder)

					# comparing with the days
					if seconds >= get_file_or_folder_age(folder_path):

						# invoking the remove_folder function
						remove_folder(folder_path)
						deleted_folders_count += 1 # incrementing count


				# checking the current directory files
				for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# comparing the days
					if seconds >= get_file_or_folder_age(file_path):

						# invoking the remove_file function
						remove_file(file_path)
						deleted_files_count += 1 # incrementing count


               else:

			# if the path is not a directory
			# comparing with the days
			if seconds >= get_file_or_folder_age(path):

				# invoking the file
				remove_file(path)
				deleted_files_count += 1 # incrementing count