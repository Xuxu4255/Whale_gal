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

define e = Character("佳亦")

define fish = Character("deepseek酱", color="#316ea4")

define claude = Character("Claude", color="#bc770e")

define littleboy = Character("梁文谷", color="#801d94")

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

    scene room_01_2 at bg_zoom
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

    

    return
