import pytest
from dz2 import get_info, new_folder,delete_folder


def test_new_folder():
    assert get_info(ya_token= 'AQAAAAAgsrE-AADLW8se8WiLSEWUhO9H3-tfWZM', folder_name='test_3') == 'Папки не существует'
    assert new_folder(ya_token='AQAAAAAgsrE-AADLW8se8WiLSEWUhO9H3-tfWZM', folder_name='test_3') == 201
    assert get_info(ya_token='AQAAAAAgsrE-AADLW8se8WiLSEWUhO9H3-tfWZM', folder_name='test_3') == 200
    assert delete_folder(ya_token='AQAAAAAgsrE-AADLW8se8WiLSEWUhO9H3-tfWZM', folder_name='test_3') == 204

