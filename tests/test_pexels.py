from pexelsapi.pexels import Pexels

pexels = Pexels('PASTE_API_KEY')


def test_search_photos():
    pexels.search_photos('ocean')


def test_curated_photos():
    pexels.curated_photos()


def test_get_photo():
    pexels.get_photo(3573351)


def test_search_videos():
    pexels.search_videos()


def test_popular_videos():
    pexels.popular_videos()


def test_get_video():
    pexels.get_video(1)
