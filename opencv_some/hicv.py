import cv2
import numpy as np

def play_video(camara_num):
    """
    使用摄像头0 捕捉图像
    0:前置, 1:后置
    """
    cap = cv2.VideoCapture(camara_num)
    #cap = cv2.VideoCapture(1)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def draw_some():
    # Create a black image
    img=np.zeros((512,512,3), np.uint8)
    # Draw a diagonal blue line with thickness of 5 px 8 
    cv2.line(img,(0,0),(511,511),(255,0,0),5)
    # Draw a diagonal green rectangle with thickness of 3 px 8 
    cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
    # Draw a diagonal red circle with 填满内圆
    cv2.circle(img,(447,63), 63, (0,0,255), -1)
    # Draw a diagonal red ellipse with ⚪中心位置, 俩焦点位置, 填满90度的内圆
    cv2.ellipse(img,(256,256),(100,50),0,0,90,255,-1)
    # Draw a 多边形
    pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts=pts.reshape((-1,1,2))# 这里 reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。
    cv2.polylines(img, pts, False, 255)
    # Draw a word
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'HiOpnCV',(10,500), font, 4,(255,255,255),2)

    cv2.imshow('frame', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def catch_mouse():
    # events=[i for i in dir(cv2) if 'EVENT'in i]
    # print(events)
    def draw_circle(event,x,y,flags,param):
        print(event, (x, y), flags, param)
        if event==cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(img,(x,y),50,(255,0,0),-1)
        
    # 创建图像与窗口并将窗口与回调函数绑定
    img=np.zeros((512,512,3),np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    while(1):
        cv2.imshow('image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def catch_mouse_upgrade():
    # 当鼠标按下时变为 True 
    global ix,iy,drawing,mode
    drawing=False
    # 如果 mode 为 true 绘制矩形。按下'm' 变成绘制曲线。 
    mode=True
    ix,iy=-1,-1
    # 创建回调函数
    def draw_circle(event,x,y,flags,param):
        global ix,iy,drawing,mode
    # 当按下左键是返回起始位置坐标
        if event==cv2.EVENT_LBUTTONDOWN:
            drawing=True
            ix,iy=x,y
        # 当鼠标左键按下并移动是绘制图形。event 可以查看移动，flag 查看是否按下 
        elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
            if drawing==True:
                if mode==True:
                    cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
                else:
                    # 绘制圆圈，小圆点连在一起就成了线，3 代表了笔画的粗细 
                    cv2.circle(img,(x,y),3,(0,0,255),-1)
                    # 下面注释掉的代码是起始点为圆心，起点到终点为半径的
                    r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                    cv2.circle(img,(x,y),r,(0,0,255),-1)
        elif event==cv2.EVENT_LBUTTONUP:
            # 当鼠标松开停止绘画.
            drawing==False
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    # 创建图像与窗口并将窗口与回调函数绑定
    img=np.zeros((512,512,3),np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    img=np.zeros((512,512,3),np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)
    while(1):
        cv2.imshow('image',img)
        k=cv2.waitKey(1)&0xFF
        if k==ord('m'):
            mode = not mode
        elif k==27:
            break
    cv2.destroyAllWindows()

def create_bar():
    """创建滑动条"""
    def nothing(x):
        pass

    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow("image")

    cv2.createTrackbar('R', "image", 0, 255, nothing)
    cv2.createTrackbar('G', "image", 0, 255, nothing)
    cv2.createTrackbar('B', "image", 0, 255, nothing)

    switch = "0:OFF\n1:ON"
    cv2.createTrackbar(switch, "image", 0, 1, nothing)

    while(1):
        cv2.imshow("image", img)
        k = cv2.waitKey(1)&0xFF
        if k==27:
            break
        r = cv2.getTrackbarPos('R', "image")
        g = cv2.getTrackbarPos('G', "image")
        b = cv2.getTrackbarPos('B', "image")
        s = cv2.getTrackbarPos(switch, "image")
        if s==0:
            img[:] = [255, 255, 0]
        else:
            img[:] = [b, g, r]
    cv2.destroyAllWindows()

def all_about_above():
    def nothing(x):
        print(x)

    global ix,iy,drawing,mode
    # 鼠标按下为True
    drawing = False
    #mode 绘制图形   True 为矩形, 按下`m`切换曲线
    mode = True

    ix,iy=-1,-1
    # 创建回调函数
    def draw_circle(event, x, y, flags, param):
        r = cv2.getTrackbarPos('R', "image")
        g = cv2.getTrackbarPos('G', "image")
        b = cv2.getTrackbarPos('B', "image")
        color = (b, g, r)

        global ix,iy,drawing,mode
        # 按下左键是返回起始位置坐标
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix, iy = x, y
        #按下左键, 并且拖动时绘制图形. event: 移动, flag: 是否按下
        elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
            if drawing == True:
                if mode == True:
                    cv2.rectangle(img,(ix,iy),(x,y),color,-1)
                else:
                    # 绘制圆圈, 小圆点连接成线
                    cv2.circle(img,(x,y),3,color,-1)
                    #r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                    #cv2.circle(img,(x,y),r,(0,0,255),-1)
        elif event == cv2.EVENT_LBUTTONUP:
            drawing == False
            #if mode==True:
            #    cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            #else:
            #    cv2.circle(img,(x,y),5,(0,0,255),-1)
    img = np.zeros((512,512,3),np.uint8)
    cv2.namedWindow("image")
    cv2.createTrackbar('R', "image", 0, 255, nothing)
    cv2.createTrackbar('G', "image", 0, 255, nothing)
    cv2.createTrackbar('B', "image", 0, 255, nothing)

    cv2.setMouseCallback('image',draw_circle)
    while(1):
        cv2.imshow("image", img)
        k = cv2.waitKey(1)&0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            # Esc
            break


if __name__ == "__main__":
    #play_video(0)
    #draw_some()
    #catch_mouse()
    #catch_mouse_upgrade()
    #create_bar()
    all_about_above()