import pandas as pd
import math

#read data from excel tables
excel_file = 'pnp1.xls'
components_table = pd.read_excel(excel_file,sheet_name='component setup')
feeders_table = pd.read_excel(excel_file, sheet_name = 'feeder settings') 
#print(components_table.head())
#print feeders_table.head()

#lets create csv file for pnp machine
f_out_top = open("out_top.csv",'w')

#write initial configs
f_out_top.write("#initial configurations")
f_out_top.write("pcb,Manual,Lock,100,100,Back,150,0,10,\n")
f_out_top.write("Mark recogniseRecognise typeManualIdentification Range of Placement Head\n")
f_out_top.write("markconfirm,Mirror,Auto,0,\n")
f_out_top.write("mark,7.718,71.649,0.8,1.2,1,75,\n")
f_out_top.write("mark,66.291,2.332,0.8,1.2,1,75,\n")
f_out_top.write("test,No,\n")
f_out_top.write("mirror_create,0,1,1,95.24,230.39,0,0,0,0,0,0,0,\n")
f_out_top.write("mirror,95.24,230.39,0,No,\n")


#write feeder settings
f_out_top.write("#feeder settings \n")
for row in feeders_table.itertuples():
    #the fields for each register are:
    #Feeder, Feeder ID
    reg = ""
    for columns in row[1:]:
        if(columns != columns):
            reg +=","
        else:
            reg += str(columns)+","
    reg +="\n"
    f_out_top.write(reg)
    #print row

    #skip one line
f_out_top.write("\n")

#write components setup
f_out_top.write("#components setup\n")
for row in components_table.itertuples():
    #the fields for each register are:
    #Stack, Nozzle, Name, Value, Footprint, _6, _7, Rotation, skip
    reg = "comp,"
    if(row.Layer == 'TopLayer'):
        for columns in row[1:8]:

            reg += str(columns)+","
            #don't write the Layer column
        reg += str(row.skip)+", \n"
        f_out_top.write(reg)





