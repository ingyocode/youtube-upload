if [ -n "$1" ]; then
  if [ -e "$1" ]; then
    python upload_video.py --title="$(date '+대한민국 %Y년 %m월 %d일 #오늘날씨 #날씨')" \
      --description="$(date '+대한민국 %Y년 %m월 %d일')" \
      --privacyStatus="public" \
      --tokenFile="$1"
    
    else 
      echo "Invalid file path"
  fi

  else
    echo "input your token file path - ./upload.sh [TOKEN_FILE_PATH]"
fi
