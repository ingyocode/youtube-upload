if [ "$#" = 2 ]; then
  if [ -e "$1" ]; then
    python auth.py --clientSecret="$1" \
      --tokenFile="$2"
    
    else 
      echo "Invalid file path"
  fi

  else
    echo "input params - ./create-token.sh [YOUR_CLIENT_SECRET_FILE] [TOKEN_FILE_NAME]"
fi
