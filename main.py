
import terminaltables
import coinmarketcap
import time
import sys
import os

What_I_have =[['bitcoin', 1] , ['stratis' , 900], ['ethereum' , 12],
              ['litecoin' , 3], ['monero' , 4] , ['ripple' , 400]]
# What_I_have =[ ['stratis' , 45] ]

def print_cryptKeep():

	def get_relevantCoinInfo_dict(my_coins):


		result = []

		coinmarketcapp = coinmarketcap.Market()
		#
		#
		All_data = coinmarketcapp.ticker()

		for coin_dict in All_data:

			for mycoin in my_coins:
				if coin_dict.get('id') in mycoin[0]:
					coin_dict['My_volume'] = round(mycoin[1], 4)
					result.append(coin_dict)

		return result

	def scrapInfo(relevantInfo):

		all_lines_coin = []
		for info in relevantInfo:
			oneline_coin = {}
			# print(info)
			oneline_coin['Name'] = info.get('name')
			oneline_coin['My_volume'] = info.get('My_volume')
			oneline_coin['Price_$'] = round(float(info.get('price_usd')), 1)
			oneline_coin['Value_$'] = round(info.get('My_volume') * float(info.get('price_usd')), 1)
			oneline_coin['Value_Btc'] = round(info.get('My_volume') * float(info.get('price_btc')), 4)

			oneline_coin['%_change_1h'] = info.get('percent_change_1h')
			oneline_coin['%_change_24h'] = info.get('percent_change_24h')
			oneline_coin['%_change_7d'] = info.get('percent_change_7d')
			all_lines_coin.append(oneline_coin)
		return all_lines_coin

	def build_table_to_print (info_sleected):
		the_table_lst = []

		#Headline , names of columns
		the_table_lst.append(list(info_sleected[0].keys()))
		the_table_lst[0].append('Allocation_%')
		#cumuled tot
		TOT_dollar = 0
		TOT_BTC = 0



		for coinz in info_sleected:
			TOT_dollar += coinz.get('Value_$')
			TOT_BTC += coinz.get('Value_Btc')




		# Get %
		for coinz in info_sleected:
			coinz['Allocation_%'] = int(coinz.get('Value_$') * 100 / TOT_dollar)
			the_table_lst.append(list(coinz.values()))

		# gettot % change:

		weightedTOTPCT_7d =0
		weightedTOTPCT_24h =0
		weightedTOTPCT_1h =0

		for coinz in info_sleected:
			weightedTOTPCT_7d += round((float(coinz.get('%_change_7d'))/100)* (coinz.get('Allocation_%')/100) * 100 , 0)
			weightedTOTPCT_24h += round((float(coinz.get('%_change_24h'))/100)* (coinz.get('Allocation_%')/100) * 100 ,0)
			weightedTOTPCT_1h += round((float(coinz.get('%_change_1h'))/100)* (coinz.get('Allocation_%')/100) * 100 ,0)


		#totalLINE , last line
		the_table_lst.append(['TOTAL', ' ', ' ',round(TOT_dollar, 1),
		                      round(TOT_BTC, 4), weightedTOTPCT_1h,weightedTOTPCT_24h,weightedTOTPCT_7d,'100'])

		return the_table_lst


	allinfo_relevantCoins = get_relevantCoinInfo_dict(What_I_have)

	select_info = scrapInfo(allinfo_relevantCoins)

	the_table_to_show = build_table_to_print(select_info)

	table = terminaltables.AsciiTable(the_table_to_show)

	# print(table.table ,flush=True)
	# sys.stdout.flush()
	# sys.stdout.write(table.table )
	print(table.table, end='\r')
	# sys.stdout.flush()
	# Clear the screen.
	# os.system('clear')
	# sys.stdout.write("\r{0}>".format("=" * i))
print_cryptKeep()
# # print_cryptKeep()
# while(True):
# 	# sys.stdout.flush()
# 	# sys.stdout.flush()
# 	# sys.stdout.flush()
# 	# sys.stdout.flush()
# 	# sys.stdout.flush()
# 	print_cryptKeep()
# 	# os.system('cls')
#
