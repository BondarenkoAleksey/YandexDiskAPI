import random
import string
number = string.digits
folder_name = 'folder-' + ''.join(random.choice(number) for _ in range(3))

params_for_create_folder = {"path": folder_name}
expected_params_of_response_create_folder = ['href', 'method', 'templated']