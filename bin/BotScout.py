#! /usr/bin/python3

import pprint
import requests


class BotScout:
    def queryMulti(self, paramsName, paramsEmail, paramsIp):
        apiUrl = "http://botscout.com/test"
        params = {
            "multi": "",
            "name": paramsName,
            "mail": paramsEmail,
            "ip": paramsIp,
        }
        resp = requests.get(apiUrl, params=params)
        return resp


    def queryEmail(self, paramsEmail):
        apiUrl = "http://botscout.com/test"
        params = {"mail": paramsEmail}
        resp = requests.get(apiUrl, params=params)
        return resp


    def queryIp(self, paramsIp):
        apiUrl = "http://botscout.com/test"
        params = {"ip": paramsIp}
        resp = requests.get(apiUrl, params=params)
        return resp


    def queryName(self, paramsName):
        apiUrl = "http://botscout.com/test"
        params = {"name": paramsName}
        resp = requests.get(apiUrl, params=params)
        return resp


    def queryAll(self, resource):
        apiUrl = "http://botscout.com/test"
        params = {"all": resource}
        resp = requests.get(apiUrl, params=params)
        return resp


if __name__ == "__main__":
    classbs = BotScout()

    resp = classbs.queryMulti("krasnhello", "krasnhello@mail.ru", "84.16.230.111")
    print(resp.status_code)
    if resp.status_code == 200:
        print(resp.text)

    resp = classbs.queryEmail("krasnhello@mail.ru")
    print(resp.status_code)
    if resp.status_code == 200:
        print(resp.text)

    resp = classbs.queryIp("84.16.230.111")
    print(resp.status_code)
    if resp.status_code == 200:
        print(resp.text)

    resp = classbs.queryName("krasnhello")
    print(resp.status_code)
    if resp.status_code == 200:
        print(resp.text)

    resp = classbs.queryAll("krasnhello")
    print(resp.status_code)
    if resp.status_code == 200:
        print(resp.text)


"""
Reference URL
 - http://botscout.com
 - http://botscout.com/api.htm
"""
