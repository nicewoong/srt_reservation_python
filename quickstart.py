""" Quickstart script for InstaPy usage 
    실행방법:  python quickstart.py

"""

# imports
from srt_reservation.main import SRT
from srt_reservation.util import parse_cli_args
import os


if __name__ == "__main__":
    # cli_args = parse_cli_args()

    # login_id = cli_args.user
    # login_psw = cli_args.psw
    # dpt_stn = cli_args.dpt
    # arr_stn = cli_args.arr
    # dpt_dt = cli_args.dt
    # dpt_tm = cli_args.tm

    # num_trains_to_check = cli_args.num
    # want_reserve = cli_args.reserve

    srt = SRT('동대구', '동탄', '20230716', '20', 1, True)
    srt.test()
    print("************************************ test 완료!! ")
    srt_id = input("SRT ID를 입력하세요: ")
    srt_psw = input("SRT 비밀번호를 입력하세요: ")

    print("입력받은 SRT ID:", srt_id)
    print("입력받은 SRT 비밀번호:", srt_psw)
    srt.run(srt_id, srt_psw)