#!/usr/bin/env python
#script for calculating required time and heating coils length for tankers
import inout
import math

def sum_list_int(list_name):
# calculating summ of list and returns integer
	return int(sum(list_name))
	
def sum_float(list_name):
# calculating summ of list and returns float
	return float(sum(list_name))
	
def tk_in (arr_name):
## input groups of same tanks
	arr_name=[]
	for groups in range (0, same_tanks_group):
		print ("Tank group: ", groups+1)
		tk=inout.get_integer("Number of Tanks within group - press '0' for 4: ", 4)
		tk_grouped.append (tk)
		tks_tot = sum_list_int(tk_grouped)
	 	arr_name.append(tk)
	return int(tks_tot)
	return arr_name
	
pname=raw_input("Project Name: ")
#general data input
Ks=inout.get_float("Heat Transfer Coef of Heating Pipe [kcal/(sqm*degC)] - press '0' for 100 or input: ", 100)
Ats=inout.get_float("Average Steam Temperature [degC] - press '0' for 170 or input: ", 170)
Dw=inout.get_float("Temperature of Sea Water [degC] - press '0' for 5 degC or input: ", 5)
Dai=inout.get_float("Temperature of Outer air [degC] - press '0' for 2 degC or input: ", 2)
Ds=inout.get_float("Temperature of air in Ship [degC] - press '0' for 10 degC or input: ", 10)
Da=inout.get_float("Temperature of Oil after heating [degC] - press '0' for 45 degC or input: ",45)
Dh=inout.get_float("Temperature of Oil before heating [degC] - press '0' for 15 degC or input: ", 15)
Spwt=inout.get_float("Specific weight of Oil before heating [kg/cum] - press '0' for 800 kg/cum or input: :", 800)
Sph=inout.get_float("Specific Heat of Oil [kcal/(kg*degC)] - press '0' for 0.45 kcal/(kg*degC): ", 0.45)
Tr=inout.get_float("Heating Period [h] - press '0' for 96 h: ", 96)
Sin=inout.get_float("Steam pressure on inlet [kg/sqm] - press '0' for 80000 kg/sqm or input: ", 80000) 
Sout=inout.get_float("Steam pressure on outlet [kg/sqm] - press '0' for 50000 kg/sqm or input: ", 50000) 
Eni=inout.get_float("Enthalpy of steam on inlet [kcal/kg] - press '0' for 660 kcal/kg or input: ", 660)
Eno=inout.get_float("Enthalpy of steam on outlet [kcal/kg] - press '0' for 150 kcal/kg or input: ", 150)
Spv=inout.get_float("Specific volume of Steam on inlet [cum/kg] - press '0' for 0.24 cum/kg: ", 0.24)
Idmm=inout.get_float("Pipe inner Diameter [mm] - press '0' for 54mm: ", 54)
Odmm=inout.get_float("Pipe outer Diameter [mm] - press '0' for 60mm: ", 60)
Id=float(Idmm/1000)    #in meters
Od=float(Odmm/1000)    #in meters
filename=pname+'.txt'
fn=open(filename, 'a')
fn.write(pname)
fn.write("\n\nInput Data:")
##writing input data
inout.write_file (fn, "Heat Transfer Coef of Heating Pipe [kcal/(sqm*degC)]: ", Ks)
inout.write_file (fn, "Average Steam Temperature [degC]: ", Ats)
inout.write_file (fn, "Temperature of Sea Water [degC]: ", Dw)
inout.write_file (fn, "Temperature of Outer air [degC]: ", Dai)
inout.write_file (fn, "Temperature of air in Ship [degC]: ", Ds)
inout.write_file (fn, "Temperature of Oil after heating [degC]: ", Da)
inout.write_file (fn, "Temperature of Oil before heating [degC]: ", Dh)
inout.write_file (fn, "Temperature of Oil before heating [degC]: ", Spwt)
inout.write_file (fn, "Specific Heat of Oil [kcal/(kg*degC)]: ", Sph)
inout.write_file (fn, "Heating Period [h]: ", Tr)
inout.write_file (fn, "Steam pressure on inlet [kg/sqm]: ", Sin)
inout.write_file (fn, "Steam pressure on outlet [kg/sqm]: ", Sout)
inout.write_file (fn, "Enthalpy of steam on inlet [kcal/kg]: ", Eni)
inout.write_file (fn, "Enthalpy of steam on outlet [kcal/kg]: ", Eno)
inout.write_file (fn, "Specific volume of Steam on inlet [cum/kg]: ", Spv)
inout.write_file (fn, "Pipe inner Diameter [mm]: ", Idmm)
inout.write_file (fn, "Pipe outer Diameter [mm]: ", Odmm)
fn.close()
#ubaciti Kws to Kho
#common data - heat transfer coef. [kcal/(sqm*degC)]
Kws=17  #shipside oil to sea 
Kwb=4   #bottom oil to sea
Kas=15  #shipside oil to air
Kad=5   #deck - oil to air
Khw=15  #oil to water in ship (ballast)
Kha=4	#oil to air in ship
Kho=4   #oil to unheated oil in ship
same_tanks_group=inout.get_integer("Number of same tanks groups - press '0' for 3: ", 3)
fn=open(filename, 'a')
for tank_group in range (0, same_tanks_group): ##pogledaj ovu petlju - da se ubaci u sledecu?!
	
	inout.write_file(fn, "Group number: ", tank_group)
#	inout.write_file(fn, "Number of same tanks in group: ", tk_grouped[tank_group])
fn.close()
#tank input - all Area units in [sqm]
#containers for tank bulkeads surface areas
Aws=[]  #Oil to sea area
Awb=[]  #bottom to sea area
Aas=[]  #Shipside oil to air area
Aad=[]  #deck - oil to air area
Ahw=[]  #oil to water in ship area
Aha=[]  #oil to air in ship area
Aho=[]  #oil to unheated oil in ship area
L3=float(1-(Sout/Sin)**2)
print (str(L3))
L1=float(127000000*Sin*Id*Id*(Eni-Eno)**2)
print (str(L1))
L2=float(Ks*Ks*Od*Od*0.0134*Spv*(Ats-Da)**2)
print (str(L2))
L4=float((L3*(L1/L2))**0.33333)
L=float(Id*L4/2)
LE=float(0.7*L)
Sum_Holder=[]
Sum_Holder2=[]
Alpha=[]
Expo=[]
Gk=[]
Gr=[]
GrL=[]
AssL=[]
Lenght=[]
Ratio=[]
LL=[]
group_desc=[] #group name
tk_cap=[] #capacity of each tank within group [cum]
tknos=[]
fn=open(filename, "a")
fn.write("\nGroup \tCapacity [cum] \tAws[sqm] \tAwb[sqm] \tAas[sqm] \tAad[sqm] \tAhw[sqm] \tAha[sqm] \tAho[sqm] \tCoils Length per Tnk [m] \tSteam to Heatup per tnk[kg/h] \tSteam to Maintain per Tnk[kg/h] \tTanks in group")
for groupping in range (0, same_tanks_group): 
	print("Tanks group: ", groupping)
	tknos1=inout.get_integer ("Enter number of tanks within same group or press '0' for 4: ", 4)
	group_name=raw_input("Group Description: ")
	tk_capacity=inout.get_float("Capacity of tank in group [cum] - press '0' for 1200: ", 1200)
	Aws1=inout.get_float("Side Area between Oil and Sea Water [sqm] - press '0' for 300: ", 300)
	Awb1=inout.get_float("Bottom Area between Oil and Sea Water [sqm] - press '0' for 450: ", 450)
	Aas1=inout.get_float("Side Area between Oil and Air in Ship [sqm] - press '0' for 400: ", 400)
	Aad1=inout.get_float("Deck Area (Oil to Outer Air) [sqm] - press '0' for 450: ", 450)
	Ahw1=inout.get_float("Bulkhead Area between Oil and Water in Ship [sqm] - press '0' for 400: ", 400)
	Aha1=inout.get_float("Bottom Area between Oil and Air in ship [sqm] - press '0' for 450: ", 450)
	Aho1=inout.get_float("Area between Heated and Unheated Oil [sqm] - press '0' for 450: ", 450)
	Sum_keep=Aws1*Kws*(Da-Dw)+Awb1*Kwb*(Da-Dw)+Aas1*Kas*(Da-Ds)+Aad1*Kad*(Da-Dai)+(Ahw1+Aha1)*Khw*(Da-Ds)+Aho1*Kho*(Ds-Dh)
	Sum_keep2=Aws1*Kws+Awb1*Kwb+Aas1*Kas+Aad1*Kad+(Ahw1+Aha1)*Khw+Aho1*Kho
	Alpha1=Sum_keep2/(Spwt*Sph*tk_capacity)
	Expo1=math.exp(Alpha1*Tr)
	Gk1=Sum_keep/(Eni-Eno)
	Gr=(Gk1+1.08*(Da-Dh)*Sum_keep/((Expo1-1)*(Eni-Eno)))*1.03
	Ass1=Gr*(Eni-Eno)/(Ks*(Ats-Da))
	Len=Ass1/(3.142*Od)
	Rat=Ass1/tk_capacity
	LL1=Len/LE
	group_desc.append(group_name)
	tk_cap.append(tk_capacity)
	Aws.append(Aws1)
	Awb.append(Awb1)
	Aas.append(Aas1)
	Aad.append(Aad1)
	Ahw.append(Ahw1)
	Aha.append(Aha1)
	Aho.append(Aho1)
	Sum_Holder.append(Sum_keep)
	Sum_Holder2.append(Sum_keep2)
	Alpha.append(Alpha1)
	Expo.append(Expo1)
	Gk.append(Gk1)
	GrL.append(Gr)
	AssL.append(Ass1)
	Lenght.append(Len)
	Ratio.append(Rat)
	LL.append(LL1)
	tknos.append(tknos1)
	inout.write_table13(fn, group_desc[groupping], str(tk_cap[groupping]), str(Aws[groupping]), str(Awb[groupping]), str(Aas[groupping]), str(Aad[groupping]), str(Ahw[groupping]), str(Aha[groupping]), str(Aho[groupping]), str(Lenght[groupping]), str(GrL[groupping]), str(Gk[groupping]), str(tknos[groupping]))
print("Calculating Group Totals")
tot_len=[]
tot_GrL=[]
tot_Gk=[]
tot_cap=[]
fn.write("\nTotals for EACH GROUP: ")
fn.write("\nGroup \tCapacity [cum] \tCoils Length[m]  \tSteam to Heatup [kg/h] \tSteam to Maintain Temp.[kg/h]")
for groupping in range (0, same_tanks_group):
	tot_len1 = Lenght[groupping]*tknos[groupping]
	tot_len.append(tot_len1)
	tot_GrL1 = tknos[groupping]*GrL[groupping]
	tot_GrL.append(tot_GrL1)
	tot_Gk1 = Gk[groupping]*tknos[groupping]
	tot_Gk.append(tot_Gk1)
	tot_cap1=tk_cap[groupping]*tknos[groupping]
	tot_cap.append(tot_cap1)
	inout.write_table5(fn, group_desc[groupping], str(tot_cap[groupping]), str(tot_len[groupping]), str(tot_GrL[groupping]), str(tot_Gk[groupping]))
print ("Calculating Totals for Whole Vessel")
fn.write("\nTotals for whole vessel")
total_cap=sum_float(tot_cap)
total_len=sum_float(tot_len)
total_GrL=sum_float(tot_GrL)
total_Gk=sum_float(tot_Gk)
inout.write_file (fn, "Total Cargo Capacity [cum]: ", total_cap)
inout.write_file (fn, "Total Length of Heating Coils [m]: ", total_len)
inout.write_file (fn, "Total Steam quantity required for initial heat-up [kg/h]: ", total_GrL)
inout.write_file (fn, "Total Steam quantity required to maintain cargo temperature [kg/h]: ", total_Gk)
fn.close()
print ("END. All results written!")