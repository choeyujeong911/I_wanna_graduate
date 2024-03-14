import sys
import pyautogui as pag

DIRECT = int(0)
CHANGE = int(1)

class Macro:
    def __init__(self, url: str, login_info: list, mode: int, sub):
        self.site = url
        self.login_info = login_info
        self.mode = mode
        if self.mode == DIRECT:
            self.sub_list = sub
        elif self.mode == CHANGE:
            self.change_dict = sub

if __name__ == "__main__":
    stu_info = ["id", "password"]
    cnt = int(0)
    
    url = str(input("Sugang Site URL >> "))
    stu_info[0] = str(input("ID >> "))
    stu_info[1] = str(input("PASSWORD >> "))
    mode = int(input("MODE NUMBER (DIRECT 0 | CHANGE 1) >> "))
    if mode == DIRECT:
        sub_list = []
        while True:
            cnt += 1
            sub_code = str(input("SUBJECT {0} CODE (00000000-00) >> ".format(cnt)))
            if len(sub_code) == 11:
                sub_list.append(sub_code)
            elif sub_code == "0":
                break
            else:
                print("ERROR: No Such Code; Try again !")
                cnt -= 1
                pass
        print("* You put {0} class.".format(cnt))
    elif mode == CHANGE:
        sub_list = {}
        while True:
            to_sub_list = []
            cnt += 1
            
            sub_code = str(input("ORIGINAL SUBJECT {0} CODE (00000000-00) >> ".format(cnt)))
            if len(sub_code) == 11:
                while True:
                    tmp = str(input("SUBJECT CODE to CHANGE into (00000000-00) >> "))
                    if len(tmp) == 11:
                        to_sub_list.append(tmp)
                        continue
                    elif tmp == "0":
                        break
                    else:
                        print("ERROR: No Such Code; Try again !")
                sub_list[sub_code] = to_sub_list
            elif sub_code == "0":
                break
            else:
                print("ERROR: No Such Code; Try again !")
                cnt -= 1
                pass
        print("* You put {0} class.".format(cnt))

    macro = Macro(url, stu_info, mode, sub_list)
