# Welcome to Pexels.com API Python Library!

An easy library to use pexels api.

Official Documenation: https://www.pexels.com/api/documentation/
API Key: API Key can be generated from official website of Pexels.com (https://www.pexels.com/api/)

## Usage

### ***Photos***

#### Photos & Videos Parameters
> - ***query***
>   (*string - required*)  
>
>   The search query. `Ocean`, `Tigers`, `Pears`, etc.
> 
> - ***orientation***
>   (*string - optional*)  
>
>   Desired photo orientation. The current supported orientations are: `landscape`, `portrait` or `square`.
> 
> - ***size***
>   (*string - optional*) 
>
>   Minimum photo size. The current supported sizes are: `large`(24MP), `medium`(12MP) or `small`(4MP).
> 
> - ***color***
>     (*string - optional*)
>
>     Desired photo color. Supported colors:  `red`,  `orange`,  `yellow`,  `green`,  `turquoise`,  `blue`,  `violet`,  `pink`, 
> `brown`,  `black`,  `gray`,  `white`  or any hexidecimal color code
> (eg.  `#ffffff`).
> 
> - ***locale***
>     (*string - optional*)
>
>     The locale of the search you are performing. The current supported locales are:  `'en-US'`  `'pt-BR'`  `'es-ES'`  `'ca-ES'`  `'de-DE'` 
> `'it-IT'`  `'fr-FR'`  `'sv-SE'`  `'id-ID'`  `'pl-PL'`  `'ja-JP'` 
> `'zh-TW'`  `'zh-CN'`  `'ko-KR'`  `'th-TH'`  `'nl-NL'`  `'hu-HU'` 
> `'vi-VN'`  `'cs-CZ'`  `'da-DK'`  `'fi-FI'`  `'uk-UA'`  `'el-GR'` 
> `'ro-RO'`  `'nb-NO'`  `'sk-SK'`  `'tr-TR'`  `'ru-RU'`.
> 
> - ***page***
>     (*integer - optional*) 	
>  
>     The page number you are requesting.  `Default: 1`
> 	
> - ***per_page***
>     (*integer - optional*)
>
>     The number of results you are requesting per page.  `Default: 15`  `Max: 80`

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
##### Parameters

> - ***min_width*** *(integer | optional)*
>
>   The minimum width in pixels of the returned videos.
> 
> - ***min_height*** *(integer | optional)*
> 
>   The minimum height in pixels of the returned videos.
> 
> - ***min_duration*** *(integer | optional)*
>
>   The minimum duration in seconds of the returned videos.
> 
> - ***max_duration*** *(integer | optional)*
>  
>   The maximum duration in seconds of the returned videos.
>  
> - ***page*** *(integer | optional)*
>
>   The page number you are requesting.  `Default: 1`
> 
> - ***per_page*** *(integer | optional)*
>
>   The number of results you are requesting per page.  `Default: 15`  `Max: 80`

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