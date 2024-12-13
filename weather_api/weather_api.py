#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file weather_api.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
import requests
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import json




# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
weather_api_spec = ["implementation_id", "weather_api", 
         "type_name",         "weather_api", 
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
# @class weather_api
# @brief ModuleDescription
# 
# 
# </rtc-template>
class weather_api(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_date_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._date_inIn = OpenRTM_aist.InPort("date_in", self._d_date_in)
        self._d_spot_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._spot_inIn = OpenRTM_aist.InPort("spot_in", self._d_spot_in)
        self._d_mtmn_out = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._mtmn_outOut = OpenRTM_aist.OutPort("mtmn_out", self._d_mtmn_out)


		


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
        self.addInPort("date_in",self._date_inIn)
        self.addInPort("spot_in",self._spot_inIn)
		
        # Set OutPort buffers
        self.addOutPort("mtmn_out",self._mtmn_outOut)
		
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
        date = self._d_date_in.data
        spot = self._d_spot_in.data

        #OpenWeatherMap APIから天気情報を取得
        weather_info = get_weather_info(date,spot)

        #天気情報を次のコンポーネントに送信
        self._d_mtmn_out.data = weather_info
        self._mtmn_outOut.write()
    
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
	


def get_weather_info(date,spot):
    ApiKey = "apitoken" 
    api = "http://api.openweathermap.org/data/2.5/forecast?units=metric&q={city}&appid={key}"
    url = api.format(city = spot, key = ApiKey)
    response = requests.get(url)
    data = response.json()
    jsonText = json.dumps(data, indent=4)
    for entry in data["list"]:
        date_text = entry["dt_txt"]
        if date in date_text and "12:00" in date_text:
            return entry["weather"][0]["description"]



def weather_apiInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=weather_api_spec)
    manager.registerFactory(profile,
                            weather_api,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    weather_apiInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("weather_api" + args)

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

