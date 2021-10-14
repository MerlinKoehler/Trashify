import cv2

# Camera Settings
cameraAutodetect = False
resolution = "FullHD"  # 'FullHD', 'HD', 'SD'
cameraID = 0  # Camera device index (only when camera autodetect is off)
cameraFps = 30

# Setting resolutions
if resolution == "FullHD":
    width, height = 1920, 1080
elif resolution == "HD":
    width, height = 1280, 720
elif resolution == "SD":
    width, height = 1024, 576


# Convert from fourcc numerical code to fourcc string character code
def decode_fourcc(cc):
    """
    :param cc: fourcc numerical code
    :return: fourcc string character code
    """
    return "".join([chr((int(cc) >> 8 * i) & 0xFF) for i in range(4)])


# Init camera
def cameraStart():
    """
    :return: video input
    """
    if cameraAutodetect:
        camera = cv2.VideoCapture(0, cv2.CAP_ANY)
    else:
        camera = cv2.VideoCapture(cameraID, cv2.CAP_DSHOW)
    camera.set(3, width)
    camera.set(4, height)
    camera.set(5, cameraFps)
    camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    print("Camera backend:", camera.getBackendName())
    print("Codec:", decode_fourcc(camera.get(6)))
    return camera
