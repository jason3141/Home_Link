# -*- coding: utf-8 -*-

import base64 


class ProxyMiddleware(object): 
	def process_request(self, request, spider):
		request.meta['proxy'] = 'http://naannawsg01-v.asce.corp.bshg.com:8082'
		proxy_user_pass = "CZH\NAA-RGC-EDIX:(ijn0okm"
		encoded_user_pass = base64.encodestring(proxy_user_pass)
		request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass