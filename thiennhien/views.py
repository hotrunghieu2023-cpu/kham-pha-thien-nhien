from django.shortcuts import render

def home(request):
    return render(request, "thiennhien/home.html")

def about(request):
    return render(request, "thiennhien/about.html")

def contact(request):
    return render(request, "thiennhien/contact.html")

def detail(request, slug):
    articles = {
        "forest": {
        "title": "🌲 Rừng nguyên sinh – Lá phổi xanh của Trái Đất",
        "image": "thiennhien/images/OIP (5).jpg",
        "content": "Rừng nguyên sinh là nơi duy trì sự sống và cân bằng sinh thái cho hành tinh của chúng ta. Đây là nơi sinh sống của rất nhiều loài động vật và thực vật.",
        },
        
        "ocean": {
            "title": "🌊 Khám phá thế giới đại dương",
            "image": "thiennhien/images/IMG_6714.jpg",
            "content": "Đại dương bao phủ hơn 70% diện tích Trái Đất và chứa đựng vô vàn điều kỳ diệu. Đây là nơi sinh sống của hàng triệu loài sinh vật.",
        },

        "mountain": {
            "title": "🏔️ Những dãy núi hùng vĩ trên thế giới",
            "image": "thiennhien/images/OIP (5).jpg",
            "content": "Những dãy núi hùng vĩ trải dài qua nhiều quốc gia, tạo nên những cảnh quan thiên nhiên tuyệt đẹp và là nơi sinh sống của nhiều loài động thực vật.",
        },

        "waterfall": {
            "title": "💧 Thác nước – Dòng chảy của thiên nhiên",
            "image": "thiennhien/images/IMG_6714.jpg",
            "content": "Thác nước là một trong những cảnh quan ấn tượng của thiên nhiên. Những dòng nước đổ xuống từ độ cao lớn tạo nên vẻ đẹp mạnh mẽ và kỳ thú.",
        },
    }

    article = articles.get(slug)

    return render(request, "thiennhien/detail.html", {
        "article": article
    })