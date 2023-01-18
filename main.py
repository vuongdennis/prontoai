import os
import subprocess
import datetime
import sys


def get_current_branch():
    res = subprocess.run(["git", "branch", "--show-current"], stdout=subprocess.PIPE)
    res_str = res.stdout.decode("utf-8").strip("\n")
    return res_str


def check_local_changes():
    res = subprocess.run(["git", "status", "--porcelain"], stdout=subprocess.PIPE)
    res_str = res.stdout.decode("utf-8")
    return True if res_str else False


def is_author_rufus():
    res = subprocess.run(["git", "log", "-1"], stdout=subprocess.PIPE)
    res_list = res.stdout.decode("utf-8").split("\n")
    author = " ".join(res_list[1].split(" ")[1:-1])
    return author == "Rufus"


def is_authored_last_week():
    res = subprocess.run(["git", "log", "-1"], stdout=subprocess.PIPE)
    res_list = res.stdout.decode("utf-8").split("\n")
    repo_date = int(res_list[2].split(" ")[5])
    current_day = datetime.datetime.now().day
    return current_day - repo_date <= 7


def is_git_repo():
    res = subprocess.run(["git", "status"], stdout=subprocess.PIPE)
    return res.returncode == 0


def main():
    os.chdir(sys.argv[1])
    if is_git_repo():
        print(f"active branch: {get_current_branch()}")
        print(f"local changes: {check_local_changes()}")
        print(f"recent commit: {is_authored_last_week()}")
        print(f"blame Rufus: {is_author_rufus()}")
    else:
        print("Try to run again, this wasn't a git repo")


if __name__ == "__main__":
    main()

