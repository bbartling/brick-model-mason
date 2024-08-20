# sensor_options.py

sensor_options = {
    "AHU": [
        # Sensors
        "Supply_Air_Temperature_Sensor",
        "Return_Air_Temperature_Sensor",
        "Outside_Air_Temperature_Sensor",
        "Mixed_Air_Temperature_Sensor",
        "Discharge_Air_Temperature_Sensor",
        "Supply_Air_Static_Pressure_Sensor",
        "Return_Air_Static_Pressure_Sensor",
        "Outside_Air_Static_Pressure_Sensor",
        "Mixed_Air_Static_Pressure_Sensor",
        "Supply_Air_Flow_Sensor",
        "Return_Air_Flow_Sensor",
        "Outside_Air_Flow_Sensor",
        "Mixed_Air_Flow_Sensor",
        "Supply_Air_Humidity_Sensor",
        "Return_Air_Humidity_Sensor",
        "Outside_Air_Humidity_Sensor",
        "Supply_Air_CO2_Sensor",
        "Return_Air_CO2_Sensor",
        "Damper_Position_Sensor",
        "Fan_Status_Sensor",
        "Filter_Status_Sensor",
        # Setpoints
        "Supply_Air_Static_Pressure_Setpoint",
        "Discharge_Air_Temperature_Setpoint",
        "Outside_Air_Damper_Setpoint",
        "Mixed_Air_Temperature_Setpoint",
        "Flow_Station_Setpoint",
    ],
    "VAV": [
        # Sensors
        "Zone_Air_Temperature_Sensor",
        "Discharge_Air_Temperature_Sensor",
        "Zone_Air_Static_Pressure_Sensor",
        "Zone_Air_Flow_Sensor",
        "Zone_Air_Humidity_Sensor",
        "Zone_Air_CO2_Sensor",
        "Damper_Position_Sensor",
        "Fan_Status_Sensor",
        "Heating_Valve_Position_Sensor",
        "Cooling_Valve_Position_Sensor",
        "Zone_Occupancy_Sensor",
        # Setpoints
        "Zone_Air_Temperature_Setpoint",
        "Zone_Air_Flow_Setpoint",
        "Damper_Setpoint",
    ],
    "Chiller": [
        # Sensors
        "Chilled_Water_Supply_Temperature_Sensor",
        "Chilled_Water_Return_Temperature_Sensor",
        "Condenser_Water_Supply_Temperature_Sensor",
        "Condenser_Water_Return_Temperature_Sensor",
        "Evaporator_Temperature_Sensor",
        "Compressor_Temperature_Sensor",
        "Chilled_Water_Supply_Pressure_Sensor",
        "Chilled_Water_Return_Pressure_Sensor",
        "Condenser_Water_Supply_Pressure_Sensor",
        "Condenser_Water_Return_Pressure_Sensor",
        "Evaporator_Pressure_Sensor",
        "Compressor_Pressure_Sensor",
        "Chilled_Water_Flow_Sensor",
        "Condenser_Water_Flow_Sensor",
        "Refrigerant_Flow_Sensor",
        "Chiller_Electrical_Power_Sensor",
        "Chilled_Water_Energy_Sensor",
        "Condenser_Water_Energy_Sensor",
        "Compressor_Status_Sensor",
        "Chiller_Status_Sensor",
        "Cooling_Tower_Water_Level_Sensor",
        # Setpoints
        "Chilled_Water_Supply_Temperature_Setpoint",
        "Condenser_Water_Supply_Temperature_Setpoint",
        "Evaporator_Temperature_Setpoint",
        "Compressor_Pressure_Setpoint",
    ],
    "Boiler": [
        # Sensors
        "Hot_Water_Supply_Temperature_Sensor",
        "Hot_Water_Return_Temperature_Sensor",
        "Flue_Gas_Temperature_Sensor",
        "Burner_Temperature_Sensor",
        "Hot_Water_Supply_Pressure_Sensor",
        "Hot_Water_Return_Pressure_Sensor",
        "Steam_Pressure_Sensor",
        "Hot_Water_Flow_Sensor",
        "Steam_Flow_Sensor",
        "Fuel_Flow_Sensor",
        "Boiler_Electrical_Power_Sensor",
        "Hot_Water_Energy_Sensor",
        "Burner_Status_Sensor",
        "Boiler_Status_Sensor",
        "Flame_Detection_Sensor",
        "Water_Level_Sensor",
        # Setpoints
        "Hot_Water_Supply_Temperature_Setpoint",
        "Steam_Pressure_Setpoint",
        "Fuel_Flow_Setpoint",
        "Burner_Temperature_Setpoint",
    ],
}

unit_options = [
    "DEG_F",
    "DEG_C",
    "PSI",
    "Inch_Water_Column",
    "Percent_Command",
    "Cubic_Meter_Per_Second",
    "Relative_Humidity",
]