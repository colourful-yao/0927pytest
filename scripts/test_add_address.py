from page.add_address_page import Add_address
from common.base import Base


def test_add_address(driver_init):
    """测试添加收货地址的正确性"""
    add = Add_address(driver_init)
    # 点击收货管理
    add.click_address()
    # 点击右上角添加地址按钮
    add.click_add_button()
    # 输入收货人姓名
    consignee = "王五"
    add.input_consignee(consignee)
    # 输入电话号码
    mobile = "13312341234"
    add.input_mobile(mobile)
    # 输入邮政编码
    postal = "610000"
    add.input_postal(postal)
    # 点击所在地区
    add.click_region()
    # 点击国家
    add.click_country()
    # 点击省
    base = Base(driver_init)
    base.swipe_up()
    add.click_province()
    # 点击市
    add.click_city()
    # 点击区
    add.click_area()
    # 输入详细地址
    detailed_address = "天府新区"
    add.input_detailed_address(detailed_address)
    # 点击添加地址按钮
    add.click_add_buttons()
    assert True


def test_see_address_list(driver_init):
    """测试查看收货地址列表"""
    add = Add_address(driver_init)
    # 点击收货管理
    add.click_address()


def test_modify_address(driver_init):
    """测试修改收货地址的正确性"""
    add = Add_address(driver_init)
    # 点击收货管理
    add.click_address()
    # 点击选择修改的收货地址
    add.click_modify_address()
    # 输入修改的收货人姓名
    newconsignee = "李四"
    add.input_newconsignee(newconsignee)
    # 输入修改的电话号码
    newmobile = "13312341234"
    add.input_newmobile(newmobile)
    # 输入修改的邮箱
    newemail = "lisi123@qq.com"
    add.input_newemail(newemail)
    # 输入修改的邮政编码
    newpostal = "614000"
    add.input_newpostal(newpostal)
    # 点击所在地区
    add.click_newregion()
    # 点击修改的国家
    add.click_newcountry()
    # 点击修改的省
    base = Base(driver_init)
    base.swipe_up()
    add.click_newprovince()
    # 点击修改的市
    add.click_newcity()
    # 点击修改的区
    add.click_newarea()
    # 输入修改的详细地址
    newdetailed_address = "上城"
    add.input_newdetailed_address(newdetailed_address)
    # 点击添加保存按钮
    add.click_preservation()
    assert True


def test_delete_address(driver_init):
    """测试收货地址删除的正确性"""
    add = Add_address(driver_init)
    # 点击收货管理
    add.click_address()
    # 点击选择删除的收货地址
    add.click_receiving_address()
    # 点击删除按钮
    add.click_delete_button()
