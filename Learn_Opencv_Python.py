# --------------- Extract frame using OpenCV -------------
# import cv2

# def frameCapture(path):
#     vid = cv2.VideoCapture(path)
#     count = 0
#     success = 1
#     while success:
#         success, image = vid.read()
#         cv2.imwrite("frame%d.jpg" % count, image)
        
#         count += 1
# if __name__ == "__main__":
#     frameCapture("G:\\Nampc\\Media\\Videos\\selfie_segmentation_web.mp4")

# -------------- Displaying the coordinates of the points clicked on the image using Python-OpenCV ----------------

import cv2

[print(i) for i in dir(cv2) if 'EVENT' in i]

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' + str(y), (x,y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
        
        print(x, ' ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1, (255, 255, 0), 2)
        cv2.imshow('image', img)
        
if __name__ == "__main__":
    img = cv2.imread('.\\annotated_image0.png', 1)
    
    cv2.imshow('image', img)
    cv2.setMouseCallback('image',click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()