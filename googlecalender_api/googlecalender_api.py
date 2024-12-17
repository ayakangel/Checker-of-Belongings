#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file googlecalender_api.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import datetime
sys.path.append(".")

import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import webbrowser

# Import RTM module
import RTC
import OpenRTM_aist




# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">

# </rtc-template>

# Google Calendar API設定
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE') 
# トークンファイルの保存場所
TOKEN_PATH = os.getenv('GOOGLE_TOKEN_PATH')


def authenticate_google():
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)

    # トークンが存在しない、もしくは無効な場合に認証を実施
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Chromeのパスを修正 (Windowsの場合)
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
            
            # webbrowserにChromeを登録
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=8080, browser='chrome')  # ポート番号を8080に変更

        # 新しいトークンを保存
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)
            

    return creds


# This module's spesification
# <rtc-template block="module_spec">
googlecalender_api_spec = ["implementation_id", "googlecalender_api", 
         "type_name",         "googlecalender_api", 
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
# @class googlecalender_api
# @brief ModuleDescription
# 
# 
# </rtc-template>
class googlecalender_api(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_message_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._message_inIn = OpenRTM_aist.InPort("message_in", self._d_message_in)
        self._d_dateday_out = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._dateday_outOut = OpenRTM_aist.OutPort("dateday_out", self._d_dateday_out)
        self._d_spot_out = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._spot_outOut = OpenRTM_aist.OutPort("spot_out", self._d_spot_out)

        

        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        self._config_credentials_file = [CREDENTIALS_FILE]
        self._config_token_path = [TOKEN_PATH]
        self.bindParameter("credentials_file", self._config_credentials_file, CREDENTIALS_FILE)
        self.bindParameter("token_path", self._config_token_path, TOKEN_PATH)

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
        self.addInPort("message_in",self._message_inIn)
		
        # Set OutPort buffers
        self.addOutPort("dateday_out",self._dateday_outOut)
        self.addOutPort("spot_out",self._spot_outOut)
        

        
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
    def onExecute(self, ec_id):
        if self._message_inIn.isNew():
            date_str = self._message_inIn.read().data  # 受信した日付情報（"YYYY-MM-DD"形式）
            # 'none' の場合、エラーメッセージを出力して処理を停止 
            if date_str == 'none': 
                self._d_dateday_out.data = RTC.TimedString(RTC.Time(0, 0), "this is not available") 
                self._d_spot_out.data = RTC.TimedString(RTC.Time(0, 0), "No location") 
                self._dateday_outOut.write() 
                self._spot_outOut.write()
                return
            # 日付フォーマットを検証 
            try: 
                datetime.datetime.strptime(date_str, '%Y-%m-%d') 
            except ValueError: 
                self._d_dateday_out.data = RTC.TimedString(RTC.Time(0, 0), "Invalid date format") 
                self._d_spot_out.data = RTC.TimedString(RTC.Time(0, 0), "No location") 
                self._dateday_outOut.write() 
                self._spot_outOut.write()

            # Google Calendarからイベント情報を取得
            credentials = authenticate_google(self._config_credentials_file[0], self._config_token_path[0])
            service = build('calendar', 'v3', credentials=credentials)
            start_of_day = date_str + 'T00:00:00Z'
            end_of_day = date_str + 'T23:59:59Z'

            events_result = service.events().list(
                calendarId='primary',
                timeMin=start_of_day,
                timeMax=end_of_day,
                singleEvents=True,
                orderBy='startTime'
            ).execute()

            events = events_result.get('items', [])

            if not events:
                self._d_dateday_out.data = RTC.TimedString(RTC.Time(0, 0), "No events")
                self._d_spot_out.data = RTC.TimedString(RTC.Time(0, 0), "No location")
            else:
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    location = event.get('location', "No location specified")

                    self._d_dateday_out.data = RTC.TimedString(RTC.Time(0, 0), start)
                    self._d_spot_out.data = RTC.TimedString(RTC.Time(0, 0), location)

                    # 出力ポートにデータを送信
                    self._dateday_outOut.write()
                    self._spot_outOut.write()

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
	



def googlecalender_apiInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=googlecalender_api_spec)
    manager.registerFactory(profile,
                            googlecalender_api,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    googlecalender_apiInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("googlecalender_api" + args)

def main():
    # remove --instance_name= option
    argv = [i for i in sys.argv if "--instance_name=" not in i]
    # Initialize manager
    mgr = OpenRTM_aist.Manager.init(argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()

