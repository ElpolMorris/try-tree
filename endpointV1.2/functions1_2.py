
import pandas as pd


# DEFINICIÓN DE COMPARTIMENTOS
compartmentDict = {
    "SIR": ["P", "I", "I_ac", "I_d", "D_d", "D_ac"],
    "SEIR": ["P", "I", "I_ac", "I_d", "D_d", "D_ac"],
    "SEIRHVD": ["P", "I", "I_ac", "I_d", "H_d", "H_ac", "V_d", "V_ac", "D_d", "D_ac"]
}


# compartimentos correspondientes a cada modelo
def compartment(c, modelDict):
    keys = compartmentDict[c]
    result = {"Compartment": c}
    
    for k in keys:
        result[k] = modelDict[k]

    return result


#-----------------------------------------------------------------------------------------------


def endpointResponse(route, df, model, scaleName, t_init, t_end, arr_fips):
    type_fips, final_result = None, None

    # if model not in ["SIR", "SEIR", "SEIRHVD"]:
    #     final_result = {"ERROR": "Compartment is not defined"}
    # else:
    arr_dfs  = []

    # if scaleName not in ["States", "Counties"]:
    #     print("Scale is not defined")
    #     final_result = {"ERROR": "Scale is not defined"}
    # else:
    #     if scaleName == "Counties" and model == "SEIRHVD":
    #         print("SEIRHVD is not defined for County")
    #         final_result = {"ERROR": "SEIRHVD is not defined for County"}
    #     else:
    if scaleName == "States":  # statesUSA
        type_fips = 'FIPS_state'

    elif scaleName == "Counties":  # countiesUSA
        type_fips = 'FIPS_county'

    # if t_end is None:
    #     t_end = t_init
        # route = 'initCond'

        
    # print(route)

    for fips in arr_fips:
        df_tmp = df[(df['DateTime'] >= t_init) & (df['DateTime'] <= t_end) & (df[type_fips] == fips)]
        arr_dfs.append(df_tmp)
            
    df_compile = pd.concat(arr_dfs)

    # if df_compile.shape[0] == 0:
        # route = str(t_init)
        # final_result = {model: "No results"}
    # else:
    attr = ['DateTime']

    for a in compartmentDict[model]:
        attr.append(a)

    #print("attr", attr)

    df_reduce = df_compile.loc[:, attr]  #[['DateTime', 'S', 'E', 'I', 'I_acum', 'I_active', 'R']]

    #print("df_reduce", df_reduce)

    df_groupby = pd.DataFrame(df_reduce.groupby(['DateTime']).sum())
    df_groupby = df_groupby.reset_index(level = None, drop = False, inplace = False, col_level = 0, col_fill = '')
                        

    requiredDates = df_groupby['DateTime'].tolist()

    n_day = ""
    long = len(requiredDates)
    tmp_result = {}

    if long == 1:
        P, I, I_ac, I_d, H_d, H_ac, V_d, V_ac, D_d, D_ac = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    else:
        P, I, I_ac, I_d, H_d, H_ac, V_d, V_ac, D_d, D_ac = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}


    tmp_dict = {
        'P'           : P, 
        'I'           : I, 
        'I_ac'        : I_ac, 
        'I_d'         : I_d, 
        'H_d'         : H_d, 
        'H_ac'        : H_ac,
        'V_d'         : V_d, 
        'V_ac'        : V_ac,
        'D_d'         : D_d, 
        'D_ac'        : D_ac
    }

    # if (route not in ["initCond", "realData"]) or (not (long == 1 and route == "initCond") and not (long > 1 and route == "realData")):
    #     final_result = {"ERROR": "Incorrect route"}, 404
    #     # return jsonify({"error": "Incorrect Email",}), 403
    # else:

    for c in compartmentDict[model]:
        for date in requiredDates:
            n_day = df_groupby.index[df_groupby['DateTime'] == date].tolist()[0]

            if long == 1 and route == "initCond":
                tmp_dict[c] = str(int(df_groupby[df_groupby['DateTime'] == date][c].sum()))
            elif long > 1 and route == "realData":
                tmp_dict[c][n_day] = str(int(df_groupby[df_groupby['DateTime'] == date][c].sum()))

            tmp_result[c] = tmp_dict[c]


    final_result = compartment(model, tmp_result)

    return final_result

