from browser import document, html

# 設定 Python 執行結果的容器　
container = document['python']  # 　Python 執行結果　<div id="python"></div>
for c in "w3-container w3-half w3-margin-top".split(' '):  # 設定基本版型
    container.classList.add(c)


# 小烏龜繪圖模組
import myTurtle
container <= html.DIV(html.H2('小烏龜繪圖模組'), Class="w3-container w3-blue  w3-margin-top")
turtleDiv = html.DIV(Class="w3-border")
myTurtle.drawTurtle(turtleDiv)
container <= turtleDiv


# 寶貝圖鑑列表
container <= html.DIV(html.H2('寶貝圖鑑列表'), Class="w3-container w3-blue  w3-margin-top")
table = html.TABLE(Class="w3-table-all")
table <= html.TR(html.TH('序號') + html.TH('中文名') + html.TH('最大CP') + html.TH('屬性'))
lines = [
    [1, '妙蛙種子', '1115', '草、毒'],
    [2, '妙蛙草', '1699', '草、毒'],
    [3, '妙蛙花', '2720', '草、毒'],
    [4, '小火龍', '980', '火'],
]
for line in lines:
    table <= html.TR(html.TD(line[0]) + html.TD(line[1]) + html.TD(line[2]) + html.TD(line[3]))
container <= table

# 寶貝圖鑑輸入表
container <= html.DIV(html.H2('寶貝圖鑑輸入表'), Class="w3-container w3-blue  w3-margin-top")
form = html.FORM(Class="w3-container w3-border")
form <= html.DIV(
    html.LABEL('中文名') +
    html.INPUT(type="text", name="firstname", value="", Class="w3-input"))
form <= html.DIV(
    html.LABEL('最大CP') +
    html.INPUT(type="number", name="最大CP", value="", Class="w3-input"))
label3 = html.LABEL('屬性')
input3 = html.SELECT(Class="w3-select")
for option in ['...', '草、毒', '火', '水']:
    input3 <= html.OPTION(option)
form <= html.DIV(label3 + input3)
form <= html.P(html.BUTTON("上傳", Class="w3-button w3-red"))
container <= form


# 畫布　Html Canvas
container <= html.DIV(html.H2('Html Canvas'),
                 Class="w3-container w3-blue  w3-margin-top")
canvas=html.CANVAS(width=300, height=300)
canvas.style={"width": "100%"}
ctx=canvas.getContext('2d')
ctx.rect(0, 0, 300, 300)
grd=ctx.createRadialGradient(150, 150, 10, 150, 150, 150)
grd.addColorStop(0, '#8ED6FF')
grd.addColorStop(1, '#004CB3')
ctx.fillStyle=grd
ctx.fill()
container <= canvas


