from scripts.read_files import readAndShowImage, readAndShowVideo
from scripts.utils import resize

from scripts.segmentation import applySegmentation

imagePath = 'data/image.jpg'
videoPath = 'data/video.mkv'

# readAndShowImage(imagePath, resize=resize, func=applySegmentation)
readAndShowVideo(videoPath, resize=resize, func=applySegmentation)