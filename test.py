x = [{"sensor mode": "ff", "resolution": "dci4k", "codec": "xavci", "chroma subsampling": 422, "bit depth": 10,
      "frame rate": 50, "bitrate": 500, "file format": "mxf"},
     {"sensor mode": "ff", "resolution": "uhd", "codec": "xavci", "chroma subsampling": 422, "bit depth": 10,
      "frame rate": 25, "bitrate": 250, "file format": "mxf"}]

for i in x:
    for k, v in i.items():
        print(k, v, sep=': ')

# for i in x:
#     print(type(i))