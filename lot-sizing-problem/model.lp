\ Model Lot sizing model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  5 Amount_produced_of_item_in_period_0
   + 10 Amount_produced_of_item_in_period_1
   + 15 Amount_produced_of_item_in_period_2
   + 20 Amount_produced_of_item_in_period_3
   + 3 Amount_produced_of_item_in_period_4
   + Amount_produced_of_item_in_period_5
   + 8 Amount_produced_of_item_in_period_6
   + 9 Amount_produced_of_item_in_period_7
   + 3 Amount_produced_of_item_in_period_8
   + 99 Amount_produced_of_item_in_period_9
   + 6 Amount_produced_of_item_in_period_10
   + 12 Amount_produced_of_item_in_period_11 + 8 Stock_on_period_0
   + 10 Stock_on_period_1 + 25 Stock_on_period_2 + 6 Stock_on_period_3
   + 3 Stock_on_period_4 + 7 Stock_on_period_5 + 10 Stock_on_period_6
   + 88 Stock_on_period_7 + 6 Stock_on_period_8 + 42 Stock_on_period_9
   + 3 Stock_on_period_10 + 41 Stock_on_period_11 + 10 Produced_on_period_0
   + 8 Produced_on_period_1 + 20 Produced_on_period_2
   + Produced_on_period_3 + 30 Produced_on_period_4
   + 50 Produced_on_period_5 + 40 Produced_on_period_6
   + 10 Produced_on_period_7 + 12 Produced_on_period_8
   + 15 Produced_on_period_9 + 6 Produced_on_period_10
   + Produced_on_period_11
Subject To
 Production_on_period_0: Amount_produced_of_item_in_period_0
   - Stock_on_period_0 = 100
 Production_and_stock_on_period_1: Amount_produced_of_item_in_period_1
   + Stock_on_period_0 - Stock_on_period_1 = 200
 Production_and_stock_on_period_2: Amount_produced_of_item_in_period_2
   + Stock_on_period_1 - Stock_on_period_2 = 30
 Production_and_stock_on_period_3: Amount_produced_of_item_in_period_3
   + Stock_on_period_2 - Stock_on_period_3 = 50
 Production_and_stock_on_period_4: Amount_produced_of_item_in_period_4
   + Stock_on_period_3 - Stock_on_period_4 = 100
 Production_and_stock_on_period_5: Amount_produced_of_item_in_period_5
   + Stock_on_period_4 - Stock_on_period_5 = 60
 Production_and_stock_on_period_6: Amount_produced_of_item_in_period_6
   + Stock_on_period_5 - Stock_on_period_6 = 80
 Production_and_stock_on_period_7: Amount_produced_of_item_in_period_7
   + Stock_on_period_6 - Stock_on_period_7 = 95
 Production_and_stock_on_period_8: Amount_produced_of_item_in_period_8
   + Stock_on_period_7 - Stock_on_period_8 = 35
 Production_and_stock_on_period_9: Amount_produced_of_item_in_period_9
   + Stock_on_period_8 - Stock_on_period_9 = 12
 Production_and_stock_on_period_10: Amount_produced_of_item_in_period_10
   + Stock_on_period_9 - Stock_on_period_10 = 20
 Production_and_stock_on_period_11: Amount_produced_of_item_in_period_11
   + Stock_on_period_10 - Stock_on_period_11 = 60
 Activation_of_production_on_period_0: Amount_produced_of_item_in_period_0
   - 99999 Produced_on_period_0 <= 0
 Activation_of_production_on_period_1: Amount_produced_of_item_in_period_1
   - 99999 Produced_on_period_1 <= 0
 Activation_of_production_on_period_2: Amount_produced_of_item_in_period_2
   - 99999 Produced_on_period_2 <= 0
 Activation_of_production_on_period_3: Amount_produced_of_item_in_period_3
   - 99999 Produced_on_period_3 <= 0
 Activation_of_production_on_period_4: Amount_produced_of_item_in_period_4
   - 99999 Produced_on_period_4 <= 0
 Activation_of_production_on_period_5: Amount_produced_of_item_in_period_5
   - 99999 Produced_on_period_5 <= 0
 Activation_of_production_on_period_6: Amount_produced_of_item_in_period_6
   - 99999 Produced_on_period_6 <= 0
 Activation_of_production_on_period_7: Amount_produced_of_item_in_period_7
   - 99999 Produced_on_period_7 <= 0
 Activation_of_production_on_period_8: Amount_produced_of_item_in_period_8
   - 99999 Produced_on_period_8 <= 0
 Activation_of_production_on_period_9: Amount_produced_of_item_in_period_9
   - 99999 Produced_on_period_9 <= 0
 Activation_of_production_on_period_10:
   Amount_produced_of_item_in_period_10 - 99999 Produced_on_period_10 <= 0
 Activation_of_production_on_period_11:
   Amount_produced_of_item_in_period_11 - 99999 Produced_on_period_11 <= 0
Bounds
Binaries
 Produced_on_period_0 Produced_on_period_1 Produced_on_period_2
 Produced_on_period_3 Produced_on_period_4 Produced_on_period_5
 Produced_on_period_6 Produced_on_period_7 Produced_on_period_8
 Produced_on_period_9 Produced_on_period_10 Produced_on_period_11
End
