import keyboard
import random
import time
import threading


# 默认语句库
excuses = [
    "卡了",
    "网卡",
    "手抖",
    "误触",
    "帧率低",
    "高延迟",
    "瓶颈期",
    "没手感",
    "没心态",
    "没状态",
    "刚‮醒睡‬没支架",
    "手酸了",
    "刚鹿完",
    "没散热器",
    "卡‮掉帧‬帧",
    "手冷手汗",
    "周‮太围‬吵",
    "在上‮厕所‬",
    "预判失误",
    "‮便随‬玩玩",
    "我在上课没‮指带‬套",
    "没‮带耳‬机",
    "屏幕太滑了",
    "手机‮烫太‬了",
    "腱鞘‮犯炎‬了",
    "天气太热了",
    "好‮没久‬玩了",
    "我‮妈叫‬我了",
    "耳机‮没电‬了",
    "电量‮提示低‬了",
    "上线第一把",
    "刚‮回游‬不会玩",
    "按键‮问有‬题",
    "打‮话电‬听不到声音",
    "没皮肤手‮不感‬行",
    "充电影‮发响‬挥",
    "延迟999了",
    "没带耳机，听声辨位失效",
    "我键盘突然失灵了",
    "刚才有人打电话",
    "散热器不行，CPU降频了",
    "我显示器突然黑屏了",
    "我家猫跳键盘上了"
]
#检查文件是否存在
try:
    with open("D:\\list.txt")as f:
        print("打开D:\\list.txt编辑内容")
except FileNotFoundError:
    with open("D:\\list.txt",'w',encoding='utf-8') as f:
        for word in excuses:
            f.write(word+"\n")
    print("已创建文件\n打开D:\\list.txt编辑内容")

def send_excuse():
    """发送随机狡辩到聊天栏"""
    with open('D:\\list.txt','r',encoding='utf-8')as f:
        lines=f.readlines()
        excuse = random.choice(lines)
    
    # 模拟按键流程
    keyboard.press_and_release('enter')  # 打开聊天框
    time.sleep(0.1)  # 等待聊天框打开
    keyboard.write(excuse)  # 输入狡辩内容
    time.sleep(0.1)
    keyboard.press_and_release('enter')  # 发送消息
    print(f"已发送: {excuse}")

def main():
    print("阵亡狡辩工具已启动")
    print("按 Enter 键发送随机狡辩")
    print("按 Shift+M 退出程序")
    
    # 创建退出事件
    exit_event = threading.Event()
    
    def on_enter():
        if not exit_event.is_set():
            send_excuse()
    
    def exit_program():
        print("\n程序已终止")
        exit_event.set()
    
    # 注册热键
    keyboard.on_press_key('enter', lambda _: on_enter())
    keyboard.add_hotkey('shift+m', exit_program)
    
    # 保持程序运行
    exit_event.wait()

if __name__ == "__main__":
    main()
