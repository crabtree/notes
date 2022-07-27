# ffmpeg

## Extract frames from movie file

```bash
ffmpeg -i moviefile.mp4 -r 1.0 img-%4d.jpg
```

- `-i moviefile.mp4` - movie file path
- `-r 1.0` - adjusting this parameter allows you to set the frequency of frames, 1.0 => 1 per second
- `img-%4d.jpg` - name of the extracted frames files, `%4d` generates 4-digit autoincrement numbers
