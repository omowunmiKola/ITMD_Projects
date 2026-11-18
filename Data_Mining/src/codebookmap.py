import numpy as np
"""
BRFSS Variable Mapping Dictionary
Defines metadata, sentinel values, and target dtypes for the 57-variable keep list.
"""

BRFSS_MAP = {
    # ==========================================
    # --- TARGET VARIABLE ---
    # ==========================================
    'DIABETE4': {
        'type': 'nominal',
        'sentinels': [7, 9],            # Example: 7 = Don't know, 9 = Refused
        'skip_pattern': None,
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',         # Converts cleanly and handles NaN
        'is_target': True               # Script uses this to rename to 'CLASS'
    },

    # ==========================================
    # --- NOMINAL VARIABLES (44) ---
    # ==========================================
    '_STATE': {
        'type': 'nominal',
        'sentinels': [],
        'skip_pattern': None,
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'category',     # Good for states/strings
        'is_target': False
    },
    '_METSTAT': {
        'type': 'nominal',
        'sentinels': [],
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'category',
        'is_target': False
    },
    '_URBSTAT': {
        'type': 'nominal',
        'sentinels': [],
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'category',
        'is_target': False
    },
    'SEXVAR': {
        'type': 'nominal',
        'sentinels': [],
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'category',
        'is_target': False
    },
    '_RACE': {
        'type': 'nominal',
        'sentinels': {9:'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'category',
        'is_target': False
    },
    'MARITAL': {
        'type': 'nominal',
        'sentinels': {9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'RENTHOM1': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'VETERAN3': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'EMPLOY1': {
        'type': 'nominal',
        'sentinels': {9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'PREGNANT': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'GENHLTH': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'PRIMINS2': {
        'type': 'nominal',
        'sentinels': {77: 'Not Sure', 99: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'MEDCOST1': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'CHECKUP1': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'EXERANY2': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'BPHIGH6': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is isignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'TOLDHI3': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'CVDINFR4': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'CVDCRHD4': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'CVDSTRK3': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'ASTHMA3': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'CHCSCNC1': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'CHCOCNC1': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'CHCCOPD3': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'ADDEPEV3': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'CHCKDNY2': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'HAVARTH4': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'DEAF': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'BLIND': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'DECIDE': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'DIFFWALK': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'DIFFDRES': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'DIFFALON': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    '_SMOKER3': {
        'type': 'nominal',
        'sentinels': {9: 'Refused'},
        'skip_pattern': '9 is blank/notsure/missing',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'USENOW3': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'ECIGNOW3': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'DRNKANY6': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': '9 is blank/notsure/missing',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'FLUSHOT7': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'HIVTST7': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'PNEUVAC4': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'TETANUS1': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'PERSDOC3': {
        'type': 'nominal',
        'sentinels': {7: 'Not Sure', 9: 'Refused'},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },

    # ==========================================
    # --- ORDINAL VARIABLES (2) ---
    # ==========================================
    'EDUCA': {
        'type': 'ordinal',
        'sentinels': {9: np.nan},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'INCOME3': {
        'type': 'ordinal',
        'sentinels': {77: np.nan, 99: np.nan},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },

    # ==========================================
    # --- CONTINUOUS VARIABLES (10) ---
    # ==========================================
    '_AGE80': {
        'type': 'continuous',
        'sentinels': [],
        'skip_pattern': 'Blank, 7 and 9 have been learned by the cdc',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'CHILDREN': {
        'type': 'continuous',
        'sentinels': {88: 0, 99: np.nan},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'PHYSHLTH': {
        'type': 'continuous',
        'sentinels': {88: 0, 77: np.nan, 99: np.nan},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'MENTHLTH': {
        'type': 'continuous',
        'sentinels': {88: 0, 77: np.nan, 99: np.nan},
        'skip_pattern': 'Blank is insignificant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    '_BMI5': {
        'type': 'continuous',
        'sentinels': [],
        'skip_pattern': 'Blank is significant',
        'decimals': 2,
        'derived_replacement': None,
        'pandas_dtype': 'float32',
        'is_target': False
    },
    'SLEPTIM1': {
        'type': 'continuous',
        'sentinels': {77: np.nan, 99: np.nan},
        'skip_pattern': 'Blank is significant',
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'Int8',
        'is_target': False
    },
    'FRUTDA2_': {
        'type': 'continuous',
        'sentinels': [],
        'skip_pattern': None,
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'float32',
        'is_target': False
    },
    'FTJUDA2_': {
        'type': 'continuous',
        'sentinels': [],
        'skip_pattern': None,
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'float32',
        'is_target': False
    },
    'GRENDA1_': {
        'type': 'continuous',
        'sentinels': [],
        'skip_pattern': None,
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'float32',
        'is_target': False
    },
    'FRNCHDA_': {
        'type': 'continuous',
        'sentinels': [],
        'skip_pattern': None,
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'float32',
        'is_target': False
    },
    'POTADA1_': {
        'type': 'continuous',
        'sentinels': [],
        'skip_pattern': None,
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'float32',
        'is_target': False
    },
    'VEGEDA2_': {
        'type': 'continuous',
        'sentinels': [],
        'skip_pattern': None,
        'decimals': 0,
        'derived_replacement': None,
        'pandas_dtype': 'float32',
        'is_target': False
    }
}