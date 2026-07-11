# 学生基本信息
student = {
    "姓名": "   张三   ",
    "高考分数": 686,
    "选科": ["物理", "化学", "生物"],
    "兴趣标签": ["计算机", "机器人", "AI", "计算机", "自动化", "AI", "游戏开发"],
    "目标城市": "杭州",
}


# 大学基础信息
# tuple 表示这些大学的基础信息一般不应该随便修改
# 格式：(大学名称, 所在城市, 最低录取分数线)
universities = (
    ("清华大学", "北京", 700),
    ("浙江大学", "杭州", 680),
    ("上海交通大学", "上海", 690),
    ("哈尔滨工业大学", "哈尔滨", 660),
    ("华中科技大学", "武汉", 655),
    ("电子科技大学", "成都", 645),
)


# 专业推荐池
major_pool = [
    "计算机科学与技术",
    "人工智能",
    "机器人工程",
    "自动化",
    "软件工程",
    "数据科学与大数据技术",
    "电子信息工程",
]


# 学生原始志愿表
wish_list = [
    ["清华大学", ["计算机科学与技术", "人工智能"]],
    ["浙江大学", ["机器人工程", "自动化"]],
    ["上海交通大学", ["人工智能", "电子信息工程"]],
    ["哈尔滨工业大学", ["机器人工程", "软件工程"]],
    ["电子科技大学", ["软件工程", "电子信息工程"]],
]
# 这里我整理了一下专业
wish = []
for i in wish_list:
    wish.extend(i[1])
wish = set(wish)

import time
import tkinter


def progress_function(sleep_time, curculation):
    print("正在计算，请稍后")
    for i in range(1, 101):
        print("■" * i, "□" * (100 - i), f"{i}%", end="\r")
        time.sleep(sleep_time)
        if i == 99:
            time.sleep(3)
    print("\n计算完成!!!")
    curculation()


# 一份复杂列表，用于完成列表遍历、清空、倒序、嵌套倒序任务

my_list = [
    "写完这段代码高考分数必如意",
    750,
    ["计算机", "机器人", "自动化"],
    "",
    12.9682,
    6 + 9j,
    ["清华大学", "浙江大学"],
    "Apple",
    progress_function,
    print("我是个print函数, 被执行了！"),
    progress_function(0.05, print),
]


def analyze_student(student, universities):
    # 1.字符串清洗
    student["姓名"] = student["姓名"].strip(" ")
    # 2.兴趣标签去除
    student["兴趣标签"] = set(student["兴趣标签"])
    student["兴趣标签"] = list(student["兴趣标签"])
    # 3.while实现clear效果
    task_list = ["整理成绩", "查询大学", "筛选专业", "提交志愿"]
    while len(task_list) >= 1:
        task_list.pop(0)
    # 4.for倒序复制
    new_list = list()
    new_list = my_list[::-1]
    for id, items in enumerate(new_list):
        if type(items) == list:
            new_list[id] = items[::-1]
    # 5.统计学生可以报考的大学
    challenge_list = []
    safe_list = []
    not_recommended_list = []
    for i in universities:
        if student["高考分数"] >= i[2]:
            safe_list.append(i)
        elif i[2] - student["高考分数"] <= 10:
            challenge_list.append(i)
        else:
            not_recommended_list.append(i)
    # 6.根据兴趣推荐专业
    major_map = {
        "计算机": ["计算机科学与技术", "软件工程"],
        "AI": ["人工智能", "数据科学与大数据技术"],
        "机器人": ["机器人工程", "自动化"],
        "自动化": ["自动化", "电子信息工程"],
        "游戏开发": ["软件工程", "计算机科学与技术"],
    }
    recommended_major = []
    for key, value in major_map.items():
        recommended_major.extend(value)
    recommended_major = set(recommended_major)
    recommended_major = recommended_major.intersection(wish)
    recommended_major = list(recommended_major)
    # 7.设计一个函数，返回多个结果
    return challenge_list, safe_list, not_recommended_list, recommended_major


# 8.设计一个生成报告的函数
def create_report(student, challenge, safe, not_recommended, recommended_majors):
    window = tkinter.Tk()
    window.geometry("600x500")
    name = student["姓名"]
    score = student["高考分数"]
    interest = major = challenge_str = safe_str = not_recommemded_str = ""
    # 设置文本
    for i in student["兴趣标签"]:
        interest += i
        interest += ","
    for i in recommended_majors:
        major += i
        major += ","
    for i in challenge:
        challenge_str += i[0]
        challenge_str += ","
    for i in safe:
        safe_str += i[0]
        safe_str += ","
    for i in not_recommended:
        not_recommemded_str += i[0]
        not_recommemded_str += ","
    # 定义Label
    interest_label = tkinter.Label(
        window,
        text=f"""
你的兴趣标签如下：
{interest}
""",
    )
    name_label = tkinter.Label(
        window,
        text=f"{name}同学你好！",
        bg="#00FF00",
        width=600,
        height=1,
        font=("微软雅黑", 20),
    )

    score_label = tkinter.Label(
        window, text=f"你的高考分数为{score}", font=("微软雅黑", 15)
    )
    major_label = tkinter.Label(
        window,
        text=f"""
推荐专业如下：
{major}
""",
    )

    challenge_label = tkinter.Label(
        window,
        text=f"""
以下院校可冲：
{challenge_str}
""",
        fg="#00FF00",
    )

    safe_label = tkinter.Label(
        window,
        text=f"""
以下院校稳妥：
{safe_str}
""",
        fg="#0000FF",
    )

    not_recommended_label = tkinter.Label(
        window,
        text=f"""
以下院校报考风险较大
{not_recommemded_str}
""",
        fg="#FF0000",
    )
    congratulation = tkinter.Label(
        window,
        width=600,
        height=2,
        text="祝金榜题名:)",
        bg="#FFFF00",
        font=("微软雅黑", 20),
    )
    name_label.pack()
    score_label.pack()
    interest_label.pack()
    major_label.pack()
    challenge_label.pack()
    safe_label.pack()
    not_recommended_label.pack()
    congratulation.pack()
    window.mainloop()


challenge, safe, not_recommamd, recommemded_major = analyze_student(
    student, universities
)
create_report(student, challenge, safe, not_recommamd, recommemded_major)
