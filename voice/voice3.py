import wave
from pyaudio import PyAudio, paInt16  # 导入用于音频处理的库
from aip import AipSpeech  # 导入百度语音识别库
import string
import re

# 设置采样参数
NUM_SAMPLES = 2000  # 单次采样的样本数量
TIME = 3  # 录音时间（秒）

# # 百度智能云平台语音技能密钥
# BaiduAPP_ID = '57883775'
# BaiduAPI_KEY = 'UbVpkCWd9Qy5Q1NMRxdObf37'
# SECRET_KEY = 'qaiCCKQ9oTTOjEM8ii97tiA1UuYFyTqa'
# client = AipSpeech(BaiduAPP_ID, BaiduAPI_KEY, SECRET_KEY)

BaiduAPP_ID = '74994563'
BaiduAPI_KEY = 'IryJywKAF3KDlTy0EZkkUApm'
SECRET_KEY = 'wg0IVFhOTm5tylMbfiDtYCiOGlihN94z'
client = AipSpeech(BaiduAPP_ID, BaiduAPI_KEY, SECRET_KEY)

# 定义录音函数，直接返回音频数据
def record():
    # print('------Start recording.')
    pa = PyAudio()  # 创建PyAudio对象
    # 开启声音输入流
    stream = pa.open(format=paInt16,
                     channels=1,
                     rate=16000,
                     input=True,
                     frames_per_buffer=NUM_SAMPLES)
    audioBuffer = []  # 存储所有录音数据的列表
    # print('------开始录音')
    count = 0
    while count < TIME*10:  # 控制录音时间
        string_audio_data = stream.read(NUM_SAMPLES)  # 读取音频数据
        audioBuffer.append(string_audio_data)  # 将读取的数据添加到列表中
        count += 1
        # print('.', end='')  # 进度显示
    # print('')
    # print('------End recording.')
    stream.close()  # 关闭流
    return audioBuffer  # 返回录音数据



# 定义一个正则表达式模式，匹配所有标点
punctuation_pattern = r'[^\w\s]'


# 语音识别函数，直接使用音频数据
def asr_updata(audio_data):
    audio_content = b''.join(audio_data)  # 将音频数据片段合并为一个音频流
    # print('调api')
    # 调用百度语音识别API，关闭标点符号识别
    result = client.asr(audio_content, 'wav', 16000, {
                        'dev_pid': 1537,  # 设置语音识别的模型参数，这里使用普通话
                        'punctuation': 0  # 设置为0，不返回标点符号
                     })

    # print(result)  # 输出识别结果的原始输出，以便调试
    if 'result' in result.keys():
        result_text = result["result"][0]  # 从识别结果中获取转换后的文本
        # print(result)
        # print(result_text)
        # 使用 re.sub 方法去除所有匹配到的标点
        result_text = re.sub(punctuation_pattern, '', result_text)
    else:
        result_text = '语音未识别'  # 识别失败时的输出
    return result_text


if __name__ == '__main__':
    print('------代码运行')
    audio_data = record()  # 调用录音函数并获取音频数据
    print('------开始识别')
    result_text = asr_updata(audio_data)  # 使用音频数据进行语音识别
    print('------识别结束')
    print("result_text")  # 打印识别得到的文本
