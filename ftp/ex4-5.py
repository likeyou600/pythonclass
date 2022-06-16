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

    ftp.login('43s1081754', 's108175443')  # Website: 246 25
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
        url = "http://43s1081754.000webhostapp.com/" + fname
        print("*** URL: " + url)
    ftp.quit()
