right_payload_states = {
    "sim1": {
        "scale": "States",
        "compartments": "SIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "spatialSelection": ["13"],
    },
    "sim2": {
        "compartments": "SEIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "scale": "States",
        "spatialSelection": ["08"],
    },
}
right_payload_counties = {
    "sim1": {
        "scale": "Counties",
        "compartments": "SIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "spatialSelection": ["36001"],
    },
    "sim2": {
        "compartments": "SIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "scale": "Counties",
        "spatialSelection": ["04015"],
    },
}
wrong_scale_states = {
    "sim1": {
        "scale": "States",
        "compartments": "SIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "spatialSelection": ["13"],
    },
    "sim2": {
        "compartments": "SEIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "scale": "State",
        "spatialSelection": ["08"],
    },
}
wrong_scale_counties = {
    "sim1": {
        "scale": "County",
        "compartments": "SIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "spatialSelection": ["22105"],
    },
    "sim2": {
        "compartments": "County",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "scale": "States",
        "spatialSelection": ["04015"],
    },
}
wrong_init_date = {
    "sim1": {
        "scale": "States",
        "compartments": "SIR",
        "timeInit": "2021-01-32",
        "timeEnd": "2021-02-01",
        "spatialSelection": ["13"],
    },
    "sim2": {
        "compartments": "SEIR",
        "timeInit": "2021-01-32",
        "timeEnd": "2021-02-01",
        "scale": "States",
        "spatialSelection": ["08"],
    },
}
wrong_end_date = {
    "sim1": {
        "scale": "States",
        "compartments": "SIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-22-01",
        "spatialSelection": ["13"],
    },
    "sim2": {
        "compartments": "SEIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-22-01",
        "scale": "States",
        "spatialSelection": ["08"],
    },
}
wrong_compartments = {
    "sim1": {
        "scale": "Counties",
        "compartments": "SITH",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "spatialSelection": ["22105"],
    },
    "sim2": {
        "compartments": "Counties",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "scale": "States",
        "spatialSelection": ["04015"],
    },
}
empty_info = {}
date_without_data = {
    "sim1": {
        "scale": "Counties",
        "compartments": "SIR",
        "timeInit": "2000-01-31",
        "timeEnd": "2021-02-01",
        "spatialSelection": ["22105"],
    },
    "sim2": {
        "compartments": "SIR",
        "timeInit": "2021-01-31",
        "timeEnd": "2021-02-01",
        "scale": "States",
        "spatialSelection": ["04"],
    },
}
