import pytest
from documents import get_doc_owner_name, get_doc_shelf, add_new_doc, delete_doc

def test_get_doc_owner_name():
    assert get_doc_owner_name('11-2') == "Геннадий Покемонов"

def test_get_doc_shelf():
    assert get_doc_shelf('10006') == '2'

def test_add_new_doc():
    assert get_doc_shelf('777') != '1'
    add_new_doc('777', 'passport', 'Mikhail', '1')
    assert get_doc_shelf('777') == '1'

def test_delete_doc():
    assert get_doc_shelf('11-2') == '1'
    delete_doc('11-2')
    assert get_doc_shelf('11-2') != '1'