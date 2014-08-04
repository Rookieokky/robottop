/mjpg_streamer -i "./input_uvc.so -n -f 15 -r 1280x960 -d /dev/video0" -o "./output_http.so -n -p 8080 -w ./www"
