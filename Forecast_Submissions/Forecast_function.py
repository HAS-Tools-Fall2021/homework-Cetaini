# This code records the function of getting forecast values
# Created by: Xiang Zhong
# Created on: 11/21/2021
# Last editted on: 11/21/2021

import numpy as np


def cal_forecast(parm_name, weight):
    """ Get forecast values.
    ------------------------------------------
    Parameters:
    Parm_name = 1D numpy array
                contains parameters for the forecast.
    Weight = 1D numpy array
             numbers between 0 to 1, and the
             summation should be 1.
    ------------------------------------------
    Returns:
    Forecast = integer
               of forecast value.
    """

    Forecast = np.sum(parm_name * weight)
    return(round(Forecast))
