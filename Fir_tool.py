import arcpy

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Animal Facility - No Permit.csv"
arcpy.env.workspace = arcpy.GetParameter(0)
path2=arcpy.GetParameter(1)
list_csv = arcpy.ListFiles("*.csv")
for pres_csv in list_csv:
    tem_str1 = pres_csv[:-4]
    tem_str0=tem_str1+"-No Permit_Layer"
    a = arcpy.MakeXYEventLayer_management(table=pres_csv,
                                          in_x_field="y",
                                          in_y_field="x", out_layer=tem_str0,
                                          spatial_reference="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision",
                                          in_z_field="#")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Animal Facility - No Permit_Layer"

    tem_str2=tem_str1.replace("-","")+".shp"
    tem_str2=tem_str2.replace("(","")
    tem_str2=tem_str2.replace(")","")
    b = arcpy.CopyFeatures_management(in_features=a, out_feature_class=tem_str2, config_keyword="#",
                                  spatial_grid_1="0", spatial_grid_2="0", spatial_grid_3="0")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "result_shape", "Animal"
    tem_str3=tem_str1.replace("-","")+"spj.shp"
    tem_str3 = tem_str3.replace("(", "")
    tem_str3 = tem_str3.replace(")", "")
    c = arcpy.SpatialJoin_analysis(target_features=path2, join_features=b,
                               out_feature_class=tem_str3, join_operation="JOIN_ONE_TO_MANY", join_type="KEEP_ALL",
                               field_mapping="""STATEFP "STATEFP" true true false 2 Text 0 0 ,First,#,result_shape,STATEFP,-1,-1;COUNTYFP "COUNTYFP" true true false 3 Text 0 0 ,First,#,result_shape,COUNTYFP,-1,-1;TRACTCE "TRACTCE" true true false 6 Text 0 0 ,First,#,result_shape,TRACTCE,-1,-1;GEOID "GEOID" true true false 11 Text 0 0 ,First,#,result_shape,GEOID,-1,-1;NAME "NAME" true true false 7 Text 0 0 ,First,#,result_shape,NAME,-1,-1;NAMELSAD "NAMELSAD" true true false 20 Text 0 0 ,First,#,result_shape,NAMELSAD,-1,-1;MTFCC "MTFCC" true true false 5 Text 0 0 ,First,#,result_shape,MTFCC,-1,-1;FUNCSTAT "FUNCSTAT" true true false 1 Text 0 0 ,First,#,result_shape,FUNCSTAT,-1,-1;ALAND "ALAND" true true false 14 Double 0 14 ,First,#,result_shape,ALAND,-1,-1;AWATER "AWATER" true true false 14 Double 0 14 ,First,#,result_shape,AWATER,-1,-1;INTPTLAT "INTPTLAT" true true false 11 Text 0 0 ,First,#,result_shape,INTPTLAT,-1,-1;INTPTLON "INTPTLON" true true false 12 Text 0 0 ,First,#,result_shape,INTPTLON,-1,-1;Field1 "Field1" true true false 9 Long 0 9 ,First,#,Animal,Field1,-1,-1;X1 "X1" true true false 19 Double 0 0 ,First,#,Animal,X1,-1,-1;X0 "X0" true true false 19 Double 0 0 ,First,#,Animal,X0,-1,-1;X0_1 "X0_1" true true false 19 Double 0 0 ,First,#,Animal,X0_1,-1,-1;X0_2 "X0_2" true true false 254 Text 0 0 ,First,#,Animal,X0_2,-1,-1;X0_3 "X0_3" true true false 254 Text 0 0 ,First,#,Animal,X0_3,-1,-1;X0_4 "X0_4" true true false 254 Text 0 0 ,First,#,Animal,X0_4,-1,-1;X0_5 "X0_5" true true false 254 Text 0 0 ,First,#,Animal,X0_5,-1,-1;X0_6 "X0_6" true true false 254 Text 0 0 ,First,#,Animal,X0_6,-1,-1;X0_7 "X0_7" true true false 254 Text 0 0 ,First,#,Animal,X0_7,-1,-1;x "x" true true false 19 Double 0 0 ,First,#,Animal,x,-1,-1;y "y" true true false 19 Double 0 0 ,First,#,Animal,y,-1,-1""",
                               match_option="INTERSECT", search_radius="#", distance_field_name="#")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "result_shape", "spj1"
    d = arcpy.JoinField_management(in_data=path2, in_field="FID", join_table=c,
                               join_field="FID", fields="Join_Count")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "result_shape"
    tem_str4=tem_str1.replace("-","")
    tem_str4=tem_str4.replace(" ","")
    tem_str4 = tem_str4.replace("(", "")
    tem_str4 = tem_str4.replace(")", "")
    if(len(tem_str4)>10):
        tem_str4=tem_str4[:10]
    arcpy.AddField_management(in_table=path2, field_name=tem_str4, field_type="LONG",
                          field_precision="#", field_scale="#", field_length="#", field_alias="#",
                          field_is_nullable="NULLABLE", field_is_required="NON_REQUIRED", field_domain="#")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "result_shape"
    arcpy.CalculateField_management(in_table=path2, field=tem_str4,
                                expression="!Join_Count!", expression_type="PYTHON", code_block="#")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "result_shape"
    arcpy.DeleteField_management(in_table=path2, drop_field="Join_Count")
