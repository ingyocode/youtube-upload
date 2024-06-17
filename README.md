1. create `client_secrets.json` file for downloading OAuth 2.0 Client
2. exec `auth.py` for creating `token.json`
3. now, you can upload by executing `upload_video.py` with file and params

available options

- file=${filePath}
- title=${youtube video title}
- description=${youtube video description}
- keywords=${youtube video keywords}
- category=${youtube video category}
- privacyStatus= "private" | "public"

example

```
python upload_video.py --file="result.mp4" \
--title="test upload" \
--description="test descriptions" \
--keywords="test, hot" \
--category="nature" \
--privacyStatus="public"
```
