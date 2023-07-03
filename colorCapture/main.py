import pyautogui
# from PIL import Image

# スクリーンショットを取得する
def capture_screen():
    screenshot = pyautogui.screenshot()
    if screenshot is None:
        print('スクリーンショットが取れていません')
    return screenshot

screenshot = capture_screen()

screenshot.save('screen.png')

#画像のサイズを取得
width,height = screenshot.size

colors=set()
for x in range(width):
    for y in range (height):
        pixel = screenshot.getpixel((x,y))
        colors.add(pixel)

for color in colors:
    print(color)

    # image = Image.new("RGB",(1,1),color)
    # image.show()
