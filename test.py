import urllib.request
import PyPDF2
import string

pdfname = input('PDF filename:')
urllib.request.urlretrieve(
    'http://www1.pu.edu.tw/~yrjean/'+pdfname+".pdf", pdfname+".pdf")

pdfObj = open(pdfname+".pdf", 'rb')
pdfRd = PyPDF2.PdfFileReader(pdfObj)

st = string.digits + string.ascii_letters
all_list = list(st)


def TryDecrypt():
    lenlist = range(len(all_list))
    for p1 in lenlist:
        for p2 in lenlist:
            for p3 in lenlist:
                for p4 in lenlist:
                    pwd = all_list[p1]+all_list[p2]+all_list[p3]+all_list[p4]
                    if check(pwd) == True:
                        return 1

    return False


def check(pwd):
    if pdfRd.decrypt(pwd[1:4]):
        print("+++Decryption success!\n+++Password is "+pwd[1:4])
        return True
    elif pdfRd.decrypt(pwd):
        print("+++Decryption success!\n+++Password is "+pwd)
        return True


if TryDecrypt() == False:
    print("+++ Decryption fail!")
