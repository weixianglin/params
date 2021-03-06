# coding: utf-8

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'djapp.settings'
import django
django.setup()

import pytest
import json
from django.test import Client
from params import InvalidParams
from params.compat import str_


def test_client():
    c = Client()
    resp = c.get('/')
    str_(resp.content) == 'GET'


def test_funcview():
    c = Client()

    with pytest.raises(InvalidParams):
        c.get('/func')

    resp = c.get('/func?a=1&b=x&b=y')
    print(resp.content)


def test_classview():
    c = Client()

    with pytest.raises(InvalidParams):
        c.get('/class')

    resp = c.get('/class?a=1')
    print(resp.content)


def test_jsonview():
    c = Client()

    # GET on json=True is not allowed
    with pytest.raises(ValueError):
        c.get('/json')

    d = {'a': 1}
    # InvalidParams: Could not parse body as json
    with pytest.raises(InvalidParams):
        c.post('/json', d)

    resp = c.post('/json', json.dumps(d), content_type='application/json')
    print(resp.content)

    d1 = {'a': 1, 'b': None}
    # InvalidParams: b type error
    with pytest.raises(InvalidParams):
        c.post('/json', json.dumps(d1), content_type='application/json')

    d1 = {'a': 1, 'b': ''}
    resp = c.post('/json', json.dumps(d1), content_type='application/json')
    print(resp.content)


def test_jsonlistview():
    c = Client()
    content_type = 'application/json'

    # GET on json=True is not allowed
    with pytest.raises(ValueError):
        c.get('/jsonlist')

    d = {'a': 1}
    # InvalidParams: request body must be of type list
    with pytest.raises(InvalidParams):
        c.post('/jsonlist', json.dumps(d), content_type=content_type)

    d = [{'a': 1}]
    resp = c.post('/jsonlist', json.dumps(d), content_type=content_type)
    print(resp.content)
