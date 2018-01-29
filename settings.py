import os

# malware 경로
MALWARE_PATH = os.path.normpath(os.path.abspath('./malware'))

# json 경로
JSON_PATH = MALWARE_PATH.replace('malware','json')

# ZIP FILE PATH
ZIP_FILE_PATH = os.path.normpath(os.path.abspath('./zipfile'))

# CPU COUNT
CPU_COUNT = 1