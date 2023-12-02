import pytest

from ..business_page.home_page import HomePage
from ..business_page.contact_us_page import ContactUsPage
from common.file_handler import read_yaml
from common.path import get_project_root, get_upload_path

data_path = get_project_root('TestCase', 'test_contact_us_data.yaml')
upload_path = get_upload_path('upload.txt')


@pytest.mark.parametrize("test_input", read_yaml(data_path)['contact_us'])
def test_user_login(init_login, test_input):
    name = test_input['name']
    email = test_input['email']
    subject = test_input['subject']
    message = test_input['message']
    upload_file = upload_path
    contact_us_page = ContactUsPage(init_login)
    home_page = HomePage(init_login)
    home_page.click_contact()
    assert init_login.title == 'Automation Exercise - Contact Us'
    contact_us_page.input_name(name)
    contact_us_page.input_email(email)
    contact_us_page.input_subject(subject)
    contact_us_page.input_message(message)
    print(upload_file)
    print(str(upload_file))
    contact_us_page.choose_file(str(upload_file))
    contact_us_page.click_submit()
    init_login.switch_to.alert.accept()
    assert contact_us_page.is_success()

