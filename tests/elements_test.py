import time
# import pdb

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            # text_box_page.fill_all_fields()
            # full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            # output_name, output_email, output_current_addr, output_perm_addr = text_box_page.check_field_form()
            input_result = text_box_page.fill_all_fields()
            output_result = text_box_page.check_field_form()
            time.sleep(5)
            # pdb.set_trace()
            assert input_result == output_result
            # assert full_name == output_name
            # assert email == output_email
            # assert current_address == output_current_addr
            # assert permanent_address == output_perm_addr
