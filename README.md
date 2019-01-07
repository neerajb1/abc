<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Ghanta.aspx.cs" Inherits="WebApplication1.Ghanta" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
			  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
		  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />
		  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<title></title>

	<style type="text/css">
		.header {
			float: left;
			color: black;
			text-align: center;
			padding: 12px;
			text-decoration: none;
			font-size: 18px;
			line-height: 25px;
			border-radius: 4px;
			width:100%;
			color:blue;
		}

		
	</style>




	<script type="text/javascript">



		$(function () {
			//alert('begin');
		});



		var data1 = {
			"non_active_beacon_store": {
				"Abu Dhabi Municipality": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM ABU DHABI MUNICIPALITY"
					}]
				},
				"Etisalat Abu Dhabi": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM ETISALAT - HO"
					}]
				},
				"Madinat Zayed ": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "AAW MADINAT ZAYED"
					}]
				},
				"Deerfield's Town Square": {
					"count": 2,
					"store_details": [{
						"STORE_NAME": "SK DEERFIELDS TOWN SQUARE"
					}, {
						"STORE_NAME": "AL DEERFIELDS TOWN SQUARE"
					}]
				},
				"Etisalat Tower Abudhabi": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM - ETISALAT T & A ABUDHABI"
					}]
				},
				"Al Ruwais Mall": {
					"count": 5,
					"store_details": [{
						"STORE_NAME": "AC AL RUWAIS MALL"
					}, {
						"STORE_NAME": "TIM AL RUWAIS MALL"
					}, {
						"STORE_NAME": "CSC  AL RUWAIS MALL"
					}, {
						"STORE_NAME": "SK RUWAIS MALL"
					}, {
						"STORE_NAME": "TCP AL RUWAIS MALL"
					}]
				},
				"Al Wahda Mall": {
					"count": 16,
					"store_details": [{
						"STORE_NAME": "CR Al WAHDA"
					}, {
						"STORE_NAME": "AR AL WAHDA  MALL"
					}, {
						"STORE_NAME": "AC AL WAHDAH MALL"
					}, {
						"STORE_NAME": "BHPC AL WAHDA MALL"
					}, {
						"STORE_NAME": "CH AL WAHDA MALL"
					}, {
						"STORE_NAME": "AAW AL WAHDA MALL"
					}, {
						"STORE_NAME": "SP AL WAHDA MALL"
					}, {
						"STORE_NAME": "TH AL WAHDA ( ACCESSORIES)"
					}, {
						"STORE_NAME": "CK AL WAHDA MALL"
					}, {
						"STORE_NAME": "AAW AL WAHDA KC KIOSK"
					}, {
						"STORE_NAME": "LE AL WAHDA MALL"
					}, {
						"STORE_NAME": "PP AL WAHDA MALL"
					}, {
						"STORE_NAME": "SK ALWAHDA MALL (KIDS)"
					}, {
						"STORE_NAME": "NA ALWAHDA MALL"
					}, {
						"STORE_NAME": "RB AL WAHDA MALL"
					}, {
						"STORE_NAME": "CSC AL WAHDA MALL"
					}]
				},
				"Bawabat Al Sharq Mall": {
					"count": 12,
					"store_details": [{
						"STORE_NAME": "ACC BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "SP BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "BK BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "BHPC BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "LVR BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "SK BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "NW BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "TCP BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "PE  BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "GM BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "QUPAC BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "JFK BAWABAT AL SHARQ MALL"
					}]
				},
				"Hamdan Shopping Center": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "SK Uni Q HAMDAN"
					}]
				},
				"Al Seef Village": {
					"count": 2,
					"store_details": [{
						"STORE_NAME": "TIM AL SEEF VILLAGE"
					}, {
						"STORE_NAME": "CSC AL SEEF VILLAGE"
					}]
				},
				"Abu Dhabi Mall": {
					"count": 12,
					"store_details": [{
						"STORE_NAME": "BHPC ABU DHABI MALL"
					}, {
						"STORE_NAME": "CH ABU DHABI MALL"
					}, {
						"STORE_NAME": "AL ABUDHABI MALL"
					}, {
						"STORE_NAME": "BK ABUDHABI MALL"
					}, {
						"STORE_NAME": "DU ABUDHABI MALL"
					}, {
						"STORE_NAME": "TIM ABU DHABI MALL"
					}, {
						"STORE_NAME": "CA ABU DHABI MALL"
					}, {
						"STORE_NAME": "KC ABUDHABI MALL"
					}, {
						"STORE_NAME": "MBT ABUDHABI MALL"
					}, {
						"STORE_NAME": "PC BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "AKAK ABUDHABI MALL"
					}, {
						"STORE_NAME": "CSC ABU DHABI MALL GF"
					}]
				},
				"Mushrif Mall": {
					"count": 6,
					"store_details": [{
						"STORE_NAME": "AD MUSHRIFF MALL"
					}, {
						"STORE_NAME": "ACC MUSHRIFF MALL"
					}, {
						"STORE_NAME": "SP MUSHRIFF MALL"
					}, {
						"STORE_NAME": "SS MUSHRIFF MALL"
					}, {
						"STORE_NAME": "IG MUSHRIFF MALL"
					}, {
						"STORE_NAME": "RB MUSHRIFF MALL"
					}]
				},
				"ADNOC Yas Island 2": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM ADNOC YAS 2"
					}]
				},
				"Khalidiya Mall Abudhabi": {
					"count": 2,
					"store_details": [{
						"STORE_NAME": "SK KHALIDIYA MALL"
					}, {
						"STORE_NAME": "PP KHALIDIYA MALL"
					}]
				},
				"Yas Mall": {
					"count": 3,
					"store_details": [{
						"STORE_NAME": "TH YAS MALL"
					}, {
						"STORE_NAME": "SG YAS MALL"
					}, {
						"STORE_NAME": "TIM SIS SG YAS MALL "
					}]
				},
				"Sowwah Square": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TH SOWWAH SQUARE"
					}]
				},
				"Marina Mall Abudhabi": {
					"count": 9,
					"store_details": [{
						"STORE_NAME": "AL MARINA MALL"
					}, {
						"STORE_NAME": "JC MARINA MALL -AXD"
					}, {
						"STORE_NAME": "AU MARINA MALL"
					}, {
						"STORE_NAME": "TH MARINA MALL AXD"
					}, {
						"STORE_NAME": "TIM MARINA MALL ABU DHABI"
					}, {
						"STORE_NAME": "LE MARINA MALL -AUH"
					}, {
						"STORE_NAME": "SK MARINA MALL -AXD"
					}, {
						"STORE_NAME": "PP MARINA MALL -AUH"
					}, {
						"STORE_NAME": "TOMS MARINA MALL (AXD)"
					}]
				},
				"Abudhabi Co-Op-Society": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM ABU DHABI CO-OP MINA"
					}]
				},
				"Dalma Mall": {
					"count": 14,
					"store_details": [{
						"STORE_NAME": "SP  DALMA MALL"
					}, {
						"STORE_NAME": "ACC DALMA MALL"
					}, {
						"STORE_NAME": "NA DALMA MALL"
					}, {
						"STORE_NAME": "CK DALMA MALL"
					}, {
						"STORE_NAME": "DP DALMA MALL"
					}, {
						"STORE_NAME": "AU DALMA MALL"
					}, {
						"STORE_NAME": "DU DALMA MALL"
					}, {
						"STORE_NAME": "PP DALMA MALL"
					}, {
						"STORE_NAME": "DSW DALMA MALL"
					}, {
						"STORE_NAME": "DU DALMA MALL"
					}, {
						"STORE_NAME": "LCW DALMA MALL"
					}, {
						"STORE_NAME": "SMYK DALMA MALL"
					}, {
						"STORE_NAME": "NW DALMA MALL"
					}, {
						"STORE_NAME": "LEVIS DALMA MALL"
					}]
				},
				"Fotouh Al Khair Abudhabi": {
					"count": 3,
					"store_details": [{
						"STORE_NAME": "NW FOTOUH AL KHAIR"
					}, {
						"STORE_NAME": "AL FATOUH AL KHAIR"
					}, {
						"STORE_NAME": "AC FATOUH AL KHAIR"
					}]
				}
			},
			"active_beacon_store": {
				"Emal": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM EMAL"
					}]
				},
				"Deerfield's Town Square": {
					"count": 9,
					"store_details": [{
						"STORE_NAME": "LVR DEERFIELDS TOWN SQUARE"
					}, {
						"STORE_NAME": "CK  DEERFIELDS TOWN SQUARE"
					}, {
						"STORE_NAME": "ACC DEERFIELDS TOWN SQUARE"
					}, {
						"STORE_NAME": "TIM DEERFIELDS TOWN SQUARE 1"
					}, {
						"STORE_NAME": "ACO DEERFIELDS TOWN SQUARE"
					}, {
						"STORE_NAME": "TCP DEERFIELDS TOWN SQUARE"
					}, {
						"STORE_NAME": "TIM DEERFIELDS TOWN SQUARE 2"
					}, {
						"STORE_NAME": "IG DEER FIELD"
					}, {
						"STORE_NAME": "NW DEERFIELDS TOWN SQUARE"
					}]
				},
				"AL Minhali Tower": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM AL MINHALI TOWER -AUH"
					}]
				},
				"AL Najda": {
					"count": 2,
					"store_details": [{
						"STORE_NAME": "TIM AL NAJDA"
					}, {
						"STORE_NAME": "CSC AL NAJDA"
					}]
				},
				"Dalma Mall": {
					"count": 7,
					"store_details": [{
						"STORE_NAME": "AR DALMA MALL"
					}, {
						"STORE_NAME": "SK DALMA MALL"
					}, {
						"STORE_NAME": "CR DALMA MALL"
					}, {
						"STORE_NAME": "IG DALMA MALL"
					}, {
						"STORE_NAME": "AL DALMA MALL"
					}, {
						"STORE_NAME": "TIM DALMA MALL"
					}, {
						"STORE_NAME": "ZG DALMA MALL"
					}]
				},
				"Abu Dhabi Mall": {
					"count": 14,
					"store_details": [{
						"STORE_NAME": "NW ABU DHABI MALL"
					}, {
						"STORE_NAME": "CK ABU DHABI MALL"
					}, {
						"STORE_NAME": "ACC ABU DHABI MALL"
					}, {
						"STORE_NAME": "NB ABU DHABI MALL"
					}, {
						"STORE_NAME": "IG ABU DHABI MALL"
					}, {
						"STORE_NAME": "NA ABUDHABI MALL"
					}, {
						"STORE_NAME": "SK ABU DHABI MALL"
					}, {
						"STORE_NAME": "SP ABUDHABI MALL"
					}, {
						"STORE_NAME": "TH ABUDHABI MALL"
					}, {
						"STORE_NAME": "LE ABUDHABI MALL"
					}, {
						"STORE_NAME": "LVR ABU DHABI MALL"
					}, {
						"STORE_NAME": "AR ABUDHABI MALL"
					}, {
						"STORE_NAME": "GR ABUDHABI MALL"
					}, {
						"STORE_NAME": "CSC ABUDHABI MALL"
					}]
				},
				"Mushrif Mall": {
					"count": 16,
					"store_details": [{
						"STORE_NAME": "CK MUSHRIFF MALL"
					}, {
						"STORE_NAME": "CR MUSHRIFF MALL"
					}, {
						"STORE_NAME": "NW MUSHRIFF MALL"
					}, {
						"STORE_NAME": "NA MUSHRIFF MALL"
					}, {
						"STORE_NAME": "AL MUSHRIFF MALL"
					}, {
						"STORE_NAME": "ACO MUSHRIFF MALL"
					}, {
						"STORE_NAME": "SK MUSHRIFF MALL"
					}, {
						"STORE_NAME": "TCP MUSHRIFF MALL"
					}, {
						"STORE_NAME": "BHPC MUSHRIF MALL"
					}, {
						"STORE_NAME": "TIM MUSHRIFF  MALL"
					}, {
						"STORE_NAME": "AU MUSHRIFF  MALL"
					}, {
						"STORE_NAME": "PP MUSHRIFF MALL"
					}, {
						"STORE_NAME": "HEMA MUSHRIFF MALL"
					}, {
						"STORE_NAME": "DU MUSHRIFF MALL"
					}, {
						"STORE_NAME": "SMYK MUSHRIFF MALL"
					}, {
						"STORE_NAME": "CSC MUSHRIFF MALL"
					}]
				},
				"ADCP Building - Muroor Road": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM ADCP MUROOR "
					}]
				},
				"Sowwah Square": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "JC THE GALLERIA -SOWWAH SQUARE"
					}]
				},
				"Marina Mall Abudhabi": {
					"count": 6,
					"store_details": [{
						"STORE_NAME": "NW MARINA MALL"
					}, {
						"STORE_NAME": "RI MARINA MALL-AXD"
					}, {
						"STORE_NAME": "ACO MARINA MALL -AXD"
					}, {
						"STORE_NAME": "CR MARINA MALL-ABU DHABI"
					}, {
						"STORE_NAME": "AFT MARINA MALL (AXB)"
					}, {
						"STORE_NAME": "DU MARINA MALL AXD"
					}]
				},
				"Madinat Zayed ": {
					"count": 2,
					"store_details": [{
						"STORE_NAME": "CK MADINAT ZAYED CENTRE"
					}, {
						"STORE_NAME": "NW MADINAT ZAYED"
					}]
				},
				"Yas Mall": {
					"count": 6,
					"store_details": [{
						"STORE_NAME": "JC YAS MALL"
					}, {
						"STORE_NAME": "CAK YAS MALL"
					}, {
						"STORE_NAME": "RI YAS MALL"
					}, {
						"STORE_NAME": "BHPC YAS MALL"
					}, {
						"STORE_NAME": "ACC YAS MALL"
					}, {
						"STORE_NAME": "AL YAS MALL"
					}]
				},
				"Adnoc Exit 381, Abu Dhabi": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM- ADNOC (Exit 381)"
					}]
				},
				"Abu Dhabi Corniche": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "CSC ABUDHABI CORNICHE"
					}]
				},
				"Al Ruwais Mall": {
					"count": 4,
					"store_details": [{
						"STORE_NAME": "SP AL RUWAIS MALL"
					}, {
						"STORE_NAME": "IG AL RUWAIS"
					}, {
						"STORE_NAME": "NA AL RUWAIS MALL"
					}, {
						"STORE_NAME": "TAC AL RUWAIS MALL"
					}]
				},
				"Al Wahda Mall": {
					"count": 12,
					"store_details": [{
						"STORE_NAME": "AL AL WAHDAH MALL"
					}, {
						"STORE_NAME": "IG AL WAHDA MALL"
					}, {
						"STORE_NAME": "DU AL WAHDAH  MALL"
					}, {
						"STORE_NAME": "TCP AL WADHA MALL"
					}, {
						"STORE_NAME": "SK ALWAHDA MALL"
					}, {
						"STORE_NAME": "BK AL WAHDA MALL"
					}, {
						"STORE_NAME": "ACO AL WAHDA  MALL"
					}, {
						"STORE_NAME": "TIM AL WAHDA MALL"
					}, {
						"STORE_NAME": "TAC KIDS AL WAHDA MALL"
					}, {
						"STORE_NAME": "AL AL WAHDA MALL 2"
					}, {
						"STORE_NAME": "LCW ALWAHDA MALL"
					}, {
						"STORE_NAME": "SMYK AL WAHDA MALL"
					}]
				},
				"Bawabat Al Sharq Mall": {
					"count": 12,
					"store_details": [{
						"STORE_NAME": "AAW BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "IG  BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "TIM BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "NA BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "ACO BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "AL BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "ZG BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "BV BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "CK BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "PF BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "GR BAWABAT AL SHARQ MALL"
					}, {
						"STORE_NAME": "CSC BAWABAT AL SHARQ MALL"
					}]
				},
				"Adnoc Al Haffar": {
					"count": 2,
					"store_details": [{
						"STORE_NAME": "TIM Testing store 2"
					}, {
						"STORE_NAME": "TIM ADNOC -AL HAFFAR"
					}]
				},
				"Khalidiya Mall Abudhabi": {
					"count": 5,
					"store_details": [{
						"STORE_NAME": "AL KHALIDIYA MALL"
					}, {
						"STORE_NAME": "IG KHALIDIYAH MALL"
					}, {
						"STORE_NAME": "AC KHALIDIYA MALL"
					}, {
						"STORE_NAME": "NW KHALIDIYA MALL"
					}, {
						"STORE_NAME": "TIM SPAR KHALIDIYAH"
					}]
				},
				"Mazyad Mall": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "SK  Uni-Q MAZYAD MALL"
					}]
				},
				"ADNOC Yas Island 1": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "TIM ADNOC - YAS 1"
					}]
				},
				"Fotouh Al Khair Abudhabi": {
					"count": 1,
					"store_details": [{
						"STORE_NAME": "DU FOTOUH AL KHAIR"
					}]
				}
			}
		};


		var data = '';
		function bindchart() {		
			var active_beacon_store = data1.active_beacon_store;
			$('#divGraph').show();
			$.each(active_beacon_store, function (index, itemData) {
				var returndata = '';
				returndata ='<tr><td> City: </td><td>'+index+'</td>';
				$.each(this, function (header, value) {
					if (header == "count") {
						returndata += '<td>Count: </td><td>' + value + '</td>'
						data += '{ label: "' + index + '", y: ' + parseInt(value) + ' },'
					}
				});
				$('#tbody').append(returndata + '</tr>');
			});
			GraphData();
			return false;
		}
		
		//window.onload =
		function GraphData() {
			debugger;

			var xyz =({ label: "New Jersey", y: 19034.5 },
						{ label: "Texas", y: 20015 },
						{ label: "Oregon", y: 25342 },
						{ label: "Montana", y: 20088 },
						{ label: "Massachusetts", y: 28234 });
			var chart = new CanvasJS.Chart("chartContainer", {
				exportEnabled: true,
				animationEnabled: true,
				title: {
					text: "Car Parts Sold in Different States"
				},
				subtitles: [{
					text: "Click Legend to Hide or Unhide Data Series"
				}],
				axisX: {
					title: "States"
				},
				axisY: {
					title: "Oil Filter - Units",
					titleFontColor: "#4F81BC",
					lineColor: "#4F81BC",
					labelFontColor: "#4F81BC",
					tickColor: "#4F81BC"
				},
				axisY2: {
					title: "Clutch - Units",
					titleFontColor: "#C0504E",
					lineColor: "#C0504E",
					labelFontColor: "#C0504E",
					tickColor: "#C0504E"
				},
				toolTip: {
					shared: true
				},
				legend: {
					cursor: "pointer",
					itemclick: toggleDataSeries
				},
				data: [{
					type: "column",
					name: "Oil Filter",
					showInLegend: true,
					yValueFormatString: "#,##0.# Units",
					dataPoints: [
						{ label: "New Jersey", y: 19034.5 },
						{ label: "Texas", y: 20015 },
						{ label: "Oregon", y: 25342 },
						{ label: "Montana", y: 20088 },
						{ label: "Massachusetts", y: 28234 }							
					]
				}

				,{
					type: "column",
					name: "Clutch",
					axisYType: "secondary",
					showInLegend: true,
					yValueFormatString: "#,##0.# Units",
					dataPoints: [
						{ label: "New Jersey", y: 210.5 },
						{ label: "Texas", y: 135 },
						{ label: "Oregon", y: 425 },
						{ label: "Montana", y: 130 },
						{ label: "Massachusetts", y: 528 }
					]
					}
				]
			});
			chart.render();

			function toggleDataSeries(e) {
				if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
					e.dataSeries.visible = false;
				} else {
					e.dataSeries.visible = true;
				}
				e.chart.render();
			}

		}
	</script>

</head>
<body>
	<form id="form1" runat="server">
		<div>
			<div class="header">
				<center>
					Header
				</center>
			</div>
			<br />  <br /> <br /> <br /> 
			<table style="width: 100%;">
				<tr>
					<td>
						 <select name="store" id="store" class="form-control input" >
						<option value="">Select store</option>
							  {% for store in store_name %}
						  <option value="{{ store }}">{{ store }}</option>
						{% endfor %}
					   </select>
					</td>
					<td>
						 <select name="store" id="store" class="form-control input" >
						<option value="">Select store</option>
							  {% for store in store_name %}
						  <option value="{{ store }}">{{ store }}</option>
						{% endfor %}
					   </select>
					</td>
					<td>
						&nbsp;
					</td>
				</tr>
				<tr>
					<td>
						&nbsp;
					</td>
				</tr>
				<tr>
					<td style="width: 100%;" colspan="5">
						<center>
							 <button type="submit" class="btn btn-default bttn-primary" id="btnSearch" onclick="return bindchart()">Search</button>
						</center>
					</td>
				</tr>
			</table>

			<div style="display:none;" id="divGraph">
				<table>
					<tr>
						<td>
							hhghrgbeg
						</td>
					</tr>
					<tbody id="tbody">

					</tbody>>
				</table>
				<div id="chartContainer" style="height: 300px; width: 100%;"></div>
				<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
			</div>		
		</div>



	</form>
</body>
</html>
