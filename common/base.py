from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 配置启动参数
def open_app():
    desired_caps = {
        "platformName": "Android",  # 操作系统
        "platformVersion": "5.1.1",  # 系统版本
        "deviceName": "127.0.0.1:21503",  # 设备信息
        "appPackage": "com.insthub.ecmobile",  # app包名
        "appActivity": ".activity.EcmobileMainActivity",  # app启动名
        "unicodeKeyboard": True,  # 启动Unicode输入法,当为True,表示允许输入中文
        # "noReset": True,  # 不重置应用--实现免登录
    }
    # 启动app
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver


class Base:
    def __init__(self, driver):
        self.driver = driver
        # 获取手机屏幕大小(分辨率)
        size = self.driver.get_window_size()
        self.width = size["width"]  # 获取手机宽度
        self.height = size["height"]  # 获取手机高度

    def swipe_up(self, time=5000):
        """
        向上滑动:y坐标从大到小
        :return:
        """
        x = self.width * 0.5
        start_y = self.height * 0.75  # y坐标起始值
        end_y = self.height * 0.25  # y坐标终止值
        self.driver.swipe(x, start_y, x, end_y, duration=time)

    def swipe_down(self, time=5000):
        """
        向下滑动:y坐标从小到大
        :return:
        """
        x = self.width * 0.5
        start_y = self.height * 0.25  # y坐标起始值
        end_y = self.height * 0.75  # y坐标终止值
        self.driver.swipe(x, start_y, x, end_y, duration=time)

    def swipe_left(self, time=5000):
        """
        向左滑动:x坐标从大到小
        :return:
        """
        start_x = self.width * 0.75  # x起始位置
        end_x = self.width * 0.25  # x终止位置
        y = self.height * 0.5
        self.driver.swipe(start_x, y, end_x, y, duration=time)

    def swipe_right(self, time=5000):
        """
        向右滑动:x坐标从小到大
        :return:
        """
        start_x = self.width * 0.25  # x起始位置
        end_x = self.width * 0.75  # x终止位置
        y = self.height * 0.5
        self.driver.swipe(start_x, y, end_x, y, duration=time)

    def find_element(self, locator: tuple = None, timeout=10):
        """
        定位元素,定位单个元素,如果找到元素返回元素本身,没找到返回False
        :param locator: 定位器 例如("class name","class属性值")
        :return: element
        EC.presence_of_element_located(locator)  # 元素定位方法
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")
            return False

    def find_elements(self, locator, timeout=10):
        """
        定位一组元素,如果找打,返回一组元素,反之返回False
        :param locator: 定位器
        :param timeout: 最大等待时间
        :return: elements
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return element
        except:
            print(f"元素{locator}没找到")
            return False

    def click(self, locator):
        """
        元素点击
        :return:
        """
        element = self.find_element(locator)  # 找元素
        element.click()  # 点击元素

    def send_keys(self, locator, text):
        """
        元素输入
        :param locator: 定位器
        :param text: 输入内容
        :return:
        """
        element = self.find_element(locator)  # 找元素
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断给定的文本是否在元素中,如果在返回True,如果不在返回False
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            # print("元素没找到")
            return False

    def get_element_text(self, locator):
        """
        获取元素文本
        :return:
        """
        try:
            element = self.find_element(locator)
            return element.text
        except:
            return False
