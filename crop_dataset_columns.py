# File representing columns

TEMPERATURE_COLUMN = "Temparature"
HUMIDITY_COLUMN = "Humidity"
MOISTURE_COLUMN = "Moisture"
SOIL_TYPE_COLUMN = "Soil Type"
CROP_TYPE_COLUMN = "Crop Type"
NITROGEN_COLUMN = "Nitrogen"
POTASSIUM_COLUMN = "Potassium"
PHOSPHOROUS_COLUMN = "Phosphorous"
FERTILIZER_NAME_COLUMN = "Fertilizer Name"

column_list = [
    TEMPERATURE_COLUMN,
    HUMIDITY_COLUMN,
    MOISTURE_COLUMN,
    SOIL_TYPE_COLUMN,
    CROP_TYPE_COLUMN,
    NITROGEN_COLUMN,
    POTASSIUM_COLUMN,
    PHOSPHOROUS_COLUMN,
    FERTILIZER_NAME_COLUMN,
]

fertilizer_groupation = {
    "10-26-26": "NPK Complex",
    "14-35-14": "NPK Complex",
    "17-17-17": "NPK Complex",  
    "20-20": "High-N/P",
    "28-28": "High-N/P",
    "DAP": "Phosphatic",
    "Urea": "Nitrogenous",
}

crop_groupation = {
    "Maize": "Cereals",
    "Paddy": "Cereals",
    "Wheat": "Cereals",
    "Barley": "Cereals",
    "Millets": "Cereals",

    "Oil seeds": "Oilseeds",
    "Ground Nuts": "Oilseeds",

    "Pulses": "Pulses",

    "Cotton": "Cash crops",
    "Sugarcane": "Cash crops",
    "Tobacco": "Cash crops",
}


NPK_COMPLEX = "NPK Complex"
HIGH_NP = "High-N/P"
PHOSPHATIC = "Phosphatic"
NITROGENOUS = "Nitrogenous"

numerical_input_columns = [
    TEMPERATURE_COLUMN,
    HUMIDITY_COLUMN,
    MOISTURE_COLUMN,
    NITROGEN_COLUMN,
    POTASSIUM_COLUMN,
    PHOSPHOROUS_COLUMN,
]

# categorical_input_columns = [SOIL_TYPE_COLUMN, FERTILIZER_NAME_COLUMN]
# output_column = [CROP_TYPE_COLUMN]

categorical_input_columns = [SOIL_TYPE_COLUMN, CROP_TYPE_COLUMN]
output_column = [FERTILIZER_NAME_COLUMN]