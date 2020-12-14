from youtubesearchpython import *




'''
Searches for all types of results like videos, channels & playlists in YouTube.

'type' key in the JSON/Dictionary can be used to differentiate between the types of result.
'''
searchAll = Search('NoCopyrightSounds', page = 1, limit = 1, language = 'en-US', region = 'US')
print(searchAll.result())




'''
Searches only for videos in YouTube.
'''
searchVideos = SearchVideos('NoCopyrightSounds', page = 1, limit = 1, language = 'en-US', region = 'US')
'''
Setting mode = ResultMode.dict for getting dictionary result instead of JSON. Default is ResultMode.json.
'''
print(searchVideos.result(mode = ResultMode.dict))




'''
Searches only for channels in YouTube.
'''
searchChannels = SearchChannels('NoCopyrightSounds', page = 1, limit = 1, language = 'en-US', region = 'US')
print(searchChannels.result())




'''
Searches only for playlists in YouTube.
'''
searchPlaylists = SearchPlaylists('NoCopyrightSounds', page = 1, limit = 1, language = 'en-US', region = 'US')
print(searchPlaylists.result())




'''
Can be used to get custom search results with defined filters.

Setting second parameter as VideoSortOrder.uploadDate, to get video results sorted according to upload date.

Few of the predefined filters for you to use are:
SearchMode.videos
VideoUploadDateFilter.lastHour
VideoDurationFilter.long
VideoSortOrder.viewCount
There are many other for you to check out.

If this much control isn't enough then, you can pass custom string yourself by seeing the YouTube query in any web browser e.g. 
"EgQIBRAB" from "https://www.youtube.com/results?search_query=NoCopyrightSounds&sp=EgQIBRAB" can be passed as second parameter to get only videos, which are uploaded this year.
'''
searchCustom = SearchCustom('NoCopyrightSounds', VideoSortOrder.uploadDate, limit = 1, language = 'en-US', region = 'US')
print(searchCustom.result())




'''
You can add/omit the optional parameters according to your requirement & use case.
'''
