import math
def step(sensor_value, nearest, farthest, steps):
    """
    docstring センサーの値をドレミの音にする
        :param sensor_value: センサーの値
        :param nearest: センサーに最も近いときの値
        :param farthest: センサーに最も遠いときの値
        :param steps: 分割数。ピアノでいうとC3からC4まで白鍵黒鍵合わせて12
    """
    width = abs(nearest - farthest) / steps
    step = math.floor(abs(nearest - sensor_value) / width)
    return step
