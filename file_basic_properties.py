import os, subprocess, hashlib, simplejson

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

def basic_properties( file_path ) :
    ret_dic = {}
    # md5, sha1
    ret_dic['MD5'], ret_dic['SHA-1'] = get_hash_str( file_path )
    # Magic
    ret_dic['Magic'] = get_magic( file_path )
    # File Size
    ret_dic['File Size'] = get_file_size(file_path)
    # SSDeep
    ret_dic['SSDeep'] = get_ssdeep(file_path)
    return ret_dic

if __name__ == '__main__' :
    #test_file_path = 'D:\\byeongal\\file_basic_properties\\DHelper.exe'
    #test_file_path = 'D:\\byeongal\\file_basic_properties\\main.cpp'
    test_file_path = 'D:\\byeongal\\file_basic_properties\\boj_10951.exe'

    json_result=simplejson.dumps(basic_properties(test_file_path))
    with open('resut.json', 'w', encoding="utf8") as f:
        simplejson.dump(basic_properties(test_file_path), f, ensure_ascii=False)