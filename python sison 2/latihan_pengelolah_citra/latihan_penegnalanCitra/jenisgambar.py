import cv2
import sys

if len(sys.argv) == 1:
    print('Masukan nama berkas gambar')
else:
    berkas = sys.argv[1]
    # membaca data gambar
    citra = cv2.imread(berkas, cv2.IMREAD_UNCHANGED)
if citra is None:
    print('Tidak dapat membaca berkas')
else:
    info = citra.shape
    if len(info) == 2:
        print('Citra keabu-abuan')
    else:
        print('citra berwarna')
