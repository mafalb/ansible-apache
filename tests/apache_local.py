# -*- coding: utf-8 -*-
import requests

def test_apache_is_installed(host):
    apache = host.package("httpd")
    assert apache.is_installed
    assert apache.version.startswith("2.4")

def test_apache_running_and_enabled(host):
    apache = host.service("httpd")
    assert apache.is_running

def test_requests_get():
    r = requests.get('http://localhost/')
    assert r.status_code == 200
