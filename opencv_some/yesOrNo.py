"""基于英特尔的OpenVINO, 不想安装, 就不测试了."""
import cv2 as cv

ie = IECore()
for device in ie.available_devices:
    print(device)
 
net = ie.read_network(model=model_xml, weights=model_bin)
input_blob = next(iter(net.input_info))
out_blob = next(iter(net.outputs))

n, c, h, w = net.input_info[input_blob].input_data.shape
print(n, c, h, w)

# cap = cv.VideoCapture("D:/images/video/Boogie_Up.mp4")
cap = cv.VideoCapture("D:/images/video/example_dsh.mp4")
# cap = cv.VideoCapture(0)
exec_net = ie.load_network(network=net, device_name="CPU")

em_net = ie.read_network(model=em_xml, weights=em_bin)
em_input_blob = next(iter(em_net.input_info))
em_it = iter(em_net.outputs)
em_out_blob1 = next(em_it)  # angle_y_fc
em_out_blob2 = next(em_it)  # angle_p_fc
em_out_blob3 = next(em_it)  # angle_r_fc
print(em_out_blob1, em_out_blob2, em_out_blob3)
en, ec, eh, ew = em_net.input_info[em_input_blob].input_data.shape
print(en, ec, eh, ew)

em_exec_net = ie.load_network(network=em_net, device_name="CPU")

cap = cv.VideoCapture(0)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
count = cap.get(cv.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv.CAP_PROP_FPS)
out = cap or cv.VideoWriter("D:/test.mp4", cv.VideoWriter_fourcc('D', 'I', 'V', 'X'), 15, (np.int(width), np.int(height)),
                     True)
while True:
    ret, frame = cap.read()
    if ret is not True:
        break
    image = cv.resize(frame, (w, h))
    image = image.transpose(2, 0, 1)
    inf_start = time.time()
    res = exec_net.infer(inputs={input_blob: [image]})
    inf_end = time.time() - inf_start
    # print("infer time(ms)：%.3f"%(inf_end*1000))
    ih, iw, ic = frame.shape
    res = res[out_blob]
    for obj in res[0][0]:
        if obj[2] > 0.75:
            xmin = int(obj[3] * iw)-10
            ymin = int(obj[4] * ih)-10
            xmax = int(obj[5] * iw)+10
            ymax = int(obj[6] * ih)+10
            if xmin < 0:
                xmin = 0
            if ymin < 0:
                ymin = 0
            if xmax >= iw:
                xmax = iw - 1
            if ymax >= ih:
                ymax = ih - 1
            roi = frame[ymin:ymax, xmin:xmax, :]
            roi_img = cv.resize(roi, (ew, eh))
            roi_img = roi_img.transpose(2, 0, 1)
            em_res = em_exec_net.infer(inputs={em_input_blob: [roi_img]})
            angle_p_fc = em_res[em_out_blob1][0][0]
            angle_r_fc = em_res[em_out_blob2][0][0]
            angle_y_fc = em_res[em_out_blob3][0][0]
            postxt = ""
            if angle_p_fc > 10 or angle_p_fc < -10:
                postxt += "pitch, "
            if angle_y_fc > 10 or angle_y_fc < -10:
                postxt += "yaw, "
            if angle_r_fc > 10 or angle_r_fc < -10:
                postxt += "roll, "

            cv.putText(frame, postxt, (xmin, ymin-10), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
            cv.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 255), 2, 8)
            cv.putText(frame, "infer time(ms): %.3f" % (inf_end * 1000), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1.0,
                       (255, 0, 255),
                       2, 8)
    cv.imshow("Face & head pose demo", frame)
    out.write(frame)
    c = cv.waitKey(1)
    if c == 27:
        break
cv.waitKey(0)
out.release()
cap.release()