from common.base import Base  # 导入Base类
from time import sleep


class Add_address(Base):
    """封装定位器"""
    address_loc = ("xpath", "//*[@text='收货地址管理']")  # 定位收货地址管理
    add_button_loc = ("id", "com.insthub.ecmobile:id/address_manage_add")  # 定位右上角添加地址按钮
    consignee_loc = ("xpath", "//*[@text='收货人姓名（必填）']")  # 定位收货人姓名
    mobile_loc = ("xpath", "//*[@text='电话号码（必填）']")  # 定位电话号码
    postal_loc = ("xpath", "//*[@text='邮政编码']")  # 定位邮编
    region_loc = ("xpath", "//*[@text='所在地区']")  # 定位所在地区
    country_loc = ("xpath", "//*[@text='中国']")  # 定位国家
    province_loc = ("xpath", "//*[@text='四川省']")  # 定位省
    city_loc = ("xpath", "//*[@text='成都市']")  # 定位市
    area_loc = ("xpath", "//*[@text='武侯区']")  # 定位区
    detailed_address_loc = ("xpath", "//*[@text='详细地址（必填）']")  # 定位详细地址
    add_buttons_loc = ("id", "com.insthub.ecmobile:id/add_address_add")  # 定位添加地址按钮

    receiving_address_loc = ("xpath", "//*[@text='李四']")  # 定位选择删除的收货地址
    delete_button_loc = ("xpath", "//*[@text='删除地址']")  # 定位删除地址按钮

    modify_address_loc = ("xpath", "//*[@text='李四']")  # 定位选择修改的收货地址栏姓名
    newconsignee_loc = ("id", "com.insthub.ecmobile:id/address_manage2_name")  # 定位修改的收货人姓名
    newmobile_loc = ("id", "com.insthub.ecmobile:id/address_manage2_telNum")  # 定位修改的手机号
    newemail_loc = ("id", "com.insthub.ecmobile:id/address_manage2_email")  # 定位修改的邮箱
    newpostal_loc = ("id", "com.insthub.ecmobile:id/address_manage2_zipCode")  # 定位修改的邮编
    newregion_loc = ("id", "com.insthub.ecmobile:id/address_manage2_area")  # 定位修改的所在地区
    newcountry_loc = ("xpath", "//*[@text='中国']")  # 定位修改的国家
    newprovince_loc = ("xpath", "//*[@text='浙江省']")  # 定位修改的省
    newcity_loc = ("xpath", "//*[@text='杭州市']")  # 定位修改的市
    newarea_loc = ("xpath", "//*[@text='上城区']")  # 定位修改的区
    newdetailed_address_loc = ("id", "com.insthub.ecmobile:id/address_manage2_detail")  # 定位修改的详细地址
    preservation_loc = ("xpath", "//*[@text='保存']")  # 定位保存按钮



    def click_address(self):
        """点击收货地址管理"""
        self.click(self.address_loc)

    def click_add_button(self):
        """点击右上角添加收货地址按钮"""
        self.click(self.add_button_loc)

    def input_consignee(self, consignee):
        """输入收货人姓名"""
        self.send_keys(self.consignee_loc, consignee)

    def input_mobile(self, mobile):
        """输入电话号码"""
        self.send_keys(self.mobile_loc, mobile)

    def input_postal(self, postal):
        """输入邮政编码"""
        self.send_keys(self.postal_loc, postal)

    def click_region(self):
        """点击所在地区"""
        self.click(self.region_loc)

    def click_country(self):
        """点击国家"""
        self.click(self.country_loc)

    def click_province(self):
        """点击省"""
        self.click(self.province_loc)

    def click_city(self):
        """点击市"""
        self.click(self.city_loc)

    def click_area(self):
        """点击区"""
        self.click(self.area_loc)

    def input_detailed_address(self, detailed_address):
        """输入详细地址"""
        self.send_keys(self.detailed_address_loc, detailed_address)

    def click_add_buttons(self):
        """点击添加地址按钮"""
        self.click(self.add_buttons_loc)

    def click_receiving_address(self):
        """点击选择删除的地址"""
        self.click(self.receiving_address_loc)

    def click_delete_button(self):
        """点击删除按钮"""
        self.click(self.delete_button_loc)

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


