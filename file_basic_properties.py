import os, subprocess, hashlib, simplejson

import multiprocessing as mp

from settings import *

def create_file_list ( root ) :
    ret_list = []
    for path, dirs, files in os.walk(root) :
        for file in files :
            ext = os.path.splitext(file)[-1]
            if ext == '.vir' :
                full_path = os.path.join(path, file)
                ret_list.append(full_path)

    return ret_list

def get_hash_str( file_path, block_size = 8192 ) :
    md5, sha_1 = hashlib.md5(), hashlib.sha1()
    with open(file_path, 'rb') as f :
        while True :
            buf = f.read(block_size)
            if not buf :
                break
            md5.update(buf)
            sha_1.update(buf)
        pass
    return md5.hexdigest(), sha_1.hexdigest()

def get_magic( file_path ) :
    try :
        return subprocess.check_output('file -b {file_path}'.format(file_path = file_path)).decode('utf-8').strip()
    except :
        pass

def get_file_size( file_path ) :
    return os.path.getsize(file_path)

def get_ssdeep( file_path ) :
    ssdeep_result = subprocess.check_output('ssdeep {file_path}'.format(file_path=file_path)).decode('utf-8').strip().split('\n')[-1].split(',')[0]
    return ssdeep_result

def make_json( file_path ) :
    ret_dic = {}
    # md5, sha1
    ret_dic['MD5'], ret_dic['SHA-1'] = get_hash_str( file_path )
    # Magic
    ret_dic['Magic'] = get_magic( file_path )
    # File Size
    ret_dic['File Size'] = get_file_size(file_path)
    # SSDeep
    ret_dic['SSDeep'] = get_ssdeep(file_path)
    json_path, json_file_name = os.path.split(file_path)
    json_path.replace('malware','json')
    json_file_name.replace('.vir','.json')
    if not os.exists(json_path) :
        os.makedirs(json_path)
    json_full_path = os.path.join(json_path, json_file_name)
    with open(json_full_path, 'w') as f:
        simplejson.dump(ret_dic, f)

def run() :
    mp.freeze_support()
    file_list = create_file_list(MALWARE_PATH)
    print("Total Malware Count : {}".format(len(file_list)))
    p = mp.Pool(CPU_COUNT)
    p.map(make_json, file_list)