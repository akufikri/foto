#!/usr/bin/env python3
"""Generate bait image (document look) for the geotrap landing page."""
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1000, 1400
F = "/System/Library/Fonts/Supplemental/Arial.ttf"
FB = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

random.seed(7)
img = Image.new("RGB", (W, H), (252, 251, 248))
d = ImageDraw.Draw(img)

# paper texture
for _ in range(26000):
    x, y = random.randrange(W), random.randrange(H)
    v = random.randint(-8, 6)
    d.point((x, y), (250 + v, 249 + v, 246 + v))

# header band
d.rectangle([0, 0, W, 132], fill=(23, 42, 74))
d.text((64, 40), "PEMBERITAHUAN", font=ImageFont.truetype(FB, 46), fill=(255, 255, 255))
d.text((64, 92), "Nomor: 0142/PN/XI/2026", font=ImageFont.truetype(F, 22), fill=(186, 202, 224))

f_b = ImageFont.truetype(FB, 26)
f_r = ImageFont.truetype(F, 24)

y = 190
d.text((64, y), "Dengan hormat,", font=f_r, fill=(28, 28, 30))
y += 52

paras = [
    "Bersama surat ini kami sampaikan bahwa dokumen yang Anda terima",
    "merupakan berkas resmi yang perlu ditinjau dan ditindaklanjuti",
    "dalam waktu 3 (tiga) hari kerja sejak surat ini dibaca.",
    "",
    "Untuk melihat rincian berkas, silakan buka tautan dokumen di bawah",
    "ini melalui perangkat Anda. Dokumen memuat data yang bersifat",
    "terbatas sehingga tidak dilampirkan dalam bentuk cetak.",
    "",
    "Demikian pemberitahuan ini disampaikan. Atas perhatian dan kerja",
    "sama yang baik, kami ucapkan terima kasih.",
]
for p in paras:
    if p:
        d.text((64, y), p, font=f_r, fill=(35, 35, 38))
    y += 40

# fake link box
y += 30
d.rounded_rectangle([64, y, W - 64, y + 92], radius=10, fill=(238, 242, 250), outline=(180, 198, 228), width=2)
d.text((88, y + 20), "Buka dokumen:", font=ImageFont.truetype(FB, 22), fill=(23, 42, 74))
d.text((88, y + 52), "klik tautan di deskripsi pesan", font=f_r, fill=(70, 96, 138))

# signature block
y += 160
d.text((W - 360, y), "Hormat kami,", font=f_r, fill=(35, 35, 38))
d.text((W - 360, y + 92), "Bagian Tata Usaha", font=f_b, fill=(20, 20, 22))
d.line([W - 360, y + 88, W - 96, y + 88], fill=(120, 120, 126), width=2)

# footer
d.line([64, H - 90, W - 64, H - 90], fill=(206, 206, 210), width=1)
d.text((64, H - 68), "Dokumen ini diterbitkan secara elektronik dan sah tanpa tanda tangan basah.",
       font=ImageFont.truetype(F, 18), fill=(126, 126, 132))

img = img.filter(ImageFilter.SMOOTH)
img.save("/Users/fikrinurhakim/lab/osint/geotrap/public/photo.jpg", quality=88, optimize=True)
print("ok")
