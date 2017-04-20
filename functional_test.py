'''
Created on 2017年3月30日

@author: xixi
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from pydoc import browse

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn("To-Do", self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", head_text)
#伊迪丝听说有一个很酷的在线待办事项应用
#她去看了这个应用的首页



#她注意到网页的标题和头部都包含“To-Do”这个词



#应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
#她在一个文本框中输入了“Buy peacock feathers”
#伊迪丝的爱好是使用假蝇做钓饵
        inputbox.send_keys('Buy peacock feathers')

#她按回车键后，页面刷新了
#待办事项表格中显示了“1：Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1：Buy peacock feathers' for row in rows))
        self.fail('Finish the test!')


#页面中又显示了一个输入框，可以输入其他的待办事项
#她输入“Use peacock feathers to make a fly”（使用孔雀羽毛做假蝇）
#伊迪丝做事很有条理

#伊迪丝再次刷新，她的清单中显示了两个待办事项

#伊迪丝想知道这个网站是否会记住她的待办事项
#她看到网站为她生成了唯一的URL
#而且页面中有一些文字解说这个功能

#她访问那个URL，发现待办事项还在

#她很满意，睡觉去了
if __name__ == '__main__':
    unittest.main(warnings = 'ignore')
