import csv
import os
import cv2
if __name__ == "__main__":
    path = 'E:/m_cc/FaceSwap/FaceShifter/chs_stars_512px/anno/'
    # 1. 创建文件对象
    csvfile = open("E:/m_cc/FaceSwap/FaceShifter/chs_stars_512px/test_ids.csv",'w',newline='')
    # 2. 基于文件对象构建 csv写入对象
    writer = csv.writer(csvfile)
    idx = 0
    # 3. 写入csv文件内容
    for file in os.listdir(path):
        if '.csv' in file:
            idx += 1
            print(idx,') ',file)
            if idx%100==0:
                writer.writerow([file.replace('.csv','.jpg')])
            # img = cv2.imread('./sample_dataset/imgs/'+file.replace('.csv','.jpg'))
            # cv2.imwrite('./sample_dataset/imgs/'+file.replace('.csv','.jpg'),cv2.resize(img, (128,128), interpolation = cv2.INTER_LINEAR))


    # 4. 关闭文件
    csvfile.close()
