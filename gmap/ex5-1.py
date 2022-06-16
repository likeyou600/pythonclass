from turtle import color
import gmplot

gmap = gmplot.GoogleMapPlotter(24.227079, 120.583611,7)

lat= 24.227079
lon = 120.583611
color='red'

gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s"
gmap.marker(lat,lon,color,title='Providence Hall')
gmap.draw("Gmap.html")

def Upload(htmlFile):

    from ftplib import FTP
    import time

    ftp = FTP()
    Not_CONNECT = True

    while Not_CONNECT:
        try:
            ftp.connect("files.000webhost.com", port=21, timeout=1000)
        except Exception as ErrorMessage:
            print("Error:", ErrorMessage)
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
        else:
            Not_CONNECT = False

    ftp.login('42s1081735', 's108173542')  # Website: 246 25
    ftp.cwd("public_html")  # Change directory
    fname = htmlFile
    tname = htmlFile

    try:
        f = open(fname, 'rb')
        ftp.storbinary('STOR ' + tname, f)
    except Exception as e:
        print('*** Upload Fail :', e)
    else:
        print("*** File %s uploaded!" % fname)
        url = "http://42s1081735.000webhostapp.com/" + fname
        print("*** URL: " + url)
    ftp.quit()

Upload("Gmap.html")