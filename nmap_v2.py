import time
import folium
import requests
import  urllib
import csv

class map:
    def __init__(self):
        url = 'https://data.nhi.gov.tw/Datasets/Download.ashx?rid=A21030000I-D03001-001&l=https://data.nhi.gov.tw/resource/Nhi_Fst/Fstdata.csv'
        webpage = urllib.request.urlopen(url)
        self.data = csv.reader(webpage.read().decode('utf-8').splitlines())
        t = open(r'C:\xampp\htdocs\map\map.txt' , 'w')
        t.close()
    def csv (self):
        file_path = (r'C:\xampp\htdocs\ogcsv.csv')
        with open(file_path,'rt', encoding = 'utf-8') as csvfile:
            reader=csv.reader(csvfile)
            self.name = [row[1]  for row in reader]
        with open(file_path,'rt', encoding = 'utf-8') as csvfile:
            reader=csv.reader(csvfile)
            self.addr = [row[2]  for row in reader]
        with open(file_path,'rt', encoding = 'utf-8') as csvfile:
            reader=csv.reader(csvfile)
            self.y     = [row[3] for row in reader]
        with open(file_path,'rt', encoding = 'utf-8') as csvfile:
            reader=csv.reader(csvfile)    
            self.x    = [row[4] for row in reader]
        with open(file_path,'rt', encoding = 'utf-8') as csvfile:
            reader=csv.reader(csvfile)    
            self.tel    = [row[5] for row in reader]
        with open(file_path,'rt', encoding = 'utf-8') as csvfile:
            reader=csv.reader(csvfile)    
            self.stime    = [row[10] for row in reader]
        self.max = len(self.tel)
        self.check = [0]*self.max
        
    def new_map(self):
        t = open(r'C:\xampp\htdocs\map\map.txt' , 'a')
        m = folium.Map(location = [25.0693126,121.3680913] , zoom_start = 14)
        for i in self.data:
            if '林口區'  in i[2] or '龜山區' in i[2]:
                for j in range (0,self.max):
                    if i[1] == self.name[j]:
                        self.check[j] = 1
                        stime = self.stime[j]
                        break
                if i[1] == '欣穎藥局' or i[1] == '一家好藥局' or i[1] == '泰臨中西藥局':
                    if int(i[7]) >= 40 :
                        color = 'green'
                    elif 20 < int(i[7]) < 40:
                        color = 'orange'
                    elif int(i[7]) <= 20 :
                        color = 'red'
                    html = "<h4> <b>藥局名稱 :&nbsp" + i[1] +"</h4></b>"+ "<br><b>藥局地址: &nbsp </b>"+i[2]+ "<br>" + "<b>藥局電話:</b>"+ i[5]+"<br><b>快篩試劑種類: </b>"+i[6]+"<br><b>快篩試劑剩餘 :  </b>"+i[7]+"<br><b>藥局備註: </b>"+i[9]+"<br><b>開賣時間: </b>"+stime+"<br><b>更新時間: </b>"+time.asctime( time.localtime(time.time()) )+"<br><b>資料來源更新時間: </b>"+i[8]+"<br><b>資料來源: https://ppt.cc/fH6l5x </b>"
                    txt = '藥局名稱: '+str(i[1])+'\n藥局地址: ' +str(i[2])+ '\n藥局電話: ' +str(i[5])+ '\n快篩試劑種類: ' +str(i[6])+ '\n快篩試劑剩餘: '+str(i[7])+'\n藥局備註: '+str(i[9])+'\n開賣時間:' +stime+'\n'
                    t.write(str(txt)+'\n')
                    iframe = folium.IFrame(html)
                    popup = folium.Popup(iframe, min_width=380,max_width=380)
                    folium.Marker([self.x[j],self.y[j]], popup=popup, icon=folium.Icon(icon='info-sign',color=color)).add_to(m)
                else:    

                    if int(i[7]) >= 40 :
                        color = 'green'
                    elif 20 < int(i[7]) < 40:
                        color = 'orange'
                    elif int(i[7]) <= 20 :
                        color = 'red'
                    html = "<h4> <b>藥局名稱 :&nbsp" + i[1] +"</h4></b>"+ "<br><b>藥局地址: &nbsp </b>"+i[2]+ "<br>" + "<b>藥局電話:</b>"+ i[5]+"<br><b>快篩試劑種類: </b>"+i[6]+"<br><b>快篩試劑剩餘 :  </b>"+i[7]+"<br><b>藥局備註: </b>"+i[9]+"<br><b>開賣時間: </b>"+stime+"<br><b>更新時間: </b>"+time.asctime( time.localtime(time.time()) )+"<br><b>資料來源更新時間: </b>"+i[8]+"<br><b>資料來源: https://ppt.cc/fH6l5x </b>"
                    txt = '藥局名稱: '+str(i[1])+'\n藥局地址: ' +str(i[2])+ '\n藥局電話: ' +str(i[5])+ '\n快篩試劑種類: ' +str(i[6])+ '\n快篩試劑剩餘: '+str(i[7])+'\n藥局備註: '+str(i[9])+'\n開賣時間:' +stime+'\n'
                    t.write(str(txt)+'\n')
                    iframe = folium.IFrame(html)
                    popup = folium.Popup(iframe, min_width=380,max_width=380)
                    folium.Marker([i[4],i[3]], popup=popup, icon=folium.Icon(icon='info-sign',color=color)).add_to(m)
        for i in range(0,self.max):
            if self.check[i] == 0:
                html = "<h4> <b>藥局名稱 :&nbsp" + self.name[i] +"</h4></b>"+ "<br><b>藥局地址: &nbsp </b>"+self.addr[i]+ "<br>" + "<b>藥局電話:</b>"+ self.tel[i]+"<br><b>快篩試劑種類: </b><br><b>快篩試劑剩餘 : 0 <br><b>開賣時間: </b>"+self.stime[i]+"<br><b>更新時間: </b>"+time.asctime( time.localtime(time.time()) )+"<br><b>資料來源更新時間: </b><br><b>資料來源: https://ppt.cc/fH6l5x </b>"
                iframe = folium.IFrame(html)
                popup = folium.Popup(iframe, min_width=380,max_width=380)
                folium.Marker([self.x[i],self.y[i]], popup=popup, icon=folium.Icon(icon='info-sign',color='gray')).add_to(m)
        m.save(r'C:\xampp\htdocs\map\map.html')
        t.close()
def monitor (live):
        ip = '120.125.82.175'
        seconds_since_epoch = time.time()
        seconds_since_epoch = seconds_since_epoch * 1000000000
        seconds_since_epoch  = format(seconds_since_epoch , '.0f')
        data =  "linkouMap,host=180 Live=%s  %s" % (live,seconds_since_epoch)
        url = 'http://'+ip+':8086/write?consistency=any&db=telegraf' 
        response = requests.post(url, data,headers={'Connection':'close'},timeout = 1)

def main ():
    
        while True:
            try:
                start = time.time()
                
                map_q = map()
                map_q.csv()
                map_q.new_map()
                print (time.asctime( time.localtime(time.time())))
                end = time.time()
                monitor(1)
                if end - start > 0:
                    time.sleep( 60 - (end - start))
            except Exception as e:
                e1 = open (r'C:\xampp\htdocs\map\log.txt','a')
                e1.write(time.asctime( time.localtime(time.time()))+str(e)+'\n')
                e1.close()
                monitor(10)
                time.sleep(60)
                print (e)
        
if __name__ == '__main__':
    main()