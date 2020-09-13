from django.shortcuts import render
from highcharts.views import HighChartsMultiAxesView, HighChartsStackedView,HighChartsBarView, HighChartsPieView, HighChartsHeatMapView
import random
from results.models import *

def BarChartView(request):
	return render(request, 'results/presidential_dashboard.html')


def PresidentialResult(request):
	polls=PresidentialPollResult.objects.aggregate(p_ndc=Sum('NDC'),p_npp=Sum('NPP'),p_cpp=Sum('CPP'))
	region=Region.objects.values('name').annotate(p_ndc=Sum('pollingstation__presidentialpollresult__NDC'),p_npp=Sum('pollingstation__presidentialpollresult__NPP'),p_cpp=Sum('pollingstation__presidentialpollresult__CPP'))
	return render(request, 'results/pres.html', {'region':region,'polls':polls})


def Constituent(request):
	context_variable=Constituency.objects.values('region__name', 'name').annotate(ndc=Sum('pollingstation__presidentialpollresult__NDC'),npp=Sum('pollingstation__presidentialpollresult__NPP'),cpp=Sum('pollingstation__presidentialpollresult__CPP'))
	return render(request, 'results/constituency.html',{'context_variable':context_variable})

def Station(request):
	context_variable=Constituency.objects.values('region__name','name','pollingstation__name', 'pollingstation__pscode','pollingstation__voter_pop','pollingstation__presidentialpollresult__NDC','pollingstation__presidentialpollresult__NPP','pollingstation__presidentialpollresult__CPP','pollingstation__presidentialpollresult__rejected','pollingstation__presidentialpollresult__valid_votes','pollingstation__presidentialpollresult__vote_cast','pollingstation__presidentialpollresult__available','pollingstation__presidentialpollresult__verified','pollingstation__presidentialpollresult__voting_status','pollingstation__presidentialpollresult__created_on')
	return render(request, 'results/stations.html',{'context_variable':context_variable})

def HeatMap(request):
	return render(request, 'results/heatmap.html')


def TileMap(request):
	return render(request, 'results/tilemap.html')


def Pie(request):
	return render(request, 'results/pie.html')






class PresidentialChartView(HighChartsBarView):
	title=' 2020 General Results'
	subtitle='Presidential'
	chart_type='column'
	legend={'enabled':True}
	categories=['Greater Accra','Ashanti','Oti', 'Western','Eastern','Upper East','Upper West','Savannah', 'Bono East','Northern','Western North','North East','Central', 'Ahafo','Bono','Volta']


	@property
	def series(self):
		return self._series
	




# Heat view
class PresidentialHeatView(HighChartsHeatMapView):
	title='Votes per party per region'
	chart_type = 'heatmap'
	tooltip={'headerFormat': 'Votes<br/>',
            'pointFormat': '{point.x:%e %b, %Y} {point.y}:00: <b>{point.value} </b>'}
	coloraxis={'min': 0,
        'minColor': '#FFFFFF',
        'maxColor': '#f39a6f',
        #'maxColor': Highcharts.getOptions().colors[0]
        }
	margin_top = 40
	margin_bottom = 80
	categories = ['Alexander', 'Marie', 'Maximilian', 'Sophia', 'Lukas', 'Maria', 'Leon', 'Anna', 'Tim', 'Laura']
	series=[{ 'name': 'Sales per employee', 'borderWidth': 1,'data': [[0, 0, 10], [0, 1, 19], [0, 2, 8], [0, 3, 24], [0, 4, 67], [1, 0, 92], [1, 1, 58], [1, 2, 78], [1, 3, 117], [1, 4, 48], [2, 0, 35], [2, 1, 15], [2, 2, 123], [2, 3, 64], [2, 4, 52], [3, 0, 72], [3, 1, 132], [3, 2, 114], [3, 3, 19], [3, 4, 16], [4, 0, 38], [4, 1, 5], [4, 2, 8], [4, 3, 117], [4, 4, 115], [5, 0, 88], [5, 1, 32], [5, 2, 12], [5, 3, 6], [5, 4, 120], [6, 0, 13], [6, 1, 44], [6, 2, 88], [6, 3, 98], [6, 4, 96], [7, 0, 31], [7, 1, 1], [7, 2, 82], [7, 3, 32], [7, 4, 30], [8, 0, 85], [8, 1, 97], [8, 2, 123], [8, 3, 64], [8, 4, 84], [9, 0, 47], [9, 1, 114], [9, 2, 31], [9, 3, 48], [9, 4, 91]], 'dataLabels': {'enabled': True, 'color': '#000000'	}}] 
	categories=['Western North','North East','Savannah','Northern','Eastern','Western','Central', 'Ahafo', 'Bono East','Bono', 'Oti','Upper West','Upper East','Volta','Ashanti','Greater Accra']
	series=[{'name':'Total Votes per Party', 'borderWidth':1, 'data':[
		[0, 0, 10], [0, 1, 19], [0, 2, 8], [0, 3, 24], [0, 4, 67],
		[1, 0, 10], [1, 1, 19], [1, 2, 8], [1, 3, 24], [1, 4, 67],
		[2, 0, 10], [2, 1, 19], [2, 2, 8], [2, 3, 24], [2, 4, 67],
		[3, 0, 10], [3, 1, 19], [3, 2, 8], [3, 3, 24], [3, 4, 67],
		[4, 0, 10], [4, 1, 19], [4, 2, 8], [4, 3, 24], [4, 4, 67],
		[5, 0, 10], [5, 1, 19], [5, 2, 8], [5, 3, 24], [5, 4, 67],
		[6, 0, 10], [6, 1, 19], [6, 2, 8], [6, 3, 24], [6, 4, 67],
		[7, 0, 10], [7, 1, 19], [7, 2, 8], [7, 3, 24], [7, 4, 67],
		[8, 0, 10], [8, 1, 19], [8, 2, 8], [8, 3, 24], [8, 4, 67],
		[9, 0, 10], [9, 1, 19], [9, 2, 8], [9, 3, 24], [9, 4, 67],
		[10, 0, 10], [10, 1, 19], [10, 2, 8], [10, 3, 24], [10, 4, 67],
		[11, 0, 10], [11, 1, 19], [11, 2, 8], [11, 3, 24], [11, 4, 67],
		[12, 0, 10], [12, 1, 19], [12, 2, 8], [12, 3, 24], [12, 4, 67],
		[13, 0, 10], [13, 1, 19], [13, 2, 8], [13, 3, 24], [13, 4, 67],
		[14, 0, 10], [14, 1, 19], [14, 2, 8], [14, 3, 24], [14, 4, 67],
		[15, 0, 10], [15, 1, 19], [15, 2, 8], [15, 3, 24], [15, 4, 67],
		],
		'dataLabels': {'enabled': True, 'color': '#000000'}
		}]
	yaxis=	{'categories':['NDC', 'NPP', 'CPP', 'PNC', 'PPP']}

	#categories=['NDC', 'NPP', 'CPP', 'PNC', 'PPP']
	# series=[{'name':'Total Votes per Party', 'borderWidth':1,'borderColor': 'rgba(255, 255, 255, 0.3)',
	# 		'dataLabels': {'enabled': True, 'color': '#000000', 'style': {
	# 		#'color': '#fff',
	# 		'font-family': 'arial, helvetica, sans-serif',
	# 		'font-size': '66px'
	# 		}},'tickWidth': 0,'lineWidth': 0,
	# 		'data':[
	# 			[0, 0, 10], [0, 1, 19], [0, 2, 8], [0, 3, 24], [0, 4, 67],[0, 5, 10], [0, 6, 19], [0, 7, 8], [0, 8, 24], [0, 9, 67],[0, 10, 10], [0, 11, 19], [0, 12, 8], [0, 13, 24], [0, 14, 67],[0, 15, 10],
	# 			[1, 0, 10], [1, 1, 19], [1, 2, 8], [1, 3, 24], [1, 4, 67],[1, 5, 10], [1, 6, 19], [1, 7, 8], [1, 8, 24], [1, 9, 67],[1, 10, 10], [1, 11, 19], [1, 12, 8], [1, 13, 24], [1, 14, 67],[1, 15, 10],
	# 			[2, 0, 10], [2, 1, 19], [2, 2, 8], [2, 3, 24], [2, 4, 67],[2, 5, 10], [2, 6, 19], [2, 7, 8], [2, 8, 24], [2, 9, 67],[2, 10, 10], [2, 11, 19], [2, 12, 8], [2, 13, 24], [2, 14, 67],[2, 15, 10],
	# 			[3, 0, 10], [3, 1, 19], [3, 2, 8], [3, 3, 24], [3, 4, 67],[3, 5, 10], [3, 6, 19], [3, 7, 8], [3, 8, 24], [3, 9, 67],[3, 10, 10], [3, 11, 19], [3, 12, 8], [3, 13, 24], [3, 14, 67],[3, 15, 10],
	# 			[4, 0, 10], [4, 1, 19], [4, 2, 8], [4, 3, 24], [4, 4, 67],[4, 5, 10], [4, 6, 19], [4, 7, 8], [4, 8, 24], [4, 9, 67],[4, 10, 10], [4, 11, 19], [4, 12, 8], [4, 13, 24], [4, 14, 67],[4, 15, 10]
			

	# 		]
	# 		}]
	# yaxis={'categories':['Western North','North East','Savannah','Northern','Eastern','Western','Central', 'Ahafo', 'Bono East','Bono', 'Oti','Upper West','Upper East','Volta','Ashanti','Greater Accra']}

	legend = {	'align': 'right',
				'layout': 'vertical',
				'margin': 0, 
				'verticalAlign': 'top',
				'y': 25, 
				'symbolHeight': 320
			}

	



# Tilemap
class TilemapView(HighChartsHeatMapView):
	title='Votes per party per region'
	chart_type = 'tilemap'
	xaxis={'visible': True}
	yaxis={'visible': True}
	series=[{
		'name': '',
        'data': [{
            'hc-a2': 'AL',
            'name': 'Alabama',
            'region': 'South',
            'x': 6,
            'y': 7,
            'value': 4849377
        }, {
            'hc-a2': 'AK',
            'name': 'Alaska',
            'region': 'West',
            'x': 0,
            'y': 0,
            'value': 737732
        }, {
            'hc-a2': 'AZ',
            'name': 'Arizona',
            'region': 'West',
            'x': 5,
            'y': 3,
            'value': 6745408
        }
		]}
		]






class BarView(HighChartsBarView):
	title='Fruit Consumption'
	subtitle='Source: Harris Interactive'
	chart_type='column'
	legend={'enabled':True}
	categories = ['Orange', 'Bananas', 'Apples']
	#template_name='high/barchart.html'
	@property
	def series(self):
		result = []
		for name in ('Joe', 'Jack', 'William', 'Averell'):
			data = []
			for x in range(len(self.categories)):
				data.append(random.randint(0, 10))
			result.append({"name": name, "data": data})
		return result



class Piechartview(HighChartsPieView):
	chart_type = 'pie'
    #options3d = ''
	title='Election Results'
	subtitle='Presidential'
	# subtitle={
	# 	'text':'Presidential',
	# 	'style':{
	# 		'margin':2
	# 	}
	# }
	tooltip={
			'pointFormat': '{series.name}: <b>{point.y}</b>',
			# 'valueSuffix': '%'

	}
	legend={
			# 'title':'Regionals',
			'enabled':True, 
			'align': 'center',

	}
	plot_options={
		
			'pie':{
				'allowPointSelect': True,
				'showInLegend': True,
				'dataLabels': {
					'enabled':True,
					'format': "{point.name} - <b>{point.percentage:.1f}%</b>",
					# 'distance': -24,
					'color': 'black',
					'style': {
					'fontWeight': 'bold'
					}
				}
			}

	}

	@property
	def series(self):
		series=	[
				{
			    'name': 'Regional votes',
			    'colorByPoint': True,
			    'data':	[
			            {'name': 'NDC',
			             'y': Region.objects.values('name','constituency__name').order_by('name').aggregate(Total_NDC=Sum('constituency__pollingstation__presidentialpollresult__NDC'))['Total_NDC'],
			             # 'sliced': 'true',
			             'color':'green',
			             'drilldown': 'windows-versions'
			             },
			            {'name': 'NPP',
			             'y': Region.objects.values('name','constituency__name').order_by('name').aggregate(Total_NPP=Sum('constituency__pollingstation__presidentialpollresult__NPP'))['Total_NPP'],
			             'color':'blue',
			             'drilldown': 'mac-versions'
			             },
			            {'name': 'CPP',
			             'y': Region.objects.values('name','constituency__name').order_by('name').aggregate(Total_CPP=Sum('constituency__pollingstation__presidentialpollresult__CPP'))['Total_CPP'],
			             'drilldown': 'linux-versions'
			             },
			             {'name':'PNC',
			             	'y':1.01,
			             },
			             {'name':'PPP',
			             	'y':1.01,
			             }
			        	]
				}
				]
		return series



class ColumnChartView(HighChartsStackedView):
	title='General Election'
	subtitle='Presidential'
	# annotations={
	# 			'labels':[
	# 					{
	# 						'point':'mahama',
	# 						'text':'Prz Mahama'
	# 					},
	# 					{
	# 						'point':'nana',
	# 						'text':'Prez Nana'
	# 					}
	# 			]
	# }
	xlabels = {#'rotation': -45,
				# 'align':'left'
	}
	exporting={
				'enabled':False
	}
	credits={
				'enabled':False
	}
	chart_type='bar'
	legend={
			'enabled':True,
			# 'align':'right',
			'title':{
						'text':'Political Parties',
						'align':'center'
			}
	}


	#@property
	def image():
		
		img='/media/images/ndc.png'
		return "<img style='width:20px; height:20px'src='"+img +"' />"
	tooltip={
			'enabled':True,
			'animation':True,
			'useHTML':True,
			# 'pointFormat': '{series.name}: <b>{point.percentage:.1f}%</b>',
			# 'valueSuffix': '%',
			'pointFormat':image(),
			'headerFormat':'<b>Polls</b><br>',
			# 'position':{
			# 			# 'verticalAlign':'top',
			# 			'x':2,
			# 			'y':50
			# }
			


	}
	
	categories = ['Results', 
				# 'Bananas', 
				# 'Apples'
	]
	plot_options={
					'bar':{
							'stacking':'percent',
							'dataLabels':{
											'enabled': True,
											'color': '#F4F4F4',
											'useHTML':True,
											# 'format':"<img style='width:100px; height:100px'src='/media/images/banana.png' />"+ "{series.name}: <b>{point.percentage:.1f}%</b><br>{point.y:,.0f}",
											# 'x':-50,
											'format':"{series.index}|{series.name}: <b>{point.percentage:.1f}%</b><br>{point.y:,.0f}<br>"+"<img style='width:20px; height:20px'src='/media/images/banana.png' />",
											# 'format':image(),
											# 'inside':True,
											'style':{
													'fontSize':'12px',

											}

							}
					}
	}
	@property
	def yaxis(self):
		yaxis={
					# 'visible':False,
					# 'gridLineColor':'red',
					# 'stackLables':{
					# 				'enabled':True,
					# 				'style':{
					# 							'color':'yellow'
					# 				}
					# },
					# 'lineColor':'blue',
					'tickInterval':50,
					# 'tickPosition':'inside',
					'title':{
								'text':'Number of Votes',
								# 'x':-20
					},
					'plotLines':[
						{
							'value':'50',
							'width':4,
							# 'height':4,
							'color':'red',
							'label':{
								# 'text':'Won',
								'rotation':0
							}
						}

					],
					'labels':{
								'enabled':False,

					}
		}
		return yaxis


	# @property
	# def xaxis(self):
	# 	xaxis={
	# 			'labels':{
	# 						'align':'left'
	# 			}
	# 	}
	# 	return xaxis
	
	series=[
			# 'dataLabels':{
			# 				'enabled':True
			# },
			{
				'name':'NDC',
				# 'data':[Region.objects.values('name','constituency__name').order_by('name').aggregate(Total_NDC=Sum('constituency__pollingstation__presidentialpollresult__NDC'))['Total_NDC']],
				'color':'green',
								# {
								# 'pattern':{
								# 		'image':'media/images/bananas.svg',
								# 		'aspectRatio':1
								# }
								# },
				'id':'mahama',
				'image':'/media/images/banana.png'
			},
			{
				'name':'NPP',
				# 'data':[Region.objects.values('name','constituency__name').order_by('name').aggregate(Total_NPP=Sum('constituency__pollingstation__presidentialpollresult__NPP'))['Total_NPP']],
				'color':'blue',
				'id':'nana',
				'image':'/media/images/apple.png'
			},
			{
				'name':'CPP',
				# 'data':[Region.objects.values('name','constituency__name').order_by('name').aggregate(Total_CPP=Sum('constituency__pollingstation__presidentialpollresult__CPP'))['Total_CPP']],
				'id':'samia',
				'image':'/media/images/orange.png'
			}
	]
	

		


