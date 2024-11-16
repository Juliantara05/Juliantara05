import requests

# Access Token (Ganti dengan token Anda)
ACCESS_TOKEN = "your_access_token"

# ID Halaman Facebook (Ganti dengan ID halaman Anda)
PAGE_ID = "your_page_id"

# Endpoint Graph API
BASE_URL = "https://graph.facebook.com/v16.0"

# Fungsi untuk membuat postingan
def create_post(message):
    url = f"{BASE_URL}/{PAGE_ID}/feed"
    params = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Post berhasil dibuat:", response.json())
    else:
        print("Gagal membuat post:", response.json())

# Fungsi untuk menyukai postingan
def like_post(post_id):
    url = f"{BASE_URL}/{post_id}/likes"
    params = {
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Post berhasil di-like.")
    else:
        print("Gagal melakukan like:", response.json())

# Contoh Penggunaan
if __name__ == "__main__":
    # Membuat Postingan
    message = "Halo, ini adalah postingan dari bot!"
    create_post(message)

    # Menyukai Postingan (Ganti dengan ID postingan)
    post_id = "post_id_to_like"
    like_post(post_id)
