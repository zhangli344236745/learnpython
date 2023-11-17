import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

encode = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./test.mp4', encode, 10, (width, height), True)
while True:
    # 每隔25毫秒播放下一帧，若键入“q”跳出循环
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    # 从摄像头获取下一帧
    ret, frame = cap.read()
    # 新开窗口展示图像
    cv2.imshow('test', frame)
    # 将当前帧写入视频文件
    out.write(frame)
# 释放VideoWriter
out.release()
# 释放摄像头
cap.release()
# 关闭窗口
cv2.destroyAllWindows()
