#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file spotmtmn_get.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
spotmtmn_get_spec = ["implementation_id", "spotmtmn_get", 
         "type_name",         "spotmtmn_get", 
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
# @class spotmtmn_get
# @brief ModuleDescription
# 
# 
# </rtc-template>
class spotmtmn_get(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_spot_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._spot_inIn = OpenRTM_aist.InPort("spot_in", self._d_spot_in)
        self._d_mtmn_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._mtmn_inIn = OpenRTM_aist.InPort("mtmn_in", self._d_mtmn_in)
        self._d_spotmtmn_out = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._spotmtmn_outOut = OpenRTM_aist.OutPort("spotmtmn_out", self._d_spotmtmn_out)


		


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
        self.addInPort("spot_in",self._spot_inIn)
        self.addInPort("mtmn_in",self._mtmn_inIn)
		
        # Set OutPort buffers
        self.addOutPort("spotmtmn_out",self._spotmtmn_outOut)
		
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
    def onExecute(self, ec_id,):
        if self._mtmn_inIn.isNew():
            mtmn_message = self._mtmn_inIn.read().data
            update_items_from_messaging_api_component(mtmn_message)

        if self._spot_inIn.isNew():
            spot_message = self._spot_inIn.read().data
            spot_location = spot_message

            if spot_location in location_items:
                items = location_items[spot_location]
                combined_message = ', '.join(items)
                self._d_spotmtmn_out.data = combined_message
                self._spotmtmn_outOut.write()
            else:
                error_message = f"{spot_location}に対応する持ち物は見つかりませんでした。"
                print(error_message)
 
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

# 持ち物リストの保存用辞書
location_items = {}
	
def update_items_from_messaging_api_component(message):
    try:
        location, items = message.split(':', 1)
        items = set(items.split(','))#重複防止のためにset式に
        if location in location_items:
            location_items[location].update(items) # 既存のアイテムリストに追加 
        else:
            location_items[location] = items
        print(f"Updated items for {location}: {items}")
    except ValueError:
        print("エラー: メッセージの形式が無効です")

def add_item_via_messaging_api(location, item,):
    # LINEメッセージを通じて持ち物を追加
    if location in location_items:
        location_items[location].append(item)
    else:
        location_items[location] = [item]
    
def delete_item_via_messaging_api(location, item):
    # LINEメッセージを通じて持ち物を削除
    if location in location_items and item in location_items[location]:
        location_items[location].remove(item)

def process_message(message): 
    command, location, items_str = message.split(':') 
    items = items_str.split(',')
    if command == "追加": 
        update_items_from_messaging_api_component(f"{location}:{items_str}") 
    elif command == "削除": 
        for item in items: 
            delete_item_via_messaging_api(location, item) 
        else: 
            print(f"無効なコマンド: {command}")



def spotmtmn_getInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=spotmtmn_get_spec)
    manager.registerFactory(profile,
                            spotmtmn_get,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    spotmtmn_getInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("spotmtmn_get" + args)

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

