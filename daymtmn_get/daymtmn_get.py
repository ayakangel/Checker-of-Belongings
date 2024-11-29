#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

# <rtc-template block="description">
"""
 @file daymtmn_get.py
 @brief ModuleDescription
 @date $Date$


"""
# </rtc-template>

import sys
import time
from datetime import datetime
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
daymtmn_get_spec = ["implementation_id", "daymtmn_get", 
         "type_name",         "daymtmn_get", 
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
# @class daymtmn_get
# @brief ModuleDescription
# 
# 
# </rtc-template>

class daymtmn_get(OpenRTM_aist.DataFlowComponentBase):
	
    ##
    # @brief constructor
    # @param manager Maneger Object
    # 
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_day_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._day_inIn = OpenRTM_aist.InPort("day_in", self._d_day_in)
        self._d_mtmn_in = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._mtmn_inIn = OpenRTM_aist.InPort("mtmn_in", self._d_mtmn_in)
        self._d_daymtmn_out = OpenRTM_aist.instantiateDataType(RTC.TimedString)
        """
        """
        self._daymtmn_outOut = OpenRTM_aist.OutPort("daymtmn_out", self._d_daymtmn_out)


		


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
        self.addInPort("day_in",self._day_inIn)
        self.addInPort("mtmn_in",self._mtmn_inIn)
		
        # Set OutPort buffers
        self.addOutPort("daymtmn_out",self._daymtmn_outOut)
		
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
     # Google Calendar APIコンポーネントから送られてきたメッセージ（仮のメッセージ）
      calendar_weekday = None

      if self._day_inIn.isNew():  # calendar_inInはGoogle Calendar APIからの曜日情報
        date_message = self._day_inIn.read().data
        calendar_weekday = convert_to_weekday(date_message)  # メッセージ形式が "曜日" の場合
        
      if self._mtmn_inIn.isNew(): 
        mtmn_message = self._mtmn_inIn.read().data 
        update_items_from_previous_component(mtmn_message) # 曜日に対する持ち物を更新

        # 曜日が一致するかどうかをチェック
        if calendar_weekday in weekday_items:
            items = weekday_items[calendar_weekday]
            combined_message = ', '.join(items)
            self._d_daymtmn_out.data = combined_message
            self._daymtmn_outOut.write()
        else:
            # 曜日が一致しない場合の処理（必要ならばエラーメッセージを送るなど）
            error_message = f"{calendar_weekday}に対応する持ち物は見つかりませんでした。"
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



def convert_to_weekday(self, iso_date):  # 追加: ISO 8601形式の日時を曜日に変換するメソッド
        date_obj = datetime.fromisoformat(iso_date)
        return date_obj.strftime('%A') 

weekday_items = {}

def update_items_from_previous_component(message):
    try:
        parts = message.split(':') 
        command = parts[0] 
        weekday = parts[1] 
        items = set(parts[2].split(',')) # セットに変換して重複を避ける

        if command == "追加": 
            if weekday in weekday_items: 
                weekday_items[weekday].update(items) # 既存のアイテムリストに追加 
            else: 
                weekday_items[weekday] = items # 新しいアイテムリストを作成 
                print(f"Added items {items} to {weekday}") 
                
        elif command == "削除": 
            for item in items: 
                delete_item_via_messaging_api(weekday, item) 
    except ValueError as e: 
        print(f"メッセージの解析エラー: {e}")

def add_item_via_messaging_api(  weekday, item):
    # LINEメッセージを通じて持ち物を追加
    if weekday in weekday_items:
        weekday_items[weekday].append(item)
    else:
        weekday_items[weekday] = [item]
    
def delete_item_via_messaging_api( weekday, item):
    # LINEメッセージを通じて持ち物を削除
    if weekday in weekday_items and item in weekday_items[weekday]:
        weekday_items[weekday].remove(item)  
    




def daymtmn_getInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=daymtmn_get_spec)
    manager.registerFactory(profile,
                            daymtmn_get,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    daymtmn_getInit(manager)

    # create instance_name option for createComponent()
    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
  
    # Create a component
    comp = manager.createComponent("daymtmn_get" + args)

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

