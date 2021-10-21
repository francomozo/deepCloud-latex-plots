import numpy as np


def get_best_n_exp(exp_dict, n):
    
    stacked = []
    for k in exp_dict.keys():
        stacked.append(exp_dict[k])
    stacked = np.array(stacked)

    # 1: get indices for min val for each row
    min_val_idx_for_row = np.argmin(stacked, axis=1)

    # 2: get those values into an array
    min_val_for_row = stacked[np.arange(stacked.shape[0]), min_val_idx_for_row] 

    # 3: get indices for the n min values of the previous array
    min_val_idx_for_exp = min_val_for_row.argsort()[:n]
    
    best_n_exp = []
    for idx, k in enumerate(exp_dict.keys()):
        if idx in min_val_idx_for_exp:
            best_n_exp.append(k)
    
    return best_n_exp
