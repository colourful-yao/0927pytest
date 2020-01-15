from common.base import Base  # 导入Base类
from time import sleep


class Modify_address(Base):
    """封装定位器"""
    personal_loc = ("id", "com.insthub.ecmobile:id/toolbar_tabfour")  # 定位个人中心
    login_loc = ("id", "com.insthub.ecmobile:id/profile_head_photo")  # 定位登录
    username_loc = ("xpath", "//*[@text='用户名']")  # 定位用户名输入框
    password_loc = ("id", "com.insthub.ecmobile:id/login_password")  # 定位密码输入框
    button_loc = ("xpath", "//*[@text='登录']")  # 定位登录按钮
    address_loc = ("xpath", "//*[@text='收货地址管理']")  # 定位收货地址管理
    modify_address_loc = ("xpath", "//*[@text='李四']")  # 定位选择修改的收货地址
    newconsignee_loc = ("id", "com.insthub.ecmobile:id/address_manage2_name")  # 定位修改的收货人姓名
    newmobile_loc = ("id", "com.insthub.ecmobile:id/address_manage2_telNum")  # 定位修改的手机号
    newemail_loc = ("id", "com.insthub.ecmobile:id/address_manage2_email")  # 定位修改的邮箱
    newpostal_loc = ("id", "com.insthub.ecmobile:id/address_manage2_zipCode")  # 定位修改的邮编
    newregion_loc = ("id", "com.insthub.ecmobile:id/address_manage2_area")  # 定位修改的所在地区
    newcountry_loc = ("xpath", "//*[@text='中国']")  # 定位修改的国家
    newprovince_loc = ("xpath", "//*[@text='浙江省']")  # 定位修改的省
    newcity_loc = ("xpath", "//*[@text='杭州市']")  # 定位修改的市
    newarea_loc = ("xpath", "//*[@text='下城区']")  # 定位修改的区
    newdetailed_address_loc = ("id", "com.insthub.ecmobile:id/address_manage2_detail")  # 定位修改的详细地址
    preservation_loc = ("xpath", "//*[@text='保存']")  # 定位保存按钮

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

    def click_modify_address(self):
        """点击选择修改的收货地址"""
        self.click(self.modify_address_loc)

    def input_newconsignee(self, newconsignee):
        """输入修改的收货人姓名"""
        self.send_keys(self.newconsignee_loc, newconsignee)

    def input_newmobile(self, newmobile):
        """输入修改的电话号码"""
        self.send_keys(self.newmobile_loc, newmobile)

    def input_newemail(self, newemail):
        """输入修改的邮箱"""
        self.send_keys(self.newemail_loc, newemail)

    def input_newpostal(self, newpostal):
        """输入修改的邮政编码"""
        self.send_keys(self.newpostal_loc, newpostal)

    def click_newregion(self):
        """点击所在地区"""
        self.click(self.newregion_loc)

    def click_newcountry(self):
        """点击修改的国家"""
        self.click(self.newcountry_loc)

    def click_newprovince(self):
        """点击修改的省"""
        self.click(self.newprovince_loc)

    def click_newcity(self):
        """点击修改的市"""
        self.click(self.newcity_loc)

    def click_newarea(self):
        """点击修改的区"""
        self.click(self.newarea_loc)

    def input_newdetailed_address(self, detailed_address):
        """输入修改的详细地址"""
        self.send_keys(self.newdetailed_address_loc, detailed_address)

    def click_preservation(self):
        """点击保存按钮"""
        self.click(self.preservation_loc)


if __name__ == '__main__':
    from common.base import open_app

    driver = open_app()
    addr = Modify_address(driver)
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
    # 点击选择修改的收货地址
    addr.click_modify_address()
    # 输入修改的收货人姓名
    newconsignee = "李四"
    addr.input_newconsignee(newconsignee)
    # 输入修改的电话号码
    newmobile = "13312341234"
    addr.input_newmobile(newmobile)
    # 输入修改的邮箱
    newemail = "lisi123@qq.com"
    addr.input_newemail(newemail)
    # 输入修改的邮政编码
    newpostal = "614000"
    addr.input_newpostal(newpostal)
    # 点击所在地区
    addr.click_newregion()
    # 点击修改的国家
    addr.click_newcountry()
    # 点击修改的省
    base = Base(driver)
    base.swipe_up()
    addr.click_newprovince()
    # 点击修改的市
    addr.click_newcity()
    # 点击修改的区
    addr.click_newarea()
    # 输入修改的详细地址
    newdetailed_address = "上城"
    addr.input_newdetailed_address(newdetailed_address)
    # 点击添加保存按钮
    addr.click_preservation()
    # # 关闭app
    driver.quit()
