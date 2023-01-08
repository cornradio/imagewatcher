'''
Black: \033[30m
Red: \033[31m
Green: \033[32m
Yellow: \033[33m
Blue: \033[34m
Magenta: \033[35m
Cyan: \033[36m
White: \033[37m
'''
verbose = True
def print_verbose(str2, str1='verbose'):
    if verbose:
        print(f"\033[1;37;40m {str1} \033[0m {str2}")
# 所有的都添加了黑色底色，因为我觉得黑色底色很帅气
def print_red(str1,str2 = ''):
    print(f"\033[1;31;40m {str1} \033[0m {str2}")
def print_green(str1,str2 = ''):
    print(f"\033[1;32;40m {str1} \033[0m {str2}")
def print_yellow(str1,str2 = ''):
    print(f"\033[1;33;40m {str1} \033[0m {str2}")
def print_cyan(str1,str2 = ''):
    print(f"\033[1;36;40m {str1} \033[0m {str2}")