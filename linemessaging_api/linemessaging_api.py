#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file linemessaging_api.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

import os
import re
import requests
import json
from flask import Flask, abort, request
from pprint import pprint
from datetime import datetime
from linebot.v3.webhook import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
import requests
import webbrowser
import os
import json


# Import RTM module
import RTC
import OpenRTM_aist

from flask import Flask, redirect, url_for, abort, request

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CREDENTIALS_FILE='CREDENTIALS_FILE'
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
calendar_service = build('calendar', 'v3', credentials=credentials)
CLIENT_SECRETS_FILE='CLIENT_SECRETS_FILE'



#チャンネルシークレット設定
handler = WebhookHandler('handler') 
#アクセストークン設定
configuration = Configuration(access_token='access_token') 
app = Flask(__name__)
app.debug = False

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# This module's spesification
# <rtc-template block="module_spec">
linemessaging_api_spec = ["implementation_id", "linemessaging_api", 
         "type_name",         "linemessaging_api", 
         "description",       "ModuleDescription", 
         "version",           "1.0.0", 
         "vendor",            "Ayaka", 
         "category",          "Category", 
         "activity_type",     "STATIC", 
         "max_instance",      "1", 
         "language",          "Python", 
         "lang_type",         "SCRIPT",
         ""]
# </rtc-template>

# <rtc-template block="component_description">
##
# @class linemessaging_api
# @brief ModuleDescription
# 
# 
# </rtc-template>
class linemessaging_api(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_daymtmn_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        self._daymtmn_inIn = OpenRTM_aist.InPort("daymtmn_in", self._d_daymtmn_in)
        self._d_spotmtmn_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        self._spotmtmn_inIn = OpenRTM_aist.InPort("spotmtmn_in", self._d_spotmtmn_in)
        self._d_weathermtmn_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        self._weathermtmn_inIn = OpenRTM_aist.InPort("weathermtmn_in", self._d_weathermtmn_in)
        self._d_message_out = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        self._message_outOut = OpenRTM_aist.OutPort("message_out", self._d_message_out)
        self._d_daymtmncombo_out = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        self._daymtmncombo_outOut = OpenRTM_aist.OutPort("daymtmncombo_out", self._d_daymtmncombo_out)
        self._d_spotmtmncombo_out = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        self._spotmtmncombo_outOut = OpenRTM_aist.OutPort("spotmtmncombo_out", self._d_spotmtmncombo_out)


		


        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
		
        # </rtc-template>


		 
    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # 
    # @return RTC::ReturnCode_t
    # 
    #
    def onInitialize(self):
        # Bind variables and configuration variable
		
        # Set InPort buffers
        self.addInPort("daymtmn_in",self._daymtmn_inIn)
        self.addInPort("spotmtmn_in",self._spotmtmn_inIn)
        self.addInPort("weathermtmn_in",self._weathermtmn_inIn)
		
        # Set OutPort buffers
        self.addOutPort("message_out",self._message_outOut)
        self.addOutPort("daymtmncombo_out",self._daymtmncombo_outOut)
        self.addOutPort("spotmtmncombo_out",self._spotmtmncombo_outOut)
		
        # Set service provider to Ports
		
        # Set service consumers to Ports
		
        # Set CORBA Service Ports
	
    	
        return RTC.RTC_OK
	
    ###
    ## 
    ## The finalize action (on ALIVE->END transition)
    ## 
    ## @return RTC::ReturnCode_t
    #
    ## 
    #def onFinalize(self):
    #

    #    return RTC.RTC_OK
	
    ###
    ##
    ## The startup action when ExecutionContext startup
    ## 
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onStartup(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The shutdown action when ExecutionContext stop
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onShutdown(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The activated action (Active state entry action)
    ##
    ## @param ec_id target ExecutionContext Id
    ## 
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onActivated(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The deactivated action (Active state exit action)
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onDeactivated(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ##
    #
    # The execution action that is invoked periodically
    #
    # @param ec_id target ExecutionContext Id
    #
    # @return RTC::ReturnCode_t
    #
    #

    
    

    @handler.add(MessageEvent, message=TextMessageContent)
    def handle_message(self,event):
        with ApiClient(configuration) as api_client:
            #相手の送信した内容で条件分岐して回答を変数に代入
            user_message = event.message.text
            # 日付パターン（例: 2024-12-25）
            date_pattern = r'(\d{4})-(\d{1,2})-(\d{1,2})'
            # 曜日パターン
            weekday_pattern = r'(月曜日|火曜日|水曜日|木曜日|金曜日|土曜日|日曜日)'
            # 日本語の曜日を英語に変換する辞書
            weekday_translation = {
        '月曜日': 'Monday',
        '火曜日': 'Tuesday',
        '水曜日': 'Wednesday',
        '木曜日': 'Thursday',
        '金曜日': 'Friday',
        '土曜日': 'Saturday',
        '日曜日': 'Sunday'
    }
        
            # メッセージが日付なのかをチェック
            date_match = re.search(date_pattern, user_message)
            if date_match:
                date_info = date_match.group(0) # YYYY-MM-DD形式で保持 
                self._d_message_out.data = self.date_info 
                self._message_outOut.write()
                if self._daymtmn_inIn.isNew():
                    data = self._daymtmn_inIn.read()
                    self.day_item = data.data

                if self._spotmtmn_inIn.isNew():
                    data = self._spotmtmn_inIn.read()
                    self.spot_item = data.data

                if self._weathermtmn_inIn.isNew():
                    data = self._weathermtmn_inIn.read()
                    self.weather_item = data.data
                
                # メッセージの生成と送信
                msg = f"{date_info}\n持ち物：{self.weather_item}, {self.spot_item}, {self.day_item}"
                msg = f"{date_info}を確認しました。"
            
            
            else:
            # メッセージが曜日なのかをチェック
                weekday_match = re.search(weekday_pattern, user_message)
                if weekday_match:
                    weekday_jp = weekday_match.group(1)
                    weekday = weekday_translation.get(weekday_jp, weekday_jp)  # 日本語の曜日を英語に変換
                    combo_info = user_message.replace(weekday_jp,weekday)
                    msg = f"{combo_info}を保存しました。"
                    self._d_daymtmncombo_out.data = combo_info
                    self._daymtmncombo_outOut.write()
                
                else:
                    # 日付でも曜日でもない場合
                    self._d_spotmtmncombo_out.data = user_message
                    self._spotmtmncombo_outOut.write()
                    msg = f"{user_message}を保存しました。"

            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=msg)]
                )
            )
    
  
    
    
    def onExecute(self, ec_id):
        return RTC.RTC_OK

    ###
    ##
    ## The aborting action when main logic error occurred.
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onAborting(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The error action in ERROR state
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onError(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The reset action that is invoked resetting
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onReset(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The state update action that is invoked after onExecute() action
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##

    ##
    #def onStateUpdate(self, ec_id):
    #
    #    return RTC.RTC_OK
	
    ###
    ##
    ## The action that is invoked when execution context's rate is changed
    ##
    ## @param ec_id target ExecutionContext Id
    ##
    ## @return RTC::ReturnCode_t
    ##
    ##
    #def onRateChanged(self, ec_id):
    #
    #    return RTC.RTC_OK



def linemessaging_apiInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=linemessaging_api_spec)
    manager.registerFactory(profile,
                            linemessaging_api,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    linemessaging_apiInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("linemessaging_api" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
