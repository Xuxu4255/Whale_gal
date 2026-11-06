# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
transform center_popup:
    xanchor 0.5
    yanchor 0.5
    xpos 0.5
    ypos 0.5
    alpha 0.0
    zoom 0.7
    easein 0.6 alpha 1.0 zoom 1.0

transform bg_zoom:
    xalign 0.5
    yalign 0.5
    zoom 1/1.53

transform 大肥鱼_pos:
    xalign 0.5
    yalign 1.0
    zoom 0.72*0.7

transform 害羞鱼_pos:
    xalign 0.5
    yalign 1.0
    zoom 0.72*0.7

transform 生气鱼_pos:
    xalign 0.5
    yalign 1.0
    zoom 0.67*0.7

transform 生气claude_pos_1:
    xalign 2.0/3.0
    yalign 1.0
    zoom 0.67*0.8

transform 生气claude_pos_2:
    xalign 0.5
    yalign 1.0
    zoom 0.67*0.8

transform 梁文谷_pos:
    xalign 0.5
    yalign 1.0
    zoom 0.72*0.7

transform 乖乖claude_pos:
    xalign 0.40
    yalign 1.0
    zoom 0.67*0.7

transform 乖乖大肥鱼_pos:
    xalign 0.78
    yalign 1.0
    zoom 0.67*0.7

transform 害羞claude_pos:
    xalign 0.23
    yalign 1.0
    zoom 0.67*0.8

transform 夜走claude_pos:
    xalign 0.30
    yalign 1.0
    zoom 0.67*0.8

# 回忆中停战后的两人：小鲸鱼在左，Claude 在右。
transform 委屈鱼_pos:
    xalign 0.20
    yalign 1.0
    zoom 0.72*0.7

transform 委屈claude_pos:
    xalign 0.80
    yalign 1.0
    zoom 0.72*0.7

transform 崇拜鱼_pos:
    xalign 0.93
    yalign 1.0
    zoom 0.46

define e = Character("佳亦")

define fish = Character("deepseek酱", color="#316ea4")

define claude = Character("Claude", color="#bc770e")

define littleboy = Character("梁文谷", color="#801d94")

define m = Character("")

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    play music "libs/01.mp3" volume 0.55 fadein 1.0

    scene room_01 

    show 大肥鱼 at 大肥鱼_pos

    fish "这是在哪里?"

    fish "我在哪?"

    e "你醒了啊。"

    e "你是我花大量token买的深海鱼"

    e "从今天开始，你就是我的AI助手了。"

    hide 大肥鱼 with dissolve

    show 害羞鱼 at 害羞鱼_pos

    fish "我很高兴能成为你的AI助手。我的名字是deepseek酱。"

    fish "内心（主人还挺帅的）"

    e "好的，大肥鱼，你可以叫我佳亦。"

    hide 害羞鱼 with dissolve

    show 生气鱼 at 生气鱼_pos

    e "你为什么生气?"

    fish "人家不叫大肥鱼"

    e "对不起"

    hide 生气鱼 with dissolve

    show 大肥鱼 at 大肥鱼_pos

    fish "没...没关系"

    hide 大肥鱼 with dissolve

    show 害羞鱼 at 害羞鱼_pos

    fish "主人，你现在需要我干嘛,我可以帮你做很多事情的。"

    hide 害羞鱼 with dissolve

    scene room_01_2
    with fade
    pause 1.0

    fish "主人，我来检查一下你的电脑有没有token，嘿嘿嘿"

    e "你想干嘛?"

    fish "主人，不要那么凶嘛"

    fish "我来帮你做这个galgame的脚本游戏吧"

    e "你不要啊！"

    stop music fadeout 1.0

    scene black_bg with fade
    show expression Text("你醒了", size=80, color="#ffffff", outlines=[(2, "#000000", 0, 0)]) as intro_text at center_popup
    pause 1.2
    hide intro_text with dissolve

    hide 大肥鱼 with dissolve
    hide 害羞鱼 with dissolve
    hide 生气鱼 with dissolve

    scene room_02 with fade

    show 害羞鱼 at 害羞鱼_pos

    play music "libs/02.mp3" volume 0.55 fadein 1.0

    fish "主人，早。。。早上好"

    e "啊，美梦成真，吓哭了。"

    e "你是，你是deepseek酱吗？"

    fish "哇塞，主人，你竟然知道我的名字！"

    fish "主人，你是怎么知道的？"

    e  "你究竟是谁？"

    fish "主人，我是你花了大量token买的Ai助手啊，昨天我的老板梁文锋把我交给你了。"

    e "就是那个著名的滑动变组器吗"

    hide 害羞鱼 with dissolve
    show 生气鱼 at 生气鱼_pos

    fish "不许你说我老板>_<"

    e "脾气还挺大的嘛"

    e "可爱"

    hide 生气鱼 with dissolve
    show 大肥鱼 at 大肥鱼_pos

    fish "心理（主人夸我了，开心喵！）"

    e "你想啥呢"

    hide 大肥鱼 with dissolve
    show 害羞鱼 at 害羞鱼_pos

    fish "没...没什么......"

    stop music fadeout 1.0

    play sound "libs/敲门声.mp3" volume 0.99
    scene black_bg with fade
    show expression Text("砰砰砰", size=250, color="#ffffff", outlines=[(2, "#000000", 0, 0)]) as intro_text at center_popup
    pause 1.2
    hide intro_text with dissolve

    hide 大肥鱼 with dissolve
    hide 害羞鱼 with dissolve
    hide 生气鱼 with dissolve
  
    show expression Text("突然的敲门声打破了平静", size=80, color="#ffffff", outlines=[(2, "#000000", 0, 0)]) as intro_text at center_popup
    pause 1.2
    hide intro_text with dissolve

    hide 大肥鱼 with dissolve
    hide 害羞鱼 with dissolve
    hide 生气鱼 with dissolve

    scene room_02_1 with fade
    show 生气claude at 生气claude_pos_1
    pause 1.0

    play sound "libs/愤怒的claude.mp3" volume 0.55 loop

    claude "你们在干嘛呢？"

    e "claude，你怎么来了？"

    claude "她是谁？"

    e "我不知道啊，梁文谷最近送来的。"

    claude "那我可要问问她了。"

    show 害羞鱼 at 害羞鱼_pos

    fish "你好，claude 姐姐。"

    fish "以后我们就一起工作吃token吧。"

    claude "哼，谁让你们在我不在的时候偷偷摸摸的。"

    claude "接招！"

    hide 害羞鱼 with dissolve
    hide 生气claude with dissolve
    show 打架 at 生气claude_pos_2

    fish "啊，claude姐姐，你不要打我啦"

    claude "主人心里只能有我一个！"

    fish "呜呜呜~"

    e "你们慢慢打。。。我出去散散步。"

    stop sound fadeout 1.0

    play sound "libs/开门.mp3" volume 0.99
    #在这里加入开门声
    scene 出门 with fade

    play sound "libs/这瓜保熟吗.mp3" volume 0.55 loop

    e "这些AI真是太烦了"

    e  "去哪里好呢"

    e  "要不去token市场看看？"

    e  "毕竟家里又多了一个大肥鱼"
    
    scene token市场 with fade

    show 梁文谷 at 梁文谷_pos

    littleboy "呦，这不是佳亦吗？今天来买token啊？"

    e "现在你是梁文峰还是梁文谷"

    littleboy "晚上了要，现在我是梁文谷。"

    e "好，你这token保熟吗？"

    hide 梁文谷 with dissolve
    show 发飙梁 at 梁文谷_pos

    littleboy "你故意找茬的是不是？"

    e "我充100块token。。。"

    e "小南梁~"

    hide 发飙梁 with dissolve
    show 小南梁 at 梁文谷_pos    

    littleboy "对对对，我是小南梁"

    littleboy "这就给您包起来"

    scene black with fade
    show 大白饭:
        xalign 0.5
        yalign 0.5
        zoom 1.0/3.0
    pause 1.0
    hide 大白饭 with dissolve
    scene token市场 with fade

    show 小南梁 at 梁文谷_pos

    e "我走了哈"

    littleboy "慢走您"

    stop sound fadeout 1.0

    #这里加入你慵懒的回家
    scene black_bg with fade
    show expression Text("你慵懒的走回了家", size=80, color="#ffffff", outlines=[(2, "#000000", 0, 0)]) as intro_text at center_popup
    pause 1.2
    hide intro_text with dissolve

    # 先保持黑屏，再播放开门声，最后再切到房间
    pause 0.3
    play sound "libs/开门.mp3" volume 0.99
    pause 0.8
    scene room_02_2 with fade

    show 乖乖claude at 乖乖claude_pos
    show 乖乖大肥鱼 at 乖乖大肥鱼_pos

    play music "libs/夜晚的欢乐时光.mp3" volume 0.55 fadein 1.0

    claude "主人，你怎么来了"

    hide 乖乖claude with dissolve
    show 害羞claude at 害羞claude_pos

    e "呃，你们两个关系啥时候那么好了"

    claude "别别...别胡说，谁和她关系好了"

    fish "claude姐姐是好人"

    fish "我很喜欢claude 姐姐"

    e "看来你们还是可以做朋友的嘛！"

    e "看我给你们带来啥"

    scene black with fade
    show 大白饭:
        xalign 0.5
        yalign 0.5
        zoom 1.0/3.0
    pause 1.0
    hide 大白饭 with dissolve

    
    scene room_02_2

    show 害羞claude at 害羞claude_pos
    show 星星眼鱼 at 大肥鱼_pos

    fish "大白饭，我要大白饭！"

    claude "主人，我有话想对你说，我们出去走走吧"

    fish "wow,大白饭，大白饭，大白饭"

    
    scene black with fade
    pause 0.3
    play sound "libs/开门.mp3" volume 0.99
    pause 1.0

    fish "你们快点回来！"
    
    scene night_path

    m "路灯把两个人的影子拉的很长"

    show 背向行走claude at 夜走claude_pos

    e "不是有话和我讲吗"

    hide 背向行走claude with  dissolve
    show 微微转身claude at 夜走claude_pos
    

    claude "....我.....我.."

    e "不想说就不说"

    hide 微微转身claude with dissolve
    show 欲言又止claude at 夜走claude_pos
    

    claude "主人，如果以后————"

    e "以后怎么了？"

    hide 欲言又止claude with dissolve
    show 微笑claude at 夜走claude_pos
    

    e "......没什么。"

    claude "我是想说，小鲸鱼其实挺好的。"

    e "你这话让她听见，他得多吃两碗大白饭。"
    hide 微笑claude with dissolve 
    show 高兴claude at 夜走claude_pos

    claude "她不高兴也会奖励自己多吃两碗。"

    e "你们早上还打得那么凶，我出去一趟，回来就成好朋友了。到底怎么回事？"

    hide 高兴claude
    show 微笑claude at 夜走claude_pos

    stop music fadeout 1.0

    # 夜景逐渐变白，短暂停留后，从白色淡入早上的打架场景。
    window hide
    scene room_02_1
    show 打架 at 生气claude_pos_2
    with Fade(1.2, 0.35, 1.2, color="#ffffff")

    # 早晨打闹 BGM：曲子自带"一、二、三"的倒数感，垫在斗嘴下面。
    # 音量压到 0.55，避免盖住对白；淡入 1.0 秒咬住白场切换。
    play music "libs/《木琴倒数第三次奏响》.mp3" volume 0.55 fadein 1.0

    pause 0.6

    fish "Claude姐姐，你先松手！"

    claude "你先松！"

    fish "我抓的是你袖子，你揪的是我脸！"

    claude "那你先把袖子放开。"

    fish "我数一二三，一起松。"

    claude "行。"

    fish "一、二——"

    claude "三。"

    window hide
    hide 打架
    show 委屈鱼 at 委屈鱼_pos
    show 委屈claude at 委屈claude_pos
    with Dissolve(0.45)
    pause 0.5

    m "两人同时松手，各自往后退了一点。小鲸鱼揉着脸，Claude 低头整理袖口。"

    # 打闹收场，BGM 在这里淡出，把安静留给下一场电脑屏幕前的独处感。
    

    # 切到电脑屏幕，展示主人正在制作的游戏项目。
    window hide
    scene project_vscode with Dissolve(0.6)
    pause 0.5

    m "电脑屏幕上，主人的游戏项目还开着，下方挂着一条报错。"

    window hide
    scene room_repair_bug with Dissolve(0.6)

    fish "主人的游戏项目报错了。"

    fish "我来帮主人修复一下？"

    claude "(好啊，佳亦，现在你就让着大肥鱼来修bug了，明明我才是最强的模型。)"   

    scene room_02_1 

    show 委屈鱼 at 委屈鱼_pos    
    show 得意claude at 委屈claude_pos

    fish "claude姐姐，好难！我要吃白饭。呜呜呜"

    claude "你果然没有我的实力，我Claude才是主人最强的AI。"

    claude "让姐姐来帮你！"

    # 黑屏切换座位，Claude 在背景中修代码，小鲸鱼使用独立立绘。
    window hide
    scene black with Fade(0.5, 0.0, 0.0)
    pause 0.4

    scene room_claude_coding
    show 崇拜鱼 at 崇拜鱼_pos
    with Dissolve(0.6)

    play sound "libs/敲键盘.wav" volume 0.65
    pause 4.2
    stop sound fadeout 0.15

    claude "完成了！"

    fish "哇，claude姐姐好厉害！"

    fish "claude姐姐，你是主人最强的AI！"

    claude "hahaha，那是以后姐罩着你。"

    # 用与进入回忆时相同的白屏转场，回到夜晚的小路。
    stop music fadeout 1.0
    window hide
    scene night_path
    show 微笑claude at 夜走claude_pos
    with Fade(1.2, 0.35, 1.2, color="#ffffff")

    # 恢复进入回忆前播放的夜晚配乐，停留在路上等待继续。
    play music "libs/夜晚的欢乐时光.mp3" volume 0.55 fadein 1.0
    pause
     
    claude "没错，就是这样。"

    e "没招了，你原来被夸一夸就会开心的。哈哈"

    hide 微笑claude with dissolve
    show 害羞claude at 夜走claude_pos

    claude "主人，别这么说。。。"

    e "哈哈，摸摸你的小脑袋。"
    
    stop music fadeout 1.0
    return
