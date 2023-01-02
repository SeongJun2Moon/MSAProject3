"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from admin.views import hello

urlpatterns = [
    path('', hello),
    # path("movies/cinema", include('movies.cinema.urls')),
    # path("movies/musers", include('movies.musers.urls')),
    # path("movies/movies", include('movies.movies.urls')),
    # path("movies/showtimes", include('movies.showtimes.urls')),
    # path("movies/theater", include('movies.theater.urls')),
    # path("movies/theaterticket", include('movies.theaterticket.urls')),

    path("blog/busers", include('blog.busers.urls')),
    # path("blog/comments", include('blog.comments.urls')),
    # path("blog/posts", include('blog.posts.urls')),
    # path("blog/tags", include('blog.tags.urls')),
    # path("blog/views", include('blog.views.urls')),

    # path("shop/susers", include('shop.susers.urls')),
    # path("shop/carts", include('shop.carts.urls')),
    # path("shop/categories", include('shop.categories.urls')),
    # path("shop/deliveries", include('shop.deliveries.urls')),
    # path("shop/orders", include('shop.orders.urls')),
    # path("shop/products", include('shop.products.urls')),

    path("exrc/stroke", include("exrc.stroke.urls")),
    path("exrc/dlearn/iris", include("exrc.dlearn.iris.urls")),
    path("exrc/dlearn/fashion", include("exrc.dlearn.fashion.urls")),
    path("exrc/dlearn/number", include("exrc.dlearn.number.url")),
    path("exrc/dlearn/aitrader", include("exrc.dlearn.aitrader.urls")),
    path("exrc/webcrawler/webcrawler", include("exrc.webcrawler.webcrawler.urls")),
    path("exrc/nlp/samsung", include("exrc.nlp.samsung_report.urls")),
    path("exrc/nlp/imdb", include("exrc.nlp.imdb.urls")),
    path("exrc/nlp/korean_classify", include("exrc.nlp.korean_classify.urls")),

    path("security/users", include("security.users.urls")),
]
