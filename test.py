song_response = [{"id":43107279,"title":"Prelude","duration":148,"replayGain":-9.97,"peak":0.998291,"allowStreaming":true,"streamReady":true,"adSupportedStreamReady":true,"djReady":true,"stemReady":false,"streamStartDate":"2015-03-17T00:00:00.000+0000","premiumStreamingOnly":false,"trackNumber":1,"volumeNumber":1,"version":null,"popularity":20,"copyright":"℗ 1991 Priority Records, LLC","bpm":null,"url":"http://www.tidal.com/track/43107279","isrc":"USPO19100001","editable":false,"explicit":true,"audioQuality":"LOSSLESS","audioModes":["STEREO"],"mediaMetadata":{"tags":["LOSSLESS"]},"artist":{"id":9127,"name":"N.W.A","type":"MAIN","picture":"84299843-40fe-487f-ad7d-35ecadb6e37c"},"artists":[{"id":9127,"name":"N.W.A","type":"MAIN","picture":"84299843-40fe-487f-ad7d-35ecadb6e37c"}],"album":{"id":43107278,"title":"Efil4zaggin","cover":"17520548-e197-4a46-b1f3-eadafcd04c56","vibrantColor":"#dd463c","videoCover":null},"mixes":{"TRACK_MIX":"00106fe26b71589bd51522cbcc8038"}},{"trackId":43107279,"assetPresentation":"FULL","audioMode":"STEREO","audioQuality":"LOSSLESS","manifestMimeType":"application/vnd.tidal.bts","manifestHash":"FAoIhKh0a+0/PdxtWvUv2XE/k7G22xSelz+z5gi+N2U=","manifest":"eyJtaW1lVHlwZSI6ImF1ZGlvL2ZsYWMiLCJjb2RlY3MiOiJmbGFjIiwiZW5jcnlwdGlvblR5cGUiOiJOT05FIiwidXJscyI6WyJodHRwczovL3NwLXByLWNmLmF1ZGlvLnRpZGFsLmNvbS9tZWRpYXRyYWNrcy9DQUVhS1JJbk1qRXpZalkwWlRjM00yUXpObUV4TWpNellUWXpZekk1TUdJNE1URmhOelJmTmpFdWJYQTAvMC5mbGFjP0V4cGlyZXM9MTcxMjM4NTMwNCZTaWduYXR1cmU9Q0IzNVFIY2lrQTBCcThtdjJYZXFqc0V4TktuemQ1VHprbTV2bVdyb2x+ajBVRi1OSHJKaEJGNzhyM2stclBqRVh5UnJxfkZ1WVEtdFo1bjY1N0NNRDdoZENFaHhMVEVXSlg2MkpNTm0wfkh0WDY4d1R+ekVieE9OY1dhb2k2U1AtZTFCWjB3V2E1aVM3dVVXLW4taElEVG9PalcxM20yS00tUkdScy03MnVKQmxJfjZIQkZJSGJXSnpNbGZZUUx4WUV5Z3pjZGxVamJ3T2NZMlFJT0p2NkNKVk9zb0ROSlU3NmIyR2ZHTGVjUlhiSn43ejZuWm51cjRpdHlMU2tWd3JleHZad3J3Qlc4bzk5VFh0UG5+RzN0NEFNT1FKREt0SWpwNVNhT2dwUUUzZFNIVGxnVlhLLWRxYTJOOGhmTXlrTUlVLXg2NFByZXNURHBEMVpRUlZRX18mS2V5LVBhaXItSWQ9SzE0TFpDWjlRVUk0SkwiXX0=","albumReplayGain":-9.97,"albumPeakAmplitude":0.999969,"trackReplayGain":-5.55,"trackPeakAmplitude":0.998291,"bitDepth":16,"sampleRate":44100},{"OriginalTrackUrl":"https://sp-pr-cf.audio.tidal.com/mediatracks/CAEaKRInMjEzYjY0ZTc3M2QzNmExMjMzYTYzYzI5MGI4MTFhNzRfNjEubXA0/0.flac?Expires=1712385304&Signature=CB35QHcikA0Bq8mv2XeqjsExNKnzd5Tzkm5vmWrol~j0UF-NHrJhBF78r3k-rPjEXyRrq~FuYQ-tZ5n657CMD7hdCEhxLTEWJX62JMNm0~HtX68wT~zEbxONcWaoi6SP-e1BZ0wWa5iS7uUW-n-hIDToOjW13m2KM-RGRs-72uJBlI~6HBFIHbWJzMlfYQLxYEygzcdlUjbwOcY2QIOJv6CJVOsoDNJU76b2GfGLecRXbJ~7z6nZnur4ityLSkVwrexvZwrwBW8o99TXtPn~G3t4AMOQJDKtIjp5SaOgpQE3dSHTlgVXK-dqa2N8hfMykMIU-x64PresTDpD1ZQRVQ__&Key-Pair-Id=K14LZCZ9QUI4JL"}].json()




def Download_song(song_response):
    with open(f"{artist['name']} - {song['name']}.flac", "wb") as f:
        f.write(requests.get(song_response[2]['OriginalTrackUrl']).content)

Download_song(song_response)
