# 导入所需模块
from io_ import input_, output_  # 导入input_和output_模块
import score  # 导入score模块
import info  # 导入info模块
import run  # 导入run模块
import load  # 导入load模块
import add_book  # 导入add_book模块
import flet as ft  # 导入flet模块，并命名为ft
from flet import *  # 导入flet模块中的所有内容
from uwords import uload  # 导入uload函数
import sys  # 导入sys模块
import json
from lang import lang  # 导入语言包模块
import sys  # 导入sys模块
import os  # 导入os模块

assert sys.version_info >= (3, 10)  # 断言Python版本不低于3.10
i = 0  # 定义计数器变量i

# 定义main函数
def main(page: ft.page):  # 定义名为main的函数，接收一个名为page的ft.page类型参数
    """
    主函数，接收一个名为page的ft.page类型参数
    """
    with open('config.json', 'r') as f:  # 打开配置文件
            config = json.load(f)  # 读取配置文件

    # 定义view_pop函数
    def view_pop(view):  # 定义名为view_pop的函数，用于页面返回
        page.views.pop()  # 弹出页面视图栈顶元素
        top_view = page.views[-1]  # 获取页面视图栈顶元素
        page.go(top_view.route)  # 页面跳转至栈顶元素的路由

    # 设置页面标题
    page.title = "affelchen"

    # 添加触觉反馈组件
    hf = ft.HapticFeedback()
    page.overlay.append(hf)  # 将触觉反馈组件添加到页面覆盖层
    pb = ft.ProgressBar(width=250)
    # 定义ftc_onclick函数
    iv = 1
    def ftc_onclick(e): 
        """
        "ftc control"的点击事件处理函数
        """
        nonlocal iv
        nonlocal i  # 使用nonlocal声明i为非局部变量
        hf.heavy_impact()  # 产生重型触觉反馈
        bookname = dd.value 
        book_words = load.load("book_"+bookname) 
        try:
            if binput.value == book_words[list(book_words)[i-1]]:
                score.add_(1)  # 增加分数
                answer = True
            else:
                print("wrong answer")  # 打印错误信息
                answer = False
        except:
            ftctext.value = lang("Score: ") + score.get_()  # 显示分数
            pb.value = 1
        
        if i < len(book_words):
            if iv == 0:
                ftctext.value = list(book_words)[i] 
                iv = 1
                pro1 = len(list(book_words))
                pro = i / pro1  # 计算进度百分比
                print(pro)
                pb.value = pro
                
            elif iv == 1:
                if answer:
                    ftctext.value = lang("Correct!")
                
                else:
                    ftctext.value = lang("Wrong!") + "\n" + lang("Correct answer:") + "\n" +book_words[list(book_words)[i-1]]
                iv = 0
            i += 1  # 增加计数器
        elif i == len(book_words):
            if iv == 0:
                ftctext.value = lang("Score: ") + score.get_()  # 显示分数
                pb.value = 1
                
            elif iv == 1:
                if answer:
                    ftctext.value = lang("Correct!")
                
                else:
                    ftctext.value = lang("Wrong!") + "\n" + lang("Correct answer:") + "\n" +book_words[list(book_words)[i-1]]
                iv = 0
            i += 1  # 增加计数器
        else:
            ftctext.value = lang("Score: ") + score.get_()  # 显示分数
        print(ftc.content)  # 打印ftc的内容
        print(len(list(book_words)))
        print(i)
        page.update()  # 更新页面

    # 定义start函数
    def start(e):  
        """
        start_button的点击事件处理函数
        """
        hf.medium_impact()  # 产生中型触觉反馈
        page.route = "/learn"  # 设置页面路由为"/learn"
        page.update()  # 更新页面
    def settings(e):  
        """
        start_button的点击事件处理函数
        """
        hf.medium_impact()  # 产生中型触觉反馈
        page.route = "/settings"  # 设置页面路由为"/learn"
        page.update() 
        


    # 定义dropdown_changed函数
    def dropdown_changed(e):
        """
        下拉菜单的选择变化处理函数
        """
        nonlocal i  # 使用nonlocal声明i为非局部变量
        i = 0  # 重置计数器
        bookname = dd.value 
        book_words = load.load("book_"+bookname) 
        ftctext.value = list(book_words)[i]  # 设置ftctext的值为bookname
        i += 1  # 增加计数器
        page.update()  # 更新页面
        print(bookname)  # 打印bookname

    # 创建下拉菜单组件
    dd = ft.Dropdown(
        label=lang("Book"),
        hint_text=lang("Choose Book from List:"),
        on_change=dropdown_changed,
        options=[]
    )
    dd2 = ft.Dropdown(
        label=lang("Language"),
        hint_text=config["lang"],
        options=[]
    )
    with open('lang/lang.json', 'r') as langf:  # 打开语言配置文件
        langs = json.loads(langf.read())  # 读取语言配置文件
    for i in range(len(langs)):
        dd2.options.append(ft.dropdown.Option(langs[i]))

    # 创建信息卡片组件
    infocard = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ARTICLE_OUTLINED),
                        title=ft.Text("affelchen GUI v.0.0.1"),
                        subtitle=ft.Text(
                            lang("Developed by hengheng\nCopyright Cherry Service 2024")
                        ),
                    ),
                ],
            )
        )
    )
    settingscard = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                        title=ft.Text(lang("Settings")),
                        subtitle=ft.ElevatedButton(lang("Go to Settings"), icon=ft.icons.START_ROUNDED, on_click=settings)
                        ),
                    
                ],
            )
        )
    )

    print(score.get_())  # 打印当前分数

    # 定义刷新函数
    def refresh(e):  
        """
        刷新分数的函数
        """
        hf.medium_impact()  # 产生中型触觉反馈
        scorecard.content.content.controls[0].title.value = lang("Score: ") + score.get_()  # 设置分数卡片的标题为当前分数
        page.update()  # 更新页面

    scorecard = ft.Card(  
        content=ft.Container(  
            content=ft.Column(  
                [
                    ft.ListTile(  
                        leading=ft.Icon(ft.icons.SCOREBOARD_OUTLINED),  
                        title=ft.Text(lang("Score: ") + score.get_()),
                        subtitle=ft.ElevatedButton("Refresh", icon=ft.icons.REFRESH_ROUNDED, on_click=refresh)
                    )
                ],
            )
        )
    )
    def close_banner(e):
        page.banner.open = False
        page.update()
    def show_banner_click():
        page.banner.open = True
        page.update()
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            lang("Oops, there were some errors while trying to read the booklist. Pleas Check the server_repo in Settings.")
        ),
        actions=[
            ft.TextButton(lang("Go to Settings"), on_click=settings),
            ft.TextButton(lang("Ignore"), on_click=close_banner),
        ],
    )
    # 从文件加载书单列表
    opts = load.load("book_listl")  
    if opts != None:  # 如果文件存在，则读取文件内容:
        for i in range(len(opts)):
            print(opts[i])  # 打印每个书单列表项
            dd.options.append(ft.dropdown.Option(opts[i]))  # 将每个书单列表项添加到下拉菜单选项中
    else:
        show_banner_click()  # 显示错误提示
    

    # 创建书单卡片组件
    bookcard = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.BOOK_OUTLINED),
                        title=ft.Text(lang("Please Choose a Book from List:")),
                        subtitle=ft.Text(" "),
                    ),
                    dd  # 添加下拉菜单组件
                ],
            )
        )
    )

    # 创建带有开始按钮的卡片组件
    startcard = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.INPUT_ROUNDED),
                        title=ft.Text(lang("Press Button to Start:")),
                        subtitle=ft.ElevatedButton(lang("Start"),icon=ft.icons.START_ROUNDED, on_click=start)
                    )
                ],
            )
        )
    )

    col = ft.Column([infocard, settingscard, scorecard, bookcard, startcard], spacing=10,scroll=ft.ScrollMode.ALWAYS,)  # 组合卡片组件并设置间距
    ftctext = ft.Text(theme_style=ft.TextThemeStyle.HEADLINE_LARGE)  # 创建文本组件
    ftc = ft.Container(  # 创建"ftc control"用于learn页面上的卡片UI
        content=ftctext,  
        alignment=ft.alignment.center,  # 设置对齐方式
        bgcolor=ft.colors.INDIGO_300,  # 设置背景颜色
        width=250,  # 设置宽度
        height=400,  # 设置高度
        border_radius=10,  # 设置边框半径
        ink=True,  # 启用墨水效果
        on_click=ftc_onclick  # 设置点击事件处理函数
    )

    binput = ft.TextField(label=lang("input"))  # 创建文本字段

    # 定义route_change函数
    def route_change(e, ftc=ftc, col=col):
        """
        包括"learn"和"settings"页面UI的切换
        """
        print("Route change:", e.route)  # 打印路由变化信息
        page.views.clear()  # 清空页面视图栈
        page.views.append(
            ft.View(
                "/",  
                [col],  
                vertical_alignment=ft.MainAxisAlignment.CENTER  
            )
        )
        def bback(e):  # 定义名为bback的函数
            hf.medium_impact()  # 产生中型触觉反馈
            page.go("/")  # 返回主页面
        if page.route == "/learn":  
            page.views.append(  
                View(  
                    "/learn",  
                    [  
                        ft.Row([ft.FloatingActionButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=bback), pb], spacing=5),  
                        ftc,  
                        binput
                    ],
                    vertical_alignment=ft.MainAxisAlignment.SPACE_AROUND,  
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER  
                )
            )
        def close_dlg(e):
            dlg.open = False
            page.update()
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(lang("Settings Saved")),
            content=ft.Text(lang("Please restart the app to apply the changes.")),
            actions=[
                ft.TextButton(lang("Ignore"), on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
        def save_url(e):  # 定义名为save_url的函数
            hf.medium_impact()  # 产生中型触觉反馈
            server_url = sutf.value # 获取输入框的值
            print(server_url)  # 打印输入框的值
            page.banner.open = False
            page.update() # 更新页面
            bback("e")
            opts = load.load("book_listl")  
            if opts != None:  # 如果文件存在，则读取文件内容:
                for i in range(len(opts)):
                    print(opts[i])  # 打印每个书单列表项
                    dd.options.append(ft.dropdown.Option(opts[i]))  # 将每个书单列表项添加到下拉菜单选项中
                    page.update()  # 更新页面
            else:
                show_banner_click()  # 显示错误提示
            if dd2.value != None:  # 如果下拉菜单有值，则更新语言配置
                config["lang"] = dd2.value  # 更新语言配置
            if server_url != "":  # 如果输入框有值，则更新服务器配置
                config["server_url"] = server_url  # 更新服务器配置
            with open('config.json', 'w') as f:  # 打开配置文件:
                json.dump(config, f)  # 写入配置文件
            page.dialog = dlg
            dlg.open = True
            page.update()
       
        sutf = ft.TextField(label=lang("book_repo"), autocorrect=False, hint_text=config["server_url"])   
        if page.route == "/settings":  
            page.views.append( 
                View(  
                    "/settings", 
                    [
                    ft.Row([ft.FloatingActionButton(icon=ft.icons.ARROW_BACK_ROUNDED, on_click=bback)], spacing=5),
                    sutf,
                    dd2,
                    ft.ElevatedButton(lang("Save"), on_click=save_url)
                    ],

                )
            )
        page.update()  # 更新页面

    page.on_route_change = route_change  # 设置页面路由变化处理函数
    page.on_view_pop = view_pop  # 设置页面返回处理函数
    page.go(page.route)  
    page.update()  

ft.app(target=main)  # 将main函数作为目标函数传递给ft.app