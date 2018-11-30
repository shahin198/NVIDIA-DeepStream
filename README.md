# NVIDIA-DeepStream

https://developer.nvidia.com/embedded/deepstream-on-jetson-downloads

# Tutorial
https://devblogs.nvidia.com/accelerate-video-analytics-deepstream-2/

https://devblogs.nvidia.com/multi-camera-large-scale-iva-deepstream-sdk/

https://devblogs.nvidia.com/deepstream-video-analytics-smart-cities/

# install Gstreamer
https://gstreamer.freedesktop.org/documentation/installing/on-linux.html
```
apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools
```
# Run
```
nvgstiva-app -c ${HOME}/configs/PGIE-FP16-CarType-CarMake-CarColor.txt
nvgstiva-app -c ${HOME}/configs/PGIE-FP16-CarType-CarMake-CarColor.txt     -i /home/nvidia/sample_720p.mp4
```
# Gstreamer
https://gstreamer.freedesktop.org/features/
```

```
