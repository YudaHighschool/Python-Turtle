import turtle
from browser import document, html
from browser.html import TABLE, TR, TH, TD, DIV, BR, H1, H2, H3, LABEL

# All the elements will be inserted in the div with the "container" id
container = document['python']  # 　Python 執行結果　<div id="python"></div>
mainDiv = DIV(Class="w3-container w3-half w3-margin-top")  # 設定基本版型


# 小烏龜繪圖模組
mainDiv <= DIV(H2('小烏龜繪圖模組'), Class="w3-container w3-blue  w3-margin-top")
turtleDiv = DIV(Class="w3-border")
turtle.set_defaults(
    turtle_canvas_wrapper=turtleDiv
)
t = turtle.Turtle()

t.width(5)
for c in ['red', '#00ff00', '#fa0', 'rgb(0,0,200)']:
    t.color(c)
    t.forward(100)
    t.left(90)
turtle.done()
mainDiv <= turtleDiv


# 寶貝圖鑑列表
mainDiv <= DIV(H2('寶貝圖鑑列表'), Class="w3-container w3-blue  w3-margin-top")
table = TABLE(Class="w3-table-all")
table <= TR(TH('序號') + TH('中文名') + TH('最大CP') + TH('屬性'))
lines = [
    [1, '妙蛙種子', '1115', '草、毒'],
    [2, '妙蛙草', '1699', '草、毒'],
    [3, '妙蛙花', '2720', '草、毒'],
    [4, '小火龍', '980', '火'],
]
for line in lines:
    table <= TR(TD(line[0]) + TD(line[1]) + TD(line[2]) + TD(line[3]))
mainDiv <= table

# 寶貝圖鑑輸入表
mainDiv <= DIV(H2('寶貝圖鑑輸入表'), Class="w3-container w3-blue  w3-margin-top")
form = html.FORM(Class="w3-container")
label1 = html.LABEL('中文名')
input1 = html.INPUT(type="text", name="firstname", value="", Class="w3-input")
Label2 = html.LABEL('最大CP')
input2 = html.INPUT(type="number", name="最大CP", value="", Class="w3-input")
Label3 = html.LABEL('屬性')
input3 = html.INPUT(type="number", name="屬性", value="", )
input3 = html.SELECT(Class="w3-select")
for c in ['...', '草、毒', '火', '水']:
    input3 <= html.OPTION(c)
input4 = html.P(html.BUTTON("上傳", Class="w3-button w3-red"))
form <= label1 + input1 + Label2 + input2 + Label3 + input3 + input4

mainDiv <= form


# 畫布　Html Canvas
canvas_title = DIV(H2('Html Canvas'),
                   Class="w3-container w3-blue  w3-margin-top")
canvas = html.CANVAS(width=300, height=300)
canvas.style = {"width": "100%"}
ctx = canvas.getContext('2d')
ctx.rect(0, 0, 300, 300)
grd = ctx.createRadialGradient(150, 150, 10, 150, 150, 150)
grd.addColorStop(0, '#8ED6FF')
grd.addColorStop(1, '#004CB3')
ctx.fillStyle = grd
ctx.fill()
mainDiv <= canvas_title
mainDiv <= canvas


container <= mainDiv
