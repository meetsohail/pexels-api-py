# Welcome to Pexels.com API Python Library!

An easy library to use pexels api.

Official Documenation: https://www.pexels.com/api/documentation/
API Key: API Key can be generated from official website of Pexels.com (https://www.pexels.com/api/)

## Usage

### ***Photos***

  #### Search Photos

```python
from pexelsapi.pexels import Pexels
pexel = Pexels('API_KEY')
search_photos = pexel.search_photos(query='ocean', orientation='', size='', color='', locale='', page=1, per_page=15)
print(search_photos)
```
#### Curated Photos
```python
from pexelsapi.pexels import Pexels
pexel = Pexels('API_KEY')
curated_photos = pexel.curated_photos(page=1, per_page=15)
print(curated_photos)
```
#### Get Photo
```python
from pexelsapi.pexels import Pexels
pexel = Pexels('API_KEY')
get_photo = pexel.get_photo(photo_id=10)
print(get_photo)
```
### ***Videos***

#### Search Videos
```python
from pexelsapi.pexels import Pexels
pexel = Pexels('API_KEY')
search_videos = pexel.search_videos(query='ocean', orientation='', size='', color='', locale='', page=1, per_page=15)
print(search_videos)
```
#### Popular Videos
```python
from pexelsapi.pexels import Pexels
pexel = Pexels('API_KEY')
popular_videos = pexel.popular_videos(min_width='', min_height='', min_duration='', max_duration='', page=1, per_page=15)
print(popular_videos)
```
#### Get Video
```python
from pexelsapi.pexels import Pexels
pexel = Pexels('API_KEY')
get_video = pexel.get_video(video_id=10)
print(get_video)
```