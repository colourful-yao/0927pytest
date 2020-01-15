from common.base import Base  # 导入Base类
from time import sleep


class Shopping(Base):
    """封装定位器"""
    personal_loc = ("id", "com.insthub.ecmobile:id/toolbar_tabfour")  # 定位个人中心
    login_loc = ("id", "com.insthub.ecmobile:id/profile_head_photo")  # 定位登录
    username_loc = ("xpath", "//*[@text='用户名']")  # 定位用户名输入框
    password_loc = ("id", "com.insthub.ecmobile:id/login_password")  # 定位密码输入框
    button_loc = ("xpath", "//*[@text='登录']")  # 定位登录按钮
    home_page_loc = ("id", "com.insthub.ecmobile:id/toolbar_tabone")  # 定位商城首页
    photo_loc = ("id", "com.insthub.ecmobile:id/good_cell_photo_two")  # 定位需要加入购物车的商品
    add_cart_loc = ("xpath", "//*[@text='加入购物车']")  # 定位加入购物车按钮
    cart_pattern_loc = ("id", "com.insthub.ecmobile: id / good_detail_shopping_cart")  # 定位购物车图案
    settlement_loc = ("xpath", "//*[@text='结算']")  # 定位结算按钮
    payment_loc = ("xpath", "//*[@text='支付方式']")  # 定位支付方式按钮
    alipay_loc = ("xpath", "//*[@text='支付宝']")  # 定位支付宝按钮
    delivery_loc = ("xpath", "//*[@text='配送方式']")  # 定位配送方式按钮
    sto_loc = ("xpath", "//*[@text='申通快递']")  # 定位申通快递按钮
    submission_loc = ("xpath", "//*[@text='提交订单']")  # 定位提交订单按钮
    determine_loc = ("xpath", "//*[@text='确定']")  # 定位确定按钮
    pay_loc = ("xpath", "//*[@text='支付宝支付']")  # 定位支付宝支付按钮
    modify_loc = ("xpath", "//*[@text='修改']")  # 定位修改按钮
    remove_loc = ("xpath", "//*[@text='移除']")  # 定位移除按钮
    determine2_loc = ("id", "com.insthub.ecmobile:id/yes")  # 定位移除的确定按钮


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

    def click_home_page(self):
        """点击商城首页"""
        self.click(self.home_page_loc)

    def click_photo(self):
        """点击要购买的商品"""
        self.click(self.photo_loc)

    def click_add_cart(self):
        """点击加入购物车按钮"""
        self.click(self.add_cart_loc)

    def click_cart_pattern(self):
        """点击购物车图案"""
        self.click(self.cart_pattern_loc)

    def click_payment(self):
        """点击支付方式按钮"""
        self.click(self.payment_loc)

    def click_alipay(self):
        """点击支付宝"""
        self.click(self.alipay_loc)

    def click_delivery(self):
        """点击配送方式"""
        self.click(self.delivery_loc)

    def click_sto(self):
        """点击申通方式配送"""
        self.click(self.sto_loc)

    def click_submission(self):
        """点击提交按钮"""
        self.click(self.submission_loc)

    def click_determine(self):
        """点击确定按钮"""
        self.click(self.determine_loc)

    def click_pay(self):
        """点击支付宝支付"""
        self.click(self.pay_loc)

    def click_modify(self):
        """点击修改"""
        self.click(self.modify_loc)

    def click_remove(self):
        """点击移除"""
        self.click(self.remove_loc)

    def click_determin2(self):
        self.click(self.determine2_loc)
