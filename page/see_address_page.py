from common.base import Base  # 导入Base类
from time import sleep


class See_address(Base):
    """封装定位器"""
    personal_loc = ("id", "com.insthub.ecmobile:id/toolbar_tabfour")  # 定位个人中心
    login_loc = ("id", "com.insthub.ecmobile:id/profile_head_photo")  # 定位登录
    username_loc = ("xpath", "//*[@text='用户名']")  # 定位用户名输入框
    password_loc = ("id", "com.insthub.ecmobile:id/login_password")  # 定位密码输入框
    button_loc = ("xpath", "//*[@text='登录']")  # 定位登录按钮
    address_loc = ("xpath", "//*[@text='收货地址管理']")  # 定位收货地址管理

    def click_personal(self):
        """点击个人中心"""
        self.click(self.personal_loc)

    def click_login(self):
        """点击登录"""
        self.click(self.login_loc)

    def input_username(self, username):
        """输入用户名"""
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        """输入密码"""
        self.send_keys(self.password_loc, password)

    def click_button(self):
        """点击登录按钮"""
        self.click(self.button_loc)

    def click_address(self):
        """点击收货地址管理"""
        self.click(self.address_loc)


if __name__ == '__main__':
    from common.base import open_app

    driver = open_app()
    addr = See_address(driver)
    sleep(2)
    # 点击个人中心
    addr.click_personal()
    sleep(2)
    # 点击登录
    addr.click_login()
    # 输入用户名
    username = "yuanma"
    addr.input_username(username)
    # 输入密码
    password = "123456"
    addr.input_password(password)
    # 点击登录按钮
    addr.click_button()
    # 点击收货管理
    addr.click_address()
    # 关闭app
    driver.quit()
