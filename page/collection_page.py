from common.base import Base  # 导入Base类
from time import sleep


class Collection(Base):
    """封装定位器"""
    personal_loc = ("id", "com.insthub.ecmobile:id/toolbar_tabfour")  # 定位个人中心
    login_loc = ("id", "com.insthub.ecmobile:id/profile_head_photo")  # 定位登录
    username_loc = ("xpath", "//*[@text='用户名']")  # 定位用户名输入框
    password_loc = ("id", "com.insthub.ecmobile:id/login_password")  # 定位密码输入框
    button_loc = ("xpath", "//*[@text='登录']")  # 定位登录按钮
    home_page_loc = ("id", "com.insthub.ecmobile:id/toolbar_tabone")  # 定位商城首页
    photo_loc = ("id", "com.insthub.ecmobile:id/good_cell_photo_one")  # 定位需要收藏的商品
    collection_loc = ("id", "com.insthub.ecmobile:id/collection_button")  # 定位收藏星星符号
    back_loc = ("id", "com.insthub.ecmobile:id/top_view_back")  # 定位返回按钮
    mycollocation_loc = ("xpath", "//*[@text='我的收藏']")  # 定位我的收藏
    edit_loc = ("xpath", "//*[@text='编辑']")  # 定位编辑
    delete_loc = ("id", "com.insthub.ecmobile:id/collect_item_remove1")  # 定位删除

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
        """点击收藏的商品"""
        self.click(self.photo_loc)

    def click_collection(self):
        """点击收藏符号"""
        self.click(self.collection_loc)

    def click_back(self):
        """点击返回按钮"""
        self.click(self.back_loc)

    def click_mycollocation(self):
        """点击我的收藏"""
        self.click(self.mycollocation_loc)

    def click_edit(self):
        """点击编辑"""
        self.click(self.edit_loc)

    def click_delete(self):
        """点击删除"""
        self.click(self.delete_loc)

if __name__ == '__main__':
    from common.base import open_app

    from common.base import open_app

    driver = open_app()
    addr = Collection(driver)
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