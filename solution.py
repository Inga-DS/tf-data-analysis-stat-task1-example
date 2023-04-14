import pandas as pd
import numpy as np


chat_id = 285728981 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    from scipy import stats
from statsmodels.stats.proportion import proportions_ztest


def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    alpha = 0.008
    stats, p_value = proportions_ztest(np.array([x_success, y_success]), np.array([x_cnt, y_cnt]), alternative = 'smaller')
    
    return True if p_value < alpha else False
